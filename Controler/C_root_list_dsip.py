from Model.Database_talk import Read_write_data
class c_root_list_dsip():
    def __init__(self,window):
        self.window = window
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
    def populate_list(self):
        for item in self.window.tree.get_children():
            self.window.tree.delete(item)
        last500ent = self.WRdata.get_last_500()
        for row in last500ent:
            display_values = {}
            for key in self.translation:
                display_values[key] = row[self.translation[key]]
            self.window.insert_new_entry(display_values)
        
