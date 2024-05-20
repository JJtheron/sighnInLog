import mysql.connector
from datetime import datetime

class Read_write_data():
    def __init__(self,host1,user,password,database):
        self.host = host1
        self.user = user
        self.password  = password
        self.database = database
        self.mydb = mysql.connector.connect(
            host=host1,
            user=self.user,
            password=self.password,
            database=self.database,
            auth_plugin='mysql_native_password'
        )
        self.mycursor = self.mydb.cursor()

    def get_last_500(self):
        #get the last 500 records and return in a dictionary
        rec_500 = {"key":"","name":"","time_in":"","time_out":"","company_name":"","visiting_who":"","phone":""}
        return rec_500
    
    def get_spisific_rec(self,key):
        rec_1 = {"key":"","name":"","time_in":"","time_out":"","company_name":"","visiting_who":"","phone":""}
        return rec_1
    
    def add_record(self,rec_add):
        sql = "INSERT INTO sign_in_sheet (name, time_in, time_out, company, visiting, phone_number) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (rec_add["name"],rec_add["time_in"], rec_add["time_out"],rec_add["company_name"], rec_add["visiting_who"],rec_add["phone"])
        sqlshow = f"""SELECT  en_id from sign_in_sheet where 
        name='{rec_add["name"]}' AND
        time_in='{rec_add["time_in"]}' AND
        time_out='{rec_add["time_out"]}' AND
        company='{rec_add["company_name"]}' AND
        visiting='{rec_add["visiting_who"]}' AND
        phone_number='{rec_add["phone"]}'
        """
        #self.mycursor.execute(sql, val)
        #self.mydb.commit()
        self.mycursor.execute(sqlshow)
        return self.mycursor.fetchall()[0][0]
    
    def change_record(self,key,new_record):
        return key
    
    def look_up_user_info(self,tag_id):
        user_rec = {"tag_id":"","name":"","company_name":"","phone":""}
        return user_rec
    
    def del_user_info(self,tag_id):
        return tag_id
    
    def add_new_user(self,user_rec):
        tag_id = "hello world"
        return tag_id
    
if __name__ == "__main__":
    print("")
    print("++++++++++++++++++++++++++++++populate database and look at keys++++++++++++++++++++++++")
    WRdata = Read_write_data("127.0.0.1","root","Copy_is_evel","sighn_in_sighn_out")
    newkey = WRdata.add_record({"name":"JJ","time_in":"2007-12-31 23:59:59","time_out":"2024-12-31 23:59:59","company_name":"hardCore","visiting_who":"myself","phone":"4582212784"})
    newkey1 = WRdata.add_record({"name":"JJ1","time_in":"2007-12-31 23:59:00","time_out":"2024-12-31 23:59:03","company_name":"hardCore","visiting_who":"myself","phone":"4582212784"})
    newkey2 = WRdata.add_record({"name":"JJ2","time_in":"2007-12-31 23:59:01","time_out":"2024-12-31 23:59:02","company_name":"hardCore","visiting_who":"myself","phone":"4582212784"})
    newkey3 = WRdata.add_record({"name":"JJ3","time_in":"2007-12-31 23:59:02","time_out":"2024-12-31 23:59:01","company_name":"hardCore","visiting_who":"myself","phone":"4582212784"})
    newkey4 = WRdata.add_record({"name":"JJ4","time_in":"2007-12-31 23:59:03","time_out":"2024-12-31 23:59:00","company_name":"hardCore","visiting_who":"myself","phone":"4582212784"})
    print(newkey)
    print(newkey1)
    print(newkey2)
    print(newkey3)
    print(newkey4)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("")
    print("++++++++++++++++++++++++++++++get_spisific_rec++++++++++++++++++++++++")
    new_record = WRdata.get_spisific_rec(newkey)
    new_record1 = WRdata.get_spisific_rec(newkey1)
    new_record2 = WRdata.get_spisific_rec(newkey2)
    new_record3 = WRdata.get_spisific_rec(newkey3)
    new_record4 = WRdata.get_spisific_rec(newkey4)
    print(new_record)
    print(new_record1)
    print(new_record2)
    print(new_record3)
    print(new_record4)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("")
    print("++++++++++++++++++++++++++++++get_last_500++++++++++++++++++++++++")
    print(WRdata.get_last_500())
    print("++++++++++++++++++++++++++++++change_record++++++++++++++++++++++++")
    key_new_maybe = WRdata.change_record(newkey,{"name":"JJ","time_in":"'2024-01-31 12:59:59","time_out":"2024-12-31 23:59:59","company_name":"LesshardCore","visiting_who":"myself","phone":"4582212784"})
    print(f"old_key <{newkey}> and the key of the record now <{key_new_maybe}>")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("")
    print("vvvvvvvvvvvvvvvvvvvvvvvvvvv check all recordes again vvvvvvvvvvvvvvvvvvvvv")
    print(WRdata.get_last_500())
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("")
    print("++++++++++++++++++++++++++++++add new user++++++++++++++++++++++++")
    tag_id = WRdata.add_new_user({"tag_id":"6546+65","name":"JJ_theron","company_name":"hardAss","phone":"4586516512"})
    print(tag_id)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("")
    print("+++++++++++++++++++++++++look_up_user_info+++++++++++++++++++++++++++++")
    user_rec = WRdata.look_up_user_info(tag_id)
    print(user_rec)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("")
    print("+++++++++++++++++++++++++del_user_info+++++++++++++++++++++++++++++")
    user_tag_delete = WRdata.del_user_info(tag_id)
    print(user_tag_delete)
    print("--------------------------the below should be empty--------------")
    user_rec2 = WRdata.look_up_user_info(user_tag_delete)
    print(user_rec2)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("")