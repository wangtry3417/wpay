from flask import Flask,redirect,render_template,url_for
import random

app = Flask("WPay")

@app.route("/wcoin")
def wcoin():
  return render_template("wcoin.html")



app.run(host="0.0.0.0",port=5000)
