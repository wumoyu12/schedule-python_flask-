
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
    global status
    status = CreateCheckFile()
    for i in range(1, 9):
        global pdnum, course, teacher, room
        pdnum = "Period " + str(i)
        course = request.form.get("course" + str(i))
        teacher = request.form.get("teacher" + str(i))
        room = request.form.get("room" + str(i))
        
        result = CheckInput()
        if result != "":
            return result
    
    return RetrieveInfo()

def CheckInput():
    if course == "" or teacher == "" or room == "":
        return render_template('personinfo.html', valid="You must enter all fields. Enter 'n/a' if not applicable")
    elif course == "n/a":
        course = "No Class"
    elif teacher == "n/a":
        teacher = "No Teacher"
    elif room == "n/a":
        room = "No Room"
    
    WriteToFile()
    return ""

def CreateCheckFile():
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    fileexist = bool(path.exists(whichfilename))

    if fileexist == False:
        return "new"
    else:
        return "edit"

def WriteToFile():
    if status == "new":
        infofile = open(whichfilename, "x")
        infofile.close()
        infofile = open(whichfilename, "w")
    else:
        infofile = open(whichfilename, "a")

    infofile.write(str(pdnum) + "," + str(course) + "," + str(teacher) + "," + str(room) + ",")
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
        # 文件不存在时返回空列表
        return render_template('output.html', schedule=[])
    
    return render_template('output.html', schedule=schedule)

if __name__ == '__main__':
    app.run(debug=True)
