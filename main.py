# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json

data = {}
note_name = ""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(664, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 641, 441))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.text = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.text.setObjectName("text")
        self.horizontalLayout.addWidget(self.text)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.notes_list = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.notes_list.setObjectName("notes_list")
        self.verticalLayout.addWidget(self.notes_list)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.create_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout_2.addWidget(self.create_btn)
        self.del_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.del_btn.setObjectName("del_btn")
        self.horizontalLayout_2.addWidget(self.del_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.save_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout.addWidget(self.save_btn)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tags_list = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.tags_list.setObjectName("tags_list")
        self.verticalLayout.addWidget(self.tags_list)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add_tag_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.add_tag_btn.setObjectName("add_tag_btn")
        self.horizontalLayout_3.addWidget(self.add_tag_btn)
        self.del_tag_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.del_tag_btn.setObjectName("del_tag_btn")
        self.horizontalLayout_3.addWidget(self.del_tag_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.search_note = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.search_note.setObjectName("search_note")
        self.verticalLayout.addWidget(self.search_note)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.show_notes()

        
        self.notes_list.itemClicked.connect(self.show)
        self.create_btn.clicked.connect(self.add)
        self.del_btn.clicked.connect(self.del_note)
        self.save_btn.clicked.connect(self.save_note)
        self.add_tag_btn.clicked.connect(self.add_tag)
        self.del_tag_btn.clicked.connect(self.del_tag)
        self.search_note.clicked.connect(self.search_tag)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Список заміток"))
        self.create_btn.setText(_translate("MainWindow", "Створити замітку"))
        self.del_btn.setText(_translate("MainWindow", "Видалити замітку"))
        self.save_btn.setText(_translate("MainWindow", "Зберегти замітку"))
        self.label_2.setText(_translate("MainWindow", "Список тегів"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введить текст..."))
        self.add_tag_btn.setText(_translate("MainWindow", "Додати до замітки"))
        self.del_tag_btn.setText(_translate("MainWindow", "Відкріпити від замітки"))
        self.search_note.setText(_translate("MainWindow", "Шукати замітки по тегу"))

    def show_notes(self):
        global data
        with open('notes.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        self.notes_list.addItems(data.keys())

    def show(self):
        t = self.notes_list.currentItem().text()
        self.text.setText(data[t]["текст"])
        self.tags_list.clear()
        self.tags_list.addItems(data[t]['теги'])

    def add(self):
        global note_name
        note_name, ok = QtWidgets.QInputDialog.getText(MainWindow, "Додати замітки", "Знайти заміту") 
        print(note_name)
        if note_name and ok:
            data[note_name] = {"текст" : "", "теги" : []}
            self.notes_list.addItem(note_name)

    def del_note(self):
        if self.notes_list.currentItem():
            t = self.notes_list.currentItem().text()
            del data[t]
            with open("notes.json", 'w', encoding='utf-8') as file:
                json.dump(data, file, sort_keys=True)
            self.notes_list.clear()
            self.text.clear()
            self.tags_list.clear()
            self.notes_list.addItems(data.keys())

    def save_note(self):
        if self.notes_list.currentItem():
            edited_txt = self.text.toPlainText()
            data[self.notes_list.currentItem().text()]['текст'] = edited_txt
            with open('notes.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, sort_keys=True)

    # def save_notes(self)
    def add_tag(self):
        if self.notes_list.currentItem():
            tag = self.lineEdit.text()
            if tag and not (tag in data[self.notes_list.currentItem().text()]["теги"]):
                data[self.notes_list.currentItem().text()]["теги"].append(tag)
                self.tags_list.addItem(tag)
                self.lineEdit.clear()
                with open("notes.json", 'w', encoding='utf-8') as file:
                    json.dump(data, file, sort_keys=True)

    def del_tag(self):
        if self.notes_list.currentItem() and self.tags_list.currentItem():
            tag = self.tags_list.currentItem().text()
            name = self.notes_list.currentItem().text()
            data[name]["теги"].remove(tag)
            with open("notes.json", 'w', encoding='utf-8') as file:
                json.dump(data, file, sort_keys=True)
            self.tags_list.clear()
            self.tags_list.addItems(data[name]["теги"])
        
    def search_tag(self):
        if self.search_note.text() == "Шукати замітки по тегу":
            tag = self.lineEdit.text()
            search_notes = {}
            for note in data:
                if tag in data[note]["теги"]:
                    search_notes[note] = data[note]
            # print(search_notes)
            self.notes_list.clear()
            for note in search_notes:
                self.notes_list.addItem(note)
            self.text.clear()
            self.tags_list.clear()
            self.search_note.setText("Скинути пошук")
            
        else:
            self.text.clear()
            self.tags_list.clear()
            self.search_note.setText("Шукати замітки по тегу")
            self.notes_list.clear()
            self.notes_list.addItems(data)


        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 3px solid black;"
                                 "background : white;"
                                 "}")
               

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Windows')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
