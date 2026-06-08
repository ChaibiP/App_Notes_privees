from flask import Flask, render_template, request, redirect, session
from db import *
from werkzeug.security import generate_password_hash, check_password_hash

from functools import wraps
from flask import session, redirect

app = Flask(__name__)

app.secret_key = "une_cle_secrete"

def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if "user_id" not in session:
            return redirect("/login")

        return func(*args, **kwargs)

    return wrapper



@app.get("/")
def index():
    if "user_id" in session:
        user_id=session["user_id"]
        notes=get_all_notes_from_user_id(user_id)
        username=get_username(user_id)[0]
    else:
        user_id=None
        notes=[]
        username="Pas Connecté"
    
    empty_notes=False

    if (user_id!=None and notes==[]):
        empty_notes=True

    return render_template("index.html",notes=notes,empty_notes=empty_notes,username=username,user_id=user_id)

@app.get("/login")
def login():
    return render_template("login.html")

@app.post("/login")
def postlogin():
    password=request.form["password"]
    name=request.form["name"]
    user=get_user_by_username(name)
    if not user:
        error=True
        return render_template("login.html",error=True)
    user = user[0]
    if not check_password_hash(user["password"],password):
        return render_template("login.html",error=True)
    session["user_id"]=user["user_id"]
    return redirect("/")

@app.get("/register")
def register():
    return render_template("register.html")


@app.post("/register")
def postregister():
    new_name=request.form["new_name"]
    new_password=request.form["new_password"]
    new_password=generate_password_hash(new_password)
    user = get_user_by_username(new_name)
    if user:
        return "Erreur Connexion , utilisateur deja existant"
    else:
        new_user(new_name,new_password)
        return redirect("/login")

@app.get("/add_note")
@login_required

def addnote():
    user_id=session["user_id"]
    return render_template("addnote.html",user_id=user_id)    

@app.post("/add_note")
@login_required
def postaddnote():
    newtitle=request.form["title"]
    newcontent=request.form["content"]
    user_id=request.form["userid"]
    new_note(user_id,newtitle,newcontent)
    return redirect("/")


@app.get("/notes/<note_id>")
@login_required
def note(note_id):
    user_id=get_userid_by_id(note_id)
    if session["user_id"]!=int(user_id):
        return "Ce n'est pas votre note vous ne pouvez pas la supprimer"
    note = get_note(note_id)
    if not note:
        return "Note introuvable"
    note = note[0]
    return render_template("note.html", note=note)

@app.post("/delete/<note_id>")
@login_required
def deletenote(note_id):
    user_id=get_userid_by_id(note_id)
    if session["user_id"]!=int(user_id):
        return "Ce n'est pas votre note vous ne pouvez pas la supprimer"
    delete_note(note_id)
    return redirect("/")

@app.post("/logout")
@login_required
def logout():
    session.clear()
    return redirect("/")

@app.get("/update/<note_id>")
@login_required
def update(note_id):
    user_id=get_userid_by_id(note_id)
    if session["user_id"]!=int(user_id):
        return "Ce n'est pas votre note vous ne pouvez pas la supprimer"
    note=get_note(note_id)
    if not note:
        return "Note introuvable"
    note=note[0]
    return render_template("update.html",note=note)


@app.post("/update/<note_id>")
@login_required
def postupdate(note_id):
    user_id=get_userid_by_id(note_id)
    if session["user_id"]!=int(user_id):
        return "Ce n'est pas votre note vous ne pouvez pas la supprimer"
    newcontent=request.form["content"]
    newtitle=request.form["title"]
    update_note(note_id,newcontent,newtitle)
    return redirect("/")
@app.get("/my_account/<user_id>")
@login_required
def myaccount(user_id):
    if session["user_id"]!=int(user_id):
        return "Vous n'avez pas acces a cette page !"
    user_id=user_id
    username=get_username(user_id)
    username=username[0]
    nb_note=nb_note_user(user_id)
    return render_template("myaccount.html",username=username,nb_note=nb_note,user_id=user_id)

@app.get("/updateaccount/<user_id>")
@login_required
def updateaccount(user_id):
    if session["user_id"]!=int(user_id):
        return "Vous n'avez pas acces a cette page !"
    username=get_username(user_id)
    username=username[0]
    return render_template("updateaccount.html",username=username,user_id=user_id)

@app.post("/updateaccount/<user_id>")
@login_required
def postupdateaccount(user_id):
    if session["user_id"]!=int(user_id):
        return "Vous n'avez pas acces a cette page !"
    new_username=request.form["username"]
    set_username(user_id,new_username)
    return redirect("/")

@app.get("/search")
def search():
    query=request.args.get("q","")
    search=f"%{query}%"
    notes_trouvées=get_note_search(search)
    user_id=session.get("user_id")
    username=get_username(user_id)[0]
    return render_template("index.html",notes=notes_trouvées,user_id=user_id,username=username,is_search=True)


            
if __name__ == "__main__":
    app.run(debug=True, port=5000)




