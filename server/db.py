import sqlite3

def _con():
    """
    Connect to database
    """
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    return con, cur

def init():
    """
    Initialize database
    """
    con,cur = _con()
    cur.execute('''CREATE TABLE users
               (id text primary key, password text, usage real)''')
    con.commit()
    con.close()

def remove_all():
    """
    Remove all rows
    """
    con,cur = _con()
    cur.execute("DELETE FROM users")
    con.commit()
    con.close()

def check_and_send(u_id, password, add:float = 0):
    """
    If username is in db and password correct, return username and usage.
    If user isnt in db, create new row.
    If password is incorrect, return dict with None.
    """
    con, cur = _con()
    cur.execute("select * from users where id=:u_id", {"u_id": u_id})
    user_list = cur.fetchall()
    if (u_id == "" or u_id == None or password == None):
        return {'username':None,'usage':None}
    if (len(user_list) == 0):
        print("user doesnt exist, adding")
        cur.execute("insert into users values (?, ?, ?)", (u_id, password, 0))
        con.commit()
        return {'username':u_id,'usage':"0.00"}
    else:
        user = user_list[0]
        if (user[1] == password):
            usage = user[-1]
            usage += add
            cur.execute("UPDATE users SET usage=? WHERE id=?;", (usage, u_id))
            con.commit()
            return {'username':u_id,'usage':"{:.2f}".format(usage)}
        else:
            print("incorrect password")
            return {'username':None,'usage':None}

def add_usage(u_id, add:float):
    """
    Add usage to userid
    """
    con, cur = _con()
    cur.execute("select * from users where id=:u_id", {"u_id": u_id})
    user_list = cur.fetchall()
    if (u_id == "" or u_id == None or len(user_list) == 0):
        return {'username':None,'usage':None}
    else:
        user = user_list[0]
        usage = user[-1]
        usage += add
        cur.execute("UPDATE users SET usage=? WHERE id=?;", (usage, u_id))
        con.commit()
        return {'username':u_id,'usage':"{:.2f}".format(usage)}

def print_all():
    """
    Prints all entries in users table
    """
    con,cur = _con()
    cur.execute("select * from users")
    print(cur.fetchall())
    con.close()

if __name__ == "__main__":
    if input("Do you want to initialize db? (y/n)").lower() == "y":
        init()
    elif input("Do you want to remove all entries in users db? (y/n)").lower() == "y":
        remove_all()
    print_all()