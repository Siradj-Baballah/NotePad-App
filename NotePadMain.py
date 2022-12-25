from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QFontDialog, QColorDialog
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt6.QtCore import QFileInfo, Qt
from PyQt6.QtGui import QFont, QIcon,QPixmap
import sys
from NotePad import Ui_MainWindow

class NotePadWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.actionNew.triggered.connect(self.new_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)

        self.actionPrint.triggered.connect(self.print_file)
        self.actionPrint_Preview.triggered.connect(self.preview)
        self.actionExport_PDF.triggered.connect(self.export_pdf)

        self.actionQuit.triggered.connect(self.exit_app)

        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo.triggered.connect(self.textEdit.redo)
        self.actionCut.triggered.connect(self.textEdit.cut)
        self.actionCopy.triggered.connect(self.textEdit.copy)
        self.actionPaste.triggered.connect(self.textEdit.paste)

        self.actionBold.triggered.connect(self.text_bold)
        self.actionItalic.triggered.connect(self.text_italic)
        self.actionUnderline.triggered.connect(self.text_underline)
        self.actionNormal.triggered.connect(self.text_normal)

        self.actionCenter.triggered.connect(self.align_center)
        self.actionLeft.triggered.connect(self.align_left)
        self.actionRight.triggered.connect(self.align_right)

        self.actionUpper.triggered.connect(self.upper)
        self.actionLower.triggered.connect(self.lower)

        self.actionJustify.triggered.connect(self.align_justify)
        self.actionFont.triggered.connect(self.font_dialog)
        self.actionColor.triggered.connect(self.color_dialog)
        self.actionAbout_App.triggered.connect(self.about)

    def maybe_save(self):
        if self.textEdit.document().isEmpty():
            return True
        ret = QMessageBox.warning(self, "New File",
                                  "The Document has been modified. \n Do you want to save your changes ?",
                                  QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel)
        if ret == QMessageBox.StandardButton.Save:
            return self.save_file()
        if ret == QMessageBox.StandardButton.Cancel:
            return False
        return True

    def new_file(self):
        if self.maybe_save():
            self.textEdit.clear()

    def save_file(self):
        filename = QFileDialog.getSaveFileName(self,"Save File","","All files(*);;Text Files(*.txt)")
        if filename[0]:
            f = open(filename[0], 'w')
            with f:
                text = self.textEdit.toPlainText()
                f.write(text)
                QMessageBox.about(self, "Save File", "File has been saved")

    def open_file(self):
        filename = QFileDialog.getOpenFileName(self,"Open File","","All files(*);;Text Files(*.txt)")
        if filename[0]:
            f = open(filename[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)

    def print_file(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer)

        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self.textEdit.print(printer)

    def preview(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.print_preview)
        previewDialog.exec()

    def print_preview(self, printer):
        self.textEdit.print(printer)

    def export_pdf(self):
        filepdf, _ = QFileDialog.getSaveFileName(self,"Export PDF","","PDF Files(*.pdf);;All files(*)")
        if filepdf != "":
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(filepdf)
            self.textEdit.document().print(printer)
            QMessageBox.about(self, "Exported File to PDF", "File has been exported")

    def exit_app(self):
        self.close()

    def text_bold(self):
        self.textEdit.setStyleSheet("font-weight: bold;")

    def text_italic(self):
        self.textEdit.setStyleSheet("font-style: italic;")

    def text_underline(self):
        self.textEdit.setStyleSheet("text-decoration: underline;")

    def text_normal(self):
        self.textEdit.setStyleSheet("")
        self.textEdit.setFont(QFont("Segoe UI", 14))

    def align_left(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def align_right(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignRight)

    def align_center(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def align_justify(self):
        self.textEdit.setAlignment(Qt.AlignmentFlag.AlignJustify)

    def font_dialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def color_dialog(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    def about(self):
        QMessageBox.about(self, "About App", 'This is a simple NotePad app with PyQt6 \ncreated py " Siradj Eddine Baballah "')

    def upper(self):
        text = self.textEdit.toPlainText()
        self.textEdit.setText(text.upper())

    def lower(self):
        text = self.textEdit.toPlainText()
        self.textEdit.setText(text.lower())


app = QApplication(sys.argv)
Note = NotePadWindow()
sys.exit(app.exec())
