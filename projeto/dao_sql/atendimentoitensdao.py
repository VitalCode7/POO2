from dao_sql.dao import DAO
from models.atendimentoitens import AtendimentoItens

class AtendimentoItensDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO atendimentositens (id_atendimento, id_servico, qtd)
            VALUES (?, ?, ?, ?)
        """
        cls.execute(sql, (obj.get_id_atendimento(), obj.get_id_servico(), obj.get_qtd()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM atendimentoitens"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [AtendimentoItens(id, id_atendimento, id_servico, qtd) for (id, id_atendimento, id_servico, qtd) in rows]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM atendimentoitens WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = AtendimentoItens(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE atendimentoitens SET id_atendimento=?, id_servico=?, qtd=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_id_atendimento(), obj.get_id_servico(), obj.get_qtd(), obj.get_valor(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM atendimentoitens WHERE id=?"
        cls.execute(sql, (obj,))
        cls.fechar()