import streamlit as st
import pandas as pd
import time
from projeto.q4_service import Service

class ManterConvenioUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterConvenioUI.listar()
        with tab2: ManterConvenioUI.inserir()
        with tab3: ManterConvenioUI.atualizar()
        with tab4: ManterConvenioUI.excluir()
    def listar():
        convenios = Service.convenio_listar()
        if len(convenios) == 0: st.write("Nenhum convenio cadastrado")
        else:
            list_dic = []
            for obj in convenios: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        if st.button("Inserir"):
            Service.convenio_inserir(nome, email, fone)
            st.success("Convenio inserido com sucesso")
            time.sleep(2)
            st.rerun()
    def atualizar():
        convenios = Service.convenios_listar()
        if len(convenios) == 0: st.write("Nenhum convenio cadastrado")
        else:
            op = st.selectbox("Atualização de Convenios", convenios)
            nome = st.text_input("Novo nome", op.get_nome())
            email = st.text_input("Novo e-mail", op.get_email())
            fone = st.text_input("Novo fone", op.get_fone())
            if st.button("Atualizar"):
                id = op.get_id()
                Service.convenio_atualizar(id, nome, email, fone)
                st.success("Convenio atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    def excluir():
        convenios = Service.convenio_listar()
        if len(convenios) == 0: st.write("Nenhum convenio cadastrado")
        else:
            op = st.selectbox("Exclusão de Convenios", convenios)
            if st.button("Excluir"):
                id = op.get_id()
                Service.convenio_excluir(id)
                st.success("Convenio excluído com sucesso")
                time.sleep(2)
                st.rerun()