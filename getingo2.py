from flask import Flask,render_template, request, redirect
import os.path
from os import path

global whichfilename;
whichfilename = "allinfo.txt";
app=Flask(__name__)

@app.route("/")

def main():
    return render_template("personinfo.html")

@app.route("/info",methods=["POST"])
def GetInfo():
    global mylist
    global mylistlen

    mylist=[]
    mylist=["Math", "Science", "English", "History", "Software Engineering"]
    mylistlen=len(mylist)
    return mylistlen, mylist

if __name__=="__main__":
    app.run()


