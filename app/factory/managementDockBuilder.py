from ControleAcervo.dock.dockManagement import DockManagement

class ManagementDockBuilder():

    def __init__(self):
        super().__init__()
        self.dockManagement = DockManagement()

    def addUserWidget(self, name, widget):
        self.dockManagement.addUserWidget(name, widget)

    def addAdminWidget(self, name, widget):
        self.dockManagement.addAdminWidget(name, widget)

    def getResult(self):
        return self.dockManagement