from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/table')
def table():
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
    f = open("text.txt", "r")
    f.readline()
    for i in range(0, len(data_new["lines"]), 1):
        data_new["lines"][i]["columns"] = list(f.readline().split())
    return render_template('table.html', data_new = data_new)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        word = str(request.form['text'])
        some1 = str(request.form['text1'])
        some2 = str(request.form['text2'])
        some3 = str(request.form['text3'])

    else:
        word = str(request.args.get('text'))
        some1 = str(request.args.get('text1'))
        some2 = str(request.args.get('text2'))
        some3 = str(request.args.get('text3'))
    f = open('text.txt', 'a')
    f.write(word)
    f.write('\t')
    f.write(some1)
    f.write('\t')
    f.write(some2)
    f.write('\t')
    f.write(some3)
    f.write('\n')
    f.close()

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)

