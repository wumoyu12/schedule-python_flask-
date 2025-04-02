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
    
    if path.exists(whichfilename):
        open(whichfilename, "w").close()
    
    status = "edit" if path.exists(whichfilename) else "new"
    
    for i in range(1, 9):
        pdnum = "Period " + str(i)
        course = request.form.get("course" + str(i), "")
        teacher = request.form.get("teacher" + str(i), "")
        room = request.form.get("room" + str(i), "")
        
        if course == "" or teacher == "" or room == "":
            return render_template('personinfo.html', valid="Don't leave BLANK")
        
        if course == "n/a":
            course = "No Class"
        if teacher == "n/a":
            teacher = "No Teacher"
        if room == "n/a":
            room = "No Room"
        
        WriteToFile(pdnum, course, teacher, room, status)
        status = "edit"
    
    return RetrieveInfo()

def WriteToFile(pdnum, course, teacher, room, status):
    if status == "new":
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
        for i in range(0, len(items), 4):
            if i+3 < len(items):
                schedule.append(items[i:i+4])
    
    return render_template('output.html', schedule=schedule)

if __name__ == '__main__':
    app.run()
