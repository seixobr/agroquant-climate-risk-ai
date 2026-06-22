import json
import os

def carregar_dados_climaticos():
    caminho = os.path.join(os.path.dirname(__file__), '../data/base_conhecimento.json')
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)['regioes_monitoradas']
    except:
        return []

def analisar_risco(regiao_input, db):
    for regiao in db:
        if regiao_input.lower() in regiao['nome'].lower():
            return regiao
    return None

def terminal_agroquant():
    db = carregar_dados_climaticos()
    print("="*50)
    print("📈 TERMINAL AGROQUANT - RISCO CLIMÁTICO 📈")
    print("="*50)
    print("IA: Terminal pronto. Digite a região para análise de risco (ex: MATOPIBA, Sul).")
    
    while True:
        msg = input("\nUsuário: ")
        if msg.lower() in ['sair', 'exit']: break
            
        dados = analisar_risco(msg, db)
        
        if dados:
            print(f"\nIA: Processando telemetria para {dados['nome']}...")
            print("-" * 40)
            print(f"Cultura Exposta: {dados['cultura_principal']}")
            print(f"Precipitação (30d): {dados['dados_climaticos_atuais']['precipitacao_acumulada_30d']} (Média: {dados['dados_climaticos_atuais']['media_historica_30d']})")
            print(f"Anomalia: {dados['dados_climaticos_atuais']['anomalia']}")
            print(f"⚠️ AVALIAÇÃO DE RISCO: {dados['impacto_estimado']}")
            print("-" * 40)
        else:
            print("IA: Região fora da cobertura atual. Monitoramos apenas MATOPIBA e Sul.")

if __name__ == "__main__":
    terminal_agroquant()
