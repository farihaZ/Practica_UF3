import csv
import mysql.connector
import pandas as pd
from mysql.connector import errorcode
import function as f
#dic to connect with databas
connection_args = {
    'host': 'mysql-fariha.alwaysdata.net',
    'user': 'fariha',
    'password': 'x6968470e'
}


def insert_data():
    #selecting the database
    connection_args.update({'database': 'fariha_prog'})
    # define the sql sentence for database
    sql = ("INSERT INTO reserves "
           "(id,nif,date,hora,motiu,datares) "
           "VALUES (%s, %s, %s, %s, %s, %s)")
    try:
        # open the connection with database
        cnx = mysql.connector.connect(**connection_args)
        with open('file/reserves.csv') as csvfile:
            read_csv = csv.reader(csvfile, delimiter=',')
            next(read_csv)
            for row in read_csv:
                crs = cnx.cursor()
                crs.execute(sql, row)
                cnx.commit()
        print("\nregistry enterd successfully.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("user or passward incorect")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("the database introduced does not exist")
        else:
            print(err)
    else:
        cnx.close()

def select_data():
    # selecting database
    connection_args.update({'database': 'fariha_prog'})
    try:
        # open the connection with data base
        cnx = mysql.connector.connect(**connection_args)
        # definim la sentència sql per a crear la bbdd
        sql = ("SELECT * FROM reserves where date = CURRENT_DATE()")
        # creem el cursor, executem la sentència i fem fetchall (per obtenir tots els registres)
        crs = cnx.cursor()
        crs.execute(sql)
        result = crs.fetchall()
        # mostra tots els resultats
        for i in result:
            print(i)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("User or Password incorrect")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("database introduce not exist")
        else:
            print(err)
    else:
        cnx.close()


def export_data():
    connection_args.update({'database': 'fariha_prog'})
    try:
        # obrim connexió a la bbdd amb els paràmetres de connection_args
        cnx = mysql.connector.connect(**connection_args)
        # definim la sentència sql per a crear la bbdd
        sql = ("SELECT * FROM reserves ")
        # creem el cursor, executem la sentència i fem fetchall (per obtenir tots els registres)
        crs = cnx.cursor()
        crs.execute(sql)
        result = crs.fetchall()
        sql_query=pd.read_sql_query('''select * from reserves ''',cnx)
        df = pd.DataFrame(sql_query)
        df.to_csv(r'file/reserve.csv')
        for i in result:
            print(i)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuari o contrassenya incorrectes")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de dades indicada no existeix")
        else:
            print(err)
    else:
        cnx.close()
