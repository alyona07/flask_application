from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def index():
    data = {
            "title": "Super Test",
            "header": "HE-HE-HE-HE... Hello World!!",
            "lines": [
                {"title": "Row_0", "columns": ["Cell_00", "Cell_01", "Cell_02", "Cell_03"]},
                {"title": "Row_1", "columns": ["Cell_10", "Cell_11", "Cell_12", "Cell_13"]},
                {"title": "Row_2", "columns": ["Cell_20", "Cell_21", "Cell_22", "Cell_23"]},
                {"title": "Row_3", "columns": ["Cell_30", "Cell_31", "Cell_32", "Cell_33"]},
            ]
    }
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(host="localhost", port=5000)

