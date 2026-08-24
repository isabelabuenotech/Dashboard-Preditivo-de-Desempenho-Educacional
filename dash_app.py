import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da Página
st.set_page_config(
    page_title="Dashboard de Acompanhamento Vestibular",
    page_icon="📊",
    layout="wide"
)

# Estilização Padrão
st.title("📊 Dashboard de Acompanhamento Pedagógico e Desempenho")
st.markdown("Visão geral de desempenho, saúde mental e planos de intervenção dos alunos.")

# Carregamento dos Dados
@st.cache_data
def load_data():
    # Substitua pelo caminho do arquivo no seu repositório
    df = pd.read_csv("mock_data.csv")
    return df

df = load_data()

# Sidebar para Filtros
st.sidebar.header("🔍 Filtros de Busca")
escola_sel = st.sidebar.multiselect(
    "Filtrar por Escola:",
    options=df["ESCOLA"].unique(),
    default=df["ESCOLA"].unique()
)

maturidade_sel = st.sidebar.multiselect(
    "Nível de Maturidade:",
    options=df["MATURIDADE"].unique(),
    default=df["MATURIDADE"].unique()
)

# Aplicação dos Filtros
df_filtered = df[(df["ESCOLA"].isin(escola_sel)) & (df["MATURIDADE"].isin(maturidade_sel))]

# Indicadores Principais (KPIs)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total de Alunos", len(df_filtered))
with col2:
    st.metric("Média ENEM 2025", f"{df_filtered['ENEM_2025'].mean():.1f}")
with col3:
    st.metric("Média Simulado FUVEST", f"{df_filtered['SIMULADO_FUVEST'].mean():.1f}")
with col4:
    st.metric("Atendimentos Pendentes", len(df_filtered[df_filtered["STATUS_AGOSTO"].str.contains("Agendar", na=False)]))

st.markdown("---")

# Visualizações
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📌 Distribuição por Curso de Interesse")
    fig_cursos = px.bar(
        df_filtered["CURSOS"].value_counts().reset_index(),
        x="CURSOS",
        y="count",
        labels={"CURSOS": "Curso", "count": "Alunos"},
        color_discrete_sequence=["#1f77b4"]
    )
    st.plotly_chart(fig_cursos, use_container_width=True)

with col_right:
    st.subheader("🎯 Chances de Aprovação no Plano Principal")
    fig_chance = px.pie(
        df_filtered,
        names="CHANCE_PLANO_PRINCIPAL",
        color="CHANCE_PLANO_PRINCIPAL",
        color_discrete_map={"Alta": "#2ca02c", "Média": "#ff7f0e", "Baixa": "#d62728"}
    )
    st.plotly_chart(fig_chance, use_container_width=True)

st.markdown("---")

# Tabela Interativa de Alunos Anonimizada
st.subheader("📋 Painel Estrutural de Alunos")
st.dataframe(
    df_filtered[[
        "N_ALUNO", "ESCOLA", "CURSOS", "MATURIDADE", 
        "ENEM_2025", "SIMULADO_FUVEST", "SAUDE_MENTAL", "STATUS_AGOSTO"
    ]],
    use_container_width=True
)
