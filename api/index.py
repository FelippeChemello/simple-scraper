from flask import Flask, jsonify, request
from newsplease import NewsPlease

app = Flask(__name__)

@app.route('/')
def scrape():
    url = request.args.get('url')

    article = NewsPlease.from_url(url)

    return jsonify(vars(article))

if __name__ == '__main__':
    app.run(debug=True)