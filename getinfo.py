from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def main():
    if(request.method == 'POST'):
        
        MainScreen()
        return render_template("forloopintro.html", mylistlen=mylistlen, mylist=mylist)
    else:
        return render_template("IndexFor.html")

def MainScreen():
    global mylist
    global mylistlen

    mylist=[]
    mylist=["Math", "Science", "English", "History", "Software Engineering"]
    mylistlen=len(mylist)
    return mylistlen, mylist

if __name__=="__main__":
    app.run()
