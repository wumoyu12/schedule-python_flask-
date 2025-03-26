from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('personinfo.html')
    else:
        return GetInfo()

def GetInfo():
    schedule_data = []
    headings = ["Period", "Course Name", "Teacher", "Room Number"]
    error_message = ""
    
    for i in range(0,8):
        course = request.form.get(f'txtcourse{i}')
        teacher = request.form.get(f'txttname{i}')
        room = request.form.get(f'txtroom{i}')
        
        what = request.form.get(f'txtwhat{i}')
        where = request.form.get(f'txtwhere{i}')
        who = request.form.get(f'txtwho{i}')
        
        # Check if both class info and activity info are filled
        class_filled = course or teacher or room
        activity_filled = what or where or who
        
        if class_filled and activity_filled:
            error_message = "Error: You filled both class information and activity information for one or more periods. Please fill only one section per period."
            return render_template('personinfo.html', ifvalid=error_message)
        elif not class_filled and not activity_filled:
            error_message = "Error: You didn't provide information for one or more periods. Please fill either class information or activity information."
            return render_template('personinfo.html', ifvalid=error_message)
        
        # Add to schedule data
        if class_filled:
            schedule_data.append([
                str(i),
                course if course else "N/A",
                teacher if teacher else "N/A",
                room if room else "N/A"
            ])
        else:
            schedule_data.append([
                str(i),
                f"Activity: {what}" if what else "Free Period",
                f"Supervisor: {who}" if who else "N/A",
                f"Location: {where}" if where else "N/A"
            ])
    
    return render_template('output.html', headings=headings, data=schedule_data)

if __name__ == '__main__':
    app.run()
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def main():
    if(request.method == 'GET'):
        return render_template('personinfo.html')
    else:
        return GetInfo()

def GetInfo():
    global ifvalid

    ifvalid=""
    
    course=request.form.get('txtcourse')
    
    tname=request.form.get('txttname')
    
    room=request.form.get('txtroom')

    CheckInfo()

    return DisplayInfo()

def CheckInfo():
    
    if (course == "" or tname="" or room=="")
        ifvalid="Your input it's invalid"
        
        GetInfo()

def DisplayInfo():
    return render_template('output.html',)

if __name__=='__main__':
    app.run()
