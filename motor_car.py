from flask import Flask
from flask import render_template, request
import RPi.GPIO as GPIO
import time


app = Flask(__name__)

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    print ("Done")
a=1
@app.route("/")
def index():
    return render_template('robot.html')

@app.route('/forward')
def forward():
    init()
    GPIO.output(11,False)
    GPIO.output(12,True)
    GPIO.output(21,True)
    GPIO.output(22,False)
    return 'true'

@app.route('/reverse')
def reverse():
    init()
    GPIO.output(11,True)
    GPIO.output(12,False)
    GPIO.output(21,False)
    GPIO.output(22,True)
    return 'true'

@app.route('/right')
def right():
    init()
    GPIO.output(11,True)
    GPIO.output(12,True)
    GPIO.output(21,True)
    GPIO.output(22,False)
    return 'true'

@app.route('/left')
def left():
    init()
    GPIO.output(11,False)
    GPIO.output(12,True)
    GPIO.output(21,False)
    GPIO.output(22,False)
    return 'true'

@app.route('/stop')
def stop():
    init()
    data1="STOP"
    GPIO.output(11 , 0)
    GPIO.output(12 , 0)
    GPIO.output(21 , 0)
    GPIO.output(22 , 0)
    return  'true'



if __name__ == "__main__":
 print ("Start")
 app.run(host='0.0.0.0',port=5000)