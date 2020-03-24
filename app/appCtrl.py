from ControleAcervo.app.factory.loginSingleton import LoginSingleton


class AppCtrl():

    def __init__(self, gisPlatform):
        # Maybe inject gisPlatform on Interface
        super(Controller, self).__init__(gisPlatform)
        self.loginView = LoginSingleton.getInstance(loginCtrl=self)
        self.gisPlatform = gisPlatform

    def loadDockSap(self):
        pass

    def loadLoginView(self):
        pass
        
    def saveLoginData(self, user, server):
        pass