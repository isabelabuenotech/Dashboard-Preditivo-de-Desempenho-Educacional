import streamlit as st
import pandas as pd
import numpy as np
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
# 2. CREDENCIAIS DE ACESSO FICTÍCIAS
# ==========================================
# Dicionário de credenciais de teste para simulação de login individual
CREDENCIAIS_ALUNOS = {
    "Lucas Mendes": "lucas123",
    "Beatriz Souza": "bia2026",
    "Gabriel Lima": "gabriel4321",
    "Mariana Costa": "mari8765"
}

# ==========================================
# 3. BASE DE CONHECIMENTO FIXA (VESTIBULARES)
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
# 4. GERAÇÃO DE DADOS FICTÍCIOS (MOCK DATA)
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
    
    alunos_lista = list(CREDENCIAIS_ALUNOS.items())
    records = []
    base_date = datetime.now() - timedelta(days=120)
    
    for i, (nome, senha) in enumerate(alunos_lista):
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

# Inicialização dos estados para as tabelas editáveis pelo aluno
if "inscricoes" not in st.session_state:
    st.session_state.inscricoes = pd.DataFrame({
        "Processo Seletivo": ["ENEM 2026", "FUVEST 2027"],
        "Inscrição Realizada": [True, False],
        "Código de Inscrição": ["10029384", "Pendente"],
        "Isenção Solicitada": ["Aprovada", "Não Solicitada"]
    })

if "medias_escola" not in st.session_state:
    st.session_state.medias_escola = pd.DataFrame({
        "Bimestre / Período": ["1º Bimestre", "2º Bimestre", "3º Bimestre", "4º Bimestre"],
        "Média Geral da Escola": [8.2, 8.5, 7.9, 8.8],
        "Faltas Acc.": [2, 1, 3, 0],
        "Observações": ["Aprovado", "Aprovado", "Atenção em Física", "Aprovado"]
    })

if "registros_simulados" not in st.session_state:
    st.session_state.registros_simulados = pd.DataFrame({
        "Nome do Simulado": ["Simulado Enem SAS 01", "Simulado Fuvest 1ª Fase", "Simulado Unicamp Geral"],
        "Data Realizada": [datetime.now().date() - timedelta(days=60), datetime.now().date() - timedelta(days=30), datetime.now().date() - timedelta(days=10)],
        "Desempenho Obtido (Pontos)": [720.5, 68.0, 74.0],
        "Meta Esperada": [750.0, 72.0, 75.0]
    })

if "registros_treineiros" not in st.session_state:
    st.session_state.registros_treineiros = pd.DataFrame({
        "Nome do Treineiro / Exame": ["Fuvest Treineiro 2ª Série", "Unicamp Treineiro"],
        "Data Realizada": [datetime.now().date() - timedelta(days=300), datetime.now().date() - timedelta(days=280)],
        "Desempenho Obtido (Pontos)": [610.0, 590.0],
        "Status de Classificação": ["Classificado p/ 2ª Fase", "Aprovado na 1ª Fase"]
    })

# ==========================================
# 5. AUTENTICAÇÃO E FILTROS DA BARRA LATERAL
# ==========================================
st.sidebar.title("🔐 Acesso do Aluno")

# Filtros globais para segmentação
escolas_disponiveis = sorted(df_raw["escola"].unique().tolist())
escolas_selecionadas = st.sidebar.multiselect("Filtrar por Colégio:", escolas_disponiveis, default=escolas_disponiveis)

series_disponiveis = sorted(df_raw["serie"].unique().tolist())
series_selecionadas = st.sidebar.multiselect("Filtrar por Série:", series_disponiveis, default=series_disponiveis)

df_filtered_global = df_raw[
    (df_raw["escola"].isin(escolas_selecionadas)) &
    (df_raw["serie"].isin(series_selecionadas))
]

if df_filtered_global.empty:
    st.warning("Ajuste os filtros de Colégio e Série na barra lateral para visualizar os alunos.")
    st.stop()

# Seleção do Aluno
alunos_disponiveis = sorted(df_filtered_global["nome"].unique().tolist())
aluno_selecionado = st.sidebar.selectbox("Selecione o seu Nome:", alunos_disponiveis)

# Campo de Senha
senha_input = st.sidebar.text_input("Senha de Acesso:", type="password")

# Validação das Credenciais com o Dicionário
df_aluno = df_filtered_global[df_filtered_global["nome"] == aluno_selecionado]
senha_correta = CREDENCIAIS_ALUNOS.get(aluno_selecionado)

if not senha_input:
    st.info("👋 Por favor, insira sua senha de acesso na barra lateral para abrir seu painel.")
    with st.expander("🔑 Clique aqui para visualizar as senhas de acesso fictícias (Modo de Teste)"):
        df_credenciais_view = pd.DataFrame(
            list(CREDENCIAIS_ALUNOS.items()),
            columns=["Nome do Aluno", "Senha Fictícia de Acesso"]
        )
        st.table(df_credenciais_view)
    st.stop()

elif senha_input != senha_correta:
    st.error("❌ Senha incorreta. Verifique suas credenciais na tabela abaixo e tente novamente.")
    with st.expander("🔑 Consultar senhas de teste"):
        df_credenciais_view = pd.DataFrame(
            list(CREDENCIAIS_ALUNOS.items()),
            columns=["Nome do Aluno", "Senha Fictícia de Acesso"]
        )
        st.table(df_credenciais_view)
    st.stop()

# Filtro por período de data após login
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

df_aluno_periodo = df_aluno[
    (df_aluno["data_registro"].dt.date >= data_inicio) &
    (df_aluno["data_registro"].dt.date <= data_fim)
].sort_values("data_registro")

if df_aluno_periodo.empty:
    st.warning("Nenhum registro acadêmico encontrado para o período selecionado.")
    st.stop()

# ==========================================
# 6. PAINEL PRINCIPAL DO ALUNO (KPIS)
# ==========================================
aluno_dados_recentes = df_aluno_periodo.iloc[-1]

st.title(f"🚀 Painel de Aprovação — {aluno_dados_recentes['nome']}")
st.caption(f"🏫 {aluno_dados_recentes['escola']} | 📌 {aluno_dados_recentes['serie']}")

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
# 7. VISUALIZAÇÕES E REGISTRO DE NOTAS PREENCHÍVEIS
# ==========================================
st.subheader("📝 Registro de Notas e Desempenho Acadêmico")
st.caption("Preencha e atualize suas notas da escola, simulados e exames de treineiro abaixo:")

tab_escola, tab_simulados, tab_treineiros = st.tabs([
    "🏫 Médias Acadêmicas na Escola", 
    "📝 Registro de Simulados", 
    "🎯 Registro de Treineiros"
])

with tab_escola:
    st.markdown("##### Preenchimento das Médias Escolares por Período:")
    df_medias_edited = st.data_editor(
        st.session_state.medias_escola,
        num_rows="dynamic",
        column_config={
            "Bimestre / Período": st.column_config.SelectboxColumn(
                "Bimestre/Período",
                options=["1º Bimestre", "2º Bimestre", "3º Bimestre", "4º Bimestre", "Recuperação", "Média Final"],
                required=True
            ),
            "Média Geral da Escola": st.column_config.NumberColumn(
                "Média Geral",
                min_value=0.0,
                max_value=10.0,
                format="%.1f",
                required=True
            ),
            "Faltas Acc.": st.column_config.NumberColumn("Faltas Acumuladas", format="%d"),
            "Observações": st.column_config.TextColumn("Observações do Trimestre/Bimestre")
        },
        use_container_width=True,
        hide_index=True,
        key="editor_medias"
    )
    st.session_state.medias_escola = df_medias_edited

with tab_simulados:
    st.markdown("##### Preenchimento dos Simulados Realizados:")
    df_simulados_edited = st.data_editor(
        st.session_state.registros_simulados,
        num_rows="dynamic",
        column_config={
            "Nome do Simulado": st.column_config.TextColumn("Nome / Identificação do Simulado", required=True),
            "Data Realizada": st.column_config.DateColumn("Data de Realização", required=True),
            "Desempenho Obtido (Pontos)": st.column_config.NumberColumn(
                "Desempenho (Pontos/Acertos)",
                min_value=0.0,
                max_value=1000.0,
                format="%.1f",
                required=True
            ),
            "Meta Esperada": st.column_config.NumberColumn("Meta Planejada", format="%.1f")
        },
        use_container_width=True,
        hide_index=True,
        key="editor_simulados"
    )
    st.session_state.registros_simulados = df_simulados_edited

with tab_treineiros:
    st.markdown("##### Preenchimento dos Exames como Treineiro:")
    df_treineiros_edited = st.data_editor(
        st.session_state.registros_treineiros,
        num_rows="dynamic",
        column_config={
            "Nome do Treineiro / Exame": st.column_config.TextColumn("Nome do Processo Seletivo / Treineiro", required=True),
            "Data Realizada": st.column_config.DateColumn("Data da Prova", required=True),
            "Desempenho Obtido (Pontos)": st.column_config.NumberColumn(
                "Desempenho Obtido",
                min_value=0.0,
                max_value=1000.0,
                format="%.1f",
                required=True
            ),
            "Status de Classificação": st.column_config.SelectboxColumn(
                "Status / Resultado",
                options=["Não Classificado", "Aprovado na 1ª Fase", "Classificado p/ 2ª Fase", "Lista de Espera", "Aprovado Final"]
            )
        },
        use_container_width=True,
        hide_index=True,
        key="editor_treineiros"
    )
    st.session_state.registros_treineiros = df_treineiros_edited

st.markdown("---")

# ==========================================
# 8. GRÁFICOS DE ACOMPANHAMENTO HISTÓRICO
# ==========================================
st.subheader("📊 Gráficos de Evolução das Notas")

g1, g2 = st.columns(2)

with g1:
    st.markdown("##### 📈 Evolução Histórica (Registros do Sistema)")
    df_chart = df_aluno_periodo.set_index("avaliacao")[["simulado_geral", "simulado_sas", "nota_treineiro"]]
    df_chart.columns = ["Simulado Geral", "Simulado SAS", "Nota Treineiro"]
    st.line_chart(df_chart)

with g2:
    st.markdown("##### 🎯 Desempenho nos Simulados Cadastrados")
    if not st.session_state.registros_simulados.empty:
        df_sim_chart = st.session_state.registros_simulados.set_index("Nome do Simulado")[["Desempenho Obtido (Pontos)"]]
        st.bar_chart(df_sim_chart)
    else:
        st.info("Cadastre seus simulados na tabela acima para visualizar o gráfico.")

st.markdown("---")

# ==========================================
# 9. PLANEJAMENTO DE CARREIRA E ESTRATÉGIA
# ==========================================
st.subheader("🎯 Orientação Profissional e Estratégia de Vestibular")

c_carreira, c_vest = st.columns([1.2, 0.8])

with c_carreira:
    st.markdown("### 🎓 Projeto de Vida e Opções de Carreira")
    st.caption("Cadastre e gerencie até 3 opções de cursos, instituições e suas respectivas motivações:")
    
    tab_op1, tab_op2, tab_op3 = st.tabs(["🥇 1ª Opção (Plano A)", "🥈 2ª Opção (Plano B)", "🥉 3ª Opção (Plano C)"])
    
    with tab_op1:
        st.text_input(
            "Área / Curso de Interesse (1ª Opção):", 
            value=aluno_dados_recentes["interesse_profissional"],
            key="curso_op1"
        )
        st.text_input(
            "Faculdade / Instituição Alvo (1ª Opção):", 
            value=aluno_dados_recentes["faculdade_interesse"],
            key="faculdade_op1"
        )
        st.text_area(
            "Justificativa e Motivação da Escolha (1ª Opção):", 
            value=aluno_dados_recentes["justificativa_carreira"], 
            height=90,
            key="just_op1"
        )

    with tab_op2:
        st.text_input(
            "Área / Curso de Interesse (2ª Opção):", 
            value="Engenharia de Produção",
            key="curso_op2"
        )
        st.text_input(
            "Faculdade / Instituição Alvo (2ª Opção):", 
            value="UNICAMP",
            key="faculdade_op2"
        )
        st.text_area(
            "Justificativa e Motivação da Escolha (2ª Opção):", 
            value="Segunda opção estratégica com foco em gestão de processos e interface com tecnologia.", 
            height=90,
            key="just_op2"
        )

    with tab_op3:
        st.text_input(
            "Área / Curso de Interesse (3ª Opção):", 
            value="Administração de Empresas",
            key="curso_op3"
        )
        st.text_input(
            "Faculdade / Instituição Alvo (3ª Opção):", 
            value="FGV / UNESP",
            key="faculdade_op3"
        )
        st.text_area(
            "Justificativa e Motivação da Escolha (3ª Opção):", 
            value="Plano C focado em ampla inserção no mercado corporativo e sólida base financeira.", 
            height=90,
            key="just_op3"
        )

with c_vest:
    st.markdown("### 📊 Distribuição de Interesses (Visão da Turma)")
    df_grupo = df_filtered_global.groupby("nome").last().reset_index()
    df_cursos = df_grupo["interesse_profissional"].value_counts().to_frame("Alunos")
    st.bar_chart(df_cursos)

# ==========================================
# 10. PROCESSOS SELETIVOS E INSCRIÇÕES
# ==========================================
st.subheader("📚 Guia de Vestibulares e Gestão de Inscrições")

tab_guia, tab_minhas_inscricoes = st.tabs(["Guia Oficial dos Vestibulares", "Minhas Inscrições e Acompanhamento"])

with tab_guia:
    st.markdown("###### Informações consolidadas sobre os principais exames do país:")
    st.dataframe(df_vestibulares, use_container_width=True, hide_index=True)

with tab_minhas_inscricoes:
    st.markdown("###### Gerencie suas inscrições e acompanhe o status em tempo real:")
    
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
        hide_index=True,
        key="editor_inscricoes"
    )
    st.session_state.inscricoes = df_inscricoes_editado

# ==========================================
# 11. REGISTRO HISTÓRICO COMPLETO
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
