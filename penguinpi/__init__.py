from __future__ import print_function

import requests
import cv2
import sys
import numpy as np

__version__ = '1.0.0'

class PiBot:
    def __init__(self, ip='localhost', port=8080):
        self.ip = ip
        self.port = port

        self.endpoint = 'http://{}:{}'.format(self.ip, self.port)

    def setVelocity(self, motor_left=0, motor_right=0, duration=None, acceleration_time=None):
        try:
            params = [
                'value={},{}'.format(motor_left, motor_right)
            ]

            if duration is not None:
                assert duration > 0, 'duration must be positive'
                assert duration < 20, 'duration must be < network timeout (20 seconds)'

                params.append('time={}'.format(duration))
            
                if acceleration_time is not None:
                    assert acceleration_time < duration / 2.0, 'acceleration_time must be < duration/2'
                    params.append('accel={}'.format(acceleration_time))

            print('{}/robot/set/velocity?{}'.format(self.endpoint, '&'.join(params)))
            resp = requests.get('{}/robot/set/velocity?{}'.format(self.endpoint, '&'.join(params)))
            
            if resp.status_code != 200:
                raise Exception(resp.text)

            return resp.json()
        except requests.exceptions.Timeout as e:
            print('Timed out attempting to communicate with {}:{}'.format(self.ip, self.port), file=sys.stderr)
            return None

    def setLED(self, number, state):
      try:
        assert number >= 2 and number <= 4, 'invalid LED number'
      
        requests.get('{}/led/set/state?id={}&value={}'.format(self.endpoint, number, 1 if bool(state) else 0))
        return True
      except requests.exceptions.Timeout as e:
        print('Timed out attempting to communicate with {}:{}'.format(self.ip, self.port), file=sys.stderr)
        return False

    def pulseLED(self, number, duration):
      try:
        assert number >= 2 and number <= 4, 'invalid LED number'
        assert duration > 0 and duration <= 0.255, 'invalid duration'
      
        requests.get('{}/led/set/count?id={}&value={}'.format(self.endpoint, number, duration * 1000))
        return True

      except requests.exceptions.Timeout as e:
        print('Timed out attempting to communicate with {}:{}'.format(self.ip, self.port), file=sys.stderr)
        return False

    def getDIP(self):
      try:
        resp = requests.get('{}/hat/dip/get'.format(self.endpoint))
        return int(resp.text)
      except requests.exceptions.Timeout as e:
        print('Timed out attempting to communicate with {}:{}'.format(self.ip, self.port), file=sys.stderr)
        return False
    
    def getButton(self):
      try:
        resp = requests.get('{}/hat/button/get'.format(self.endpoint))
        return int(resp.text)
      except requests.exceptions.Timeout as e:
        print('Timed out attempting to communicate with {}:{}'.format(self.ip, self.port), file=sys.stderr)
        return False
   
    def setLEDArray(self, value):
      try:
        requests.get('{}/hat/ledarray/set?value={}'.format(self.endpoint, int(value)))
        return True
      except requests.exceptions.Timeout as e:
        print('Timed out attempting to communicate with {}:{}'.format(self.ip, self.port), file=sys.stderr)
        return False

    def printfOLED(self, text, *args):
      try:
        requests.get('{}/hat/screen/print?value={}'.format(self.endpoint, text % args))
        return True
      except requests.exceptions.Timeout as e:
        print('Timed out attempting to communicate with {}:{}'.format(self.ip, self.port), file=sys.stderr)
        return False

    def setScreen(self, screen):
      try:
        requests.get('{}/hat/screen/set?value={}'.format(self.endpoint, int(screen)))
        return True
      except requests.exceptions.Timeout as e:
        print('Timed out attempting to communicate with {}:{}'.format(self.ip, self.port), file=sys.stderr)
        return False
    
    def stop(self):
        try:
            resp = requests.get('{}/robot/stop'.format(self.endpoint), timeout=1)
            return resp.json()
        except requests.exceptions.Timeout as e:
            print('Timed out attempting to communicate with {}:{}'.format(self.ip, self.port), file=sys.stderr)
            return None

    def resetPose(self):
        try:
            resp = requests.get('{}/robot/pose/reset'.format(self.endpoint), timeout=5)
            return True
        except requests.exceptions.Timeout as e:
            print('Timed out attempting to communicate with {}:{}'.format(self.ip, self.port), file=sys.stderr)
            return False

    def resetEncoder(self):
        try:
            resp = requests.get('{}/robot/hw/reset'.format(self.endpoint), timeout=5)
            return True
        except requests.exceptions.Timeout as e:
            print('Timed out attempting to communicate with {}:{}'.format(self.ip, self.port), file=sys.stderr)
            return False

    def getImage(self):
        try:
            resp = requests.get('{}/camera/get'.format(self.endpoint), timeout=1)
            data = np.fromstring(resp.content, np.uint8)
            return cv2.imdecode(data, cv2.IMREAD_COLOR)
        except requests.exceptions.Timeout as e:
            print('Timed out attempting to communicate with {}:{}'.format(self.ip, self.port), file=sys.stderr)
            return None

    def getVoltage(self):
        try:
            resp = requests.get('{}/battery/get/voltage'.format(self.endpoint), timeout=1)
            return float(resp.text) / 1000
        except requests.exceptions.Timeout as e:
            print('Timed out attempting to communicate with {}:{}'.format(self.ip, self.port), file=sys.stderr)
            return None
    
    def getCurrent(self):
        try:
            resp = requests.get('{}/battery/get/current'.format(self.endpoint), timeout=1)
            return float(resp.text) / 1000
        except requests.exceptions.Timeout as e:
            print('Timed out attempting to communicate with {}:{}'.format(self.ip, self.port), file=sys.stderr)
            return None
