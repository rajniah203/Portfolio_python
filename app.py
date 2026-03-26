from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send', methods=['POST'])
def send():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    print(name, email, message)

    return redirect('/contact')

if __name__ == '__main__':
    app.run(debug=True)