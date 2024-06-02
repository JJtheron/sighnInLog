import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from threading import Thread
from queue import Queue
import time
from signal import pause
from gpiozero import Button
from Controler.C_Push_button_func import check_out_check_in_users

class global_var():
    def __init__(self,main_window):
         self.SHARED_MEM = ""
         self.last_id_new_user = ""
         self.last_id_new_entry = ""
         self.last_id_chek_out = ""
         self.tag_age = time.time()
         self.main_window = main_window


# read the tag ID and put it in the given queu
class readRFID(Thread):
        def __init__(self,gvar):
            super().__init__()
            self.gvar = gvar
    
        def run(self):
            while True:
                reader = SimpleMFRC522()
                #try:
                self.gvar.SHARED_MEM, value = reader.read()
                self.gvar.tag_age = time.time()+5
                print(f"{self.gvar.SHARED_MEM} frid reader thread{value}")
                GPIO.cleanup()
                time.sleep(1)
            
            #finally:
class chack_on_age(Thread):
        def __init__(self,gvar):
            super().__init__()
            self.gvar = gvar
    
        def run(self):
            while True:
                if(self.gvar.tag_age < time.time()):
                    self.gvar.SHARED_MEM = ""
                time.sleep(1)


#Use pin 22,24,26 as button for chekIN, CheckOut and newUser
#comms.Check_out_button = 0
#comms.newuser = 0

class readCheckInButton(): #Thread):
        def __init__(self,gvar,rfid):
            #super().__init__()
            self.pin =2
            self.gvar = gvar
            self.rfid = rfid
            self.button = Button(self.pin)
            self.button_pushedT = Thread(target=self.button_pushed,name="button_therad_checkIn")

        def actions_on_program(self,user_id):
             cccontroller = check_out_check_in_users()
             cccontroller.checkin_known_user(user_id)
             self.gvar.main_window.controller.populate_list()

        def button_pushed(self):
            end_time = time.time() + 5
            t_now = time.time()
            while end_time >= t_now:
                t_now = time.time()
                if self.gvar.SHARED_MEM:
                    if(self.gvar.last_id_new_entry != self.gvar.SHARED_MEM):               
                        print(self.gvar.SHARED_MEM)
                        self.actions_on_program(self.gvar.SHARED_MEM)
                        self.gvar.last_id_new_entry = self.gvar.SHARED_MEM
                        self.gvar.SHARED_MEM = ""
                time.sleep(1)

            self.gvar.last_id_new_entry = ""

        def createthread_for_button(self):
             if (not self.button_pushedT.is_alive()):
                self.button_pushedT = Thread(target=self.button_pushed,name="button_therad_checkIn")
                self.button_pushedT.setDaemon(True)
                self.button_pushedT.start()

        def run(self):
            self.button.when_pressed = self.createthread_for_button
            #pause()

class readCheckOUTButton():
        def __init__(self,gvar,rfid):
            self.pin =3
            self.gvar = gvar
            self.button = Button(self.pin)
            self.rfid = rfid
            self.button_pushedT = Thread(target=self.button_pushed,name="button_therad_checkOUT")

        def button_pushed(self):
            end_time = time.time() + 5
            t_now = time.time()
            while end_time >= t_now:
                t_now = time.time()
                if self.gvar.SHARED_MEM:
                    if(self.gvar.last_id_chek_out != self.gvar.SHARED_MEM):
                        print(self.gvar.SHARED_MEM)
                        self.gvar.last_id_chek_out = self.gvar.SHARED_MEM
                        self.gvar.SHARED_MEM = ""
                    
                time.sleep(1)
            self.gvar.last_id_chek_out = ""

        def createthread_for_button(self):
             print("pushed out")
             if (not self.button_pushedT.is_alive()):
                self.button_pushedT = Thread(target=self.button_pushed,name="button_therad_checkOut")
                self.button_pushedT.setDaemon(True)
                self.button_pushedT.start()
            
        def run(self):
             self.button.when_pressed = self.createthread_for_button
            
class readCheckNewUserButton(): #Thread):
        def __init__(self,gvar,rfid):
            #super().__init__()
            self.pin = 4
            self.gvar = gvar
            self.button = Button(self.pin)
            self.rfid = rfid
            self.button_pushedT = Thread(target=self.button_pushed,name="button_therad_newUser")
        

        def actions_on_program(self,user_id):
             self.gvar.main_window.check_in_tag(user_id)

        def button_pushed(self):
            print("new_user_button")
            end_time = time.time() + 5
            t_now = time.time()
            while end_time >= t_now:
                t_now = time.time()
                if(self.gvar.last_id_new_user != self.gvar.SHARED_MEM):
                    if self.gvar.SHARED_MEM:
                        print(self.gvar.SHARED_MEM)
                        self.actions_on_program(self.gvar.SHARED_MEM)
                        self.gvar.last_id_new_user = self.gvar.SHARED_MEM
                        self.gvar.SHARED_MEM = ""
                time.sleep(1)
            self.gvar.last_id_new_user = ""
            
        def createthread_for_button(self):
             print("pushed out")
             if (not self.button_pushedT.is_alive()):
                self.button_pushedT = Thread(target=self.button_pushed,name="button_therad_create_new_user")
                self.button_pushedT.setDaemon(True)
                self.button_pushedT.start()
            
        def run(self):
             self.button.when_pressed = self.createthread_for_button

class overseeer():
    def __init__(self, main_window = None):
        #super().__init__()
        gvar = global_var(main_window)
        self.rfid_read = readRFID(gvar)
        self.rfid_age = chack_on_age(gvar)
        self.new_user_button = readCheckNewUserButton(gvar,self.rfid_read)
        #self.new_user_button.setDaemon(False)
        self.checkin_button = readCheckInButton(gvar,self.rfid_read)
        #self.checkin_button.setDaemon(False)
        self.checkout_button = readCheckOUTButton(gvar,self.rfid_read)
        #self.checkout_button.setDaemon(False)

    def run(self):
        self.rfid_age.setDaemon(True)
        self.rfid_read.setDaemon(True)
        self.rfid_age.start()
        self.rfid_read.start()
        self.new_user_button.run()
        self.checkin_button.run()
        self.checkout_button.run()


if __name__ == "__main__":
    over = overseeer()
    over.run()
    #over.kill_all_threads()
    pause()