import sqlite3

class Data_base:
    def __init__(self, name='system.db') -> None:
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_company(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Clientes(
                CPF TEXT PRIMARY KEY,
                NOME TEXT,
                EMAIL TEXT,
                SENHA TEXT
            );
        """)

    def register_company(self, fullDataSet):
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO Clientes (CPF, NOME, EMAIL, SENHA) VALUES (?, ?, ?, ?)",
                fullDataSet,
            )
            self.connection.commit()
            return "OK"
        except Exception as e:
            return f"Erro: {e}"

    def select_all_companies(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Clientes ORDER BY NOME")
            return cursor.fetchall()
        except:
            return []

    def delete_companies(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Clientes WHERE CPF = ?", (id,))
            self.connection.commit()
            return "Cadastro do Cliente excluído com sucesso!"
        except:
            return "Erro ao excluir registro!"

    def update_company(self, fullDataSet):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE Clientes SET
                    NOME = ?,
                    EMAIL = ?,
                    SENHA = ?
                WHERE CPF = ?
            """, (fullDataSet[1], fullDataSet[2], fullDataSet[3], fullDataSet[0]))
            self.connection.commit()
        except Exception as e:
            print(f"Erro ao atualizar cliente: {e}")
