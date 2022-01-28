import db_io

class register:
    # Constructor
    id = 4
    def __init__(self, f_name, l_name, email, passwd, phone):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.passwd = passwd
        self.phone = phone
        self.id = register.id
        db_io.add_info(self.id,self.f_name, self.l_name, self.email, self.passwd, self.phone)
        register.id = +1

    @classmethod
    def reg(cls):
        return cls(
            input("first name: "),
            input("last name: "),
            input("email: "),
            input("password: "),
            input("phone: "),
        )

    # @staticmethod
    # def login(email, passwd):
    #     while True:
    #         email = input("email: ")
    #         if email != "john":
    #             pass
    #         passwd = input("password: ")
    # def check_budget(self, budget):
    #     # Check if the budget is valid
    #     if not isinstance(budget, (int, float)):
    #         print('Enter float or int')
    #         exit()
    #     if budget < 0:
    #         print('Sorry you don\'t have money')
    #         exit()
    #
    # def get_change(self, budget):
    #     return budget - self.price
    #
    # def sell(self, budget):
    #     self.check_budget(budget)
    #     if budget >= self.price:
    #         print(f'You can buy the {self.name} coffee')
    #         if budget == self.price:
    #             print('It\'s complete')
    #         else:
    #             print(f'Here is your change {self.get_change(budget)}$')
    #
    #         exit('Thanks for your transaction')

class login:
    def __init__(self, email, passwd):
        self.email = email
        self.passwd = passwd
    @classmethod
    def cred(cls):
        return cls(
            input("email: "),
            input("password: "),
        )
    def check_cerd(self):
        print(self.email +" this is email")
        if self.email != db_io.get_email(self.email):
            print("no such email exists")
            print(self.email)
        if self.passwd != db_io.get_passwd(self.passwd):
            print("password doesnt match")
            print(self.passwd)
    def log(self):
        print(self.passwd)
        self.check_cerd()


class interface(login):
    def __init__(self, email = None, passwd = None):
        print ("foobar init")
        login.__init__(self, email, passwd)
        print(self.email)
        print(self.passwd)
    def start_page(self):
        nav = input(print("to register press 1 \n to login press 2\n"))
        if nav == "1":
            register.reg()
        if nav == "2":
            self.run()
    def run(self):
        while True:
            self.cred()
            self.log()





# usr1 = user('j','m','john@gmail.com','12345','2131231')
#
# print(usr1.f_name)

# interface.start_page()

interface().run()

