from flask import Flask, Response, request
from flask_cors import CORS
import json
import logging
import time
import utils.rest_utils as rest_utils
from database_services.subscription_service import SubscriptionService
from database_services.userDBService import UserDBService
from database_services.notice_service import NoticeService

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)

##################################################################################################################

# DFF TODO A real service would have more robust health check methods.
# This path simply echoes to check that the app is working.
# The path is /health and the only method is GETs
@app.route("/health", methods=["GET"])
def health_check():
    rsp_data = {"status": "healthy", "time": str(datetime.now())}
    rsp_str = json.dumps(rsp_data)
    rsp = Response(rsp_str, status=200, content_type="app/json")
    return rsp


# TODO Remove later. Solely for explanatory purposes.
# The method take any REST request, and produces a response indicating what
# the parameters, headers, etc. are. This is simply for education purposes.
#
@app.route("/api/demo/<parameter1>", methods=["GET", "POST", "PUT", "DELETE"])
@app.route("/api/demo/", methods=["GET", "POST", "PUT", "DELETE"])
def demo(parameter1=None):
    """
    Returns a JSON object containing a description of the received request.

    :param parameter1: The first path parameter.
    :return: JSON document containing information about the request.
    """

    # DFF TODO -- We should wrap with an exception pattern.
    #

    # Mostly for isolation. The rest of the method is isolated from the specifics of Flask.
    inputs = rest_utils.RESTContext(request, {"parameter1": parameter1})

    # DFF TODO -- We should replace with logging.
    r_json = inputs.to_json()
    msg = {
        "/demo received the following inputs": inputs.to_json()
    }
    print("/api/demo/<parameter> received/returned:\n", msg)

    rsp = Response(json.dumps(msg), status=200, content_type="application/json")
    return rsp

# couch server


import couchdb
couch = couchdb.Server("http://admin:root@44.212.66.47:5984")
try:
    db = couch.create('hist')
except:
    db = couch['hist']
sdb = couch["subscriptions"]

@app.route("/api/create_user_profile", methods=["POST"])
def create_user_profile():
    body = request.get_data()
    body = json.loads(body)
    print(body)
    ret = UserDBService.create_user(body)
    SubscriptionService.create_user_record(body["user_id"], body["email"])

    if ret is not None:
        return Response(json.dumps(ret), status=200, content_type="application/json")
    return Response(json.dumps({"status": "success"}), status=200, content_type="application/json")

@app.route("/", methods=["GET"])
def hello():
    return "Hello World!"



@app.route("/api/subscribe", methods=["POST"])
def subscribe():
    body = request.get_data()
    body = json.loads(body)
    from_user = body["from_user"]
    to_user = body["to_user"]
    print(body)
    status = SubscriptionService.create_subscription(from_user, to_user)
    if status is None:
        rsp = Response(json.dumps({"status": "Successfully subscribed"}), status=400, content_type="application/json")
    else:
        rsp = Response(json.dumps({"status": "Subscription failed", "error_msg": status}), status=400, content_type="application/json")
    return rsp

@app.route("/api/unsubscribe", methods=["POST"])
def unsubscribe():
    body = request.get_data()
    body = json.loads(body)
    from_user = body["from_user"]
    to_user = body["to_user"]
    ret = SubscriptionService.unsubscribe(from_user, to_user)
    if ret is None:
         return Response(json.dumps({'status': 'success', 'message': 'Unsubscribed successfully'}), status=200, content_type="application/json")
    else:
        return Response(json.dumps({'status': 'failure', 'message': ret}), status=400, content_type="application/json")

@app.route("/api/get_subscriptions", methods=["GET"])
def get_subscriptions():
    header = request.args
    start, end = None, None
    user_id = header["user_id"]
    print(header)
    try:
        start, end = header["start"], header["offset"]
    except:
        start = 0
        end = 10
    print(start, end)

    ret = SubscriptionService.get_subscribed(user_id, start, end)
    data = []
    for i in ret:
        data.append({"user_id": i})
    return Response(json.dumps({"status": "ok", "data": data}), status=200, content_type="application/json")

@app.route("/api/get_subscribers", methods=["GET"])
def get_subscribers():
    header = request.args
    start, end = None, None
    user_id = header["user_id"]
    print(header)
    try:
        start, end = header["start"], header["offset"]
    except:
        start, end = 0, 10
    print(start, end)
    ret = SubscriptionService.get_subscribers(user_id, start, end)
    data = []
    print(ret)
    for i in ret:
        data.append({"user_id": i})

    return Response(json.dumps({"status": "ok", "data": data}, indent=2), status=200, content_type="application/json")

@app.route("/api/subscription_history", methods=["GET"])
def subscription_history():
    header = request.headers
    header = request.args
    start, to = None, None
    user_id = header["user_id"]
    try:
        start = int(header["start"])
        to = int(header["to"])
    except:
        start = 0
        to = 100

    ret = SubscriptionService.get_history(user_id, start, to)
    return Response(json.dumps({'status': "ok", "data": ret}), status=200, content_type="application/json")

@app.route("/api/get_notice/<user_id>", methods=["GET"])
def get_notice(user_id):
    notice = NoticeService.get_notice(user_id)
    str = "%Y_%m_%d_%H_%M_%S"
    srt_lst = str.split('_')
    date = time.strftime('_'.join(srt_lst[:3]), time.localtime(time.time()))
    return Response(json.dumps({"user_id": user_id, "time": date, "notice": notice}), status=200, content_type="application/json")

@app.route("/apply", methods=["POST"])
def apply():
    import pymysql
    conn = pymysql.connect(host='localhost', user='root', password='', db='coms4156_db')
    cur = conn.cursor()
    body = request.get_data()
    body = json.loads(body)
    sender = body["sender"]
    receiver = body["receiver"]
    content = body["content"]
    sql = "insert into application (applicant, recipient, date , message) values ('%s', '%s', '%d', '%s')" % (sender, receiver, int(time.time()),content)
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    return Response(json.dumps({"status": "ok"}), status=200, content_type="application/json")

@app.route("/api/get_by_sender", methods=["GET"])
def get_application():
    import pymysql
    conn = pymysql.connect(host='localhost', user='root', password='', db='coms4156_db')
    cur = conn.cursor()
    header = request.args
    receiver = header["sender"]

    sql = "select * from application where applicant = '%s'" % receiver
    cur.execute(sql)
    ret = cur.fetchall()
    cur.close()
    conn.close()
    return Response(json.dumps({"status": "ok", "data": ret}), status=200, content_type="application/json")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5051)
