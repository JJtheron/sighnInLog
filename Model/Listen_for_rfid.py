#import RPi.GPIO as GPIO
#from mfrc522 import SimpleMFRC522
from threading import Thread
#from threading import Lock

class readRFID(Thread):
        def __init__(self,q):
            super().__init__()
            self.queue = q
            

        def run(self):
            #reader = SimpleMFRC522()
            try:
                #id, text = reader.read()
                #print(id)
                #print(text)
                
                input()
                self.queue.put("test")
            finally:
                #GPIO.cleanup()
                return "fail"
