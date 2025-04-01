from flask import Flask, render_template, request
import os
from os import path

app = Flask(__name__)
whichfilename = "schedule.txt"

@app.route('/')
def main():
    return render_template('personinfo.html')

@app.route("/info", methods=['POST'])
def storeinfo():
    schedule = []
    
    for i in range(1, 9):
        course = request.form.get("course" + str(i), "N/A")
        teacher = request.form.get("teacher" + str(i), "N/A")
        room = request.form.get("room" + str(i), "N/A")
        
        schedule.append(["Period " + str(i), course, teacher, room])
    
    # 保存到文件
    WriteToFile(schedule)
    
    # 从文件读取并显示
    return RetrieveInfo()

def WriteToFile(schedule):
    with open(whichfilename, 'w') as f:
        for item in schedule:
            f.write(','.join(item) + '\n')

def RetrieveInfo():
    if not path.exists(whichfilename):
        return render_template('output.html', schedule=[])
    
    schedule = []
    with open(whichfilename, 'r') as f:
        for line in f:
            items = line.strip().split(',')
            if len(items) == 4:  # 确保有4个字段
                schedule.append(items)
    
    return render_template('output.html', schedule=schedule)

if __name__ == '__main__':
    app.run()
