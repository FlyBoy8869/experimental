__author__ = 'charles'

from PyQt4 import QtGui, QtCore


class ValidatedItemDelegate(QtGui.QStyledItemDelegate):

    def createEditor(self, widget, option, index):
        if not index.isValid():
            return 0

        if index.column() == 0:  # only on the cells in the first column
            editor = QtGui.QLineEdit(widget)
            validator = QtGui.QRegExpValidator(QtCore.QRegExp('0x4020[0-9A-F]{4}'), editor)
            editor.setValidator(validator)
            return editor

        elif index.column() == 4:  # 3.30 volts
            exp = '^(3\.)((2([5-9]))|(3([0-5])))$'
            editor = QtGui.QLineEdit(widget)
            validator = QtGui.QRegExpValidator(QtCore.QRegExp(exp), editor)
            editor.setValidator(validator)
            return editor

        elif index.column() == 5:  # 1.80 volts
            exp = '^(1\.)((7([5-9]))|(8([0-5])))$'
            editor = QtGui.QLineEdit(widget)
            validator = QtGui.QRegExpValidator(QtCore.QRegExp(exp), editor)
            editor.setValidator(validator)
            return editor

        elif index.column() == 6:  # 3.00 volts
            exp = '^([23]\.)((9([5-9]))|(0([1-5])))$'
            editor = QtGui.QLineEdit(widget)
            validator = QtGui.QRegExpValidator(QtCore.QRegExp(exp), editor)
            editor.setValidator(validator)
            return editor

        elif index.column() == 7:  # Battery Voltage
            exp = '^[4-9]\.\d\d'
            editor = QtGui.QLineEdit(widget)
            validator = QtGui.QRegExpValidator(QtCore.QRegExp(exp), editor)
            editor.setValidator(validator)
            return editor

        return super(ValidatedItemDelegate, self).createEditor(widget, option, index)