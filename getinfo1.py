from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def main():
    if(request.method == 'GET'):
        return render_template('personinfo.html')
    else:
        return GetInfo()

def GetInfo():
    
    course=request.form.get('txtcourse')
    
    tname=request.form.get('txttname')
    
    room=request.form.get('txtroom')

    CheckInfo()

    return DisplayInfo()

def CheckInfo():
    if (course == "" or tname="" or room=="")
        print("")

def DisplayInfo():
    return render_template('output.html',)

if __name__=='__main__':
    app.run()
