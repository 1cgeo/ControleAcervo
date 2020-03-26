# -*- coding: utf-8 -*-
from pathlib import Path
from PyQt5 import QtCore, uic, QtWidgets
from ControleAcervo.config import Config
# Import interface, if necessary
from ControleAcervo.app.factory.messageSingleton  import MessageSingleton

class Login(QtWidgets.QDialog):

    uiPath = Path(__file__).resolve().joinpath('../uis/login.ui')

    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi(self.uiPath, self)
        self.version_text.setText("<b>versão: {}</b>".format(Config.VERSION))
        
    def loadData(self, user, server):
        self.user.setText(user) 
        self.server.setText(server)  
        self.password.setText("")

    def showView(self):
        self.exec_()

    def closeView(self):
        self.close()

    def showError(self, title, text):
        MessageSingleton.getInstance().showError(
            self,
            title, 
            text
        )
        
    def validInput(self):
        test = ( 
            self.server.text() 
            and  
            self.user.text() 
            and
            self.password.text()
        )
        return test

    @QtCore.pyqtSlot(bool)
    def on_submitBtn_clicked(self):
        if not self.validInput():
            html = u'<p style="color:red">Todos os campos devem ser preenchidos!</p>'
            self.showError('Aviso', html)
            return
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        try:
            self.login()
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()

    def login(self):
        user = self.user.text() 
        password = self.password.text()
        server = self.server.text() 
        # self.loginCtrl.authUser(user, password, server)

    
        


    