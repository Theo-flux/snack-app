from flask import Flask, render_template, request, url_for, redirect
from snack import Snack

app = Flask(__name__)

cookies = Snack(name="cookies", kind="desert")
cakes = Snack(name="cake", kind="pastries")
snack_list = [cookies,cakes]

@app.route( '/snacks', methods = [ "GET","POST" ] )
def index():
    if( request.method == "POST" ):
        snack_name = request.form[ "name" ]
        snack_kind = request.form[ "kind" ]
        new_snack = Snack( name=snack_name, kind=snack_kind )
        snack_list.append(new_snack)
        return redirect( url_for('index') )
    return render_template( 'snack.html', snacks = snack_list )

@app.route( '/snacks/new', methods=["GET", "POST"])
def new():
    if( request.method == "POST"):
        new_snack_name = request.form["name"]
        new_snack_kind = request.form["kind"]
        snack_list.append(Snack( name = new_snack_name, kind = new_snack_kind ))
    return render_template( 'new.html' )

@app.route( '/snacks/<int:id>')
def show(id):
    selected_snack = next(snack for snack in snack_list if snack.id == id)
    return render_template('show.html', snack = selected_snack)

@app.route( '/snacks/<int:id>/edit', methods = [ "GET","POST"])
def update(id):
    selected_snack = next(snack for snack in snack_list if snack.id == id)
    if(request.method == "POST" and id == selected_snack.id):
        selected_snack.name = request.form["name"]
        selected_snack.kind = request.form["kind"]
        return redirect( url_for('index') )
    return render_template('edit.html', snack=selected_snack)

@app.route( '/snacks/<int:id>/delete', methods = [ "GET","POST"])
def delete(id):
    selected_snack = next(snack for snack in snack_list if snack.id == id)
    if(request.method == "POST" and id == selected_snack.id):
        snack_list.remove(selected_snack)
        return redirect( url_for('index') )
    return render_template('delete.html', snack=selected_snack)
