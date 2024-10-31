from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route('/' , methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']    
        tasks.append(task)
        return render_template('index.html', tasks=tasks)

    return render_template('index.html', tasks='')

@app.route('/clear', methods=['POST'])
def clear():
    tasks.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)