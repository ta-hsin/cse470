from view import View
from model import Model


class Controller:
    def __init__(self):
        super().__init__()
        self.view = View(self)

    def show_main(self, username, password, top):
        Model.login(self, username, password, top)

    def submit(self, name, email, address, gender, course, phone, total_fee):
        Model.submit(self, name, email, address, gender, course, phone, total_fee)

    def edit_fee(self, stuent_email,  total_fee, paid_fee_entry):
        Model.editfee(self, stuent_email, total_fee, paid_fee_entry)

    def add_amount(self, add_amount, student_phone):
        Model.add_amount(self, add_amount, student_phone)

    def show_student_details(self, var):
        Model.showdetails(self, var)

    def show_visitors_details(self, var):
        Model.show_visitors_details(self, var)

    def input_enquiry(self, e_name, e_mail, e_phone, e_purpose):
        Model.put_enquiry(self, e_name, e_mail, e_phone, e_purpose)

    def show_reg(self, reg_form):
        reg_form

    def fee_option(self, fee_option):
        fee_option

    def show_std_details(self, std_det_opt):
        std_det_opt

    def root(self):
        self.view.root

    def enquiry_option(self, e):
        e

    def show_visitor(self, var):
        var

if __name__ == '__main__':
    c = Controller()
    c.root()
