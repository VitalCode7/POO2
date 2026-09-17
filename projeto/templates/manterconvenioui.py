import streamlit as st
import pandas as pd
import time
from service import Service

class ManterConvenioUI:
    def main():
        st.header("Cadastro de Convenios")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterConvenioUI.listar()
        with tab2: ManterConvenioUI.inserir()
        with tab3: ManterConvenioUI.atualizar()
        with tab4: ManterConvenioUI.excluir()
    def listar():
        convenios = Service.convenio_listar()
        if len(convenios) == 0: st.write("Nenhum convênio cadastrado")
        else:
            list_dic = []
            for obj in convenios: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        nome = st.text_input("Informe o nome")
        contato = st.text_input("Informe o contato")
        fone = st.text_input("Informe o fone")
        if st.button("Inserir"):
            Service.convenio_inserir(nome, contato, fone)
            st.success("Convênio inserido com sucesso")
            time.sleep(2)
            st.rerun()
    def atualizar():
        convenios = Service.convenio_listar()
        if len(convenios) == 0: st.write("Nenhum convênio cadastrado")
        else:
            op = st.selectbox("Atualização de Convênios", convenios)
            nome = st.text_input("Novo nome", op.get_nome())
            contato = st.text_input("Novo contato", op.get_contato())
            fone = st.text_input("Novo fone", op.get_fone())
            if st.button("Atualizar"):
                id = op.get_id()
                Service.convenio_atualizar(id, nome, contato, fone)
                st.success("Convênio atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    def excluir():
        convenios = Service.convenio_listar()
        if len(convenios) == 0: st.write("Nenhum convênio cadastrado")
        else:
            op = st.selectbox("Exclusão de Convênios", convenios)
            if st.button("Excluir"):
                id = op.get_id()
                Service.convenio_excluir(id)
                st.success("Convênio excluído com sucesso")
                time.sleep(2)
                st.rerun()