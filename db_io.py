import sqlite3

with sqlite3.connect('useres.db') as conn:
    cur = conn.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS user_info2 (email TEXT PRIMARY KEY, f_name TEXT, l_name TEXT, password TEXT,phone TEXT);"
)

cur.execute(
    "CREATE TABLE IF NOT EXISTS project_info2 (id integer PRIMARY KEY, title TEXT,details TEXT, target integer, st_date TEXT, t_date TEXT , email TEXT ,FOREIGN KEY (email) references user_info2 (email) );"
)

def add_user(email, f_name, l_name, passwd, phone):
        cur.execute(
            "INSERT INTO user_info2 VALUES (?,?,?,?,?);",
            (email, f_name, l_name, passwd, phone,)
        )
        conn.commit()

def add_project(id, title, details, target, st_date,t_date,email):
    cur.execute(
        "INSERT INTO project_info2 VALUES (?,?,?,?,?,?,?);",
        (id, title, details, target, st_date,t_date,email,)
    )
    conn.commit()


def get_email(email):
    try:
        cur.execute(
            "SELECT email FROM user_info2 where email = ?",
            (email, )
        )
        ret_email = cur.fetchall()[0][0]
        conn.commit()
        return ret_email
    except Exception:
        pass

def get_passwd(passwd):
    try:
        cur.execute(
            "SELECT password FROM user_info2 where password = ?",
            (passwd, )
        )
        ret_passwd = cur.fetchall()[0][0]
        print(ret_passwd)
        conn.commit()
        return ret_passwd
    except Exception:
        pass

def max_id():
    cur.execute(
        "SELECT * FROM project_info2 order by id desc limit 1",
    )
    ret_id = cur.fetchall()[0][0]
    print(ret_id)
    return ret_id

def get_projects():
    for row in cur.execute(
        "SELECT * FROM project_info2"
    ):
        print (f'Title: {row[1]}. \nDescription: {row[2]}. \nTarget: {row[3]}EGP\n\n')

def get_user_projects(email):
    for row in cur.execute(
        "SELECT * FROM project_info2 where email = ?",
            (email,)
    ):
        print (f'Title: {row[1]}. \nDescription: {row[2]}. \nTarget: {row[3]}EGP\n\n')

def delete_table(email, title):
    try:
        cur.execute(
            "SELECT email FROM user_info2 where email = ? AND title = ?",
            (email,title,)
        )
        print("Deleted Successfully")
    except Exception:
        print("no project to delete")

# def udpate_table(email, title):
#     try:
#         print("Updated Successfully")
#     except Exception:
#         print("no project to update")