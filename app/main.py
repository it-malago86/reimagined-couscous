from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Carica la landing page
    return render_template('landing.html')

@app.route('/vetrina')
def shop():
    # Carica il catalogo prodotti
    products_path = os.path.join('data', 'products.json')
    try:
        with open(products_path, 'r') as f:
            products = json.load(f)
    except Exception as e:
        print(f"Errore caricamento prodotti: {e}")
        products = []
    
    return render_template('index.html', products=products, phone="3912345678")

if __name__ == '__main__':
    # debug=True è fondamentale per vedere gli errori nel terminale
    app.run(host='0.0.0.0', port=5000, debug=True)
