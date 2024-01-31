#   主窗口
import sys
import os
import matplotlib
from PySide6.QtCore import Signal
from PySide6.QtGui import QAction


matplotlib.use('QtAgg')
from PySide6 import QtCore, QtGui, QtWidgets
# from PySide6.QtGui import *
from PySide6.QtWidgets import (
    QMainWindow,
    QFileDialog,
    QFileSystemModel,
    QApplication,
    QDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QInputDialog
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import pandas as pd

basedir = os.path.dirname(__file__)


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=4, height=5, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MplCanvas, self).__init__(self.fig)

class Ui_MainWindow(QMainWindow):
    #   添加构造方法
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.path = None
        self.setupUi(self)
    def setupUi(self, MainWindow):
        #   主窗口初始化及设置
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1128, 672)
        icon = QtGui.QIcon()#   窗口图标
        icon.addPixmap(QtGui.QPixmap("../../Public/Icon/Gas.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        #   设置中心界面
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 591))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 2, 2, 1)
        self.labelContents = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.labelContents.setFont(font)
        self.labelContents.setAutoFillBackground(True)
        self.labelContents.setScaledContents(True)
        self.labelContents.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.labelContents.setObjectName("labelContents")
        self.gridLayout.addWidget(self.labelContents, 1, 0, 1, 2)
        self.treeView = QtWidgets.QTreeView(parent=self.centralwidget)
        self.treeView.setObjectName("treeView")
        self.gridLayout.addWidget(self.treeView, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1128, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(parent=self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(parent=self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuTools = QtWidgets.QMenu(parent=self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewProject = QtGui.QAction(parent=MainWindow)
        self.actionNewProject.setObjectName("actionNewProject")
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Public/Icon/Open-Menu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionLineChart = QtGui.QAction(parent=MainWindow)
        self.actionLineChart.setObjectName("actionLineChart")
        self.menuFile.addAction(self.actionNewProject)
        self.menuFile.addAction(self.actionOpen)
        self.menuTools.addAction(self.actionLineChart)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        #   信号与插槽
        self.actionOpen.triggered.connect(self.selectFiles)
        # self.actionLineChart.triggered.connect(self.lineChart)
        self.menuTools.triggered[QAction].connect(self.tools)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "H2s"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "CH4"))
        self.labelContents.setText(_translate("MainWindow", "Tabel Of Contents"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNewProject.setText(_translate("MainWindow", "NewProject"))
        self.actionOpen.setText(_translate("MainWindow", "open"))
        self.actionLineChart.setText(_translate("MainWindow", "Line Chart"))
    def selectFiles(self):
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.FileMode.Directory)
        if fd.exec():
            path = fd.selectedFiles()
            print(self)
            # self.actionOpen.triggered.connect(self.treeView.show)
            self.path = path[0]
            self.treeView.model = QFileSystemModel()
            self.treeView.model.setRootPath(self.path)
            self.treeView.setModel(self.treeView.model)
            self.treeView.setRootIndex(self.treeView.model.index(self.path))

    def getData(self,gasType:str,filePath:str):
        #   获取数据
        point = []
        value = []
        gas = {}

        dataFrame = pd.read_csv(filePath)
        for _,data in dataFrame.iterrows():
          sensors = data['sensors']
          # h2sPoint.append(data['point'])
          sensorsName = sensors.split("/")
          for i in sensorsName:
              if i != '':
                  sensorsData = i.split(":")
                  if sensorsData[0] == gasType.lower():
                      # h2sValue.append(float(sensorsData[1]))
                      gas[data['point']] = float(sensorsData[1])
        # 将点位排序
        tmp = sorted(gas.items(),key=lambda x:x[0])
        for i in tmp:
          point.append(i[0])
          value.append(i[1])
        return point, value
    def lineChart(self,filePath,gasType):
        newVerticalLayout = self.createTab(gasType)
        h2sPoint,h2sValue = self.getData(gasType,filePath)
        sc = MplCanvas(self,width=4,height=5,dpi=100)
        sc.fig.tight_layout()
        axes = sc.fig.add_subplot(1,1,1)
        axes.plot(h2sPoint, h2sValue)
        axes.set_xlabel('Point')
        axes.set_ylabel(gasType.capitalize())
        newVerticalLayout.addWidget(sc)
  
    def createTab(self,name):
            newTab = QtWidgets.QWidget()
            newTab.setObjectName(name+'Tab')
            newVerticalLayoutWidget = QtWidgets.QWidget(parent=newTab)
            newVerticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 591))
            newVerticalLayoutWidget.setObjectName("verticalLayoutWidget")
            newVerticalLayout = QtWidgets.QVBoxLayout(newVerticalLayoutWidget)
            newVerticalLayout.setContentsMargins(0, 0, 0, 0)
            newVerticalLayout.setObjectName(name+"verticalLayout")
            self.tabWidget.addTab(newTab,name)
            return newVerticalLayout
            
            
            
        

    def tools(self, m):
        if m.text() == "Line Chart":
            childWindow = ChildWindow()
            childWindow.lineChartSignal.connect(self.lineChart)
            childWindow.exec()
            

class ChildWindow(QDialog):
    lineChartSignal = Signal(str,str)
    def __init__(self,parent=None):
        super(ChildWindow,self).__init__(parent)
        self.setWindowTitle('Line Chart Selection')
        self.resize(400,200)
        layout = QHBoxLayout()
        filePath = QLabel('File Path:')
        gasType = QLabel('Gas Type:')
        self.filePathLineEdit = QLineEdit()
        self.gasTypeLineEdit = QLineEdit()
        self.okBtn = QPushButton('OK')
        layout.addWidget(filePath)
        layout.addWidget(self.filePathLineEdit)
        layout.addWidget(gasType)
        layout.addWidget(self.gasTypeLineEdit)
        layout.addWidget(self.okBtn)
        self.setLayout(layout)
        #   绑定信号
        self.filePathLineEdit.textEdited.connect(self.selectFile)
        self.gasTypeLineEdit.textEdited.connect(lambda: self.getCategory(self.gasTypeLineEdit))
        self.okBtn.clicked.connect(self.lineChartPathType)
    def lineChartPathType(self):
        filePath = self.filePathLineEdit.text()
        gasType = self.gasTypeLineEdit.text()
        self.lineChartSignal.emit(filePath,gasType)
        self.close()
    #   选择文件
    def selectFile(self):
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.FileMode.ExistingFiles)
        #   设置初始化路径
        fd.setDirectory('C:\\')
        #   过滤文件
        fd.setNameFilter('数据文件(*.csv )')
        if fd.exec():
            self.filePathLineEdit.setText(str(fd.selectedFiles()[0]))
    def getCategory(self, categoryInput):
        content, ok = QInputDialog.getItem(self, '类别', '请选择类别', ('H2s', 'So2', 'Ch4', 'Cs2'), 0, True)
        if ok:
            categoryInput.setText(content)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open(os.path.join(basedir,'../../Style/mainWindow.qss')) as style:
        app.setStyleSheet(style.read())
    ui = Ui_MainWindow()

    ui.show()
    sys.exit(app.exec())
