from ControleAcervo.dock.dockManagement import DockManagement

class ManagementDockBuilder():

    def __init__(self):
        super().__init__()
        self.dockManagement = DockManagement()

<<<<<<< Updated upstream
    def addLoadLayersWidget(self, name, widget):
        self.dockManagement.addLoadLayersWidget(name, widget)
=======
    def addUserWidget(self, name, widget):
        self.dockManagement.addUserWidget(name, widget)

    def addAdminWidget(self, name, widget):
        self.dockManagement.addAdminWidget(name, widget)
>>>>>>> Stashed changes

    def getResult(self):
        return self.dockManagement