from flask import Flask,jsonify
import requests

app = Flask(__name__)


@app.route("/stonks", methods=["GET", "OPTIONS"])
def stonks():
    r = requests.get("https://live.euronext.com/en/intraday_chart/getChartData/FR0000051732-XPAR/max", headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0"})
    stonks = r.json()
    r_ = requests.get("https://live.euronext.com/en/intraday_chart/getChartData/FR0000051732-XPAR/intraday", headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0"})
    stonks_ = r_.json()
    data = {"price": stonks_[-1]["price"],"stonks": r.json()[-1000:]}
    resp = jsonify(data)
    resp.headers.add("Access-Control-Allow-Origin", "*")
    resp.headers.add("Access-Control-Allow-Headers", "*")
    resp.headers.add("Access-Control-Allow-Methods", "*")
    return resp

app.run(host="0.0.0.0")
