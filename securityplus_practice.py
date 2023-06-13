import PyQt6.QtWidgets as wid
from bs4 import BeautifulSoup
import requests
from sys import argv, exit
from random import randint

class MainWindow(wid.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Security+ Practice Questions")
        self.buttonA = wid.QPushButton("A")
        self.buttonA.clicked.connect(lambda: self.button_pressed(self.buttonA.text()))

        self.buttonB = wid.QPushButton("B")
        self.buttonB.clicked.connect(lambda: self.button_pressed(self.buttonB.text()))

        self.buttonC = wid.QPushButton("C")
        self.buttonC.clicked.connect(lambda: self.button_pressed(self.buttonC.text()))

        self.buttonD = wid.QPushButton("D")
        self.buttonD.clicked.connect(lambda: self.button_pressed(self.buttonD.text()))

        self.buttonE = wid.QPushButton("E")
        self.buttonE.clicked.connect(lambda: self.button_pressed(self.buttonE.text()))

        self.checkbox_lst = []
        
        self.checkboxA = wid.QCheckBox("A")
        self.checkbox_lst.append(self.checkboxA)
        self.checkboxB = wid.QCheckBox("B")
        self.checkbox_lst.append(self.checkboxB)
        self.checkboxC = wid.QCheckBox("C")
        self.checkbox_lst.append(self.checkboxC)
        self.checkboxD = wid.QCheckBox("D")
        self.checkbox_lst.append(self.checkboxD)
        self.checkboxE = wid.QCheckBox("E")
        self.checkbox_lst.append(self.checkboxE)
        self.checkboxF = wid.QCheckBox("F")
        self.checkbox_lst.append(self.checkboxF)
        self.confirm = wid.QPushButton("Confirm Selection")
        self.confirm.clicked.connect(lambda: self.button_pressed(True))

        button_hbox = wid.QHBoxLayout()
        button_hbox.addWidget(self.buttonA)
        button_hbox.addWidget(self.buttonB)
        button_hbox.addWidget(self.buttonC)
        button_hbox.addWidget(self.buttonD)
        button_hbox.addWidget(self.buttonE)

        checkbox_hbox = wid.QHBoxLayout()
        checkbox_hbox.addWidget(self.checkboxA)
        checkbox_hbox.addWidget(self.checkboxB)
        checkbox_hbox.addWidget(self.checkboxC)
        checkbox_hbox.addWidget(self.checkboxD)
        checkbox_hbox.addWidget(self.checkboxE)
        checkbox_hbox.addWidget(self.checkboxF)
        checkbox_hbox.addWidget(self.confirm)

        self.buttonFrame = wid.QFrame()
        self.buttonFrame.setLayout(button_hbox)
        self.checkboxFrame = wid.QFrame()
        self.checkboxFrame.setLayout(checkbox_hbox)
        
        self.score = 0
        self.dic = {}
        self.get_questions()
        self.question_lst = self.create_question_list()

        self.label = wid.QLabel()
        self.set_question()

        self.score_label = wid.QLabel(f"Score={self.score}")

        self.correct_label = wid.QLabel()

        vbox = wid.QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.buttonFrame)
        vbox.addWidget(self.checkboxFrame)
        vbox.addWidget(self.score_label)
        vbox.addWidget(self.correct_label)
        container = wid.QWidget()
        container.setLayout(vbox)
        self.setCentralWidget(container)
    
    def get_questions(self):
        def scrape(url, fst):
            source = requests.get(url, verify=False).text
            soup = BeautifulSoup(source, "html.parser")
            contents = soup.find_all(class_= "sfContentBlock")
            questions = contents[0].find_all("p")
            answers = contents[1].find_all("p")
            question_lst = []
            answers_lst = []
            for i in range(0, len(questions), 2):
                tmp_lst = questions[i].text[11:].split(".")
                tmp_str = ".\n".join(tmp_lst)
                question_lst.append(tmp_str + "\n" + questions[i+1].text.replace("\u200b", ""))
            for i in answers:
                if fst and "Question 1)" in i.text:
                    tmp = i.text.replace("\u200b", "").split(",")
                    tmp[0] = tmp[0][12:13]
                    tmp[1] = tmp[1][1]
                    tmp[2] = tmp[2][5]
                    answers_lst.append(tmp)
                else:
                    answers_lst.append(i.text.replace("\u200b", "")[12:][0])
            for i in range(len(question_lst)):        
                self.dic[question_lst[i]] = answers_lst[i]

        fst_url = "https://www.comptia.org/training/resources/practice-tests/security-501-practice-questions"
        snd_url = "https://www.comptia.org/training/resources/practice-tests/security-601-practice-questions"
        scrape(fst_url, True)
        scrape(snd_url, False)
    
    def create_question_list(self):
        lst = []
        for i in self.dic:
            lst.append(i)
        return lst
    
    def check(self, question, answer):
        if self.dic[question] == answer:
            self.score += 1
            return True
        return False
    
    def button_pressed(self, button_text):
        if button_text == True:
            answers = []
            for i in self.checkbox_lst:
                if i.isChecked():
                    answers.append(i.text())
        else:
            answers = button_text
        try:
            if self.check(self.label.text(), answers):
                self.correct_label.setText("Correct!")
            else:
                self.correct_label.setText(f"That was incorrect :(\nThe correct answer was {self.dic[self.label.text()]}")
        except:
            pass
        if len(self.question_lst) > 0:
            self.set_question()
            self.score_label.setText(f"Score={self.score}")
        else:
            self.buttonFrame.show()
            self.checkboxFrame.hide()
            self.label.setText(f"You got {self.score}/13")
            self.score_label.setText("")
            self.buttonA.setText("")
            self.buttonA.clicked.connect(lambda: exit())
            self.buttonB.setText("")
            self.buttonB.clicked.connect(lambda: exit())
            self.buttonC.setText("")
            self.buttonC.clicked.connect(lambda: exit())
            self.buttonD.setText("")
            self.buttonD.clicked.connect(lambda: exit())
            self.buttonE.setText("")
            self.buttonE.clicked.connect(lambda: exit())

    def set_question(self):
        rand = randint(0, len(self.question_lst)-1)
        self.label.setText(self.question_lst[rand])
        if "Select THREE" in self.question_lst[rand]:
            self.buttonFrame.hide()
            self.checkboxFrame.show()
        else:
            self.buttonFrame.show()
            self.checkboxFrame.hide()
            if "Which of the following characteristics BEST" in self.question_lst[rand]:
                self.buttonE.show()
            else:
                self.buttonE.hide()
        self.question_lst.remove(self.question_lst[rand])


def main():
    app = wid.QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()