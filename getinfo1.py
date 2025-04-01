from flask import Flask, render_template, request
import os.path
from os import path

app = Flask(__name__)
whichfilename = "schedule.txt"

@app.route('/')
def main():
    return render_template('personinfo.html')

@app.route("/info", methods=['POST'])
def GetInfo():
    schedule = []
    
    # 先收集所有数据
    for i in range(1, 9):
        pdnum = "Period " + str(i)
        course = request.form.get("course" + str(i), "N/A")
        teacher = request.form.get("teacher" + str(i), "N/A")
        room = request.form.get("room" + str(i), "N/A")
        schedule.append([pdnum, course, teacher, room])
    
    # 写入文件
    CreateCheckFile()
    with open(whichfilename, 'w') as infofile:
        for item in schedule:
            infofile.write(",".join(item) + "\n")
    
    return RetrieveInfo()
        
def CreateCheckFile():
    if not path.exists(whichfilename):
        with open(whichfilename, 'w') as f:
            pass  # 只创建空文件
    
def RetrieveInfo():
    schedule = []
    if path.exists(whichfilename):
        with open(whichfilename, 'r') as infofile:
            for line in infofile:
                items = line.strip().split(",")
                if len(items) == 4:  # 确保有4个字段
                    schedule.append(items)
    
    return render_template('output.html', schedule=schedule)

if __name__ == '__main__':
    app.run()
