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
        
        self.treeWidgetLoadLayers = QtWidgets.QTreeWidget()
        self.treeWidgetLoadLayers.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.treeWidgetLoadLayers.setColumnCount(1)
        self.treeWidgetLoadLayers.header().hide()
        self.connectQtreeWidgetSignals(self.treeWidgetLoadLayers)
        self.projectTab.layout().addWidget(self.treeWidgetLoadLayers)

        self.treeWidgetDownloadlayers = QtWidgets.QTreeWidget()
        self.treeWidgetDownloadlayers.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.treeWidgetDownloadlayers.setColumnCount(1)
        self.treeWidgetDownloadlayers.header().hide()
        self.connectQtreeWidgetSignals(self.treeWidgetDownloadlayers)
        self.creationTab.layout().addWidget(self.treeWidgetDownloadlayers)

        self.treeWidgetManagementTools = QtWidgets.QTreeWidget()
        self.treeWidgetManagementTools.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.treeWidgetManagementTools.setColumnCount(1)
        self.treeWidgetManagementTools.header().hide()
        self.connectQtreeWidgetSignals(self.treeWidgetManagementTools)

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

    def addLoadLayersWidget(self, name, widget):
        topLevelItem = QtWidgets.QTreeWidgetItem([name])
        topLevelItem.setIcon(0, QtGui.QIcon(self.item_icon_path))
        childItem = QtWidgets.QTreeWidgetItem()
        topLevelItem.addChild(childItem)
        self.treeWidgetLoadLayers.addTopLevelItem(topLevelItem)
        self.treeWidgetLoadLayers.setItemWidget(childItem, 0, widget)

    def addDownloadLayersWidget(self, name, widget):
        topLevelItem = QtWidgets.QTreeWidgetItem([name])
        topLevelItem.setIcon(0, QtGui.QIcon(self.item_icon_path))
        childItem = QtWidgets.QTreeWidgetItem()
        topLevelItem.addChild(childItem)
        self.treeWidgetDownloadlayers.addTopLevelItem(topLevelItem)
        self.treeWidgetDownloadlayers.setItemWidget(childItem, 0, widget)

    def addManagementToolsWidget(self, name, widget):
        topLevelItem = QtWidgets.QTreeWidgetItem([name])
        topLevelItem.setIcon(0, QtGui.QIcon(self.item_icon_path))
        childItem = QtWidgets.QTreeWidgetItem()
        topLevelItem.addChild(childItem)
        self.treeWidgetManagementTools.addTopLevelItem(topLevelItem)
        self.treeWidgetManagementTools.setItemWidget(childItem, 0, widget)

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