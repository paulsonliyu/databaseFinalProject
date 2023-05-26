import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='YU_oppdivide!20', db='menagerie')
c = conn.cursor()


def read_data():
    c.execute('SELECT * FROM pet')
    pets = c.fetchall()
    for pet in pets:
        print(pet)


def main():
    read_data()


if __name__ == '__main__':
    main()