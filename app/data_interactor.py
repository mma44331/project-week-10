import mysql.connector
from mysql.connector import errorcode



def get_cnx():
    try:
        cnx = mysql.connector.connect(user='root', password='root',
                                      host='127.0.0.1',
                                      port='3306',
                                      database='contacts_db')
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()


class Connect():
    def __init__(self):
        self.cnx = get_cnx()

    def get_contacts(self):
        cursor = self.cnx.cursor()
        cursor.execute("select * from contacts")
        data = cursor.fetchall()
        return data

    def create_new_contact(self,contact)->dict:
        cursor = self.cnx.cursor()
        sql = """INSERT INTO contacts(first_name, last_name, phone_number) VALUES (%s,%s,%s) """
        valuse = (contact.first_name,contact.last_name,contact.phone_number)
        cursor.execute(sql,valuse)
        id = cursor.lastrowid
        self.cnx.commit()
        return {"message": "Contact created successfully","id": id}

    def updeta_contact(self,id,contact):
        contact = contact.dict()
        cursor = self.cnx.cursor()
        for key,val in contact.items():
            cursor.execute(
                f"""update contacts
                    set `{key}` = %s
                    WHERE id = %s
                    """,
                (val,id)
            )
        self.cnx.commit()
        return "The contact person was successfully updated."

    def delete_contact(self,id):
        cursor = self.cnx.cursor()
        cursor.execute(f"DELETE from contacts WHERE id = %s",(id,))
        self.cnx.commit()
        return "The contact was successfully deleted."




