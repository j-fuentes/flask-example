import os
from flask import Flask, jsonify
import redis

app = Flask(__name__)
r = redis.StrictRedis(host='db', port=6379, db=0)


@app.route("/set/<smthng>")
def produce(smthng):
    try:
        r.set('data', str(smthng))
    except Exception, e:
        return str(e)
    return jsonify({'data':str(smthng), 'action':'set'})

@app.route("/")
def consume():
    data = str(r.get('data'))
    if not data:
        data = ''

    result = {'data':data, 'action':'get'}
    return jsonify(result)

if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
