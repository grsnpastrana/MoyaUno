from flask import Flask, render_template

app = Flask(_name_)


@app.route('/')
def index():
    conn =mysql.conneector.connect(
        host='localhost',
        user='root',
        password='<PASSWORD>',
        database='db'
    )
    cursor = conn.cursor()
    cursor.execute('select * from students')
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', students=students)


if _name_ == '_main_':
    app.run(host='0.0.0.0',port=5000,debug=True)