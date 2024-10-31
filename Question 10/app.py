from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        temp = request.form['celsius']
        try:
            temp = float(temp)

        except ValueError:
            return render_template('index.html', error='Invalid input. Please enter a number.', fahrenheit='')

        fahrenheit = (temp * 9/5) + 32
        return render_template('index.html', fahrenheit=fahrenheit, error='')
    
    return render_template('index.html', fahrenheit='', error='')

if __name__ == '__main__':
    app.run(debug=True)