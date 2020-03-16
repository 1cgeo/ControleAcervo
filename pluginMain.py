import os, sys
from pathlib import Path
from qgis import core, gui
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon

class PluginControleAcervo(QObject):

    path_icon = Path(__file__).parent.resolve().joinpath('icon.jpg')

    def __init__(self, iface):
        super(PluginControleAcervo, self).__init__()
        self.plugin_dir = Path.parent(__file__)
        self.iface = iface
        self.action = QAction(
            QIcon(self.path_icon),
            "Ferramentas de Controle de Acervo",
            self.iface.mainWindow()
        )
        self.action.triggered.connect(
            self.startPlugin
        )

    def initGui(self):
        self.iface.digitizeToolBar().addAction(
            self.action
        )
        
    def unload(self):
        self.iface.digitizeToolBar().removeAction(
            self.action
        )

    def startPlugin(self):
        # Init controllers and show login dialog