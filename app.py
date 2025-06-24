from password_checker import analyze_password

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    strength = None
    suggestions = []
    password = ''
    if request.method == 'POST':
        password = request.form.get('password', '')
        strength, suggestions = analyze_password(password)
    return render_template('index.html', strength=strength, suggestions=suggestions, password=password)

if __name__ == '__main__':
    app.run(debug=True)
