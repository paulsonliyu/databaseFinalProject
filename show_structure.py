import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='YU_oppdivide!20', db='menagerie')
c = conn.cursor()


def show_structure():
    c.execute("DESCRIBE pet")
    datas = c.fetchall()
    for data in datas:
        print(data)


def main():
    show_structure()


if __name__ == '__main__':
    main()
