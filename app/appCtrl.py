from ControleAcervo.app.factory.loginSingleton import LoginSingleton
from ControleAcervo.app.factory.dockDirector import DockDirector
from ControleAcervo.app.factory.managementDockBuilder import ManagementDockBuilder


class AppCtrl():

    def __init__(self, gisPlatform):
        # Maybe inject gisPlatform on Interface
        super().__init__(gisPlatform)
        self.loginView = LoginSingleton.getInstance(loginCtrl=self)
        self.gisPlatform = gisPlatform
        self.dockApp= None

    def loadWidgetApp(self):
        dockDirector = DockDirector()
        managementDockBuilder = ManagementDockBuilder()
        dockDirector.constructSapManagementDock(managementDockBuilder, sapCtrl=self)
        self.dockApp = managementDockBuilder.getResult()
        self.gisPlatform.addDockWidget(self.dockApp)

    def showLoginView(self):
        pass

    def loadLoginView(self):
        pass
        
    def saveLoginData(self, user, server):
        pass

    def authUser(self, user, password, server):
        pass

