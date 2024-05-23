import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from threading import Thread
from shared import shared_memory
from queue import Queue
import time
# read the tag ID and put it in the given queu
class readRFID(Thread):
        def __init__(self):
            super().__init__()
            self.queue = shared_memory()
    
        def run(self):
            reader = SimpleMFRC522()
            try:
                id = reader.read()
                self.queue.put(id)
            finally:
                GPIO.cleanup()
                return "fail"
            
#Use pin 22,24,26 as button for chekIN, CheckOut and newUser
#comms.Check_out_button = 0
#comms.newuser = 0

class readCheckInButton(Thread):
        def __init__(self):
            super().__init__()
            self.pin = 22
            self.queue = shared_memory()
            GPIO.setwarnings(False) # Ignore warning for now
            GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
            GPIO.setup(self.pin , GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        def button_pushed(self):
            self.queue.Check_in_button = 1
            
        def run(self):
            GPIO.add_event_detect(self.pin ,GPIO.RISING,callback=self.button_pushed)
            while True:
                time.sleep(100)

class readCheckOUTButton(Thread):
        def __init__(self):
            super().__init__()
            self.pin = 24
            self.queue = shared_memory()
            GPIO.setwarnings(False) # Ignore warning for now
            GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
            GPIO.setup(self.pin , GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        def button_pushed(self):
            self.queue.Check_out_button = 1
            
        def run(self):
            GPIO.add_event_detect(self.pin ,GPIO.RISING,callback=self.button_pushed)
            while True:
                time.sleep(100)

class readCheckNewUserButton(Thread):
        def __init__(self):
            super().__init__()
            self.pin = 26
            self.queue = shared_memory()
            GPIO.setwarnings(False) # Ignore warning for now
            GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
            GPIO.setup(self.pin , GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        def button_pushed(self):
            self.queue.newuser = 1
            
        def run(self):
            GPIO.add_event_detect(self.pin ,GPIO.RISING,callback=self.button_pushed)
            while True:
                time.sleep(100)

class overseeer(Thread):
    def __init__(self):
        super().__init__()
        self.comms = shared_memory()
        self.rfid_read = readRFID()
        self.new_user_button = readCheckNewUserButton()
        self.checkin_button = readCheckInButton()
        self.checkout_button = readCheckOUTButton()
    def run(self):
        self.rfid_read.start()
        self.new_user_button.start()
        self.checkin_button.start()
        self.checkout_button.start()
        while True:
            print(f"{comms.rfid_queue_in.get()}--{comms.Check_in_button}--{comms.Check_out_button}--{comms.newuser}")
            time.sleep(30)

if __name__ == "__main__":
    comms = shared_memory()
    comms.rfid_queue_in = Queue()
    comms.Check_in_button = 0
    comms.Check_out_button = 0
    comms.newuser = 0
    over = overseeer()
    over.start()