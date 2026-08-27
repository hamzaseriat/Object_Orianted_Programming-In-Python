import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    Questions = ["Are you gay?","Do you like Denizli?","Would you go a summer destination?","Do you have dog?","Are you continuning your education?","Did you eat sushi?","Are you smoking?","Have you ever been in a prison?"]
    def __init__(self):
        super().__init__()
        self.Confirms = []
        self.Unconfirms = self.Questions.copy()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("Preferences")
        self.setStyleSheet("Background-color: black")
        self.initUI()

    def initUI(self):
        central_wid = QWidget()
        self.setCentralWidget(central_wid)
        vboxx = QVBoxLayout()
        
        for q in self.Questions:
            checkbox = QCheckBox(q)
            checkbox.setStyleSheet("Background-color: orange; font-size: 20px")
            checkbox.stateChanged.connect(lambda state, question=q: self.checkbox_changed(question, state))
            vboxx.addWidget(checkbox)

        print_button = QPushButton("Print answers")
        print_button.clicked.connect(self.write_habits)
        vboxx.addWidget(print_button)
        central_wid.setLayout(vboxx)
        
    def checkbox_changed(self,q,state):
        if state==2:
            if q not in self.Confirms:
                self.Confirms.append(q)
            if q in self.Unconfirms:
                self.Unconfirms.remove(q)
        else:
            if q not in self.Unconfirms:
                self.Unconfirms.append(q)
            if q in self.Confirms:
                self.Confirms.remove(q)
            
    def write_habits(self):
        print("You confirmed:")
        print()
        for conf in self.Confirms:
            print(conf)
        print()
        print("You did not confirm:")
        print()
        for unc in self.Unconfirms:
            print(unc)
            
        
            

 
if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec_())