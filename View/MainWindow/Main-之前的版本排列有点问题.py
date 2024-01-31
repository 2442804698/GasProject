#   主窗口
import sys
import matplotlib
matplotlib.use('QtAgg')
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Ui_MainWindow(QMainWindow):
    #   添加构造方法
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.path = None
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1128, 672)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Public/Icon/Gas.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(260, 20, 871, 611))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.verticalLayoutWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageLineChart = QtWidgets.QWidget()
        self.pageLineChart.setObjectName("pageLineChart")
        self.stackedWidget.addWidget(self.pageLineChart)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_3 = QtWidgets.QLabel(parent=self.page_2)
        self.label_3.setGeometry(QtCore.QRect(190, 290, 53, 15))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 261, 22))
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label.setObjectName("label")
        self.treeView = QtWidgets.QTreeView(parent=self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(0, 21, 261, 619))
        self.treeView.setObjectName("treeView")
        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 20, 1130, 2))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(250, 0, 20, 631))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
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
        self.stackedWidget.setCurrentIndex(0)
        self.actionOpen.triggered.connect(self.selectFiles)
        self.actionLineChart.triggered.connect(self.lineChart)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gas"))
        self.stackedWidget.setToolTip(_translate("MainWindow", "页面二"))
        self.label_3.setText(_translate("MainWindow", "页面二"))
        self.label.setText(_translate("MainWindow", "Tabel Of Contents"))
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

    def lineChart(self):
        sc = MplCanvas(self,width=5,height=4,dpi=100)
        sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
        self.verticalLayout.addWidget(sc)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('../../Style/mainWindow.qss') as style:
        app.setStyleSheet(style.read())
    ui = Ui_MainWindow()

    ui.show()
    sys.exit(app.exec())
