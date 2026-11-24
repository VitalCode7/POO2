from dao_sql.dao import DAO
from models.profissional import Profissional

class ProfissionalDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO profissional (nome, email, especialidade, senha)
            VALUES (?, ?, ?, ?)
        """
        cls.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_especialidade(), obj.get_senha()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM profissional"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [Profissional(id, nome, email, especialidade, senha) for (id, nome, email, especialidade, senha) in rows]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM profissional WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Profissional(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE profissional SET nome=?, email=?, fone=?, senha=?, imagem=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_especialidade(), obj.get_senha(), obj.get_imagem(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM profissional WHERE id=?"
        cls.execute(sql, (obj,))
        cls.fechar()