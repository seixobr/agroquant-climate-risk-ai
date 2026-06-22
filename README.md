![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat-square&logo=python)
![Finance](https://img.shields.io/badge/Domain-Quant_Finance-005571?style=flat-square)
![Status](https://img.shields.io/badge/Status-Protótipo_Funcional-success?style=flat-square)

# 📈 AgroQuant AI - Assistente de Risco Climático

O AgroQuant AI é um protótipo de assistente especializado em análise de risco climático para commodities agrícolas. Inspirado em fluxos de trabalho utilizados em mercados agrícolas, o sistema traduz anomalias climáticas em avaliações estruturadas de risco para apoiar a tomada de decisão.

O projeto utiliza uma base de conhecimento simulada para demonstrar conceitos de recuperação de conhecimento, engenharia de prompts e processamento de dados estruturados.

## 🚀 Exemplo de Uso

**Usuário:**

> Como está o MATOPIBA?

**AgroQuant:**

> **[ALERTA DE RISCO CLIMÁTICO]**
>
> - **Região:** MATOPIBA
> - **Cultura Exposta:** Soja
> - **Anomalia:** Seca severa (El Niño) - 45 mm acumulados vs 120 mm (Média Histórica)
> - **Avaliação de Risco:** ALTO
> - **Análise:** Estresse hídrico na fase de enchimento de grãos
> - **Impacto Potencial:** Projeção de quebra de safra entre 15% e 20%

## 🎯 Objetivos

- Demonstrar o uso de Inteligência Artificial em um cenário de análise de risco climático.
- Simular um fluxo de recuperação de conhecimento especializado.
- Aplicar engenharia de prompts para controle de domínio e redução de respostas não fundamentadas.
- Estruturar relatórios analíticos a partir de dados climáticos organizados.

## 🛠️ Tecnologias Utilizadas

- Python
- JSON
- Engenharia de Prompt
- Processamento de Dados Estruturados

---

## 🏗️ Arquitetura do Projeto

O fluxo de funcionamento do assistente segue uma arquitetura baseada em recuperação de dados estruturados:

```text
Usuário (Input)
   ↓
Prompt (Regras de Negócio)
   ↓
AgroQuant (Motor Python)
   ↓
JSON Climático (Base de Conhecimento)
   ↓
Relatório de Risco (Output)
```

## 📖 Documentação do Agente

### Problema de Negócio

O clima é um dos principais riscos da produção agrícola e influencia diretamente a produtividade, a oferta de commodities e a formação de preços nos mercados futuros.

### Solução

O AgroQuant AI atua como um assistente especializado que cruza informações meteorológicas com regras agronômicas para gerar relatórios de risco instantâneos, reduzindo o esforço necessário para interpretar dados climáticos brutos.

### Público-Alvo

- Estudantes interessados em IA aplicada ao agronegócio.
- Profissionais interessados em análise de risco climático.
- Pessoas que desejam explorar aplicações de IA em cenários de tomada de decisão.

## 🗄️ Base de Conhecimento e Prompts

### Base de Conhecimento (`data/`)

A pasta `data/` contém um arquivo JSON que simula o retorno de uma API climática combinada com informações de safra.

Os dados incluem:

- Região analisada
- Cultura agrícola
- Anomalias climáticas
- Média histórica
- Avaliação de risco

### Prompts (`docs/`)

O System Prompt define:

- Persona do assistente
- Regras de comportamento
- Tom analítico das respostas
- Política de não inventar informações

Caso o usuário consulte uma região não cadastrada, o assistente deve informar que não possui dados suficientes para realizar a análise.

## ⚙️ Instalação e Execução

Clone o repositório:

```bash
git clone https://github.com/seixobr/agroquant-climate-risk-ai.git
cd agroquant-climate-risk-ai
```

Execute a aplicação:

```bash
python src/app.py
```

## 📊 Critérios de Avaliação

A qualidade do assistente foi avaliada com base nos seguintes critérios:

- **Consistência de domínio:** utilização correta dos conceitos agronômicos e climáticos definidos na documentação.
- **Extração correta dos dados:** recuperação precisa das informações armazenadas na base de conhecimento.
- **Controle de respostas:** rejeição de consultas para regiões não cadastradas.
- **Aderência ao prompt:** manutenção da persona e das regras estabelecidas para o agente.

## ⚠️ Aviso Legal (Disclaimer)

Este projeto possui finalidade exclusivamente educacional e demonstrativa.

O AgroQuant AI utiliza uma base de conhecimento simulada e foi desenvolvido para ilustrar conceitos de Inteligência Artificial aplicada à análise de risco climático em commodities agrícolas. As informações, projeções e avaliações apresentadas pelo assistente não constituem recomendação de investimento, consultoria financeira, previsão agrícola oficial ou qualquer forma de orientação profissional.

Os resultados gerados dependem integralmente dos dados cadastrados na base de conhecimento local e não refletem condições climáticas ou de mercado em tempo real.

Para decisões operacionais, financeiras ou de investimento, recomenda-se a utilização de fontes oficiais, dados atualizados e análise especializada.

## 🔍 Escopo do Protótipo

O objetivo deste projeto é demonstrar a aplicação de técnicas de recuperação de conhecimento, engenharia de prompts e processamento de dados estruturados em um contexto de análise de risco climático.

O sistema não possui integração com provedores externos de dados meteorológicos, modelos preditivos de safra ou mecanismos de atualização em tempo real.

## 🎤 Pitch

> "No mercado de commodities, quem sabe do clima primeiro, reage primeiro. O AgroQuant AI reduz a distância entre o dado climático e a interpretação do risco, transformando informações meteorológicas em análises estruturadas para apoio à tomada de decisão."

## 📚 Contexto

Projeto desenvolvido como parte do Lab "Construa Seu Assistente Virtual com Inteligência Artificial", integrante do bootcamp **Accenture - Python para Análise e Automação de Dados**, promovido pela DIO.

O projeto tem foco na aplicação de IA Generativa em problemas de domínio específico, com ênfase em análise de dados e automação com Python.
