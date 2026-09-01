import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# ==========================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Painel do Aluno | Aprovação Vestibular",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. BASE DE CONHECIMENTO FIXA (VESTIBULARES)
# ==========================================
@st.cache_data
def load_vestibulares_info():
    """Retorna dados de referência sobre os principais processos seletivos do Brasil."""
    return pd.DataFrame([
        {
            "Processo Seletivo": "ENEM 2026",
            "Instituição/Âmbito": "Nacional / SUT",
            "Período de Inscrição": "Maio / Junho",
            "Data da Prova": "Novembro",
            "Taxa (R$)": 85.00,
            "Formato": "180 questões + Redação (2 domingos)"
        },
        {
            "Processo Seletivo": "FUVEST 2027",
            "Instituição/Âmbito": "USP (São Paulo)",
            "Período de Inscrição": "Agosto / Setembro",
            "Data da Prova": "Novembro (1ª Fase) / Dezembro (2ª Fase)",
            "Taxa (R$)": 211.00,
            "Formato": "90 M.C. (1ª Fase) + Discursivas/Redação (2ª Fase)"
        },
        {
            "Processo Seletivo": "UNICAMP 2027",
            "Instituição/Âmbito": "UNICAMP (São Paulo)",
            "Período de Inscrição": "Agosto / Setembro",
            "Data da Prova": "Outubro (1ª Fase) / Dezembro (2ª Fase)",
            "Taxa (R$)": 210.00,
            "Formato": "72 M.C. (1ª Fase) + Discursivas/Redação (2ª Fase)"
        },
        {
            "Processo Seletivo": "VUNESP / UNESP 2027",
            "Instituição/Âmbito": "UNESP (São Paulo)",
            "Período de Inscrição": "Setembro / Outubro",
            "Data da Prova": "Novembro (1ª Fase) / Dezembro (2ª Fase)",
            "Taxa (R$)": 192.00,
            "Formato": "90 M.C. (1ª Fase) + Discursivas/Redação (2ª Fase)"
        }
    ])

# ==========================================
# 3. GERAÇÃO DE DADOS FICTÍCIOS (MOCK DATA)
# ==========================================
@st.cache_data
def load_student_mock_data():
    """Gera dados simulados do histórico acadêmico e planos de alunos do 3º Ano."""
    np.random.seed(42)
    
    escolas = ["Colégio Dom Pedro", "Instituto de Educação Moderna", "Escola Santa Maria"]
    series = ["3ª Série EM - Turma A", "3ª Série EM - Turma B", "3ª Série EM - Turma C"]
    interesses = ["Medicina", "Engenharia de Software", "Direito", "Psicologia", "Arquitetura"]
    justificativas = [
        "Vocação para a área da saúde e forte interesse em pesquisa biológica.",
        "Afeição por tecnologia, resolução de problemas lógicos e inovação digital.",
        "Interesse em ciências sociais aplicadas e defesa de direitos fundamentais.",
        "Desejo de atuar no suporte à saúde mental e neuropsicologia.",
        "Paixão por design urbano, planejamento de cidades e artes visuais."
    ]
    faculdades = ["USP", "UNICAMP", "UNESP", "FEDERAL/ENEM", "PUC"]
    
    alunos_info = [
        ("Lucas Mendes", "1234"),
        ("Beatriz Souza", "5678"),
        ("Gabriel Lima", "4321"),
        ("Mariana Costa", "8765")
    ]
    
    records = []
    base_date = datetime.now() - timedelta(days=120)
    
    for i, (nome, senha) in enumerate(alunos_info):
        escola = escolas[i % len(escolas)]
        serie = series[i % len(series)]
        interesse = interesses[i % len(interesses)]
        justificativa = justificativas[i % len(justificativas)]
        faculdade = faculdades[i % len(faculdades)]
        
        # Histórico de 4 avaliações por aluno ao longo do ano
        for aval in range(1, 5):
            data_reg = base_date + timedelta(days=aval * 30)
            
            records.append({
                "aluno_id": i + 1,
                "nome": nome,
                "senha": senha,
                "escola": escola,
                "serie": serie,
                "data_registro": data_reg,
                "avaliacao": f"Simulado 0{aval}",
                "media_academica": round(float(np.random.uniform(6.5, 9.8)), 1),
                "simulado_geral": round(float(np.random.uniform(550, 880)), 0),
                "simulado_sas": round(float(np.random.uniform(600, 910)), 0),
                "nota_treineiro": round(float(np.random.uniform(500, 850)), 0),
                "interesse_profissional": interesse,
                "justificativa_carreira": justificativa,
                "faculdade_interesse": faculdade,
                "curso_interesse": interesse
            })
            
    df = pd.DataFrame(records)
    df["data_registro"] = pd.to_datetime(df["data_registro"])
    return df

df_raw = load_student_mock_data()
df_vestibulares = load_vestibulares_info()

# Initialize session state for user-editable inscriptions
if "inscricoes" not in st.session_state:
    st.session_state.inscricoes = pd.DataFrame({
        "Processo Seletivo": ["ENEM 2026", "FUVEST 2027"],
        "Inscrição Realizada": [True, False],
        "Código de Inscrição": ["10029384", "Pendente"],
        "Isenção Solicitada": ["Aprovada", "Não Solicitada"]
    })

# ==========================================
# 4. AUTENTICAÇÃO E FILTROS DA BARRA LATERAL
# ==========================================
st.sidebar.title("🔐 Acesso do Aluno")

# Filtros globais obrigatórios para segmentação da base
escolas_disponiveis = sorted(df_raw["escola"].unique().tolist())
escolas_selecionadas = st.sidebar.multiselect("Filtrar por Colégio:", escolas_disponiveis, default=escolas_disponiveis)

series_disponiveis = sorted(df_raw["serie"].unique().tolist())
series_selecionadas = st.sidebar.multiselect("Filtrar por Série:", series_disponiveis, default=series_disponiveis)

# Aplicar filtros globais antes da lista de seleção individual
df_filtered_global = df_raw[
    (df_raw["escola"].isin(escolas_selecionadas)) &
    (df_raw["serie"].isin(series_selecionadas))
]

if df_filtered_global.empty:
    st.warning("Ajuste os filtros de Colégio e Série na barra lateral para visualizar os alunos.")
    st.stop()

# Seleção de Aluno
alunos_disponiveis = sorted(df_filtered_global["nome"].unique().tolist())
aluno_selecionado = st.sidebar.selectbox("Selecione o seu Nome:", alunos_disponiveis)

# Campo de Senha
senha_input = st.sidebar.text_input("Senha de Acesso:", type="password")

# Validação do Acesso
df_aluno = df_filtered_global[df_filtered_global["nome"] == aluno_selecionado]
senha_correta = df_aluno["senha"].iloc[0] if not df_aluno.empty else None

if not senha_input:
    st.info("👋 Por favor, insira sua senha de acesso na barra lateral para abrir seu painel.")
    st.stop()
elif senha_input != senha_correta:
    st.error("❌ Senha incorreta. Verifique suas credenciais e tente novamente.")
    st.stop()

# Filtro adicional de data
min_date = df_aluno["data_registro"].min().date()
max_date = df_aluno["data_registro"].max().date()

st.sidebar.markdown("---")
st.sidebar.subheader("📅 Período de Análise")
data_inicio, data_fim = st.sidebar.date_input(
    "Filtrar Registros:",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Filtragem Final do Estudante Autenticado
df_aluno_periodo = df_aluno[
    (df_aluno["data_registro"].dt.date >= data_inicio) &
    (df_aluno["data_registro"].dt.date <= data_fim)
].sort_values("data_registro")

if df_aluno_periodo.empty:
    st.warning("Nenhum registro acadêmico encontrado para o período de data selecionado.")
    st.stop()

# ==========================================
# 5. PAINEL PRINCIPAL DO ALUNOS (KPIS)
# ==========================================
aluno_dados_recentes = df_aluno_periodo.iloc[-1]

st.title(f"🚀 Painel de Aprovação — {aluno_dados_recentes['nome']}")
st.caption(f"🏫 {aluno_dados_recentes['escola']} | 📌 {aluno_dados_recentes['serie']}")

# Cálculos de Indicadores Acadêmicos
media_atual = aluno_dados_recentes["media_academica"]
media_anterior = df_aluno_periodo.iloc[-2]["media_academica"] if len(df_aluno_periodo) > 1 else media_atual
delta_media = round(media_atual - media_anterior, 1)

simulado_atual = aluno_dados_recentes["simulado_geral"]
simulado_anterior = df_aluno_periodo.iloc[-2]["simulado_geral"] if len(df_aluno_periodo) > 1 else simulado_atual
delta_simulado = round(simulado_atual - simulado_anterior, 0)

sas_atual = aluno_dados_recentes["simulado_sas"]
sas_anterior = df_aluno_periodo.iloc[-2]["simulado_sas"] if len(df_aluno_periodo) > 1 else sas_atual
delta_sas = round(sas_atual - sas_anterior, 0)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Média Acadêmica (Escola)", f"{media_atual:.1f}", delta=f"{delta_media:.1f} vs ant.")
col2.metric("Último Simulado Geral", f"{simulado_atual:.0f} pts", delta=f"{delta_simulado:.0f} pts")
col3.metric("Último Simulado SAS", f"{sas_atual:.0f} pts", delta=f"{delta_sas:.0f} pts")
col4.metric("Nota Treineiro", f"{aluno_dados_recentes['nota_treineiro']:.0f} pts")

st.markdown("---")

# ==========================================
# 6. VISUALIZACÕES GRÁFICAS (PLOTLY)
# ==========================================
st.subheader("📊 Desempenho e Evolução Acadêmica")

g1, g2 = st.columns(2)

with g1:
    st.markdown("##### 📈 Evolução das Notas nos Simulados e Média")
    fig_evolucao = px.line(
        df_aluno_periodo,
        x="avaliacao",
        y=["simulado_geral", "simulado_sas", "nota_treineiro"],
        markers=True,
        labels={"value": "Pontuação / Nota", "avaliacao": "Avaliação", "variable": "Indicador"},
        title="Desempenho Histórico nos Exames"
    )
    fig_evolucao.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    st.plotly_chart(fig_evolucao, use_container_width=True)

with g2:
    st.markdown("##### 🎯 Metas e Distribuição de Desempenho")
    df_melted = df_aluno_periodo.melt(
        id_vars=["avaliacao"], 
        value_vars=["simulado_geral", "simulado_sas", "nota_treineiro"],
        var_name="TipoExame", 
        value_name="Pontuacao"
    )
    fig_barras = px.bar(
        df_melted,
        x="Pontuacao",
        y="TipoExame",
        color="avaliacao",
        barmode="group",
        orientation="h",
        title="Comparativo entre Modalidades de Simulados"
    )
    st.plotly_chart(fig_barras, use_container_width=True)

st.markdown("---")

# ==========================================
# 7. PLANEJAMENTO DE CARREIRA E ESTRATÉGIA
# ==========================================
st.subheader("🎯 Orientação Profissional e Estratégia de Vestibular")

c_carreira, c_vest = st.columns(2)

with c_carreira:
    st.markdown("### 🎓 Projeto de Vida e Carreira")
    st.text_input("Área/Curso de Interesse:", value=aluno_dados_recentes["interesse_profissional"])
    st.text_input("Faculdade/Instituição Alvo:", value=aluno_dados_recentes["faculdade_interesse"])
    st.text_area("Justificativa e Motivação da Escolha:", value=aluno_dados_recentes["justificativa_carreira"], height=100)

with c_vest:
    st.markdown("### 🥧 Distribuição de Interesses (Visão de Grupo)")
    # Mapeamento do perfil de escolhas gerais do grupo
    df_grupo = df_filtered_global.groupby("nome").last().reset_index()
    
    fig_pizza_cursos = px.pie(
        df_grupo,
        names="interesse_profissional",
        title="Cursos Mais Procurados na Turma",
        hole=0.4
    )
    st.plotly_chart(fig_pizza_cursos, use_container_width=True)

st.markdown("---")

# ==========================================
# 8. PROCESSOS SELETIVOS E INSCRIÇÕES
# ==========================================
st.subheader("📚 Guia de Vestibulares e Gestão de Inscrições")

tab_guia, tab_minhas_inscricoes = st.tabs(["Guia Oficial dos Vestibulares", "Minhas Inscrições e Acompanhamento"])

with tab_guia:
    st.markdown("###### Informações consolidadas sobre os principais exames do país:")
    st.dataframe(df_vestibulares, use_container_width=True, hide_index=True)

with tab_minhas_inscricoes:
    st.markdown("###### Gerencie suas inscrições e acompanhe o status em tempo real:")
    
    # Editor interativo de tabela para o aluno preencher
    df_inscricoes_editado = st.data_editor(
        st.session_state.inscricoes,
        num_rows="dynamic",
        column_config={
            "Processo Seletivo": st.column_config.SelectboxColumn(
                "Processo Seletivo",
                options=df_vestibulares["Processo Seletivo"].tolist() + ["Outro"],
                required=True
            ),
            "Inscrição Realizada": st.column_config.CheckboxColumn("Confirmada?"),
            "Código de Inscrição": st.column_config.TextColumn("Nº de Inscrição/Protocolo"),
            "Isenção Solicitada": st.column_config.SelectboxColumn(
                "Status Isenção",
                options=["Não Solicitada", "Pendente", "Aprovada", "Indeferida"]
            )
        },
        use_container_width=True,
        hide_index=True
    )
    st.session_state.inscricoes = df_inscricoes_editado

# ==========================================
# 9. REGISTRO HISTÓRICO COMPLETO
# ==========================================
with st.expander("📄 Visualizar Tabela Completa do Histórico Acadêmico Individual"):
    cols_historico = [
        "avaliacao", "data_registro", "media_academica", 
        "simulado_geral", "simulado_sas", "nota_treineiro"
    ]
    st.dataframe(
        df_aluno_periodo[cols_historico],
        column_config={
            "avaliacao": "Avaliação",
            "data_registro": st.column_config.DateColumn("Data"),
            "media_academica": st.column_config.NumberColumn("Média Escolar", format="%.1f"),
            "simulado_geral": st.column_config.NumberColumn("Simulado Geral", format="%d pts"),
            "simulado_sas": st.column_config.NumberColumn("Simulado SAS", format="%d pts"),
            "nota_treineiro": st.column_config.NumberColumn("Treineiro", format="%d pts")
        },
        use_container_width=True,
        hide_index=True
    )
