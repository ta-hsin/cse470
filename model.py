import sqlite3
from tkinter import END


class Model:
    def __init__(self):
        super().__init__()

    def login(self, username, password, top):
        if username == 1 and password == 1:
            top
        else:
            print("Invalid")

    def submit(self, name, email, address, gender, course, phone, total_fee):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()

        c.execute("INSERT INTO data VALUES (:name, :email, :address, :gender, :course, :phone, :total_fee)",
                  {
                      'name': name,
                      'email': email,
                      'address': address,
                      'gender': gender,
                      'course': course,
                      'phone': phone,
                      'total_fee': total_fee
                  }
                  )

        conn.commit()
        conn.close()

        print("success")

    def put_enquiry(self, e_name, e_mail, e_phone, e_purpose):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()

        c.execute("INSERT INTO enquiry VALUES (:name, :email, :phone, :purpose)",
                  {
                      'name': e_name,
                      'email': e_mail,
                      'phone': e_phone,
                      'purpose': e_purpose
                  }
                  )

        conn.commit()
        conn.close()

        print("success")

    def showdetails(self, var):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("SELECT * FROM data")
        records = c.fetchall()
        print_record=''
        res = ''
        for r in records:
            print_record += str(r) + "\n"
            res = str(print_record)[1:-1]

        print(res)
        conn.commit()
        conn.close()

    def show_visitors_details(self, var):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("SELECT * FROM enquiry")
        records = c.fetchall()
        print_record = ''
        res=''
        for r in records:
            print_record += str(r) + "\n"
            print_record.split(",")
            res = str(print_record)[1:-1]

        conn.commit()
        conn.close()
        print(res)


    def editfee(self, student_email, total_fee, paid_fee):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()

        c.execute("SELECT * FROM data WHERE phone= " + student_email)
        records = c.fetchall()
        print(records)

        for r in records:
            total_fee.insert(6, r[6])
            paid_fee.insert(7, r[7])
        # name_editor.insert(0, r[0])
        # address_editor.insert(0, r[1])
        # phone_editor.insert(0, r[2])

    def add_amount(self, add_amount, student_phone):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        add_amount = add_amount
        student_phone = student_phone

        query = """UPDATE data SET paid_fee = ? where phone = ?"""
        data = (add_amount, student_phone)
        c.execute(query, data)
        conn.commit()
        conn.close()
