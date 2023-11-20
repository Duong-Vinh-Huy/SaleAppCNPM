from flask import render_template, request, redirect
import dao
from app import app, login
from flask_login import login_user

@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)
@app.route("/")
def index():
    kw = request.args.get('kw')

    cates = dao.get_categories()
    prods = dao.get_products(kw)

    return render_template('index.html', categories=cates, products=prods)
@app.route('/admin/login', methods=['post'])
def admin_login():
    userna = request.form.get('username')
    passwo = request.form.get('password')

    user = dao.auth_user(userna, passwo)
    if user:
        login_user(user)
    return redirect('/admin')

if __name__ == '__main__':
    from app import admin
    app.run(debug=True)
