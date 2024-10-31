from flask import Flask, request, render_template

app = Flask(__name__)

table_data = [
    {
        "Name": "Abhay",
        "Age": 25,
        "City": "Bangalore"
    },
    {
        "Name": "Kiara",
        "Age": 32,
        "City": "Mumbai"
    },
    {
        "Name": "Madhuri",
        "Age": 37,
        "City": "Delhi"
    },
    {
        "Name": "Vijay",
        "Age": 43,
        "City": "Chennai"
    },
    {
        "Name": "Varun",
        "Age": 23,
        "City": "Pune"
    }
]

@app.route('/')
def index():
    return render_template('index.html', tab=table_data)

if __name__ == '__main__':
    app.run(debug=True)