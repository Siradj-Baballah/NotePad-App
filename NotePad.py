# Form implementation generated from reading ui file 'NotePad.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/notepad.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFormat = QtWidgets.QMenu(self.menubar)
        self.menuFormat.setObjectName("menuFormat")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/new.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionNew.setIcon(icon1)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/open.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/save.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName("actionSve")
        self.actionPrint = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/print.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPrint.setIcon(icon4)
        self.actionPrint.setObjectName("actionPrint")
        self.actionPrint_Preview = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/printprev.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPrint_Preview.setIcon(icon5)
        self.actionPrint_Preview.setObjectName("actionPrint_Preview")
        self.actionExport_PDF = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/pdf.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExport_PDF.setIcon(icon6)
        self.actionExport_PDF.setObjectName("actionExport_PDF")
        self.actionQuit = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionQuit.setIcon(icon7)
        self.actionQuit.setObjectName("actionQuit")
        self.actionUndo = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/undo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionUndo.setIcon(icon8)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/redo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionRedo.setIcon(icon9)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("images/cut.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCut.setIcon(icon10)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("images/copy.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCopy.setIcon(icon11)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("images/paste.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPaste.setIcon(icon12)
        self.actionPaste.setObjectName("actionPaste")
        self.actionBold = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("images/bold.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionBold.setIcon(icon13)
        self.actionBold.setObjectName("actionBold")
        self.actionItalic = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("images/italic.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionItalic.setIcon(icon14)
        self.actionItalic.setObjectName("actionItalic")
        self.actionNormal = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("images/normal.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionNormal.setIcon(icon15)
        self.actionNormal.setObjectName("actionNormal")
        self.actionUnderline = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("images/underline.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionUnderline.setIcon(icon16)
        self.actionUnderline.setObjectName("actionUnderline")
        self.actionCenter = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("images/center.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCenter.setIcon(icon17)
        self.actionCenter.setObjectName("actionCenter")
        self.actionLeft = QtGui.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("images/left.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionLeft.setIcon(icon18)
        self.actionLeft.setObjectName("actionLeft")
        self.actionRight = QtGui.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("images/right.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionRight.setIcon(icon19)
        self.actionRight.setObjectName("actionRight")

        self.actionUpper = QtGui.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("images/upper.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionUpper.setIcon(icon20)
        self.actionUpper.setObjectName("actionUpper")

        self.actionLower = QtGui.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("images/lower.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionLower.setIcon(icon21)
        self.actionLower.setObjectName("actionLower")

        self.actionJustify = QtGui.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("images/justify.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionJustify.setIcon(icon22)
        self.actionJustify.setObjectName("actionJustify")
        self.actionFont = QtGui.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("images/font.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionFont.setIcon(icon21)
        self.actionFont.setObjectName("actionFont")
        self.actionColor = QtGui.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("images/color.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionColor.setIcon(icon23)
        self.actionColor.setObjectName("actionColor")
        self.actionAbout_App = QtGui.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("images/aboutqt.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAbout_App.setIcon(icon24)
        self.actionAbout_App.setObjectName("actionAbout_App")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionPrint_Preview)
        self.menuFile.addAction(self.actionExport_PDF)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuFormat.addAction(self.actionBold)
        self.menuFormat.addAction(self.actionItalic)
        self.menuFormat.addAction(self.actionUnderline)
        self.menuFormat.addAction(self.actionNormal)
        self.menuFormat.addSeparator()
        self.menuFormat.addAction(self.actionCenter)
        self.menuFormat.addAction(self.actionLeft)
        self.menuFormat.addAction(self.actionRight)
        self.menuFormat.addSeparator()
        self.menuFormat.addAction(self.actionUpper)
        self.menuFormat.addAction(self.actionLower)
        self.menuFormat.addSeparator()
        self.menuFormat.addAction(self.actionJustify)
        self.menuFormat.addAction(self.actionFont)
        self.menuFormat.addAction(self.actionColor)
        self.menuAbout.addAction(self.actionAbout_App)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFormat.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " NotePad App"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuFormat.setTitle(_translate("MainWindow", "Format"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionPrint_Preview.setText(_translate("MainWindow", "Print Preview"))
        self.actionPrint_Preview.setShortcut(_translate("MainWindow", "Ctrl+Shift+P"))
        self.actionExport_PDF.setText(_translate("MainWindow", "Export PDF"))
        self.actionExport_PDF.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionBold.setText(_translate("MainWindow", "Bold"))
        self.actionBold.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.actionItalic.setText(_translate("MainWindow", "Italic"))
        self.actionItalic.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionUnderline.setText(_translate("MainWindow", "Underline"))
        self.actionUnderline.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionNormal.setText(_translate("MainWindow", "Normal"))
        self.actionNormal.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionCenter.setText(_translate("MainWindow", "Center"))
        self.actionCenter.setShortcut(_translate("MainWindow", "Ctrl+K"))
        self.actionLeft.setText(_translate("MainWindow", "Left"))
        self.actionLeft.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionRight.setText(_translate("MainWindow", "Right"))
        self.actionRight.setShortcut(_translate("MainWindow", "Ctrl+R"))

        self.actionUpper.setText(_translate("MainWindow", "Upper"))
        self.actionUpper.setShortcut(_translate("MainWindow", "Ctrl+Shift+U"))
        self.actionLower.setText(_translate("MainWindow", "Lower"))
        self.actionLower.setShortcut(_translate("MainWindow", "Ctrl+Shift+L"))

        self.actionJustify.setText(_translate("MainWindow", "Justify"))
        self.actionJustify.setShortcut(_translate("MainWindow", "Ctrl+J"))
        self.actionFont.setText(_translate("MainWindow", "Font"))
        self.actionFont.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionColor.setText(_translate("MainWindow", "Color"))
        self.actionColor.setShortcut(_translate("MainWindow", "Ctrl+Shift+C"))
        self.actionAbout_App.setText(_translate("MainWindow", "About App"))

