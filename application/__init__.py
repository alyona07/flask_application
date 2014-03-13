from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/', methods = ['GET', 'POST'])
def index():
    """
    Just a test enter
    """
    data_new = {"layout": "Some text",
            "title": "Super Test",
            "header": "HE-HE-HE-HE... Hello World!!",
            "lines": [
                {"title": "0", "columns": ["first_00", "first_01", "first_02", "first_03"]},
                {"title": "1", "columns": ["second_10", "second_11", "second_12", "second_13"]},
                {"title": "0", "columns": ["third_20", "third_21", "third_22", "third_23"]},
                {"title": "1", "columns": ["fourth_30", "fourth_31", "fourth_32", "fourth_33"]},
            ]
    }
    if request.method == 'POST':
        word = str(request.form['text'])
        some = str(request.form['text1'])

    else:
        word = str(request.args.get('text'))
        some = str(request.args.get('text1'))


    return render_template('index.html', word={'entered': [word , some]}, data_new = data_new, data = {} )




if __name__ == "__main__":
    app.run(host="localhost", port=5000)

def word():
    if request.method == 'POST':
        word = str(request.form['text'])
        lang = str(request.form['lang'])
    else:
        word = str(request.args.get('text'))
        lang = str(request.args.get('lang'))

    if word == 'None' and lang == 'None':
        return render_template('index.html', word={'entered': word}, data={})
