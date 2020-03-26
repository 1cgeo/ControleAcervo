from ControleAcervo.app.factory.messageSingleton  import MessageSingleton

from pathlib import Path
from PyQt5 import QtCore, uic, QtWidgets, QtGui

class DockManagement(QtWidgets.QDockWidget):

    dialog_path = Path(__file__).resolve().parent.joinpath(
        'uis', 'managementDock.ui')

    tab_icon_path = Path(__file__).resolve().parent.joinpath(
        'icons', 'DSG.svg')

    item_icon_path = Path(__file__).resolve().parent.joinpath(
        'icons', 'config.png')

    def __init__(self):
        super().__init__()
        uic.loadUi(self.dialog_path, self)
        self.tabWidget.setTabIcon(0, QtGui.QIcon(self.tab_icon_path))
        self.tabWidget.setTabIcon(1, QtGui.QIcon(self.tab_icon_path))

        self.treeWidgetUserTab = QtWidgets.QTreeWidget()
        self.treeWidgetUserTab.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.treeWidgetUserTab.setColumnCount(1)
        self.treeWidgetUserTab.header().hide()
        self.connectQtreeWidgetSignals(self.treeWidgetUserTab)
        self.projectTab.layout().addWidget(self.treeWidgetUserTab)

        self.treeWidgetAdminTab = QtWidgets.QTreeWidget()
        self.treeWidgetAdminTab.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.treeWidgetAdminTab.setColumnCount(1)
        self.treeWidgetAdminTab.header().hide()
        self.connectQtreeWidgetSignals(self.treeWidgetAdminTab)
        self.creationTab.layout().addWidget(self.treeWidgetAdminTab)

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

    def addUserWidget(self, name, widget):
        topLevelItem = QtWidgets.QTreeWidgetItem([name])
        topLevelItem.setIcon(0, QtGui.QIcon(self.item_icon_path))
        childItem = QtWidgets.QTreeWidgetItem()
        topLevelItem.addChild(childItem)
        self.treeWidgetUserTab.addTopLevelItem(topLevelItem)
        self.treeWidgetUserTab.setItemWidget(childItem, 0, widget)

    def addAdminWidget(self, name, widget):
        topLevelItem = QtWidgets.QTreeWidgetItem([name])
        topLevelItem.setIcon(0, QtGui.QIcon(self.item_icon_path))
        childItem = QtWidgets.QTreeWidgetItem()
        topLevelItem.addChild(childItem)
        self.treeWidgetAdminTab.addTopLevelItem(topLevelItem)
        self.treeWidgetAdminTab.setItemWidget(childItem, 0, widget)

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