__author__ = 'charles.cognato'

import sys
from PyQt4 import QtGui
from qtstuff.test_ui_subclass import TestUi

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = TestUi()
    window.show()
    sys.exit(app.exec_())
