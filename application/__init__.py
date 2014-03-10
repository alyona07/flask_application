from flask import Flask, render_template, url_for

app = Flask(__name__)



@app.route('/')
def index():
    """
    Just a test enter
    """
    data = {
            "title": "Super Test",
            "header": "HE-HE-HE-HE... Hello World!!",
            "lines": [
                {"title": "0", "columns": ["first_00", "first_01", "first_02", "first_03"]},
                {"title": "1", "columns": ["second_10", "second_11", "second_12", "second_13"]},
                {"title": "0", "columns": ["third_20", "third_21", "third_22", "third_23"]},
                {"title": "1", "columns": ["fourth_30", "fourth_31", "fourth_32", "fourth_33"]},
            ]
    }

    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(host="localhost", port=5000)

