# 📊 Dashboard - Painel preditivo de desempenho escolar/acadêmico

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)

O **Dashboard de Acompanhamento Preditivo de Vestibular** foi desenvolvido para centralizar, visualizar e gerenciar o desempenho acadêmico e a jornada de alunos em preparação para vestibulares. 

---
## 📌 O que é o projeto?

O Dashboard Preditivo de Desempenho Educacional é uma solução completa de Business Intelligence e Data Analytics desenvolvida para transformar o acompanhamento de estudantes do 3º Ano do Ensino Médio durante a preparação para o vestibular. Desenvolvida na interseção entre inteligência de dados, orientação pedagógica e psicologia escolar, a plataforma centraliza a jornada individual do estudante em uma interface segura, analítica e preditiva.

A aplicação unifica dados quantitativos de desempenho escolar e exames (médias acadêmicas, simulados gerais/SAS e registros como treineiro) a um planejamento estratégico de carreira com até 3 opções de cursos/universidades (Planos A, B e C), além de um guia interativo com gerenciador de inscrições em vestibulares brasileiros.

---

## 🔑 Diferenciais: Funcionalidades e Impacto de Negócio

- **Autenticação e Acesso Individual do Aluno:** Sistema restrito de login por senha individual simples, garantindo a privacidade dos dados do estudante e permitindo a troca segura entre perfis em ambiente de simulação/teste.

- **Central de Registro e Edição Interativa de Notas (st.data_editor):** médias acadêmicas por período/bimestre; histórico de simulados com controle dinâmico de notas, datas e registro de desempenho; registro de treineiros com status de classificação por fases.

- **Gerenciador de Inscrições e Isenções em Vestibulares:** Guia com informações consolidadas dos principais processos seletivos do país (ENEM, FUVEST, UNICAMP, UNESP) integrado a uma tabela editável para o aluno gerenciar números de protocolo, confirmações e solicitações de isenção de taxa.

- **Projeto de Vida e Estratégia de Carreira em Abas (Planos A, B e C):** Interface modular em st.tabs para cadastro e acompanhamento de até 3 opções de cursos e universidades, com espaço individual para justificativa e motivação da escolha.

---

## 🛠️ Arquitetura e Tecnologias

* **Streamlit:** Framework principal para construção da interface Web, gerenciamento de estado (session_state), navegação modular em abas (st.tabs), formulários e editores de dados (st.data_editor).

* **Gráficos e Visualizações Nativas:** Componentes visuais (st.line_chart e st.bar_chart) executados sem dependências externas adicionais, garantindo alta performance e leveza.

* **Processamento e Manipulação de Dados (ETL):** Pandas e NumPy para estruturação de dataframes, cálculos de variação (deltas) e filtros dinâmicos temporais.

* **Formatos de Dados e Estado:** Estrutura base em CSV e gerenciamento em memória (st.session_state) para manipulação de tabelas editáveis durante a sessão do usuário.
  
---

## 💡 Como Acessar e Navegar na Dashboard
1. O dashboard está publicado e disponível para navegação direta através do ecossistema cloud do Streamlit:
👉 [Acesse o Dashboard Online Aqui](https://preditivo-de-desempenho-educacional-para-aprovacao.streamlit.app/)

2. A navegação foi estruturada de forma intuitiva para atender tanto a análises táticas quanto operacionais:

### Painel Geral de Turmas (Visão Macro):

- **Filtros Laterais:** Utilize a sidebar para filtrar o grupo por unidade escolar, nível de maturidade e prioridade de atendimento.

- **Cartões de KPI:** Visualize métricas consolidadas como média geral dos exames, total de alunos monitorados e volume de atendimentos pendentes.

- **Gráficos de Distribuição:** Analise a demanda de cursos por área e a probabilidade geral de aprovação do grupo.

### Visão Individual do Aluno (Student Deep-Dive):

- **Acesso Individual Restrito por Autenticação:** Acesso protegido por senha simples configurada por estudante, permitindo a consulta segura aos dados individuais em modo de simulação de testes (com painel expansível de credenciais fictícias de acesso).

- **Métricas de Performance Instantâneas (KPIs):** Visualização no topo do painel das últimas médias acadêmicas da escola, notas recentes dos simulados gerais e SAS, pontuação em exames como treineiro e indicadores de evolução temporal (deltas) em relação às avaliações anteriores.

- **Central de Registro e Edição Interativa de Notas (st.data_editor):**

    - *Médias Acadêmicas na Escola:* Tabela preenchível para acompanhamento por bimestre/período, lançamento de médias, controle de faltas acumuladas e observações pedagógicas.

    - *Registro de Simulados:* Tabela editável para digitação do nome do simulado, data de realização, pontuação/acertos obtidos e acompanhamento contra a meta planejada.

    - *Registro de Treineiros:* Tabela preenchível dedicada ao histórico de provas realizadas como treineiro, contendo nome do processo seletivo, data e status de classificação (fases/aprovado).

**Painel de Evolução e Gráficos Nativos:** Gráficos interativos sem dependências externas (st.line_chart e st.bar_chart) apresentando a linha do tempo das avaliações e o comparativo do desempenho mais recente.

**Projeto de Vida e Mapeamento Multi-Opções de Carreira (Planos A, B e C):** Interface modular em abas (st.tabs) para que o aluno cadastre e gerencie até 3 opções de escolhas universitárias (1ª Opção / Plano A, 2ª Opção / Plano B e 3ª Opção / Plano C), cada uma com espaço dedicado para Curso, Instituição Alvo e Justificativa/Motivação individual.

**Guia Oficial de Vestibulares e Gestão de Inscrições:** Tabela de consulta sobre os principais processos seletivos do Brasil (ENEM, FUVEST, UNICAMP, UNESP) acompanhada de um gerenciador editável de inscrições para o aluno controlar confirmação, número de protocolo e solicitações de isenção de taxa.

---
## 🧪 Validação e Qualidade da Aplicação (QA)

Para garantir a estabilidade, precisão dos cálculos acadêmicos e fluidez da aplicação, foram aplicadas boas práticas de Garantia de Qualidade (QA) durante o desenvolvimento:

- **Validação de Regras de Negócio e Entrada de Dados (st.data_editor):** Testes de consistência na digitação e edição de tabelas dinâmicas — garantindo validações de limites (BVA) para notas escolares ($0.0$ a $10.0$), pontuações de simulados/treineiros ($0$ a $1000$ pontos) e datas válidas de realização das provas.
  
- **Validação de Autenticação e Controle de Acesso:** Testes do fluxo de autenticação individual por aluno com dicionário de credenciais de teste, incluindo checagem de mensagens de erro para senhas incorretas e validação da visibilidade do painel expansível de credenciais em modo de teste.

- **Tratamento de Exceções e Resiliência (Fallback Data):** Implementação de estratégias de manipulação de dados para assegurar o carregamento gracioso do dashboard, evitando falhas de tela quando tabelas de simulados ou inscrições estiverem vazias ou apresentarem valores omissos.

- **Testes de Layout e Compatibilidade Nativa:** Validação dos componentes visuais nativos do Streamlit (gráficos st.line_chart e st.bar_chart), garantindo funcionamento $100\%$ autônomo sem dependências externas adicionais (como Plotly), boa adaptação do layout em colunas e legibilidade das abas (st.tabs) em múltiplos tamanhos de tela.

---

# 👩‍💻 Autora e Contato
> **Isabela Bueno**
> Psicóloga Escolar | Analista Educacional Sênior | Data & Tech Enabler (QA & Python)

📧 **E-mail:** isabelabueno.tech@gmail.com
💼 **LinkedIn:** isabela-bueno-silva
🐱 **GitHub:** @isabelabuenotech
