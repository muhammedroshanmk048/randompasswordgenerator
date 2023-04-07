from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    length = int(request.form['length'])
    num_special_chars = int(request.form['num_special_chars'])
    num_numbers = int(request.form['num_numbers'])

    special_chars = string.punctuation
    numbers = string.digits
    chars = string.ascii_letters

    password = ''

    for i in range(num_special_chars):
        password += random.choice(special_chars)

    for i in range(num_numbers):
        password += random.choice(numbers)

    for i in range(length - num_special_chars - num_numbers):
        password += random.choice(chars)

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
