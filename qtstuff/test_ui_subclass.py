__author__ = 'charles.cognato'

# import pymongo
from PyQt4 import QtGui, QtCore
from qtstuff.test_ui import Ui_MainWindow

from qtstuff.validated_item_delagate import ValidatedItemDelegate

# MOD([DEC_NUM], 5) + 1) / 2 + 402.5

headers = ('Serial Number', 'PCBA S/N', 'Tx Freq', 'Work Order', '3.30v',
           '1.80v', '3.00v', 'Batt Voltage', 'Technician1', 'Date1', 'SW Rev',
            'S/N Match', 'Freq. Match', 'Transmit GPS Mode (0,1)', 'Technician2', 'Date2',
            'Time 3D Fix', 'PADS S/N', 'Pressure', 'Humidity', 'Temperature', 'Vbatt',
            'RSSI', 'Sat CNO', 'RF Level', 'Technician3', 'Date3', 'Pass/Fail', 'NCM #', 'Notes')


class TestUi(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(TestUi, self).__init__(parent)
        self.setupUi(self)

        self.actionExit.triggered.connect(self.action_exit_clicked)
        self.tableWidget.cellClicked.connect(self._cell_clicked)
        self.tableWidget.cellChanged.connect(self._cell_changed)

        self.buttonAddRow.clicked.connect(self._add_row)
        self.buttonDeleteRow.clicked.connect(self._delete_row)

        self._setup_tablewidget()

        validator = QtGui.QRegExpValidator(QtCore.QRegExp('0x4020[0-9A-F]{4}'), self)
        self.lineEdit.setValidator(validator)

        validated_item = ValidatedItemDelegate()
        self.tableWidget.setItemDelegate(validated_item)

    def event(self, event):
        if event.type() == QtCore.QEvent.KeyRelease:
            if event.key() == QtCore.Qt.Key_Return:
                print('you pressed the return key...')
            return True

        return QtGui.QMainWindow.event(self, event)

    def action_exit_clicked(self):
        self.close()

    def _setup_tablewidget(self):
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)

    def _cell_changed(self, row, col):
        # MOD([DEC_NUM], 5) + 1) / 2 + 402.5
        if col == 0 and self.tableWidget.item(row, 0).text() != '':
            item_freq = self.tableWidget.item(row, 2)
            if item_freq is None:
                print('no QTableWidgetItem found...')
                return
            else:
                print(item_freq)

            serial = self.tableWidget.item(row, col).text()
            serial = serial[-4:]
            freq = (int(serial, 16) % 5 + 1) / 2 + 402.5
            item_freq.setText(str(freq))

    def _cell_clicked(self, row, col):
        print('cell clicked: ', row, col)

    def _add_row(self):
        if len(self.tableWidget.selectedIndexes()) == len(headers):
            row = self.tableWidget.currentRow()
            self.tableWidget.insertRow(row)
            new_row = self.tableWidget.currentRow() - 1
            self.tableWidget.initialize_row(new_row)
        else:
            row = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(row + 1)
            self.tableWidget.initialize_row(row)

        # print('row count: ', self.tableWidget.rowCount())
        # print('selected cell count: ', len(self.tableWidget.selectedIndexes()))

    def _delete_row(self):
        if len(self.tableWidget.selectedIndexes()) % len(headers) == 0:
            for selected_range in self.tableWidget.selectedRanges():
                # selected_range = self.tableWidget.selectedRanges()[0]
                row = selected_range.topRow()
                for i in range(selected_range.topRow(), selected_range.bottomRow() + 1):
                    self.tableWidget.removeRow(row)
