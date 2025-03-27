import os.path
from os import path
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def main():
    if request.method == 'GET':
        return render_template('AskInfo.html')
    else:
        GetInfo()
        return render_template('AskInfo.html')

@app.route('/info', methods=['GET', 'POST'])
def GetInfo():
    global username,userpassword;

    username=request.form.get('txtusername')
    userpassword=request.form.get('txtuserpassword')
    
    while True:
        if (username=="" or userpassword==""):
            return render_template('AskInfo.html', valid="Please enter all information.")

    FileConnectivity()
    
    fileinfo=open(filename, "r")
    userinfo=fileinfo.read(),split(",")
    fileinfo.close();

    username=userinfo[0].strip();
    userpassword=userinfo[1].strip();
    


    
    return render_template('Output.html', username=username, password=userpassword)


def FileConnectivity():
    global exist, filename
    filename = "userinfo.txt"
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    fileexist = bool(path.exists(filename))
    if (fileexist == True):
        WriteFile()
    else:
        pythfile = open(filename, "x")
        pythfile.close();
        WriteFile()

def WriteFile():
    pythfile = open(filename, "w")
    pythfile.write(username + "," + userpassword)
    pythfile.close();

if __name__ == "__main__":
    app.run()
 
