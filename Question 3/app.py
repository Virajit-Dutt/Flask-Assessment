from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ans = 0
        try:
            num1 = int(request.form['num1'])
            num2 = int(request.form['num2'])
            op = request.form['op']

            print(num1, num2, op)
            if op == '+':
                ans = num1 + num2
            elif op == '-':
                ans = num1 - num2
            elif op == '*':
                ans = num1 * num2
            elif op == '/':
                ans = num1 / num2
            else:
                ans = 'Invalid Operator'

        except:
            ans = 'Invalid Input'

        return render_template('index.html', ans=ans)
    return render_template('index.html', ans='')


if __name__ == '__main__':
    app.run(debug=True)