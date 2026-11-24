from dao_sql.dao import DAO
from models.servico import Servico

class ServicoDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO servico (descricao, valor)
            VALUES (?, ?)
        """
        cls.execute(sql, (obj.get_descricao(), obj.get_valor()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM servico"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [Servico(id, descricao, valor) for (id, descricao, valor) in rows]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM servico WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Servico(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE servico SET descricao=?, valor=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_descricao(), obj.get_valor(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM servico WHERE id=?"
        cls.execute(sql, (obj,))
        cls.fechar()