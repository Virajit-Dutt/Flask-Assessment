from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form['username']
        pwd = request.form['password']
        
        if name == 'user' and pwd == 'password':
            return redirect(url_for('home'))
        else:
            return render_template('index.html', error='Invalid Credentials. Please try again.')
        
    return render_template('index.html', error='')

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)