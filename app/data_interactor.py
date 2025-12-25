import os
import mysql.connector
from mysql.connector import errorcode, Error

def get_cnx():
    try:
        cnx = mysql.connector.connect(user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"),
                                      host=os.getenv("DB_HOST"),
                                      port=os.getenv("DB_PORT"),
                                      database=os.getenv("DB_NAME"))
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

class Connect():
    def __init__(self):
        self.cnx = get_cnx()
        if not self.cnx:
            raise ConnectionError("Cannot connect to the database")

    def get_contacts(self)->list | dict:
        try:
            with self.cnx.cursor(dictionary=True) as cursor:
                cursor.execute("select * from contacts")
                data = cursor.fetchall()
                return data
        except Error as err:
            print(f"Error db {err}")
            return {"error":str(err)}


    def create_new_contact(self,contact)->dict:
        try:
            with self.cnx.cursor() as cursor:
                sql = """INSERT INTO contacts(first_name, last_name, phone_number) VALUES (%s,%s,%s) """
                values = (contact.first_name,contact.last_name,contact.phone_number)
                cursor.execute(sql,values)
                id = cursor.lastrowid
                self.cnx.commit()
                return {"message": "Contact created successfully","id": id}
        except Error as err:
            print(f"error: {err}")
            return {f"error": err}

    def update_contact(self,id,contact)->dict | str:
        try:
            with self.cnx.cursor() as cursor:
                contact = contact.dict()
                for key,val in contact.items():
                    if val == None:
                        continue
                    cursor.execute(
                        f"""update contacts
                            set `{key}` = %s
                            WHERE id = %s
                            """,
                        (val,id)
                    )
                self.cnx.commit()
                return "The contact person was successfully updated."
        except Error as err:
            print(f"error: {err}")
            return {f"error": err}


    def delete_contact(self,id)->dict | str:
        try:
            with self.cnx.cursor() as cursor:
                cursor.execute(f"DELETE from contacts WHERE id = %s",(id,))
                self.cnx.commit()
                return "The contact was successfully deleted."
        except Error as err:
            print(f"error: {err}")
            return {f"error": err}



