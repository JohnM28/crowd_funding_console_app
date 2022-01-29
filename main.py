import db_io

class Login():
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
            print("ERROR no such email exists \n")
            print(self.email)
            return False
        if self.passwd != db_io.get_passwd(self.passwd):
            print("ERROR password doesnt match \n")
            print(self.passwd)
            return False
        else:
            return True
    def log(self):
        print(self.passwd)
        self.check_cerd()


class Register:
    # Constructor
    # id = 1
    def __init__(self, email, f_name, l_name,  passwd, phone):
        self.email = email
        self.f_name = f_name
        self.l_name = l_name
        self.passwd = passwd
        self.phone = phone
        # self.id = Register.id
        db_io.add_user(self.email, self.f_name, self.l_name, self.passwd, self.phone)
        # Register.id = +1

    @classmethod
    def reg(cls):
        return cls(
            input("email: "),
            input("first name: "),
            input("last name: "),
            input("password: "),
            input("phone: "),
        )



class Projects():
    id = db_io.max_id()
    def __init__(self,title= None, details= None, target= None, st_time= None, e_time= None, email = None):
        self.title = title
        self.details = details
        self.target = target
        self.st_time = st_time
        self.e_time = e_time
        self.email = email
        self.id = Projects.id
        db_io.add_project(self.id, self.title, self.details, self.target, self.st_time, self.e_time, self.email)
        Projects.id = +1

    @classmethod
    def prog(cls, email):
        return cls(
            input("Title: "),
            input("Details: "),
            input("Target: "),
            input("Start 'use a dd-mm-yy formula': "),
            input("End: 'use a dd-mm-yy formula': "),
            email,
        )


class Interface():
    def start_page(self):
        print(f'Welcome to the main page!')
        while True:
            print("choose from the menu:")
            nav = input("1)Register \n2)Login")
            if nav == "1":
                Register.reg()
            if nav == "2":
                self.user = Login.cred()
                if self.user.check_cerd():
                    break


    def project_page(self):
        while True:
            print(f'\nWelcome to projects page {self.user.email}!')
            print("choose from the menu:")
            nav = input("1)Create new project \n2)View all projects \n3)View your projects \n3)edit your projects \n4)delete your projects")
            if nav == "1":
                Projects.prog(self.user.email)
                print("project created successfully")
            if nav == "2":
                db_io.get_projects()
                input("press any key when you are done")
            if nav == "3":
                db_io.get_user_projects(self.user.email)
                input("press any key when you are done")
            if nav == "4":
                pass
            if nav == "5":
                d_title = input("whats the title of your project you want to delete")
                db_io.delete_table(self.user.email, d_title)

    def run(self):
        self.start_page()
        self.project_page()

if __name__ == "__main__":
    Interface().run()

