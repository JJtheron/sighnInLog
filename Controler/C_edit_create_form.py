from Model.Database_talk import Read_write_data

import time
class c_create_entry():
    def __init__(self,window):
        self.window = window
        self.translation = {
                            "ID":"en_id",
                            "Name":"name",
                            "Company Name":"company_name",
                            "Person Visiting":"visiting_who",
                            "Phone Number":"phone",
                            "Tag#":"tag_id"
                            }
        self.WRdata = Read_write_data("127.0.0.1",
                                      "root",
                                      "Copy_is_evel",
                                      "sighn_in_sighn_out")
    def submit_info(self):
        send_data = {"time_in":time.strftime('%Y-%m-%d %H:%M:%S')}
        for key in self.window.user_info:
            send_data[self.translation[key]]=self.window.user_info[key]
        send_data["time_out"] = None
        self.window.user_info["ID"] = self.WRdata.add_record(send_data)
        self.window.user_info["Time In"]  = send_data["time_in"]
        self.window.user_info["Time Out"]  = send_data["time_out"]
        self.window.parent.main_window.insert_new_entry(self.window.user_info)