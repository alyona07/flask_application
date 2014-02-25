from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def index():
    data = {
            "title": "Super Test",
            "header": "HE-HE-HE-HE... Hello World!!",
            "lines": [
                {"title": "Row_0", "columns": ["first_00", "first_01", "first_02", "first_03"]},
                {"title": "Row_1", "columns": ["second_10", "second_11", "second_12", "second_13"]},
                {"title": "Row_2", "columns": ["third_20", "third_21", "third_22", "third_23"]},
                {"title": "Row_3", "columns": ["fourth_30", "fourth_31", "fourth_32", "fourth_33"]},
            ]
    }
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(host="localhost", port=5000)

