#insert dockwidgets here!
from ControleAcervo.app.dockWidgets.loadLayers  import LoadLayers
from ControleAcervo.app.dockWidgets.downloadLayers  import DownloadLayers

class DockDirector:

    #interface
    def constructAppManagementDock(self, dockBuilder, appCtrl):
        #User tab
        for functionWidget in [
                {
                    "name" : 'Carregar camada',
                    "widget" : LoadLayers(appCtrl)
                },
                {
                    "name" : 'Baixar camada',
                    "widget" : DownloadLayers(appCtrl)
                }
            ]:
            dockBuilder.addUserWidget(functionWidget['name'], functionWidget['widget'])
        #Admin tab
        # for functionWidget in [
        #         {
        #             "name" : 'Adicionar nova revisão',
        #             "widget" : AddNewRevision(sapCtrl)
        #         }
        #     ]:
        #     dockBuilder.addAdminWidget(functionWidget['name'], functionWidget['widget'])
