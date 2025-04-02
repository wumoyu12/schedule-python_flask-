
from flask import Flask, render_template, request, redirect
import os.path
from os import path

app = Flask(__name__)
whichfilename = "schedule.txt"
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

@app.route('/')
def main():
    return render_template('personinfo.html')

@app.route("/info", methods=['POST'])
def GetInfo():
    # 清空旧数据
    if path.exists(whichfilename):
        open(whichfilename, "w").close()
    
    # 获取课程数据
    periods_data = []
    for i in range(1, 9):
        course = request.form.get("course" + str(i), "")
        teacher = request.form.get("teacher" + str(i), "")
        room = request.form.get("room" + str(i), "")
        
        if course == "" or teacher == "" or room == "":
            return render_template('personinfo.html', valid="所有字段都必须填写。如果不适用请输入'n/a'")
        
        if course == "n/a":
            course = "No Class"
        if teacher == "n/a":
            teacher = "No Teacher"
        if room == "n/a":
            room = "No Room"
        
        periods_data.append((course, teacher, room))
    
    # 写入文件(周一到周五相同课程)
    for day in weekdays:
        for period in range(8):
            pdnum = f"{day} Period {period+1}"
            course, teacher, room = periods_data[period]
            WriteToFile(pdnum, course, teacher, room)
    
    return RetrieveInfo()

def WriteToFile(pdnum, course, teacher, room):
    infofile = open(whichfilename, "a")
    infofile.write(pdnum + "," + course + "," + teacher + "," + room + ",")
    infofile.close()

def RetrieveInfo():
    schedule = []
    if path.exists(whichfilename):
        infofile = open(whichfilename, "r")
        content = infofile.read()
        infofile.close()
        items = [item for item in content.split(",") if item]
        for i in range(0, len(items), 4):
            if i+3 < len(items):
                schedule.append(items[i:i+4])
    
    return render_template('output.html', schedule=schedule)

if __name__ == '__main__':
    app.run(debug=True)
