__author__ = 'charles'

from PyQt4 import QtGui, QtCore

technicians = ['Babb', 'Benoit', 'Burt', 'Cognato', 'Malzone']


class ValidatedItemDelegate(QtGui.QStyledItemDelegate):
    def __init__(self, validation_object, parent=None):
        super(ValidatedItemDelegate, self).__init__(parent)
        self.validation_object = validation_object

        self.invalid_icon = QtGui.QPixmap('./resources/red-x-icon-8x8.png')

    def createEditor(self, widget, option, index):
        if not index.isValid():
            return 0

        if index.column() == 0:  # serial number
            exp = '0x4020[0-9A-F]{4}'
            return self._create_qlineedit_validator(widget, exp)

        elif index.column() == 4:  # 3.30 volts
            #exp = '^(3\.)((2([5-9]))|(3([0-5])))$'
            exp = '^([0-9])\.([0-9])([0-9])$'
            return self._create_qlineedit_validator(widget, exp)

        elif index.column() == 5:  # 1.80 volts
            # exp = '^(1\.)((7([5-9]))|(8([0-5])))$'
            exp = '^([0-9])\.([0-9])([0-9])$'
            return self._create_qlineedit_validator(widget, exp)

        elif index.column() == 6:  # 3.00 volts
            # exp = '^([23]\.)((9([5-9]))|(0([0-5])))$'
            exp = '^([0-9])\.([0-9])([0-9])$'
            return self._create_qlineedit_validator(widget, exp)

        elif index.column() == 7:  # Battery Voltage
            # exp = '^[4-9]\.\d\d'
            exp = '^([0-9])\.([0-9])([0-9])$'
            return self._create_qlineedit_validator(widget, exp)

        elif index.column() == 8:  # Technician1
            return self._create_technician_combobox(widget,
                technicians, index.data())

        return super(ValidatedItemDelegate, self).createEditor(widget, option, index)

    def paint(self, QPainter, QStyleOptionViewItem, QModelIndex):
        cell = str(QModelIndex.row()) + str(QModelIndex.column())

        if cell in self.validation_object:
            painter = QPainter
            painter.setPen(QtCore.Qt.black)
            option = QStyleOptionViewItem
            painter.drawPixmap(option.rect.right() - self.invalid_icon.width() - 1,
                               option.rect.y() + 1, self.invalid_icon)

        QtGui.QStyledItemDelegate(self).paint(QPainter, QStyleOptionViewItem, QModelIndex)

    def _create_technician_combobox(self, widget, techs, data):
        editor = QtGui.QComboBox(widget)
        editor.addItems(techs)
        if data is None:
            editor.setCurrentIndex(0)
        else:
            editor.setCurrentIndex(editor.findText(data))
        return editor

    def _create_qlineedit_validator(self, widget, exp):
            editor = QtGui.QLineEdit(widget)
            validator = QtGui.QRegExpValidator(QtCore.QRegExp(exp), editor)
            editor.setValidator(validator)
            return editor
