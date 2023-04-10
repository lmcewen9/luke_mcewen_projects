import random
import PyQt6.QtWidgets as wid
import PyQt6.QtCore as core
from sys import argv, exit

map = {
    "New York": "Albany",
    "California": "Sacremento",
    "Arizona": "Phoenix",
    "Florida": "Tallahassee",
    "Indiana": "Indianapolis",
    "Oregon": "Salem",
    "Colorado": "Denver",
    "Wyoming": "Cheyenne",
    "Texas": "Austin",
    "New Jersey": "Trenton",
    "Nevada": "Carson City",
    "Alaska": "Juneau",
    "Tennessee": "Nashville",
    "Delware": "Dover",
    "Massachusetts": "Boston",
    "Iowa": "Des Moines",
    "Montana": "Helena",
    "Illinois": "Springfield",
    "Oklahoma": "Oklahoma City",
    "Louisana": "Baton Rouge",
    "North Dakota": "Bismarck",
    "Arkansas": "Little Rock",
    "New Mexico": "Santa Fe",
    "Utah": "Salt Lake City",
    "North Carolina": "Raleigh",
    "Alabama": "Montgomery",
    "Pennsylvania": "Harrisburg",
    "South Dakota": "Pierre",
    "Kentucky": "Frankfort",
    "Maryland": "Annapolis",
    "Vermont": "Montpelier",
    "Ohio": "Columbus",
    "Kansas": "Topeka",
    "Rhode Island": "Providence",
    "Hawaii": "Honolulu",
    "Virgina": "Richmond",
    "Michigan": "Lansing",
    "Idaho": "Boise",
    "Missouri": "Jefferson City",
    "Connecticut": "Hartford",
    "West Virgina": "Charleston",
    "Wisconsin": "Madison",
    "Minnesota": "St Paul",
    "New Hampshire": "Concord",
    "South Carolina": "Columbia",
    "Maine": "Augusta",
    "Nebraska": "Lincoln",
    "Washington": "Olympia",
    "Georgia": "Atlanta",
    "Mississippi": "Jackson"
}

class StatesCapitals():
    def __init__(self, map):
        self.map = map
        self.score = 0
    
    def get_score(self):
        return self.score
    
    def get_capital(self, state):
        return self.map[state]
    
    def check(self, state, check):
        if self.map[state].lower() == check.lower():
            self.score += 1
            return True
        return False
    
    def create_state_list(self):
        lst = []
        for i in self.map:
            lst.append(i)
        return lst
    
    def create_capital_list(self):
        lst = []
        for i in self.map:
            lst.append(self.map[i])
        return lst
    
    def four_random_capitals(self, capital):
        lst = []
        tmp = self.create_capital_list()
        tmp.remove(capital)
        k = len(tmp)
        random_num = 5
        for i in range(5):
            if random_num != False:
                test = random.randint(1, random_num)
            
            if random_num != False and test == 1:
                lst.append(capital)
                random_num = False
            else:
                num = random.randint(0, k-1)
                ran_capital = tmp[num]
                lst.append(ran_capital)
                tmp.remove(ran_capital)
                k -= 1
                if random_num != False:
                    random_num -= 1
        
        return lst

class MainWindow(wid.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.game = StatesCapitals(map)
        self.state_arr = self.game.create_state_list()
        self.setWindowTitle("States and Capitals Game")
        self.over = 0

        self.decrement = len(self.state_arr)
        self.state = self.state_arr[random.randint(0, self.decrement-1)]
        self.state_arr.remove(self.state)

        self.label = wid.QLabel(f"What is the capital of {self.state}?")
        self.label.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.setFixedSize(core.QSize(1000, 300))

        layout = wid.QVBoxLayout()
        button_layout = wid.QHBoxLayout()

        random_caps = self.game.four_random_capitals(self.game.get_capital(self.state))

        self.button1 = wid.QPushButton(random_caps[0])
        self.button1.setFixedSize(200, 50)
        self.button1.clicked.connect(lambda: self.button_was_clicked(self.button1.text()))
        self.button2 = wid.QPushButton(random_caps[1])
        self.button2.setFixedSize(200, 50)
        self.button2.clicked.connect(lambda: self.button_was_clicked(self.button2.text()))
        self.button3 = wid.QPushButton(random_caps[2])
        self.button3.setFixedSize(200, 50)
        self.button3.clicked.connect(lambda: self.button_was_clicked(self.button3.text()))
        self.button4 = wid.QPushButton(random_caps[3])
        self.button4.setFixedSize(200, 50)
        self.button4.clicked.connect(lambda: self.button_was_clicked(self.button4.text()))
        self.button5 = wid.QPushButton(random_caps[4])
        self.button5.setFixedSize(200, 50)
        self.button5.clicked.connect(lambda: self.button_was_clicked(self.button5.text()))

        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        button_layout.addWidget(self.button3)
        button_layout.addWidget(self.button4)
        button_layout.addWidget(self.button5)

        self.score = wid.QLabel()

        layout.addWidget(self.label)
        layout.addLayout(button_layout)
        layout.addWidget(self.score)
        container = wid.QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def _exit(self):
        exit()
    
    def button_was_clicked(self, capital):
        if self.game.check(self.state, capital):
            self.score.setText(f"Correct!\nScore = {self.game.get_score()}")
        
        else:
            self.score.setText(f"Incorrect :(  Answer was {self.game.get_capital(self.state)}\nScore = {self.game.get_score()}")
        
        if self.over < 49:
            self.decrement -= 1
            self.state = self.state_arr[random.randint(0, self.decrement-1)]
            self.state_arr.remove(self.state)
            self.label.setText(f"What is the capital of {self.state}?")

            random_caps = self.game.four_random_capitals(self.game.get_capital(self.state))
            self.button1.setText(random_caps[0])
            self.button2.setText(random_caps[1])
            self.button3.setText(random_caps[2])
            self.button4.setText(random_caps[3])
            self.button5.setText(random_caps[4])

            self.over += 1
        
        else:
            self.label.setText(f"You scored a {round(self.game.get_score()/50 *100)}%")
            self.score.setText("")
            self.button1.setText("")
            self.button1.clicked.connect(self._exit)
            self.button2.setText("")
            self.button2.clicked.connect(self._exit)
            self.button3.setText("")
            self.button3.clicked.connect(self._exit)
            self.button4.setText("")
            self.button4.clicked.connect(self._exit)
            self.button5.setText("")
            self.button5.clicked.connect(self._exit)

def main():
    app = wid.QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()