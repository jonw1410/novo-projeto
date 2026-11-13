# Tasks: migrate-env-to-streamlit-secrets

## 1. Configuração do Arquivo de Secrets

- [x] 1.1 Formatar `.streamlit/secrets.toml` com sintaxe TOML válida para as chaves de configuração do Xano

## 2. Migração da Leitura de Configuração para Streamlit Secrets

- [x] 2.1 Implementar a função `get_config_value` em `utils/xano_client.py` priorizando `st.secrets` com fallback para `os.getenv`
- [x] 2.2 Atualizar as telas de Perfil (`pages/3_👤_Perfil.py`), Disciplinas (`pages/1_📚_Disciplinas.py`) e Tarefas (`pages/2_📝_Tarefas.py`) para ler as configurações via `st.secrets`
