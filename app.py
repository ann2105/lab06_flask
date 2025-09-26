from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        value = request.form['value']
        return render_template('form.html', name=name, email=email, value=value)
    return render_template('form.html')

@app.route('/data')
def data():
    products = []
    with open('data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            products.append(row)
    return render_template('data.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
