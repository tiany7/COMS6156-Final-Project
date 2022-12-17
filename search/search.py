
import re
import pandas as pd
import spacy
import string
import gensim
import operator
import requests
from gensim.similarities import MatrixSimilarity

spacy_nlp = spacy.load("en_core_web_sm")

punctuations = string.punctuation
stop_words = spacy.lang.en.stop_words.STOP_WORDS

def spacy_tokenizer(sentence):
 
    #remove distracting single quotes.
    sentence = re.sub('\'','',sentence)

    #remove digits adnd words containing digits.
    sentence = re.sub('\w*\d\w*','',sentence)

    #replace extra spaces with single space.
    sentence = re.sub(' +',' ',sentence)

    #remove unwanted lines starting from special charcters.
    sentence = re.sub(r'\n: \'\'.*','',sentence)
    sentence = re.sub(r'\n!.*','',sentence)
    sentence = re.sub(r'^:\'\'.*','',sentence)
    
    #remove non-breaking new line characters.
    sentence = re.sub(r'\n',' ',sentence)
    
    #remove punctunations.
    sentence = re.sub(r'[^\w\s]',' ',sentence)
    
    #creating token object.
    tokens = spacy_nlp(sentence)
    
    #lower, strip and lemmatize.
    tokens = [word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in tokens]
    
    #remove stopwords, and exclude words less than 2 characters.
    tokens = [word for word in tokens if word not in stop_words and word not in punctuations and len(word) > 2]
    
    #return tokens.
    return tokens

def request_data():
    url = 'https://api.aylien.com/news/stories?aql=industries:({{id:in.are}}) AND categories:({{taxonomy:aylien AND id:ay.biz}}) AND language:(en) AND sentiment.title.polarity:(negative neutral positive)&per_page=50&cursor=*&published_at.end=NOW&published_at.start=NOW-7DAYS/DAY'
    payload = {}

    headers = {
        'X-Application-ID': 'dcf2074d',
        'X-Application-Key': 'b53a0a447ae382b8030df674cf9ed946'
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    return response.json()

def lambda_func(search_term, top_n_similar):
    # TODO: change the data fectch from API to AWS database.
    news_l = [[i["title"], i["body"]] for i in request_data()["stories"]]
    df = pd.DataFrame(news_l, columns=["title", "body"])
    df["news_tokenized"] = df["body"].map(lambda x: spacy_tokenizer(x))

    # create a corpora dictionary.
    dictionary = gensim.corpora.Dictionary(df["news_tokenized"])

    # useless word to be removed.
    stoplist = set('hello and if this can would should could tell ask stop come go')
    stop_ids = [dictionary.token2id[stopword] for stopword in stoplist if stopword in dictionary.token2id]
    dictionary.filter_tokens(stop_ids)
    
    # feature extraction to build corpus.
    corpus = [dictionary.doc2bow(desc) for desc in  df["news_tokenized"]]

    # build tf-idf and laten semantic indexing.
    tfidf_model = gensim.models.TfidfModel(corpus, id2word=dictionary)
    lsi_model = gensim.models.LsiModel(tfidf_model[corpus], id2word=dictionary, num_topics=300)

    # serialize and Store the corpus locally for easy retrival whenver required.
    gensim.corpora.MmCorpus.serialize('tfidf_model_mm', tfidf_model[corpus])
    gensim.corpora.MmCorpus.serialize('lsi_model_mm',lsi_model[tfidf_model[corpus]])

    # load the indexed corpus.
    lsi_corpus = gensim.corpora.MmCorpus('lsi_model_mm')

    news_index = MatrixSimilarity(lsi_corpus, num_features = lsi_corpus.num_terms)

    # setup query parameter
    query_bow = dictionary.doc2bow(spacy_tokenizer(search_term))
    query_tfidf = tfidf_model[query_bow]
    query_lsi = lsi_model[query_tfidf]

    news_index.num_best = top_n_similar
    news_list = news_index[query_lsi]
    news_list.sort(key=operator.itemgetter(1), reverse=True)
    news_names = []

    for i, news in enumerate(news_list):
        news_names.append({
            "Relevence": round((news[1] * 100),2),
            "News Title": df["title"][news[0]],
            "News Content": df["body"][news[0]],
        })
        if i == (news_index.num_best-1):
            break
    return pd.DataFrame(news_names, columns=["Relevence", "News Title", "News Content"])

if __name__ == "__main__":
    print(lambda_func("China Economy", 5))