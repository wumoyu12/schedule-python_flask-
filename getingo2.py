from flask import Flask,render_template, request, redirect
import os.path
from os import path

global whichfilename
whichfilename = "schedule.txt"

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('personinfo.html')

@app.route("/info", methods=['POST'])
def GetInfo():
    
    CreateCheckFile()
    global pdnum, course, teacher, room
    for i in range(1, 9):
        
        pdnum="Period " + str(i)
        course = request.form.get("course" + str(i), "N/A")
        teacher = request.form.get("teacher" + str(i), "N/A")
        room = request.form.get("room" + str(i), "N/A")

        CreateCheckFile()

    RetrieveInfo()
        
def CreateCheckFile():
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    fileexist = bool(path.exists(whichfilename))

    if (fileexist == False):
        status = "new"
    else:
        status = "edit"

    WriteToFile(status)
    
def WriteToFile(whichstatus):
    if (whichstatus == "new"):
        infofile = open(whichfilename,"x")
        infofile.close()
        infofile = open(whichfilename,"w")
    else:
        infofile = open(whichfilename,"a")

    infofile.write(pdnum + "," + course + "," + teacher + "," + room + ",")
    infofile.close()
    
def RetrieveInfo():
    schedule = []
    infofile = open(whichfilename,"r")
    items = infofile.read().split(",");
    schedule.append(items)
    
    return render_template('output.html', schedule=schedule)

if __name__ == '__main__':
    app.run()
