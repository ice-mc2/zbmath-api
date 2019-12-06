from flask import Flask, escape, request, jsonify
from services.zbmath import ZbMath

app = Flask(__name__)

api = ZbMath()


@app.route('/search')
def search():
    return jsonify(api.run_query(request.args.get('query')))
