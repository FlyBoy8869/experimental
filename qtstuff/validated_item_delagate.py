__author__ = 'charles'

from PyQt4 import QtGui, QtCore


class ValidatedItemDelegate(QtGui.QStyledItemDelegate):
    def __init__(self, reg_exp='*'):
        super(ValidatedItemDelegate, self).__init__()
        self.reg_exp = reg_exp

    def createEditor(self, widget, option, index):
        if not index.isValid():
            return 0
        if index.column() == 0: #only on the cells in the first column
            editor = QtGui.QLineEdit(widget)
            validator = QtGui.QRegExpValidator(QtCore.QRegExp(self.reg_exp), editor)
            editor.setValidator(validator)
            return editor
        return super(ValidatedItemDelegate, self).createEditor(widget, option, index)