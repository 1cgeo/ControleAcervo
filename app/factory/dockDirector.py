# Import dockwidgets .py definitions here

class DockDirector:

    #interface
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
            
            