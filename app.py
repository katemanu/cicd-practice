from flask import Flask
from calculator import add, subtract, multiply

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Calculator App</h1>
    <p>Welcome! This app was deployed via CI/CD pipeline.</p>
    <ul>
        <li>2 + 3 = {}</li>
        <li>10 - 4 = {}</li>
        <li>5 x 6 = {}</li>
    </ul>
    '''.format(add(2,3), subtract(10,4), multiply(5,6))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)