from flask import Flask, render_template, json
import os

app = Flask(__name__)

def load_products():
    with open('data/products.json', 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    products = load_products()
    # Numero di telefono dell'artigiano (da configurare)
    whatsapp_number = "393331234567" 
    return render_template('index.html', products=products, phone=whatsapp_number)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
