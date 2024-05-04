from threading import Thread
from threading import Lock
import Listen_for_rfid
from queue import Queue
from time import sleep
import Save_data


class Controller(Thread):
    def __init__(self,command, rfid_queue,writing_queue,reading_queue):
        super().__init__()

        self.action = command
        self.WRITE_DATA = "write"
        self.READ_DATA = "read"
        self.RFIDthreads = [] 
        self.reading_threads = []
        self.writing_threads = []

        self.RFIDQUEUE = rfid_queue
        self.WRITTING_QUEUE = writing_queue
        self.READING_QUEUE = reading_queue

    def __read_command_start(self):
        command = self.action.get()
        match command:
            case self.WRITE_DATA:
                self.__start_writing_queue()
            case self.READ_DATA:
                self.__start_reading_queue()   


    def run(self):
        self.__start_rfid_queue()
        while True:
            if self.action.empty():
                self.__read_command_start()
                
            sleep(1)

    def __start_rfid_queue(self):
        listenRFID = Listen_for_rfid.readRFID(self.RFIDQUEUE)
        self.RFIDthreads.append(listenRFID)
        for t in self.RFIDthreads:
            t.start()
    
    def __start_reading_queue(self):
        Reading = Save_data.Read_data_from_disk(self.READING_QUEUE)
        self.reading_threads.append(Reading)
        for t in self.threads:
            t.start()

    def __start_writing_queue(self):
        Writing = Save_data.Write_data_to_disk(self.WRITTING_QUEUE)
        self.writing_threads.append(Writing)
        for t in self.threads:
            t.start()
        
    def __check_queues(self,q):
        self.myqueue.put(q.get())
        if not self.myqueue.empty():
            for t in self.threads:
                t.join()
                return True
        sleep(1)



if __name__ == "__main__":
    rfid_queue = Queue()
    writing_queue = Queue()
    reading_queue = Queue()
    control = Controller(rfid_queue,writing_queue,reading_queue)
    control.start()
    while not q_main.empty():
        sleep(1)
    print(q_main.get())
    control.join()
    