""" INICIAR SERVIDOR LOCAL python app.py """

from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conexion MySQL
app.config['MYSQL_HOST'] = 'us-cdbr-east-06.cleardb.net'
app.config['MYSQL_USER'] = 'bbf7220214418e'
app.config['MYSQL_PASSWORD'] = '78d86c96'
app.config['MYSQL_DB'] = 'heroku_acd89444b840722'

mysql = MySQL(app)


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    query = 'SELECT * FROM votos'
    cur.execute(query)
    result = cur.fetchall()
    totalVotos = result[4][1]
    if (totalVotos > 0):
        primerPorc = round((100*result[0][1])/result[4][1], 2)
        segundoPorc = round((100*result[1][1])/result[4][1], 2)
        tercerPorc = round((100*result[2][1])/result[4][1], 2)
        cuartoPorc = round((100*result[3][1])/result[4][1], 2)
    else:
        primerPorc = 0
        segundoPorc = 0
        tercerPorc = 0
        cuartoPorc = 0
    return render_template('index.html', variable=totalVotos, primero=primerPorc, segundo=segundoPorc, tercero=tercerPorc, cuarto=cuartoPorc)


""" @app.route('/')
def Index():
    return render_template('index.html')
 """


@app.route('/voted', methods=['POST'])
def newVote():
    if request.method == 'POST':

        cur = mysql.connection.cursor()
        query = 'SELECT * FROM votos'
        cur.execute(query)
        result = cur.fetchall()
        if request.form['card'] == '1':
            votos = result[0][1]
            votos += 1
            totalVotos = result[4][1] + 1
            cur.execute(
                'UPDATE votos SET votos = %s WHERE id = 1', [str(votos)])
            cur.execute(
                'UPDATE votos SET votos = %s WHERE id = 5', [str(totalVotos)])
            mysql.connection.commit()
        elif request.form['card'] == '2':
            votos = result[1][1]
            votos += 1
            totalVotos = result[4][1] + 1
            cur.execute(
                'UPDATE votos SET votos = %s WHERE id = 2', [str(votos)])
            cur.execute(
                'UPDATE votos SET votos = %s WHERE id = 5', [str(totalVotos)])
            mysql.connection.commit()
        elif request.form['card'] == '3':
            votos = result[2][1]
            votos += 1
            totalVotos = result[4][1] + 1
            cur.execute(
                'UPDATE votos SET votos = %s WHERE id = 3', [str(votos)])
            cur.execute(
                'UPDATE votos SET votos = %s WHERE id = 5', [str(totalVotos)])
            mysql.connection.commit()
        elif request.form['card'] == '4':
            votos = result[3][1]
            votos += 1
            totalVotos = result[4][1] + 1
            cur.execute(
                'UPDATE votos SET votos = %s WHERE id = 4', [str(votos)])
            cur.execute(
                'UPDATE votos SET votos = %s WHERE id = 5', [str(totalVotos)])
            mysql.connection.commit()
    return redirect(url_for('Index'))


if __name__ == '__main__':
    app.run()
