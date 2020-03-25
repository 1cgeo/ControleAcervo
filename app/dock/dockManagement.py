from ControleAcervo.app.factory.messageSingleton  import MessageSingleton

from pathlib import Path
from PyQt5 import QtCore, uic, QtWidgets, QtGui

class ManagementDock(QtWidgets.QDockWidget, IManagementDock):

    dialog_path = Path(__file__).parent.resolve().joinpath(
        'uis', 'managementDock.ui')

    tab_icon_path = Path(__file__).parent.resolve().joinpath(
        'icons', 'DSG.svg')

    item_icon_path = Path(__file__).parent.resolve().joinpath(
        'icons', 'config.png')

    def __init__(self):
        super(ManagementDock, self).__init__()
        uic.loadUi(self.dialog_path, self)
        self.tabWidget.setTabIcon(0, QtGui.QIcon(self.tab_icon_path))
        self.tabWidget.setTabIcon(1, QtGui.QIcon(self.tab_icon_path))
        self.tabWidget.setTabIcon(2, QtGui.QIcon(self.tab_icon_path))
        self.tabWidget.setTabIcon(3, QtGui.QIcon(self.tab_icon_path))
        
        self.treeWidgetManagement = QtWidgets.QTreeWidget()
        self.treeWidgetManagement.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.treeWidgetManagement.setColumnCount(1)
        self.treeWidgetManagement.header().hide()
        self.connectQtreeWidgetSignals(self.treeWidgetManagement)
        self.projectTab.layout().addWidget(self.treeWidgetManagement)

        self.treeWidgetCreation = QtWidgets.QTreeWidget()
        self.treeWidgetCreation.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.treeWidgetCreation.setColumnCount(1)
        self.treeWidgetCreation.header().hide()
        self.connectQtreeWidgetSignals(self.treeWidgetCreation)
        self.creationTab.layout().addWidget(self.treeWidgetCreation)

        self.treeWidgetDanger = QtWidgets.QTreeWidget()
        self.treeWidgetDanger.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.treeWidgetDanger.setColumnCount(1)
        self.treeWidgetDanger.header().hide()
        self.connectQtreeWidgetSignals(self.treeWidgetDanger)
        self.dangerZoneTab.layout().addWidget(self.treeWidgetDanger)

    def connectQtreeWidgetSignals(self, treeWidget):
        treeWidget.itemExpanded.connect(
            self.handleItemExpanded
        )

    def disconnectQtreeWidgetSignals(self, treeWidget):
        treeWidget.itemExpanded.disconnect(
            self.handleItemExpanded
        )

    def handleItemExpanded(self, item):
        treeWidget = self.sender()
        treeWidget.collapseAll()
        self.disconnectQtreeWidgetSignals(treeWidget)
        item.setExpanded(True)
        self.connectQtreeWidgetSignals(treeWidget)

    def addProjectManagementWidget(self, name, widget):
        topLevelItem = QtWidgets.QTreeWidgetItem([name])
        topLevelItem.setIcon(0, QtGui.QIcon(self.item_icon_path))
        childItem = QtWidgets.QTreeWidgetItem()
        topLevelItem.addChild(childItem)
        self.treeWidgetManagement.addTopLevelItem(topLevelItem)
        self.treeWidgetManagement.setItemWidget(childItem, 0, widget)

    def addProjectCreationWidget(self, name, widget):
        topLevelItem = QtWidgets.QTreeWidgetItem([name])
        topLevelItem.setIcon(0, QtGui.QIcon(self.item_icon_path))
        childItem = QtWidgets.QTreeWidgetItem()
        topLevelItem.addChild(childItem)
        self.treeWidgetCreation.addTopLevelItem(topLevelItem)
        self.treeWidgetCreation.setItemWidget(childItem, 0, widget)

    def addDangerZoneWidget(self, name, widget):
        topLevelItem = QtWidgets.QTreeWidgetItem([name])
        topLevelItem.setIcon(0, QtGui.QIcon(self.item_icon_path))
        childItem = QtWidgets.QTreeWidgetItem()
        topLevelItem.addChild(childItem)
        self.treeWidgetDanger.addTopLevelItem(topLevelItem)
        self.treeWidgetDanger.setItemWidget(childItem, 0, widget)

    def showError(self, title, text):
        MessageSingleton.getInstance().showError(
            self,
            title, 
            text
        )

    def showInfo(self, title, text):
        MessageSingleton.getInstance().showInfo(
            self,
            title, 
            text
        )