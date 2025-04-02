from flask import Flask, render_template, request, redirect
import os.path
from os import path

app = Flask(__name__)
whichfilename = "schedule.txt"

@app.route('/')
def main():
    return render_template('personinfo.html')

@app.route("/info", methods=['POST'])
def GetInfo():
    global status, result
    status = CreateCheckFile()
    result = ""
    
    for i in range(1, 9):
        pdnum = "Period " + str(i)
        course = request.form.get("course" + str(i), "")
        teacher = request.form.get("teacher" + str(i), "")
        room = request.form.get("room" + str(i), "")
        
        
        if course == "" or teacher == "" or room == "":
            return render_template('personinfo.html', valid="Please don't leave any BLANK")
        
        
        if course == "n/a":
            course = "No Class"
        if teacher == "n/a":
            teacher = "No Teacher"
        if room == "n/a":
            room = "No Room"
        
        
        WriteToFile(pdnum, course, teacher, room)
    
    return RetrieveInfo()

def CreateCheckFile():
    global status
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    fileexist = bool(path.exists(whichfilename))

    if fileexist == False:
        status = "new"
    else:
        status = "edit"

def WriteToFile(pdnum, course, teacher, room):
    if status == "new":
        infofile = open(whichfilename, "x")
        infofile.close()
        infofile = open(whichfilename, "w")
    else:
        infofile = open(whichfilename, "a")

    infofile.write(pdnum + "," + course + "," + teacher + "," + room + ",")
    infofile.close()

def RetrieveInfo():
    schedule = []
    if path.exists(whichfilename):
        infofile = open(whichfilename, "r")
        content = infofile.read()
        infofile.close()
        items = content.split(",")
        for i in range(0, len(items)-1, 4):
            if i+3 < len(items):
                schedule.append(items[i:i+4])
    else:
        return render_template('output.html', schedule=[])
    
    return render_template('output.html', schedule=schedule)

if __name__ == '__main__':
    app.run()
