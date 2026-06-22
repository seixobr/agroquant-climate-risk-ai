![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat-square&logo=python)
![Finance](https://img.shields.io/badge/Domain-Quant_Finance-005571?style=flat-square)
![Status](https://img.shields.io/badge/Status-Protótipo_Funcional-success?style=flat-square)

# 📈 AgroQuant AI - Assistente de Risco Climático

Este projeto é a entrega do desafio "Assistente Virtual com IA" da DIO. Ele é um protótipo inspirado nos fluxos de trabalho de gestores de risco em mercados agrícolas, focado em traduzir anomalias climáticas em projeções de impacto para commodities.

## 🚀 Exemplo de Uso

**Usuário:**
> Como está o MATOPIBA?

**AgroQuant:**
> 📊 **[ALERTA DE RISCO CLIMÁTICO]**
> - **Região:** MATOPIBA
> - **Cultura Exposta:** Soja
> - **Anomalia:** Seca severa (El Niño) - 45mm acumulados vs 120mm (Média Histórica).
> - **Avaliação de Risco:** ALTO. Estresse hídrico na fase de enchimento de grãos. Projeção de quebra de safra de 15% a 20%.

---

## 🛠️ Tecnologias Utilizadas
- **Python** (Lógica da aplicação)
- **JSON** (Estruturação da base de conhecimento)
- **Engenharia de Prompt** (Calibragem de persona e restrições)
- **Processamento de Dados Estruturados**

## 🏗️ Arquitetura do Projeto
O fluxo de funcionamento do assistente segue uma arquitetura simplificada de RAG (Retrieval-Augmented Generation):

```text
Usuário (Input)
   ↓
Prompt (Regras de Negócio)
   ↓
AgroQuant (Motor Python)
   ↓
JSON Climático (Base de Conhecimento / Mock de API)
   ↓
Relatório de Risco (Output)
