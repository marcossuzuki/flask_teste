import MySQLdb

print('Conectando...')
conn = MySQLdb.connect(
    user='root',
    passwd='admin',
    db='jogoteca',
    host='0.0.0.0',
    port=3306
    )

cursor = conn.cursor()
cursor.execute(
    'INSERT INTO usuario (id, nome, senha) '
    'VALUES (%s, %s, %s)'
    )
