from Model.Database_talk import Read_write_data
import time

class check_out_check_in_users():
    def __init__(self):
        self.translation = {
                            "Name":"name",
                            "Company Name":"company_name",
                            "Phone Number":"phone",
                            "Tag#":"tag_id"}
        self.WRdata = Read_write_data("127.0.0.1",
                                      "root",
                                      "Copy_is_evel",
                                      "sighn_in_sighn_out")
    def checkin_known_user(self,tag):
        entry = self.WRdata.look_up_user_info(tag)
        print("______________________________")
        print(entry)
        entry["time_in"] = time.strftime('%Y-%m-%d %H:%M:%S')
        entry["time_out"] = None
        entry["visiting_who"] = None
        print("______________________________")
        self.WRdata.add_record(entry)