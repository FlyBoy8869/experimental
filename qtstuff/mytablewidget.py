__author__ = 'charles'

from PyQt4.QtCore import QEvent, Qt
from PyQt4.QtGui import QTableWidget, QWidget, QTableWidgetItem

headers = ('Serial Number', 'PCBA S/N', 'Tx Freq', 'Work Order', '3.30v',
           '1.80v', '3.00v', 'Batt Voltage', 'Technician1', 'Date')


class MyTableWidget(QTableWidget):
    def __init__(self, parent=None):
        super(MyTableWidget, self).__init__(parent)

        self.keys = [Qt.Key_Left,
                     Qt.Key_Right,
                     Qt.Key_Return]

    #def focusInEvent(self, event):
    #    return QTableWidget.focusInEvent(self, event)

    #def focusOutEvent(self, event):
    #    return QTableWidget.focusOutEvent(self, event)

    def event(self, event):
        if not self.hasFocus() and event.type() == QEvent.KeyRelease and event.key() in self.keys:
            self._move_cursor(event.key())

        return QTableWidget.event(self, event)

    def keyPressEvent(self, event):
        if self.hasFocus():
            if event.key() != Qt.Key_Return:  # this allows moving down one line by pressing the return key
                return QTableWidget.keyPressEvent(self, event)

        self._move_cursor(event.key())

    def _move_cursor(self, key):
        row = self.currentRow()
        col = self.currentColumn()

        if key == Qt.Key_Left and col > 0:
            col -= 1

        elif key == Qt.Key_Right and col < self.columnCount():
            col += 1

        elif key == Qt.Key_Up and row > 0:
            row -= 1

        elif key == Qt.Key_Down and row < self.rowCount():
            row += 1

        elif key == Qt.Key_Return:
            if row < self.rowCount() - 1:
                row += 1
            elif self.hasFocus():  # we're at the bottom of the table
                row += 1
                self.setRowCount(self.rowCount() + 1)
                self.initialize_row(row)

        else:
            return

        self.setCurrentCell(row, col)
        #self.edit(self.currentIndex())

    def initialize_row(self, row):
        for i in range(len(headers)):
            item = QTableWidgetItem()
            self.setItem(row, i, item)