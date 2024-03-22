from flask import Flask,jsonify
import requests

app = Flask(__name__)


@app.route("/stonks", methods=["GET", "OPTIONS"])
def stonks():
    r = requests.get("https://live.euronext.com/en/intraday_chart/getChartData/FR0000051732-XPAR/intraday")
    stonks = r.json()
    data = {"price": stonks[-1]["price"],"stonks": r.json()[-100:]}
    resp = jsonify(data)
    resp.headers.add("Access-Control-Allow-Origin", "*")
    resp.headers.add("Access-Control-Allow-Headers", "*")
    resp.headers.add("Access-Control-Allow-Methods", "*")
    return resp
app.run()
