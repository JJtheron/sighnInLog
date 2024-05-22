from Model.Database_talk import Read_write_data
import time
class c_create_entry():
    def __init__(self,window):
        self.window = window
        self.translation = {
                            "Name":"name",
                            "Company Name":"company_name",
                            "Person Visiting":"visiting_who",
                            "Phone Number":"phone"
                            }
        self.WRdata = Read_write_data("127.0.0.1",
                                      "root",
                                      "Copy_is_evel",
                                      "sighn_in_sighn_out")
    def submit_info(self):
        send_data = {"time_in":time.strftime('%Y-%m-%d %H:%M:%S')}
        for key in self.translation:
            send_data[self.translation[key]]=self.window.user_info[key]
        send_data["time_out"]= '1000-12-12 12:12:12'
        self.WRdata.add_record(send_data)