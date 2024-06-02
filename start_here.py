import View.root_list_disp as root
from queue import Queue
from shared import shared_memory
from HWComponents.Listen_HW_changes import overseeer


comms = shared_memory()


comms.rfid_queue_in = Queue()
comms.Check_in_button = 0
comms.Check_out_button = 0
comms.newuser = 0


start_window = root.main_window()
wh_components = overseeer(start_window)
wh_components.run()

start_window.mainloop()