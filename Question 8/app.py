from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
feedbacks = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        feedback = request.form['feedback']
        feedbacks[name] = feedback
        return render_template('index.html', feedbacks=feedbacks)
    
    return render_template('index.html', feedbacks=feedbacks)

@app.route('/clear', methods=['POST'])
def clear():
    feedbacks.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)