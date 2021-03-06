# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from block  import BlockchaininApp
import database


blockchainInApp = BlockchaininApp()

x = database.select_db()
j = 0
for i in x:
    if j == 0:
        blockchainInApp.new_block(previous_hash=i[5])
        j = 1
    else:
        blockchainInApp.new_transaction(i[0], i[1], i[2],i[3])
        blockchainInApp.new_block()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(846, 651)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 801, 611))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(130, 340, 201, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(320, 50, 131, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(160, 140, 272, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(450, 140, 471, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(480, 340, 201, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab)
        self.comboBox_3.setGeometry(QtCore.QRect(130, 420, 201, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(130, 490, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(130, 290, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(480, 290, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(130, 370, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(340, 40, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(340, 50, 81, 41))
        self.label_8.setObjectName("label_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 100, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget.setGeometry(QtCore.QRect(120, 140, 521, 391))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(110, 110, 81, 41))
        self.label_13.setObjectName("label_13")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_4.setGeometry(QtCore.QRect(170, 120, 361, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 120, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(340, 40, 81, 41))
        self.label_12.setObjectName("label_12")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(110, 160, 521, 391))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_15 = QtWidgets.QLabel(self.tab_5)
        self.label_15.setGeometry(QtCore.QRect(310, 40, 131, 41))
        self.label_15.setObjectName("label_15")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_5)
        self.textBrowser_4.setGeometry(QtCore.QRect(240, 140, 271, 401))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 100, 141, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(340, 40, 101, 41))
        self.label_14.setObjectName("label_14")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 100, 111, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(240, 140, 271, 401))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Basic - Blockchain"))
        self.comboBox.setItemText(0, _translate("MainWindow", "BOOM Esports"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Fnatic"))
        self.comboBox.setItemText(2, _translate("MainWindow", "T1"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Team SMG"))
        self.comboBox.setItemText(4, _translate("MainWindow", "OB.Neon"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Execration"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Motivate.Trust Gaming"))
        self.comboBox.setItemText(7, _translate("MainWindow", "TNC Predator"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Team</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">1 : BOOM Esports </span></p><p><span style=\" font-size:12pt;\">2 : Fnatic </span></p><p><span style=\" font-size:12pt;\">3 : T1 </span></p><p><span style=\" font-size:12pt;\">4 : Team SMG </span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">5 : OB.Neon</span></p><p><span style=\" font-size:12pt;\">6 : Execration</span></p><p><span style=\" font-size:12pt;\">7 : Motivate.Trust Gaming</span></p><p><span style=\" font-size:12pt;\">8 : TNC Predator</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "BOOM Esports"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Fnatic"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "T1"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Team SMG"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "OB.Neon"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Execration"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Motivate.Trust Gaming"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "TNC Predator"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "0 - 2"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "1 - 2"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "2 - 0"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "2 - 1"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Team 1</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Team 2</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Score</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Create block</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Create block"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">All Block</span></p><p><br/></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Updata Data"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Team1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Team2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Score"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Timestap"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "All Block"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Team</span></p></body></html>"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "BOOM Esports"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Fnatic"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "T1"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Team SMG"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "OB.Neon"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "Execration"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "Motivate.Trust Gaming"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "TNC Predator"))
        self.pushButton_2.setText(_translate("MainWindow", "Search"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Team data</span></p></body></html>"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Team1"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Team2"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Score"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Timestap"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Team Data"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Transaction verify</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI Symbol\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "Check Transaction Verify"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Transaction Verify"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Data verify</span></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "Check Data Verify"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI Symbol\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Data Verify"))
        self.pushButton.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(self.search)
        self.pushButton_3.clicked.connect(self.allblock)
        self.pushButton_4.clicked.connect(self.verify)
        self.pushButton_5.clicked.connect(self.verifytransaction)


    def save(self):
        team1 = self.comboBox.currentText()
        team2 = self.comboBox_2.currentText()
        score = self.comboBox_3.currentText()
        if(team1 != team2):
            blockchainInApp.new_transactionindatabase(team1,team2,score)
            blockchainInApp.new_blockindatabase()
        


    def allblock(self):
        row = 0
        self.tableWidget.setRowCount(len(blockchainInApp.chain)-1)
        for round in range(len(blockchainInApp.chain)):
                if round >=1 :
                        transactions = blockchainInApp.chain[round].get('transactions')
                        team1 = transactions[0].get('Team1')
                        team2 = transactions[0].get('Team2')
                        score = transactions[0].get('Score')
                        time =  transactions[0].get('timestamp')
                        self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(team1))
                        self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(team2))
                        self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(score))
                        self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(time))
                        row = row+1
    
    def search(self):
        team = self.comboBox_4.currentText()
        row = 0
        for round in range(len(blockchainInApp.chain)):
            if round >=1 :
                transactions = blockchainInApp.chain[round].get('transactions')
                team1 = transactions[0].get('Team1')
                team2 = transactions[0].get('Team2')
                if team1 == team  or team2 == team:
                    row+=1
        self.tableWidget_2.setRowCount(row)
        row = 0
        for round in range(len(blockchainInApp.chain)):
            if round >=1 :
                transactions = blockchainInApp.chain[round].get('transactions')
                team1 = transactions[0].get('Team1')
                team2 = transactions[0].get('Team2')
                score = transactions[0].get('Score')
                time =  transactions[0].get('timestamp')
                if team1 == team  or team2 == team:
                    self.tableWidget_2.setItem(row,0,QtWidgets.QTableWidgetItem(team1))
                    self.tableWidget_2.setItem(row,1,QtWidgets.QTableWidgetItem(team2))
                    self.tableWidget_2.setItem(row,2,QtWidgets.QTableWidgetItem(score))
                    self.tableWidget_2.setItem(row,3,QtWidgets.QTableWidgetItem(time))
                    row+=1

    def verify(self):  
        self.textBrowser_3.setHtml("")
        self.textBrowser_3.append('{:-<65}'.format(' '))
        self.textBrowser_3.append('{:^65}'.format('Data Verification'))
        self.textBrowser_3.append('{:-<65}'.format(' '))
        for round in range(len(blockchainInApp.chain)):
                hashchaintx = blockchainInApp.chain[round].get('transactions_hash')
                hashchainpre = blockchainInApp.chain[round].get('previous_hash')
                hashdatatx = ''
                hashdatapre = ''
                tmp = str(round+1)
                x = database.selecthash_db((tmp))
                for i in x:
                        hashdatatx = i[0]
                        hashdatapre=i[1]
                if(round == 0 and hashchainpre == hashdatapre):
                        self.textBrowser_3.append('{:^65}'.format('Data block 0 is correct'))
                elif(round == 0 and hashchainpre != hashdatapre):
                        self.textBrowser_3.append('{:^65}'.format('Data block 0 is not correct'))
                else:
                        if (hashchaintx == hashdatatx and hashchainpre == hashdatapre ):
                                self.textBrowser_3.append('{:^65}'.format('Data block %d is correct' % round))
                        else:
                                self.textBrowser_3.append('{:^65}'.format('Data block %d is not correct' % round))
        self.textBrowser_3.append('{:-<65}'.format(' '))

    def verifytransaction(self):  
        self.textBrowser_4.setHtml("")
        self.textBrowser_4.append('{:-<65}'.format(' '))
        self.textBrowser_4.append('{:^65}'.format('Transaction Verification'))
        self.textBrowser_4.append('{:-<65}'.format(' '))
        for round in range(len(blockchainInApp.chain)):
                hashchaintx = blockchainInApp.chain[round].get('transactions_hash')
                hashchainpre = blockchainInApp.chain[round].get('previous_hash')
                hashdatatx = ''
                hashdatapre = ''
                tmp = str(round+1)
                x = database.selecthash_db((tmp))
                for i in x:
                        hashdatatx = i[0]
                        hashdatapre=i[1]
                if(round == 0 and hashchainpre == hashdatapre):
                        self.textBrowser_4.append('{:^65}'.format('Transaction block 0 is correct'))
                elif(round == 0 and hashchainpre != hashdatapre):
                        self.textBrowser_4.append('{:-<65}'.format(' '))
                        self.textBrowser_4.append('{:^65}'.format('Transaction block 0 is not correct'))
                        self.textBrowser_4.append('{:-<65}'.format(' '))
                else:
                        if (hashchaintx == hashdatatx):
                                self.textBrowser_4.append('{:^65}'.format('Transaction block %d is correct' % round))
                        else:
                                self.textBrowser_4.append('{:=<33}'.format(' '))
                                self.textBrowser_4.append('{:^65}'.format('Transaction block %d is not correct' % round))
                                self.textBrowser_4.append('{:=<33}'.format(' '))
        self.textBrowser_4.append('{:-<65}'.format(' '))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
