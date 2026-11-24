import streamlit as st
from service import Service
import time
import base64

class PerfilProfissionalUI:
    def main():
        st.header("Meus Dados")
        op = Service.profissional_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
        senha = st.text_input("Informe a nova senha", op.get_senha(),type="password")
        foto = st.file_uploader("Insira uma imagem", type=["png", "jpg", "jpeg"])
        if st.button("Atualizar"):
            id = op.get_id()
            try: 
                if foto is not None:
                    bytes_da_imagem = foto.getvalue()
                    imagem_string = base64.b64encode(bytes_da_imagem).decode("utf-8")
                Service.profissional_atualizar(id, nome, email, especialidade, senha, imagem_string)
                st.success("Profissional atualizado com sucesso")
            except ValueError as e:
                st.write(e)
                st.error("Informações não podem ser alteradas!")
            finally: 
                time.sleep(2)
                st.rerun()