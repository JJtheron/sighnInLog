import View.root_list_disp as root
from queue import Queue
from shared import shared_memory

comms = shared_memory()

comms.rfid_queue_in = Queue()
comms.Check_in_button = 0
comms.Check_out_button = 0
comms.newuser = 0


start_window = root.main_window()

start_window.mainloop()