import sqlite3

DB_NAME = "notes.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def db_query(query, params=()):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    conn.commit()
    conn.close()


def db_fetch(query, params=()):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    result = cursor.fetchall()

    conn.close()

    return result


def db_insert(query, params=()):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    conn.commit()

    last_id = cursor.lastrowid

    conn.close()

    return last_id




def get_all_notes_from_user_id(user_id):
    return db_fetch("SELECT * FROM notes WHERE user_id = ?",(user_id,))

def add_note(title,content,user_id):
    return db_insert("INSERT INTO notes (title,content,user_id) VALUES (?,?,?)",(title,content,user_id))

def get_note(id):
    return db_fetch("SELECT * FROM notes WHERE id=?",(id,))

def delete_note(id):
    db_query("DELETE FROM notes WHERE id=?",(id,))

def update_note(id,new_content,new_title):
    db_query("UPDATE notes SET content=? , title=?  WHERE id=?",(new_content,new_title,id,))

def get_username(user_id):
    user = db_fetch(
        "SELECT username FROM users WHERE user_id=?",
        (user_id,)
    )
    return user[0]

def get_all_usernames():
    return db_fetch("SELECT username FROM users",all=True)
def get_user_by_username(name):
    return db_fetch("SELECT * FROM users WHERE username=?",(name,))

def new_user(newname,newpassword):
    db_insert("INSERT INTO users (username,password) VALUES (?,?)",(newname,newpassword))
def new_note(user_id,title,content):
    return db_insert("INSERT INTO notes (user_id,title,content) VALUES (?,?,?)",(user_id,title,content))

def nb_note_user(user_id):
    result = db_fetch(
        "SELECT COUNT(*) AS nb_notes FROM notes WHERE user_id = ?",
        (user_id,)
    )
    return result[0]["nb_notes"]
def set_username(user_id,new_username):
    db_query("UPDATE users SET username=? WHERE user_id=?",(new_username,user_id))

def get_userid_by_id(note_id):
    result = db_fetch("SELECT user_id FROM notes WHERE id=?", (note_id,))
    return result[0]["user_id"] if result else None
