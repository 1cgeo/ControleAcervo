import os, sys, copy
from PyQt5 import QtCore, uic, QtWidgets, QtGui

from ControleAcervo.app.factory.messageSingleton  import MessageSingleton

class DockWidget(QtWidgets.QWidget):

    def __init__(self, sapCtrl):
        super(DockWidget, self).__init__(sapCtrl=sapCtrl)
        uic.loadUi(self.getUiPath(), self)

    def loadIconBtn(self, button, pathIcon, toolTip):
        button.setIcon(QtGui.QIcon(pathIcon))
        button.setIconSize(QtCore.QSize(24,24))
        button.setToolTip(toolTip)
      
    def getUiPath(self):
        raise NotImplementedError()

    def runFunction(self):
        raise NotImplementedError()

    def validInput(self):
        raise NotImplementedError()

    def clearInput(self):
        raise NotImplementedError()
        
    def showMessageErro(self, title, text):
        MessageSingleton.getInstance().showError(
            self,
            title, 
            text
        )
        
    @QtCore.pyqtSlot(bool)
    def on_okBtn_clicked(self):
        if not self.validInput():
            self.showMessageErro('Aviso', "<p>Preencha todos os campos!</p>")
            return
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        try:
            self.runFunction()
            self.clearInput()
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()