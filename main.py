from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtCore import Qt
from ui_main import UI_MainWindow
from database import Data_base
import pandas as pd
import sys
import sqlite3



class MainWindow(QMainWindow, UI_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Cadastro de Clientes")

        self.btn_home.clicked.connect(lambda: self.Page.setCurrentWidget(self.pg_home))
        self.btn_cadastrar.clicked.connect(lambda: self.Page.setCurrentWidget(self.pg_cadastrar))
        self.pushButton_4.clicked.connect(self.cadastrar_clientes)
        self.pushButton_6.clicked.connect(self.update_company)
        self.btn_excluir.clicked.connect(self.deletar_clientes)
        self.btn_excel.clicked.connect(self.gerar_excel)

        self.buscar_clientes()

    def cadastrar_clientes(self):
        db = Data_base()
        db.connect()

        fullDataSet = (
            self.lineEdit_3.text(),
            self.lineEdit_2.text(),
            self.lineEdit_5.text(),
            self.lineEdit_4.text(),
        )

        resp = db.register_company(fullDataSet)

        if resp == "OK":
            QMessageBox.information(self, "Cadastro Realizado", "Cadastro realizado com sucesso!")
            self.buscar_clientes()
        else:
            QMessageBox.critical(self, "Erro", "Erro ao cadastrar, verifique os dados.")

        db.close_connection()
    
    def buscar_clientes(self):
        db = Data_base()
        db.connect()
        result = db.select_all_companies()

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                item = QTableWidgetItem(str(data))
                if column == 0:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.tableWidget.setItem(row, column, item)

        db.close_connection()

    def update_company(self):
        update_dados = []

        for row in range(self.tableWidget.rowCount()):
            linha = []
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                if item is not None:
                    linha.append(item.text())
                else:
                    linha.append("")
            if all(linha):  # Verifica se todos os campos estão preenchidos
                update_dados.append(tuple(linha))

        if not update_dados:
            QMessageBox.warning(self, "Aviso", "Nenhuma linha válida para atualizar.")
            return

        db = Data_base()
        db.connect()

        for cliente in update_dados:
            db.update_company(cliente)

        db.close_connection()

        QMessageBox.information(self, "Atualização", "Dados atualizados com sucesso!")
        self.buscar_clientes()

    def deletar_clientes(self):

        db = Data_base()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registor será excluído.")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            cpf = self.tableWidget.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.delete_companies(cpf)
            self.buscar_clientes()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Clientes")
            msg.setText(result)
            msg.exec()

        db.close_connection()
 
    def gerar_excel(self):

        cnx = sqlite3.connect("system.db")

        clientes = pd.read_sql_query("""SELECT * FROM Clientes""", cnx)

        clientes.to_excel("Clientes.xlsx", sheet_name='clientes', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()



if __name__ == "__main__":
    db = Data_base()
    db.connect()
    db.create_table_company()
    db.close_connection()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
