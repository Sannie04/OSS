from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

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
        self.ca_fe.setGeometry(QtCore.QRect(90, 40,81, 20))
        self.ca_fe.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.ca_fe.setObjectName("ca_fe")
        self.bim_bim = QtWidgets.QCheckBox(self.groupBox_2)
        self.bim_bim.setGeometry(QtCore.QRect(340, 40, 81, 20))
        self.bim_bim.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.bim_bim.setObjectName("bim_bim")
        self.nguoi_lon = QtWidgets.QSpinBox(self.groupBox_2)
        self.nguoi_lon.setGeometry(QtCore.QRect(170, 90, 42, 22))
        self.nguoi_lon.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.nguoi_lon.setObjectName("nguoi_lon")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(90, 90, 61, 21))
        self.label_5.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(90, 140, 61, 21))
        self.label_6.setStyleSheet("border-image: url(:/pic/bang-trang-trang-khung-nhom-nep-nho.webp);")
        self.label_6.setObjectName("label_6")
        self.tre_em = QtWidgets.QSpinBox(self.groupBox_2)
        self.tre_em.setGeometry(QtCore.QRect(170, 140,42, 22))
        self.tre_em.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.tre_em.setObjectName("tre_em")
        self.tien_tra = QtWidgets.QPushButton(self.groupBox_2)
        self.tien_tra.setGeometry(QtCore.QRect(400, 130, 171, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tien_tra.setFont(font)
        self.tien_tra.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.tien_tra.setObjectName("tien_tra")
        self.tien = QtWidgets.QLineEdit(self.groupBox_2)
        self.tien.setGeometry(QtCore.QRect(400, 90, 171, 22))
        self.tien.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.tien.setObjectName("tien")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(610, 90, 55, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.label_7.setObjectName("label_7")
        self.XAC_NHAN = QtWidgets.QPushButton(self.centralwidget)
        self.XAC_NHAN.setGeometry(QtCore.QRect(360, 660, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.XAC_NHAN.setFont(font)
        self.XAC_NHAN.setStyleSheet("border-image: url(:/pic/bang-trang-khung-nhom-nep-nho.webp);")
        self.XAC_NHAN.setObjectName("XAC_NHAN")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tien_tra.clicked.connect(self.tt)
        self.XAC_NHAN.clicked.connect(self.ht)

        # Connect to MySQL database
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "ỨNG DỤNG BÁN VÉ"))
        self.groupBox.setTitle(_translate("MainWindow", "THÔNG TIN KHÁCH HÀNG"))
        self.label_2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "HỌ TÊN:"))
        self.label_3.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "GIỚI TÍNH :"))
        self.comboBox.setItemText(0, _translate("MainWindow", "NAM"))
        self.comboBox.setItemText(1, _translate("MainWindow", "NỮ"))
        self.comboBox.setItemText(2, _translate("MainWindow", "KHÁC"))
        self.label_4.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "SĐT :"))
        self.groupBox_2.setTitle(_translate("MainWindow", "DỊCH VỤ"))
        self.ca_fe.setText(_translate("MainWindow", "CAFE"))
        self.bim_bim.setText(_translate("MainWindow", "BIMBIM"))
        self.label_5.setText(_translate("MainWindow", "Người Lớn"))
        self.label_6.setText(_translate("MainWindow", "TRẺ EM "))
        self.tien_tra.setText(_translate("MainWindow", "Thành tiền"))
        self.label_7.setText(_translate("MainWindow", "VNĐ"))
        self.XAC_NHAN.setText(_translate("MainWindow", "XÁC NHẬN"))

    def tt(self):
        price = {
            "ca_fe": 50000,
            "bim_bim": 20000,
            "nguoi_lon": 100000,
            "tre_em": 70000,
        }
        tcf = 0
        if self.ca_fe.isChecked() != 0:
            tcf = price["ca_fe"]
        tbb = 0
        if self.bim_bim.isChecked() != 0:
            tbb = price["bim_bim"]
        tnl = int(self.nguoi_lon.text()) * price["nguoi_lon"]
        tte = int(self.tre_em.text()) * price["tre_em"]
        self.sum = tcf + tbb+ tnl + tte
        self.tien.setText(str(self.sum))

    def ht(self):
        ho_ten = self.ho_ten.text()
        comboBox_text = self.comboBox.currentText()
        ho_ten_2 = self.ho_ten_2.text()
        sum_value = self.sum  # Sử dụng self.sum thay vì sum

        try:
            with self.connection.cursor() as cursor:
                # Insert into KhachHang table
                sql_khachhang = "INSERT INTO KhachHang (ho_ten, gioi_tinh, sdt, tong_tien) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql_khachhang, (ho_ten, comboBox_text, ho_ten_2, sum_value))

                # Get the last inserted ID
                khach_hang_id = cursor.lastrowid

                # Insert services into DichVu table
                if self.ca_fe.isChecked():
                    sql_dichvu = "INSERT INTO DichVu (ten_dich_vu, gia, khach_hang_id) VALUES (%s, %s, %s)"
                    cursor.execute(sql_dichvu, ('CAFE', 50000, khach_hang_id))

                if self.bim_bim.isChecked():
                    sql_dichvu = "INSERT INTO DichVu (ten_dich_vu, gia, khach_hang_id) VALUES (%s, %s, %s)"
                    cursor.execute(sql_dichvu, ('BIMBIM', 20000, khach_hang_id))

                if int(self.nguoi_lon.text()) > 0:
                    sql_dichvu = "INSERT INTO DichVu (ten_dich_vu, gia, khach_hang_id) VALUES (%s, %s, %s)"
                    cursor.execute(sql_dichvu, ('NGUOI_LON', int(self.nguoi_lon.text()) * 100000, khach_hang_id))

                if int(self.tre_em.text()) > 0:
                    sql_dichvu = "INSERT INTO DichVu (ten_dich_vu, gia, khach_hang_id) VALUES (%s, %s, %s)"
                    cursor.execute(sql_dichvu, ('TRE_EM', int(self.tre_em.text()) * 70000, khach_hang_id))

                self.connection.commit()
            print("Thêm khách hàng và dịch vụ thành công!")
        except pymysql.MySQLError as err:
            print(f"Lỗi khi thêm khách hàng và dịch vụ vào MySQL: {err}")

        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Thông báo")
        msg.setText("Đã thanh toán thành công")
        msg.setInformativeText(f'Họ tên: {ho_ten}\nGiới tính: {comboBox_text}\nSĐT: {ho_ten_2}\nTổng tiền: {sum_value}')
        msg.exec_()

import vd1_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
