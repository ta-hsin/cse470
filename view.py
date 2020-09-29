import sqlite3
from tkinter import *


class View:
    def visitors(self):
        v = Tk()
        v.title("Visitors")
        v.attributes('-fullscreen', True)
        v.bind("<F11>",
               lambda event: v.attributes("-fullscreen",
                                          not v.attributes("-fullscreen")))
        v.bind("<Escape>",
               lambda event: v.attributes("-fullscreen",
                                          False))
        label = Label(v, text="SCHOOL MANAGEMENT SYSTEM", font=("times new roman", 35), bg="#90EE90",
                      fg="white")
        label.pack(side=TOP, fill=X)

        show = Entry(v, width=100, fg='blue')
        show.place(x=400, y=300, width=500, height=500)

        show_btn = Button(v, text="Show", width=8, font=("times new roman", 15),
                          command=lambda: self.controller.show_visitors_details(show)).place(x=50, y=80)

    def std_details(self):
        std = Tk()
        std.title("Student Details")
        std.attributes('-fullscreen', True)
        std.bind("<F11>",
                 lambda event: std.attributes("-fullscreen",
                                              not std.attributes("-fullscreen")))
        std.bind("<Escape>",
                 lambda event: std.attributes("-fullscreen",
                                              False))
        label = Label(std, text="SCHOOL MANAGEMENT SYSTEM", font=("times new roman", 35), bg="#90EE90",
                      fg="white")
        label.pack(side=TOP, fill=X)

        var = StringVar()

        e = Entry(std, width=100, fg='blue')
        e.place(x=400, y=300, width=500, height=500)

        show_btn = Button(std, text="Show", width=8, font=("times new roman", 15),
                          command=lambda: self.controller.show_student_details(e)).place(x=50, y=80)

    def enquiry(self):
        enq = Tk()
        enq.title("Enquiry")
        enq.attributes('-fullscreen', True)
        enq.bind("<F11>",
                 lambda event: enq.attributes("-fullscreen",
                                              not enq.attributes("-fullscreen")))
        enq.bind("<Escape>",
                 lambda event: enq.attributes("-fullscreen",
                                              False))
        label = Label(enq, text="SCHOOL MANAGEMENT SYSTEM", font=("times new roman", 35), bg="#90EE90",
                      fg="white")
        label.pack(side=TOP, fill=X)

        enquiry_name = Label(enq, text="Name", font=("times new roman", 20)).pack()
        enquiry_name_entry = Entry(enq, width=20, font=("times new roman", 20))
        enquiry_name_entry.pack()

        enquiry_email = Label(enq, text="Email", font=("times new roman", 20)).pack()
        enquiry_email_entry = Entry(enq, width=20, font=("times new roman", 20))
        enquiry_email_entry.pack()

        enquiry_phone = Label(enq, text="Phone", font=("times new roman", 20)).pack()
        enquiry_phone_entry = Entry(enq, width=20, font=("times new roman", 20))
        enquiry_phone_entry.pack()

        options = {
            "Learn Programming",
            "Learn Machine Learning",
            "Fee Details",
            "Student Details"
        }
        clicked = StringVar()
        clicked.set("Select")

        enquiry_purpose = Label(enq, text="Purpose", font=("times new roman", 20)).pack()
        enquiry_purpose_entry = OptionMenu(enq, clicked, *options)
        enquiry_purpose_entry.pack()

        def save():
            self.controller.input_enquiry(enquiry_name_entry.get(), enquiry_email_entry.get(),
                                          enquiry_phone_entry.get(), clicked.get())

        btn = Button(enq, text="Show", width=8, font=("times new roman", 15), command=save)
        btn.pack()

    def fee_details(self):
        fee = Tk()
        fee.title("Course Fee")
        fee.attributes('-fullscreen', True)
        fee.bind("<F11>",
                 lambda event: fee.attributes("-fullscreen",
                                              not fee.attributes("-fullscreen")))
        fee.bind("<Escape>",
                 lambda event: fee.attributes("-fullscreen",
                                              False))

        label = Label(fee, text="SCHOOL MANAGEMENT SYSTEM", font=("times new roman", 35), bg="#90EE90",
                      fg="white")
        label.pack(side=TOP, fill=X)

        student_phone = Label(fee, text="Enter Student Phone", font=("times new roman", 20)).pack()
        student_phone_entry = Entry(fee, width=20, font=("times new roman", 20))
        student_phone_entry.pack()

        amount = Label(fee, text="Enter Amount", font=("times new roman", 20)).pack()
        amount_entry = Entry(fee, width=20, font=("times new roman", 20))
        amount_entry.pack()

        add_fee_btn = Button(fee, text="Add Fee", width=8, font=("times new roman", 15),
                             command=lambda: self.controller.add_amount(amount_entry.get(),
                                                                        student_phone_entry.get())).place(x=950, y=165)

        paid_fee = Label(fee, text="Paid Fee", font=("times new roman", 20)).pack()
        paid_fee_entry = Entry(fee, width=20, font=("times new roman", 20))
        paid_fee_entry.pack()

        total_fee = Label(fee, text="Total Fee", font=("times new roman", 20)).pack()
        total_fee_entry = Entry(fee, width=20, font=("times new roman", 20))
        total_fee_entry.pack()

        login = Button(fee, text="Login", width=8, font=("times new roman", 15),
                       command=lambda: self.controller.edit_fee(student_phone_entry.get(), total_fee_entry,
                                                                paid_fee_entry)).place(x=950, y=90)

    def reg(self):
        reg = Toplevel()
        reg.title("Main")
        reg.attributes('-fullscreen', True)
        reg.bind("<F11>",
                 lambda event: reg.attributes("-fullscreen",
                                              not reg.attributes("-fullscreen")))
        reg.bind("<Escape>",
                 lambda event: reg.attributes("-fullscreen",
                                              False))

        label = Label(reg, text="SCHOOL MANAGEMENT SYSTEM", font=("times new roman", 35), bg="#90EE90",
                      fg="white")
        label.pack(side=TOP, fill=X)

        name = Label(reg, text="Name", font=("times new roman", 20)).pack()
        name_entry = Entry(reg, width=20, font=("times new roman", 20)).pack()

        email = Label(reg, text="Email", font=("times new roman", 20)).pack()
        email_entry = Entry(reg, width=20, font=("times new roman", 20)).pack()

        address = Label(reg, text="Address", font=("times new roman", 20)).pack()
        address_entry = Entry(reg, width=20, font=("times new roman", 20)).pack()

        gender = Label(reg, text="Gender", font=("times new roman", 20)).pack()
        var = StringVar()
        var.set("male")
        R1 = Radiobutton(reg, text="Male", variable=var, value="male", font=("times new roman", 15))
        R1.pack()
        R2 = Radiobutton(reg, text="Female", variable=var, value="female", font=("times new roman", 15))
        R2.pack()

        course = Label(reg, text="Course", font=("times new roman", 20)).pack()
        options = {
            "Python",
            "Machine Learning",
            "Java",
            "Ruby",
            "C Programming"
        }
        clicked = StringVar()
        clicked.set("Select")

        course_entry = OptionMenu(reg, clicked, *options).pack()

        phone = Label(reg, text="Phone", font=("times new roman", 20)).pack()
        phone_entry = Entry(reg, width=20, font=("times new roman", 20)).pack()

        total_fee = Label(reg, text="Total Fee", font=("times new roman", 20)).pack()
        total_fee_entry = Entry(reg, width=20, font=("times new roman", 20)).pack()

        submit_button = Button(reg, text="Submit", width=8, font=("times new roman", 15),
                               command=lambda: self.controller.submit(name_entry.get(), email_entry.get(),
                                                                      address_entry.get(), var.get(),
                                                                      clicked.get(),
                                                                      phone_entry.get(), total_fee_entry.get())).pack()

    def main_view(self):
        self.root.destroy()
        main = Tk()
        main.title("Details")
        main.attributes('-fullscreen', True)
        main.bind("<F11>",
                  lambda event: main.attributes("-fullscreen",
                                                not main.attributes("-fullscreen")))
        main.bind("<Escape>",
                  lambda event: main.attributes("-fullscreen",
                                                False))

        label = Label(main, text="SCHOOL MANAGEMENT SYSTEM", font=("times new roman", 35), bg="#90EE90",
                      fg="white")
        label.pack(side=TOP, fill=X)

        var = StringVar()
        lbl = Label(main, textvariable=var).pack()

        reg = Button(main, text="Registration", width=12, font=("times new roman", 15),
                     command=lambda: self.controller.show_reg(View.reg(self))).pack()
        fee_details = Button(main, text="Fee Details", width=12, font=("times new roman", 15),
                             command=lambda: self.controller.fee_option(View.fee_details(self))).pack()
        enquiry = Button(main, text="Enquiry", width=12, font=("times new roman", 15),
                         command=lambda: self.controller.enquiry_option(View.enquiry(self))).pack()
        visitor = Button(main, text="Visitor", width=12, font=("times new roman", 15),
                         command=lambda: self.controller.show_visitor(View.visitors(self))).pack()
        student_details = Button(main, text="Student Details", width=12, font=("times new roman", 15),
                                 command=lambda: self.controller.show_std_details(View.std_details(self))).pack()

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.root = Tk()
        self.root.title('Welcome')
        self.root.attributes('-fullscreen', True)
        self.root.bind("<F11>",
                       lambda event: self.root.attributes("-fullscreen",
                                                          not self.root.attributes("-fullscreen")))
        self.root.bind("<Escape>",
                       lambda event: self.root.attributes("-fullscreen",
                                                          False))

        label = Label(self.root, text="SCHOOL MANAGEMENT SYSTEM", font=("times new roman", 35), bg="#90EE90",
                      fg="white")
        label.pack(side=TOP, fill=X)

        username = Label(self.root, text="Username", font=("times new roman", 20)).pack()
        username_entry = Entry(self.root, width=20, font=("times new roman", 20))
        username_entry.pack()
        password = Label(self.root, text="Password", font=("times new roman", 20)).pack()
        password_entry = Entry(self.root, show="*", width=20, font=("times new roman", 20))
        password_entry.pack()

        login_button = Button(self.root, text="Login", width=8, font=("times new roman", 15),
                              command=lambda: self.controller.show_main(username_entry.get(),
                                                                        password_entry.get(),
                                                                        View.main_view(self)))
        login_button.pack()

        self.root.mainloop()
