import sqlite3

def _con():
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    return con, cur

def init():
    con,cur = _con()
    cur.execute('''CREATE TABLE users
               (id text primary key, password text, usage real)''')
    con.commit()
    con.close()

def remove_all():
    con,cur = _con()
    cur.execute("DELETE FROM users")
    con.commit()
    con.close()

def check(u_id, password):
    con,cur = _con()
    cur.execute("select * from users where id=:u_id, password=:pass", {"u_id": u_id, "pass": password})
    return len(cur.fetchall())>0

def check_and_append(u_id, password):
    con,cur = _con()
    cur.execute("select * from users where id=:u_id", {"u_id": u_id})
    user_list = cur.fetchall()
    if (len(user_list) == 0):
        print("user doesnt exist, adding")
        cur.execute("insert into users values (?, ?, ?)", (u_id, password, 0))
        con.commit()
        return 0
    else:
        if (user_list[1] == password):
            return user_list[0][-1]
        return None

def check_and_add(u_id, password, add:float):
    con, cur = _con()
    cur.execute("select * from users where id=:u_id", {"u_id": u_id})
    user_list = cur.fetchall()
    if (u_id == ""):
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

def print_all():
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