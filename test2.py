from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(50, 50, 81, 21))
        self.username_label.setObjectName("username_label")
        self.username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input.setGeometry(QtCore.QRect(150, 50, 200, 22))
        self.username_input.setObjectName("username_input")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(50, 100, 81, 21))
        self.password_label.setObjectName("password_label")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(150, 100, 200, 22))
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(150, 150, 93, 28))
        self.login_button.setObjectName("login_button")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        self.login_button.clicked.connect(self.handle_login)

        try:
            self.connection = pymysql.connect(
                host='localhost',
                user='root',
                password='0728012004',
                database='banve'
            )
            print("Kết nối thành công!")
        except pymysql.MySQLError as err:
            print(f"Lỗi khi kết nối đến MySQL: {err}")

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.username_label.setText(_translate("LoginWindow", "Username:"))
        self.password_label.setText(_translate("LoginWindow", "Password:"))
        self.login_button.setText(_translate("LoginWindow", "Login"))

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM Users WHERE username = %s AND password = %s"
                cursor.execute(sql, (username, password))
                result = cursor.fetchone()

                if result:
                    print("Login successful!")
                    self.open_main_window()
                else:
                    print("Invalid credentials!")
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("Invalid username or password.")
                    msg.exec_()
        except pymysql.MySQLError as err:
            print(f"Lỗi khi kiểm tra thông tin đăng nhập: {err}")

    def open_main_window(self):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        LoginWindow.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(999, 762)
        MainWindow.setStyleSheet("background-image: url(:/pic/pngtree-yellow-clothing-promotion-background-design-picture-image_1145330.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 70, 441, 95))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(:/pic/pngtree-vietnam-flag-border-background-picture-image_1177640.jpg);")
        self.label.setIndent(55)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(100, 190, 771, 211))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("border-image: url(:/pic/mau-khung-hinh-nen-co-dien_022126362.jpg);")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setToolTipDuration(20)
        self.label_2.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.label_2.setIndent(5)
        self.label_2.setObjectName("label_2")
        self.ho_ten = QtWidgets.QLineEdit(self.groupBox)
        self.ho_ten.setGeometry(QtCore.QRect(150, 30, 311, 22))
        self.ho_ten.setAutoFillBackground(False)
        self.ho_ten.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.ho_ten.setObjectName("ho_ten")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(60, 90, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setToolTipDuration(20)
        self.label_3.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.label_3.setIndent(5)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(190, 90, 73, 22))
        self.comboBox.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(60, 150, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setToolTipDuration(20)
        self.label_4.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.label_4.setIndent(5)
        self.label_4.setObjectName("label_4")
        self.ho_ten_2 = QtWidgets.QLineEdit(self.groupBox)
        self.ho_ten_2.setGeometry(QtCore.QRect(150, 150, 311, 22))
        self.ho_ten_2.setAutoFillBackground(False)
        self.ho_ten_2.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.ho_ten_2.setObjectName("ho_ten_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(100, 430, 771, 221))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("border-image: url(:/pic/mau-khung-hinh-nen-co-dien_022126362.jpg);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.ca_fe = QtWidgets.QCheckBox(self.groupBox_2)
        self.ca_fe.setGeometry(QtCore.QRect(60, 40, 70, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ca_fe.setFont(font)
        self.ca_fe.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.ca_fe.setObjectName("ca_fe")
        self.nuoc_ngot = QtWidgets.QCheckBox(self.groupBox_2)
        self.nuoc_ngot.setGeometry(QtCore.QRect(60, 100, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nuoc_ngot.setFont(font)
        self.nuoc_ngot.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.nuoc_ngot.setObjectName("nuoc_ngot")
        self.banh_my = QtWidgets.QCheckBox(self.groupBox_2)
        self.banh_my.setGeometry(QtCore.QRect(60, 160, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.banh_my.setFont(font)
        self.banh_my.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.banh_my.setObjectName("banh_my")
        self.kem = QtWidgets.QCheckBox(self.groupBox_2)
        self.kem.setGeometry(QtCore.QRect(320, 40, 70, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.kem.setFont(font)
        self.kem.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.kem.setObjectName("kem")
        self.nuoc_loc = QtWidgets.QCheckBox(self.groupBox_2)
        self.nuoc_loc.setGeometry(QtCore.QRect(320, 100, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nuoc_loc.setFont(font)
        self.nuoc_loc.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.nuoc_loc.setObjectName("nuoc_loc")
        self.banh_keo = QtWidgets.QCheckBox(self.groupBox_2)
        self.banh_keo.setGeometry(QtCore.QRect(320, 160, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.banh_keo.setFont(font)
        self.banh_keo.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.banh_keo.setObjectName("banh_keo")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(100, 690, 771, 31))
        self.groupBox_3.setStyleSheet("border-image: url(:/pic/mau-khung-hinh-nen-co-dien_022126362.jpg);")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.thanh_toan = QtWidgets.QPushButton(self.groupBox_3)
        self.thanh_toan.setGeometry(QtCore.QRect(600, 0, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.thanh_toan.setFont(font)
        self.thanh_toan.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.thanh_toan.setObjectName("thanh_toan")
        self.thoat = QtWidgets.QPushButton(self.groupBox_3)
        self.thoat.setGeometry(QtCore.QRect(30, 0, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.thoat.setFont(font)
        self.thoat.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.thoat.setObjectName("thoat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 999, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.thoat.clicked.connect(self.exit_app)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "PHẦN MỀM BÁN HÀNG"))
        self.groupBox.setTitle(_translate("MainWindow", "Thông tin khách hàng"))
        self.label_2.setText(_translate("MainWindow", "Họ tên"))
        self.label_3.setText(_translate("MainWindow", "Loại khách hàng"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Vip"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Thân thiết"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Vãng lai"))
        self.label_4.setText(_translate("MainWindow", "Số điện thoại"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Dịch vụ"))
        self.ca_fe.setText(_translate("MainWindow", "Cà phê"))
        self.nuoc_ngot.setText(_translate("MainWindow", "Nước ngọt"))
        self.banh_my.setText(_translate("MainWindow", "Bánh mỳ"))
        self.kem.setText(_translate("MainWindow", "Kem"))
        self.nuoc_loc.setText(_translate("MainWindow", "Nước lọc"))
        self.banh_keo.setText(_translate("MainWindow", "Bánh kẹo"))
        self.thanh_toan.setText(_translate("MainWindow", "Thanh toán"))
        self.thoat.setText(_translate("MainWindow", "Thoát"))

    def exit_app(self):
        QtCore.QCoreApplication.instance().quit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
