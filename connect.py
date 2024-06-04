import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='0728012004',
        database='banve'
    )
    print("Kết nối thành công!")
except pymysql.MySQLError as err:
    print(f"Lỗi khi kết nối đến MySQL: {err}")
