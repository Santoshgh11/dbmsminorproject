from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # To handle cross-origin requests

# MySQL Configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = 'password'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'ecommerce'

mysql = MySQL(app)

# Home Route
@app.route('/')
def home():
    return "Backend for E-commerce Website"

# Login API
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    user = cursor.fetchone()
    cursor.close()
    if user:
        return jsonify({'message': 'Login successful', 'user_id': user[0]})
    return jsonify({'message': 'Invalid credentials'}), 401

# Signup API
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    if password != confirm_password:
        return jsonify({'message': 'Passwords do not match'}), 400

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Signup successful'}), 201

# Add to Cart API
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.json
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO cart (user_id, product_id, quantity) VALUES (%s, %s, %s)",
        (user_id, product_id, quantity)
    )
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Product added to cart'}), 201

# Fetch Cart API
@app.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT p.name, p.price, c.quantity, (p.price * c.quantity) as subtotal
        FROM products p
        JOIN cart c ON p.id = c.product_id
        WHERE c.user_id = %s
    """, (user_id,))
    cart_items = cursor.fetchall()
    cursor.close()

    cart = [{'name': item[0], 'price': item[1], 'quantity': item[2], 'subtotal': item[3]} for item in cart_items]
    total = sum(item['subtotal'] for item in cart)
    return jsonify({'cart': cart, 'total': total})

# Checkout API
@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.json
    user_id = data.get('user_id')
    address = data.get('address')
    payment_details = data.get('payment_details')

    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO orders (user_id, address, payment_details) VALUES (%s, %s, %s)",
        (user_id, address, payment_details)
    )
    order_id = cursor.lastrowid

    cursor.execute("DELETE FROM cart WHERE user_id = %s", (user_id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Order placed successfully', 'order_id': order_id}), 201

if __name__ == '__main__':
    app.run(debug=True)
