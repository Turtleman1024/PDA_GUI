import sys
from Configuration_Settings import Configuration_Settings
from Validate_Def_File import Validate_Def_File
from Automaton import Automaton
from Input_Strings import Input_Strings
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenuBar, QMenu, QLabel, QLineEdit, QPushButton, QListWidget, QSpinBox, QCheckBox, QPlainTextEdit, QStatusBar, QShortcut, QFileDialog, QTreeWidget, QTreeWidgetItem, QVBoxLayout
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt

class PushDownAutomaton(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Creating an Automaton class instance
        self.Automaton = Automaton()
        # Creating a Input_String class instance
        self.Strings = Input_Strings()
        # Creating a Configuration_Setting instance
        self.Config_Setting = Configuration_Settings()
        # A attribute to remember the def_path
        self.def_path = ''
        # A attribute to remember if the automaton was opened
        self.automaton_open = False

        self.setWindowTitle("Pushdown Automaton")
        self.resize(640, 480)

        self.mainMenu = self.menuBar()

        self.fileMenu = self.mainMenu.addMenu("File")
        self.fileMenu.addAction("Open Automaton     Ctrl+O", self.open_automaton_action)
        self.openShorcut = QShortcut(QKeySequence("Ctrl+O"), self)
        self.openShorcut.activated.connect(self.open_automaton_action)
        #self.fileMenu.addAction("View Automaton", self.view_automaton_action)
        self.fileMenu.addAction("Quit                            Ctrl+Shift+Q", self.quit_action)
        self.quitAppShorcut = QShortcut(QKeySequence("Ctrl+Shift+Q"), self)
        self.quitAppShorcut.activated.connect(self.quit_action)

        self.helpMenu = self.mainMenu.addMenu("Help")
        self.helpMenu.addAction("User Manual        Ctrl+H", self.user_manual_action)
        self.userManualShorcut = QShortcut(QKeySequence("Ctrl+H"), self)
        self.userManualShorcut.activated.connect(self.user_manual_action)

        self.inputStringLabel = QLabel(self)
        self.inputStringLabel.setGeometry(20, 40, 111, 16)
        self.inputStringLabel.setText("Input String")

        self.inputStringLineEdit = QLineEdit(self)
        self.inputStringLineEdit.setGeometry(20, 60, 231, 20)

        self.addToListPushButton = QPushButton(self)
        self.addToListPushButton.setGeometry(80, 90, 111, 23)
        self.addToListPushButton.setText("Add to List")
        self.addToListPushButton.clicked.connect(self.add_to_list_clicked)
        self.addToListShorcut = QShortcut(QKeySequence("Ctrl+Shift+A"), self)
        self.addToListShorcut.activated.connect(self.add_to_list_clicked)
        self.addToListPushButton.setToolTip("Ctrl+Shift+A")

        self.inputStringListLabel = QLabel(self)
        self.inputStringListLabel.setGeometry(20, 125, 111, 16)
        self.inputStringListLabel.setText("Input String List")

        self.inputStringListWidget = QListWidget(self)
        self.inputStringListWidget.setGeometry(20, 145, 231, 260)

        self.runStringPushButton = QPushButton(self)
        self.runStringPushButton.setGeometry(80, 415, 111, 23)
        self.runStringPushButton.setText("Run String")
        self.runStringPushButton.clicked.connect(self.run_string_clicked)
        self.runStringShorcut = QShortcut(QKeySequence("Ctrl+R"), self)
        self.runStringShorcut.activated.connect(self.run_string_clicked)
        self.runStringPushButton.setToolTip("Ctrl+R")

        self.fileNameLabel = QLabel(self)
        self.fileNameLabel.setGeometry(440, 40, 160, 16)
        self.fileNameLabel.setText("Automaton Title")
        self.fileNameLabel.setStyleSheet("color: blue")

        self.outputLabel = QLabel(self)
        self.outputLabel.setGeometry(300, 60, 47, 16)
        self.outputLabel.setText("Output")

        self.maxTransitionsLabel = QLabel(self)
        self.maxTransitionsLabel.setGeometry(370, 60, 80, 16)
        self.maxTransitionsLabel.setText("Max. Transitions")

        self.maxTransitionsSpinBox = QSpinBox(self)
        self.maxTransitionsSpinBox.setGeometry(455, 57, 42, 20)
        self.maxTransitionsSpinBox.setMinimum(1)
        #access value with self.maxTransitionsSpinBox.value

        self.displayPathsCheckBox = QCheckBox(self)
        self.displayPathsCheckBox.setGeometry(530, 60, 101, 17)
        self.displayPathsCheckBox.setText("Display Paths")
        #access true or false with self.displayPathsCheckBox.checked

        self.outputPlainTextEdit = QPlainTextEdit(self)
        self.outputPlainTextEdit.setGeometry(300, 80, 271, 253) #300, 80, 281, 283

        self.stackPlainTextEdit = QPlainTextEdit(self)
        self.stackPlainTextEdit.setGeometry(581, 80, 30, 253)

        self.pathLabel = QLabel(self)
        self.pathLabel.setGeometry(300, 335, 47, 16)
        self.pathLabel.setText("Path")

        self.pathPlainTextEdit = QPlainTextEdit(self)
        self.pathPlainTextEdit.setGeometry(300, 355, 311, 50)

        self.quitRunningStringPushButton = QPushButton(self)
        self.quitRunningStringPushButton.setGeometry(335, 415, 111, 23)
        self.quitRunningStringPushButton.setText("Quit Running String")
        self.quitRunningStringPushButton.clicked.connect(self.quit_running_string_clicked)
        self.quitRunningStringShorcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.quitRunningStringShorcut.activated.connect(self.quit_running_string_clicked)
        self.quitRunningStringPushButton.setToolTip("Ctrl+Q")

        self.closeAutomatonPushButton = QPushButton(self)
        self.closeAutomatonPushButton.setGeometry(465, 415, 111, 23)
        self.closeAutomatonPushButton.setText("Close Automaton")
        self.closeAutomatonPushButton.clicked.connect(self.close_automaton_clicked)
        self.closeAutomatonShorcut = QShortcut(QKeySequence("Ctrl+Alt+C"), self)
        self.closeAutomatonShorcut.activated.connect(self.close_automaton_clicked)
        self.closeAutomatonPushButton.setToolTip("Ctrl+Alt+C")

        # Style for status label text
        self.styleError = 'font: 15pt Arial; color: maroon'
        self.styleNormal = 'font:15pt Arial; color: green'

        self.statusBar = self.statusBar()
        self.statusLabel = QLabel("application status messages will go here (when something completes, etc.)")
        self.statusLabel.setStyleSheet(self.styleNormal)
        self.statusBar.addPermanentWidget(self.statusLabel)

        self.show()

    def parseConfigFile(self, file_path):
        # Load the config settings
        self.Config_Setting.load(file_path)
        # Set the value parsed from the config file to the spinbox
        self.maxTransitionsSpinBox.setValue(int(self.Config_Setting.max_trans[0]))
        return

    def parseInputStringFile(self, file_path):
        # If the input string widget is empty add the input strings to the widget
        if self.inputStringListWidget.count() == 0:
            # Loading the string into the Strings attribute input_strings
            self.Strings.load(file_path)
            for string in self.Strings.input_strings:
                # If the string is valid
                if self.Strings.validate(self.Automaton.Input_Alpha.alphabet, string) == True:
                    # Add the string to the widget
                    self.inputStringListWidget.addItem(string)
        return

    # A method to update the input string widget
    def update_input_string_widget(self):
        self.inputStringListWidget.clear()
        for string in self.Strings.input_strings:
            self.inputStringListWidget.addItem(string)

    def quit_action(self):
        sys.exit(0)

    def open_automaton_action(self):
        #self.outputPlainTextEdit.setPlainText("Open Automaton Clicked")

        # Save the location of the def file
        self.def_path, _ = QFileDialog.getOpenFileName(self, "Select Definition File", "", ".def files (*.def)")
        #self.def_path = 'pda.def'
        #self.invalid_def_path = 'invalid_pda.def'

        # Check if the defintion file is valid
        Valid_def = Validate_Def_File(self.def_path)
        if Valid_def.def_valid == True:
           # Load the Automaton
           self.Automaton.load(self.def_path)
           # Store the the automaton is opened
           self.automaton_open = True
           # Set def path to the status bar
           self.statusLabel.setText(self.def_path)
           # Now parse config file
           self.parseConfigFile(self.def_path)
           # Now parse the input strings
           self.parseInputStringFile(self.def_path)
           # Set normal label styling
           self.statusLabel.setStyleSheet(self.styleNormal)
           # Change automaton title label
           self.fileNameLabel.setText(self.def_path.split("/")[-1])
        else:
            error_list = []
            error_list = Valid_def.is_invalid_def()
            for item in error_list:
                self.outputPlainTextEdit.appendPlainText(item)
            # Set status label
            status = self.def_path + " is invalid!"
            self.statusLabel.setText(status)
            # Set error label styling
            self.statusLabel.setStyleSheet(self.styleError)

        return

    #def view_automaton_action(self):
    #    self.outputPlainTextEdit.setPlainText("View Automaton Clicked")
    #    file = open(self.def_path, 'r')
    #    for line in file:
    #        self.outputPlainTextEdit.appendPlainText(line)
    #    return

    def user_manual_action(self):
        userMan = HelpMenu()
        userMan.__init__()

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
        selected_string = ''

        if len(self.inputStringListWidget.selectedItems()) > 0:
            selected_string = self.inputStringListWidget.selectedItems()[0].text()
        else:
            self.statusLabel.setStyleSheet(self.styleError)
            self.statusLabel.setText('No input string selected')

        #self.outputPlainTextEdit.setPlainText("Run String Button Clicked")
        self.Automaton.run_string(selected_string)
        outputTransitions = self.Automaton.transitions_list
        outputStack = self.Automaton.stack
        outputPath = str(outputTransitions[0])

        #self.outputPlainTextEdit.setPlainText(outputTransitions)
        for element in outputTransitions:
            self.outputPlainTextEdit.setPlainText(str(element))
        #self.stackPlainTextEdit.setPlainText(outputStack) #add \n's
        self.stackPlainTextEdit.setPlainText("")
        for char in outputStack:
            self.stackPlainTextEdit.appendPlainText(char)
        if (self.displayPathsCheckBox.isChecked()):
            self.pathPlainTextEdit.appendPlainText(outputPath + " -> ") #add ->'s

    def quit_running_string_clicked(self):
        self.outputPlainTextEdit.setPlainText("Quit Running String Button Clicked")
        return

    def close_automaton_clicked(self):
        self.outputPlainTextEdit.clear()
        self.inputStringListWidget.clear()
        self.statusLabel.clear()
        self.outputPlainTextEdit.setPlainText("Close Automaton Button Clicked")
        return

class HelpMenu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Help Guide")
        self.resize(640, 480)
        
        #create output window
        self.helpListOutput = QPlainTextEdit(self)
        #self.helpListOutput.setReadOnly(True)
        self.helpListOutput.setGeometry(20, 40, 600, 360)

        #add close button
        self.helpQuitButton = QPushButton(self)
        self.helpQuitButton.setGeometry(220, 410, 200, 40)
        self.helpQuitButton.setText("Close")
        self.helpQuitButton.clicked.connect(self.close)

        #help topics content
        self.helpText = """RUN AUTOMATON
To run the pushdown automaton, you must do the following:
1. Load the pushdown automaton definition file.
---This can be done by selecting the "File" menu from the top of the window and selecting "Open Automaton" from the menu.
---This will open a file browser to select the desired pushdown automaton definition file.
2. Select an input string to run the pushdown automaton on
---After loading the definition file, you must either manually add a valid input string or select an input string from the "Input String List" that was loaded from a "pda.str" text file containing input strings.
3. Click "Run String"
---After selecting the desired input string to be ran with the given pushdown automaton definition file, click the "Run String" button.
---Once the pushdown automaton has been started, the current state of the pushdown automaton as well as any results returned will be displayed in the output subwindow on the right side of the window.

STOP AUTOMATON
While the pushdown automaton is running, you have the option of stopping its execution on the input string by clicking the "Quit Running String" button just below the output window.
If you have the pushdown automaton halt its execution, you may then select a different input string to be ran instead.
If you are interested in loading a different definition file for the pushdown automaton, you may click the "Close Automaton" button below the output subwindow.
This will cause the current pushdown automaton definition file to be unloaded, and a different definition file may be loaded using the same process as was done to load the original pushdown automaton definition file.
Any error that are encountered will be shown at the bottom of the window in red, as well as giving more information about the error.

LOAD AUTOMATON
This command allows the user to select a definition file from the file browser.
If the definition file is not present, an error message will be presented in the status label on the bottom right corner of the window.
An input string list file is not required to be present in order to run load the pushdown automaton.

INPUT STRING TEXT BOX
This text box allows the user to create input strings manually.
After entering a valid input string in this text box, click the ‘Add to List’ button to add the input string to the ‘Input String List’ that is below.
If an invalid input string is provided, an error message will be presented on the bottom right corner of the application window, indicating such.

INPUT STRING LIST
This section shows the available input strings that can be ran with the pushdown automaton. To select an input string, click on the desired input string from the list shown. 
Once clicked, the selected input string will be highlighted.
To run the input string with the currently loaded pushdown automaton, click the ‘Run String’ button at the bottom of the window. 
An input string must be selected from this list to be run with the pushdown automaton.
If there aren’t any input strings in this list, one will have to be added manually using the ‘Input String’ textbox above.

OUTPUT WINDOW
The results of running the pushdown automaton will be displayed within this box on the right side of the application window. 
These results include the progress of the pushdown automaton as it is running as well as the final results of running the selected input string with the current pushdown automaton.
To the right of the output section is a tall and narrow section which indicated the current and running contents of the stack within the pushdown automaton.

MAX TRANSITIONS
This option indicated the maximum number of transitions to be allowed while running the pushdown automaton. 
This option can be changed by clicking on the arrows to the right of the number just to the right of the ‘Max. Transit’ label.
This number cannot be less than 1.

DISPLAY PATH TEXT
This checkbox determines whether you want to show the path of the pushdown automaton. If this box is checked, the path will be displayed at the bottom of the output section.

QUIT RUNNING BUTTON
This button will force the pushdown automaton to stop running on the selected input string."""

        self.helpListOutput.setPlainText(self.helpText)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    ex = PushDownAutomaton()
    sys.exit(app.exec_())