import View.root_list_disp as root
from queue import Queue

rfid_queue_in = Queue()
rfid_queue_out = Queue()
writing_queue = Queue()
reading_queue = Queue()


start_window = root.main_window(rfid_queue_in,rfid_queue_out,writing_queue,reading_queue)

start_window.mainloop()