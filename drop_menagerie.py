import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='YU_oppdivide!20')
c = conn.cursor()


def dropdb():
    c.execute("DROP DATABASE IF EXISTS menagerie")


def main():
    dropdb()


if __name__ == '__main__':
    main()
