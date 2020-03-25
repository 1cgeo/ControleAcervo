from ControleAcervo.dock.dockManagement import DockManagement

class DockBuilder():

    def __init__(self):
        super().__init__()
        self.dockManagement = DockManagement()

    def addWidget(self, name, widget):
        self.dockManagement.addWidget(name, widget)

    def getResult(self):
        return self.dockManagement