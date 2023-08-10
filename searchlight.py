import csv
import os
from tkinter.filedialog import askdirectory
import typing
from PyQt6 import QtCore
import PyQt6.QtWidgets as wid
from sys import argv

from PyQt6.QtWidgets import QWidget

def get_files():
    dic = {}
    os.chdir(askdirectory())
    path = os.getcwd()

    file_lst = os.listdir(path)
    for i in file_lst:
        with open(f"{path/{i}}") as file:
            reader = csv.reader(file)
            for count, line in enumerate(reader, 0):
                if count != 0:
                    dic[f"{line[0]} ({''.join(line[3].split(' '))})"] = line[4]
    return dic, path

def create_set(dic):
    s = set()
    for i in dic:
        if " - " in dic[i] and "searchlight" in dic[i].lower():
            s.add(" - ".join(dic[i].split(" - ")[x] for x in range(len(dic[i].split(" - "))) if x != 0))

    return s

def write_file(format, ticket_dic, set_lst, path):
    with open(f"{path}/../ticket_list.{format}", "w") as file:
        count = 0
        for k in set_lst:
            file.write(f"{k},\n")
            tmp = []
            for i in ticket_dic:
                if k in ticket_dic[i]:
                    count += 1
                    if format == "csv":
                        tmp.append(i)
                    else:
                        file.write(f"\t{i}\r")
            if format == "csv":
                tmp.append("\n\n")
                file.write(",".join(tmp))
            file.write(f"Total Tickets: {count}")

def run():
    ticket_dic, path = get_files()
    set_lst = create_set(ticket_dic)
    write_file("txt", ticket_dic, set_lst, path)
    write_file("csv", ticket_dic, set_lst, path)


class MainWindow(wid.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Searchlight Converter")
        self.label = wid.QLabel("Push button to select directory\nwhere searchlight file is located.")
        self.button = wid.QPushButton("Select Directory")

        self.button.clicked.connect(self.button_push)

        vbox = wid.QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.button)
        container = wid.QWidget()
        container.setLayout(vbox)
        self.setCentralWidget(container)
    
    def button_push(self):
        run()
        self.label.setText("Your files have been converted.")

def main():
    app = wid.QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()