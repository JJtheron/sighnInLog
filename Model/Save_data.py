from threading import Thread

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
