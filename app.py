from flask import Flask, render_template, request

app = Flask(__name__)

import google.generativeai as palm
palm.configure(api_key="AIzaSyCCT1K99BJ1JbLwhCE7qOcQ5KOZcPJ9ZZ4")
model = {"model":"models/chat-bison-001"}

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/generative-ai",methods=["GET","POST"])
def generative_ai():
    q = request.form.get("q")
    r = palm.chat(**model, messages=q)
    return(render_template("generative-ai.html", r=r.last))

@app.route("/dapp-add-value",methods=["GET","POST"])
def dapp_add_value():
    return(render_template("index.html"))

if __name__ == "__main__":
    app.run()
