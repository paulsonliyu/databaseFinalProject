import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='YU_oppdivide!20', db='menagerie')
c = conn.cursor()


def show_owned():
    c.execute('SELECT owner, COUNT(*) FROM pet GROUP BY owner')
    owned = c.fetchall()
    for own in owned:
        print(own)


def main():
    show_owned()


if __name__ == '__main__':
    main()
