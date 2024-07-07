from flask import Flask, request, render_template, redirect, url_for
from adafruit_motorkit import MotorKit
import threading
import time

app = Flask(__name__)
kit = MotorKit()

def run_motor(duration):
    kit.motor1.throttle = 1.0
    time.sleep(duration)
    kit.motor1.throttle = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_motor', methods=['POST'])
def start_motor():
    kit.motor1.throttle = 1.0
    return redirect(url_for('index'))

@app.route('/stop_motor', methods=['POST'])
def stop_motor():
    kit.motor1.throttle = 0
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
