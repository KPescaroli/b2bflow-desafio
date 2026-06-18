import os
import logging
import requests
from dotenv import load_dotenv
from supabase import create_client

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configuração do log (mostra o que está acontecendo no terminal)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Pega as variáveis de ambiente
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")

# Conecta ao Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def buscar_contatos():
    """Busca os contatos cadastrados no Supabase"""
    try:
        response = supabase.table("contatos").select("*").limit(3).execute()
        logging.info(f"{len(response.data)} contato(s) encontrado(s) no banco.")
        return response.data
    except Exception as e:
        logging.error(f"Erro ao buscar contatos: {e}")
        return []

def enviar_mensagem(telefone, nome):
    """Envia mensagem via Z-API"""
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"
    payload = {
        "phone": telefone,
        "message": f"Olá, {nome} tudo bem com você?"
    }
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            logging.info(f"Mensagem enviada para {nome} ({telefone})")
        else:
            logging.error(f"Erro ao enviar para {nome}: {response.status_code} - {response.text}")
    except Exception as e:
        logging.error(f"Erro de conexão ao enviar para {nome}: {e}")

def main():
    logging.info("Iniciando envio de mensagens...")
    contatos = buscar_contatos()

    if not contatos:
        logging.warning("Nenhum contato encontrado. Encerrando.")
        return

    for contato in contatos:
        nome = contato.get("nome")
        telefone = contato.get("telefone")
        enviar_mensagem(telefone, nome)

    logging.info("Envio finalizado!")

if __name__ == "__main__":
    main()