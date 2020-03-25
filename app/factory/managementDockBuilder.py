from ControleAcervo.dock.dockManagement import DockManagement

class ManagementDockBuilder():

    def __init__(self):
        super().__init__()
        self.dockManagement = DockManagement()

    def addLoadLayersWidget(self, name, widget):
        self.dockManagement.addLoadLayersWidget(name, widget)

    def getResult(self):
        return self.dockManagement