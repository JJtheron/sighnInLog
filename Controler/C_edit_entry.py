from Model.Database_talk import Read_write_data
from datetime import datetime

import time
class c_edit_create():
    def __init__(self,window,pitem):
        self.window = window
        self.parent_item = pitem
        self.translation = {
                            "ID":"en_id",
                            "Name":"name",
                            "Company Name":"company_name",
                            "Person Visiting":"visiting_who",
                            "Phone Number":"phone",
                            "Tag#":"tag",
                            "Time In":"time_in",
                            "Time Out":"time_out"
                            }
        self.WRdata = Read_write_data("127.0.0.1",
                                      "root",
                                      "Copy_is_evel",
                                      "sighn_in_sighn_out")
    def look_up_value(self,en_id):
        record = self.WRdata.get_spisific_rec(en_id)
        display_values = {}
        for key in self.translation:
            display_values[key] = record[self.translation[key]]
        for i in self.window.user_info:
            self.window.get_user_info[i].set(display_values[i])
        return display_values
    
    def submit_info(self,en_id):
        send_data = {}
        send_data["time_out"]= None
        for key in self.window.user_info:
            send_data[self.translation[key]]=self.window.user_info[key]
        if send_data["time_out"]:
            send_data["time_out"]= datetime.strptime(send_data["time_out"], '%m/%d/%y %H:%M:%S')
        self.window.user_info["ID"] = self.WRdata.change_record(en_id,send_data)
        self.window.parent.main_window.controller.populate_list()