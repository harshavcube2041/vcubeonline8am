# application.py, application.py

from flask import Flask, request
import json

application = Flask(__name__)

@application.route("/",methods=["GET"])
def test():
    return "hello world welcome to vcube"
    # html code
    # css code

@application.route("/test",methods=['POST'])
def posttest():
    data=request.data
    print(json.loads(data))
    return "received"

# @app.route("/mongoinsert",methods=['POST'])
# def mongoTest():
#     data=request.data
#     final_data=json.loads(data)
#     #final_db=collection.insert_one(final_data)
#     return "True"


if __name__ == '__main__':
    application.run(host="0.0.0.0",port=5000)
