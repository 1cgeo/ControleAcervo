from pathlib import Path
from PyQt5 import QtCore, uic, QtWidgets, QtGui
from ControleAcervo.app.dockWidgets.dockWidget  import DockWidget
 
class  DownloadLayers(DockWidget):

    def __init__(self, appCtrl):
        super().__init__(appCtrl=appCtrl)

    def getUiPath(self):
        return Path(__file__).resolve().parent.joinpath('uis', 'downloadLayers.ui')

    def clearInput(self):
        self.projectInProgressCkb.setChecked(False)

    def validInput(self):
        return True

    def runFunction(self):
        self.appCtrl.loadLayersQgisProject(
            self.projectInProgressCkb.isChecked()
        )