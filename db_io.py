import sqlite3

with sqlite3.connect('useres.db') as conn:
    cur = conn.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS user_info (id integer PRIMARY KEY, f_name TEXT, l_name TEXT, email TEXT, password TEXT,phone TEXT);"
)

def add_info(id,f_name, l_name, email, passwd, phone):
        cur.execute(
            "INSERT INTO user_info VALUES (?,?,?,?,?,?);",
            (id,f_name, l_name, email, passwd, phone, )
        )
        conn.commit()
def get_email(email):
    try:
        cur.execute(
            "SELECT email FROM user_info where email = ?",
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
            "SELECT password FROM user_info where password = ?",
            (passwd, )
        )
        ret_passwd = cur.fetchall()[0][0]
        print(ret_passwd)
        conn.commit()
        return ret_passwd
    except Exception:
        pass

