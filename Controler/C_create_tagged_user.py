from Model.Database_talk import Read_write_data

class c_entry_window_tag():
    def __init__(self,window):
        self.window = window
        self.translation = {
                            "Name":"name",
                            "Company Name":"company_name",
                            "Phone Number":"phone",
                            "Tag#":"tag_id"}
        self.WRdata = Read_write_data("127.0.0.1",
                                      "root",
                                      "Copy_is_evel",
                                      "sighn_in_sighn_out")
          
    def submit_info(self):
        send_data = {}
        for key in self.translation:
            send_data[self.translation[key]]=self.window.user_info[key]
        self.WRdata.add_new_user(send_data)