from flask import render_template, request, redirect,session, jsonify
import dao
import utils
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

@app.context_processor
def common_response():
    return {
        'categories' : dao.get_categories(),
        'cart' : utils.count_cart(session.get('cart'))
    }

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route("/api/cart", methods=["post"])
def add_to_cart():
    data =  request.json  #lấy dữ liệu client gửi lên bằng json
    cart  =session.get('cart')
    if cart is None:
        cart = {}

    id = str(data.get('id'))
    if id in cart: # nếu đã có trong giỏ hàng
        cart[id]['quantity'] +=1
    else:
        cart[id] = {
            "id":id,
            "name": data.get("name"),
            "price" : data.get("price"),
            "quantity" : 1
        }
    session['cart'] = cart
    print(cart)


    return jsonify({
        "total_amount": 0,
        "total_quantity": 0
    })
@app.route('/api/cart/<product_id>', methods = ['put'])
def update_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
        quantity = request.json.get('quantity')
        cart[product_id]['quantity'] = int(quantity)

    session['cart'] = cart
    # return jsonify(utils.count_cart(cart))
@app.route('/api/cart/<product_id>', methods = ['delete'])
def delete_in_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
        del cart[product_id]

    session['cart'] = cart



if __name__ == '__main__':
    from app import admin
    app.run(debug=True)
