<<<<<<< Updated upstream
# Import dockwidgets .py definitions here
=======
#insert dockwidgets here!
from ControleAcervo.app.dockWidgets.loadLayers  import LoadLayers
from ControleAcervo.app.dockWidgets.downloadLayers  import DownloadLayers
>>>>>>> Stashed changes

class DockDirector:

    #interface
<<<<<<< Updated upstream
    def constructManagementDock(self, dockBuilder, sapCtrl):
        # For each widget on addLoadLayers
        for functionWidget in [
                # {
                #     "name" : 'Avançar atividades para próxima etapa',
                #     "widget" : AdvanceActivityToNextStep(sapCtrl)
                # }
            ]:
            dockBuilder.addLoadLayersWidget(functionWidget['name'], functionWidget['widget'])
        # repeat for other tabs
        # Update managementDockBuilder.py
            
            
=======
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
>>>>>>> Stashed changes
