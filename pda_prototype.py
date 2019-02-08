import sys
from Validate_Def_File import Validate_Def_File
from Automaton import Automaton
from Input_Alphabet import Input_Alphabet
from Input_Strings import Input_Strings
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QMenuBar, QMenu, QLabel, QLineEdit, QPushButton, QListWidget, QSpinBox, QCheckBox, QPlainTextEdit, QStatusBar

class PushDownAutomaton(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.Automaton = Automaton()
        # Creating a Input_String class instance
        self.Strings = Input_Strings()
        # A attribute to remeber the def_path
        self.def_path = ''
        # A attribute to remeber if the automaton was opened
        self.automaton_open = False

        self.setWindowTitle("Pushdown Automaton")
        self.resize(640, 480)

        self.mainMenu = self.menuBar()

        self.fileMenu = self.mainMenu.addMenu("File")
        self.fileMenu.addAction("Open Automaton", self.open_automaton_action)
        self.fileMenu.addAction("View Automaton", self.view_automaton_action)

        self.helpMenu = self.mainMenu.addMenu("Help")
        self.helpMenu.addAction("User Manual", self.user_manual_action)
        
        self.inputStringLabel = QLabel(self)
        self.inputStringLabel.setGeometry(20, 40, 111, 16)
        self.inputStringLabel.setText("Input String")

        self.inputStringLineEdit = QLineEdit(self)
        self.inputStringLineEdit.setGeometry(20, 60, 231, 20)

        self.addToListPushButton = QPushButton(self)
        self.addToListPushButton.setGeometry(80, 90, 111, 23)
        self.addToListPushButton.setText("Add to List")
        self.addToListPushButton.clicked.connect(self.add_to_list_clicked)

        self.inputStringListLabel = QLabel(self)
        self.inputStringListLabel.setGeometry(20, 125, 111, 16)
        self.inputStringListLabel.setText("Input String List")

        self.inputStringListWidget = QListWidget(self)
        self.inputStringListWidget.setGeometry(20, 145, 231, 260)

        self.runStringPushButton = QPushButton(self)
        self.runStringPushButton.setGeometry(80, 415, 111, 23)
        self.runStringPushButton.setText("Run String")
        self.runStringPushButton.clicked.connect(self.run_string_clicked)

        self.outputLabel = QLabel(self)
        self.outputLabel.setGeometry(300, 40, 47, 16)
        self.outputLabel.setText("Output")

        self.sequencesLabel = QLabel(self)
        self.sequencesLabel.setGeometry(390, 40, 51, 16)
        self.sequencesLabel.setText("Sequences")

        self.sequencesSpinBox = QSpinBox(self)
        self.sequencesSpinBox.setGeometry(450, 37, 42, 20)
        self.sequencesSpinBox.setMinimum(1)
        #access value with self.sequencesSpinBox.value

        self.displayPathsCheckBox = QCheckBox(self)
        self.displayPathsCheckBox.setGeometry(530, 40, 101, 17)
        self.displayPathsCheckBox.setText("Display Paths")
        #access true or false with self.displayPathsCheckBox.checked

        self.outputPlainTextEdit = QPlainTextEdit(self)
        self.outputPlainTextEdit.setGeometry(300, 60, 311, 346)

        self.quitRunningStringPushButton = QPushButton(self)
        self.quitRunningStringPushButton.setGeometry(335, 415, 111, 23)
        self.quitRunningStringPushButton.setText("Quit Running String")
        self.quitRunningStringPushButton.clicked.connect(self.quit_running_string_clicked)

        self.closeAutomatonPushButton = QPushButton(self)
        self.closeAutomatonPushButton.setGeometry(465, 415, 111, 23)
        self.closeAutomatonPushButton.setText("Close Automaton")
        self.closeAutomatonPushButton.clicked.connect(self.close_automaton_clicked)
        
        # Style for status label text
        self.styleError = 'font: 15pt Arial; color: maroon'
        self.styleNormal = 'font:15pt Arial; color: white'

        self.statusBar = self.statusBar()
        self.statusLabel = QLabel("application status messages will go here (when something completes, etc.)")
        self.statusLabel.setStyleSheet(self.styleNormal)
        self.statusBar.addPermanentWidget(self.statusLabel)
        
        self.show()


    def parseConfigFile(self):
        #TODO: handle the values from the config file at the start of execution
        return

    def parseInputStringFile(self, file_path):
        # If the input string widget is empty add the input strings to the widget
        if self.inputStringListWidget.count() == 0:
            # Loading the string into the Strings attribute input_strings
            self.Strings.load(file_path)
            for string in self.Strings.input_strings:
                # Add the string to the widget
                self.inputStringListWidget.addItem(string)
        else:
            # If there are already string in the widget do nothing
            # strings have already been parsed.
            pass
        return

    # A method to update the input string widget
    def update_input_string_widget(self):
        self.inputStringListWidget.clear()
        for string in self.Strings.input_strings:
            self.inputStringListWidget.addItem(string)

    def open_automaton_action(self):
        self.outputPlainTextEdit.setPlainText("Open Automaton Clicked")
        
        # Save the location of the def file
        self.def_path = 'pda.def'
        #self.def_path = 'invalid_pda.def'

        # Check if the defintion file is valid
        valid_def = Validate_Def_File(self.def_path)
        if valid_def.def_valid == True:
           # Load the Automaton
           self.Automaton.load(self.def_path)
           # Set def path to the status bar
           self.statusLabel.setText(self.def_path)
           # Now parse config file        
           self.parseConfigFile()
           # Now parse the input strings
           self.parseInputStringFile(self.def_path)
        else:
            error_list = []
            error_list = valid_def.is_invalid_def()
            for item in error_list:
                self.outputPlainTextEdit.appendPlainText(item)

        return

    def view_automaton_action(self):
        self.outputPlainTextEdit.setPlainText("View Automaton Clicked")
        file = open(self.def_path, 'r')
        for line in file:
            self.outputPlainTextEdit.appendPlainText(line)
        return

    def user_manual_action(self):
        QMessageBox.about(self, 'User Manual', 'Help List Goes here')
        return        

    def add_to_list_clicked(self):

        # If the user just clicks add string
        if(self.inputStringLineEdit.text() == ''):
           return

        if self.Strings.is_duplicate(self.inputStringLineEdit.text()) == True:
           status = self.inputStringLineEdit.text() + ' is a duplicate string'
           self.statusLabel.setText(status)
           self.statusLabel.setStyleSheet(self.styleError)
           self.inputStringLineEdit.clear()
           return

        if self.Strings.validate(self.Automaton.Input_Alpha.alphabet, self.inputStringLineEdit.text()) == True:
           self.Strings.add_input_string(self.Automaton.Input_Alpha.alphabet, self.inputStringLineEdit.text())
           self.update_input_string_widget()
           # Make new string the selected string
           self.inputStringListWidget.setCurrentRow((self.inputStringListWidget.count() - 1))
           self.inputStringLineEdit.clear()
           self.statusLabel.setStyleSheet(self.styleNormal)
           self.statusLabel.setText('')
        else:            
           status = self.inputStringLineEdit.text() + ' is not a valid string'
           self.statusLabel.setText(status)
           self.statusLabel.setStyleSheet(self.styleError)
           self.update_input_string_widget()
           self.inputStringLineEdit.clear()

        return

    def run_string_clicked(self):
        self.outputPlainTextEdit.setPlainText("Run String Button Clicked")
        self.statusLabel.setText('Running on string: aba')
        self.outputPlainTextEdit.appendPlainText('[s0]aba')
        self.outputPlainTextEdit.appendPlainText('[s1]ba')
        return

    def quit_running_string_clicked(self):
        self.outputPlainTextEdit.clear()
        self.outputPlainTextEdit.setPlainText("Quit Running String Button Clicked")
        return

    def close_automaton_clicked(self):
        self.outputPlainTextEdit.clear()
        self.inputStringListWidget.clear()
        self.statusLabel.clear()
        self.outputPlainTextEdit.setPlainText("Close Automaton Button Clicked")
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PushDownAutomaton()
    sys.exit(app.exec_())