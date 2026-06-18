# b2bflow-desafio

Código Python que lê contatos cadastrados no Supabase e envia mensagens personalizadas via Z-API (WhatsApp).

## Como funciona

1. Busca até 3 contatos da tabela `contatos` no Supabase
2. Para cada contato, envia via WhatsApp: "Olá, {nome} tudo bem com você?"

## Setup da tabela no Supabase

Crie uma tabela chamada `contatos` com as colunas:

| Coluna | Tipo |
|--------|------|
| id | int8 |
| created_at | timestamptz |
| nome | text |
| telefone | text |

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

SUPABASE_URL=sua_url_do_supabase

SUPABASE_KEY=sua_chave_do_supabase

ZAPI_INSTANCE_ID=seu_id_da_instancia

ZAPI_TOKEN=seu_token_da_instancia

## Como rodar

Instale as dependências:
pip install supabase requests python-dotenv

Execute:
python main.py