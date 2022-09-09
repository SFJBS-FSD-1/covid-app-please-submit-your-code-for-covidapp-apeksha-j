from flask import Flask,render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def mycovidapp():
    if request.method=="POST":
        country=request.form["country"]
        print(country)
        url = "https://api.covid19api.com/summary"
        print(url)
        response = requests.get(url).json()
        print(response)
        Countries=response["Countries"]
        print(Countries)
        for i in range(len(Countries)):
            if Countries[i]["Country"]==country:
                # print("Country found")
                data = {"place": Countries[i]["Country"], "confirmed": Countries[i]["TotalConfirmed"],"ded": Countries[i]["TotalDeaths"]}
                return render_template("covid19.html",data=data)
    else:
        data= None
        return render_template("covid19.html",data=data)

app.run()