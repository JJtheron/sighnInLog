from threading import Thread

from time import sleep
{"Name": "JJ", "Company Name": "JJ Co", "Person Visiting": "no one", "Phone Number": "0563165194", "TimeIn":"10/65/32 213464", "TimeOut":"10/65/32 213464"}
class Write_data_to_disk(Thread):
    def __init__(self,q):
        super().__init__()
        self.queue = q

    def run(self):
        try:           
            self.queue.put("Data_written")
        finally:
            return "fail"

class Read_data_from_disk(Thread):
    def __init__(self,q):
        super().__init__()
        self.queue = q  

    def run(self):
        try:           
            self.queue.put("Data_That_was_read")
        finally:
            return "fail"
