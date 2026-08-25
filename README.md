# 📊 Dashboard - Painel preditivo de desempenho escolar/acadêmico

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)

O **Dashboard de Acompanhamento Vestibular** foi desenvolvido para centralizar, visualizar e gerenciar o desempenho acadêmico e a jornada de alunos em preparação para vestibulares. 

---
## 📌 O que é o projeto?

O Dashboard Preditivo de Desempenho Educacional (Vestibulares 2026) é uma solução completa de Business Intelligence e Data Analytics projetada para transformar a gestão de acompanhamento vestibular. Desenvolvido para atuar na interseção entre inteligência de dados e psicologia escolar, a plataforma centraliza a jornada do estudante em uma única interface preditiva e analítica.

Em vez de analisar apenas notas isoladas, o projeto unifica métricas acadêmicas quantitativas (desempenho no ENEM, FUVEST e simulados) a dados qualitativos e socioemocionais (saúde mental, contexto familiar e vulnerabilidade). Isso permite que orientadores pedagógicos e analistas educacionais identifiquem riscos precocemente, avaliem a viabilidade real dos planos de aprovação do aluno e tomem decisões fundamentadas para maximizar o sucesso de ingressos universitários.

A ferramenta unifica dados de desempenho (ENEM, Simulados Fuvest e exames próprios) com dados estratégicos (maturidade de escolha de curso, planos A/B de aprovação) e dados qualitativos (saúde mental, fatores de risco e planos de intervenção pedagógica/psicológica).

---

## 🔑 Diferenciais: Funcionalidades e Impacto de Negócio

- **Visão Holística 360° do Estudante:** Combina o desempenho técnico e cognitivo com fatores de risco socioemocionais (ansiedade, suporte familiar, vulnerabilidade socioeconômica), superando a análise fria de boletins tradicionais.

- **Matriz de Viabilidade Preditiva (Planos A/B):** Cruza a nota atual do aluno com as notas de corte de múltiplos exames, mapeando a margem real de probabilidade de aprovação no plano principal e sugerindo ajustes estratégicos em planos alternativos.

- **Gestão Ativa de Intervenções Pedagógicas:** Transforma diagnósticos em ação com um sistema interno de controle de pendências, fila de prioridades (Alta, Média e Baixa) e acompanhamento de planos de intervenção para aluno e família.

- **Design System Customizado para EdTech:** Interface rica desenvolvida com CSS3 e HTML5 injetados no Streamlit, garantindo alta usabilidade, badges dinâmicos de status e acessibilidade para equipes educacionais.

---

## 🛠️ Arquitetura e Tecnologias

* **Streamlit:** Framework para construção da interface Web, gerenciamento de estado (`session_state`), navegação modular em abas e colunas.

* **HTML5 & CSS3 Customizado:** Injeção de estilos para *design system* próprio (fontes *Google Fonts*, botões interativos, badges de status, alertas e componentes acessíveis).

* **Processamento e Tratamento de Dados (ETL):** Pandas
  
* **Formatos de Dados:** Estruturas CSV e JSON para manipulação do estado da aplicação e estruturas de dados.

---
## 💡 Como Navegar na Dashboard

A navegação foi estruturada de forma intuitiva para atender tanto a análises táticas quanto operacionais:

### Painel Geral de Turmas (Visão Macro):

- **Filtros Laterais:** Utilize a sidebar para filtrar o grupo por unidade escolar, nível de maturidade e prioridade de atendimento.

- **Cartões de KPI:** Visualize métricas consolidadas como média geral dos exames, total de alunos monitorados e volume de atendimentos pendentes.

- **Gráficos de Distribuição:** Analise a demanda de cursos por área e a probabilidade geral de aprovação do grupo.

### Visão Individual do Aluno (Student Deep-Dive):

- **Seção de Diagnóstico:** Acesse o histórico resumido, análise qualitativa do orientador e status de saúde mental.

- **Tabela de Opções e Planos:** Verifique os cursos cadastrados (Planos A a F), as notas do aluno vs. nota de corte e a classificação automática de viabilidade (Atingimento, Dentro da Nota, Reconsiderar).

- **Evolução Histórica:** Acompanhe o gráfico de linhas e barras com o desempenho comparativo por área do conhecimento ao longo das edições dos exames.

---
## 🧪 Validação e Qualidade da Aplicação (QA)

Para garantir a estabilidade, precisão dos cálculos acadêmicos e fluidez da aplicação, foram aplicadas boas práticas de Garantia de Qualidade (QA) durante o desenvolvimento:

- **Validação de Regras de Negócio e Cálculos:** Testes de consistência na geração dinâmica de métricas — como cálculo do diferencial de notas de corte, evolução percentual do ENEM e rotulagem correta das chances de aprovação.

- **Tratamento de Exceções e Resiliência:** Implementação de estratégias de manipulação de erros com para assegurar o carregamento gracioso da dashboard caso o arquivo de dados apresente valores nulos ou formatação inconsistente.

- **Testes de Layout e Responsividade:** Validação de componentes visuais, contraste em badges de status, integridade das fontes customizadas e adaptação do layout em colunas para múltiplos tamanhos de tela.

---

# 👩‍💻 Autora e Contato
> **Isabela Bueno**
> Psicóloga Escolar | Analista Educacional Sênior | Data & Tech Enabler (QA & Python)

📧 **E-mail:** isabelabueno.tech@gmail.com

💼 **LinkedIn:** isabela-bueno-silva

🐱 **GitHub:** @isabelabuenotech
