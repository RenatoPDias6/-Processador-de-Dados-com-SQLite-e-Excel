# 📊 Processador de Dados CSV → SQLite → Excel

Este projeto em Python realiza a leitura de um arquivo CSV, armazena os dados em um banco SQLite e exporta informações selecionadas para um arquivo Excel. É uma ferramenta simples, útil e reutilizável para automatizar rotinas de tratamento de dados.

---

## ✅ O que o script faz

- Lê os dados do arquivo `dados.csv`
- Converte e armazena os dados em uma base de dados SQLite (`meu_projeto.db`)
- Realiza uma consulta SQL para selecionar apenas os campos importantes
- Exporta os dados filtrados para o arquivo `dados_processados_sqlite.xlsx`
- Mostra uma prévia no terminal e encerra a conexão com o banco

---

## 🚀 Como usar

1. Coloque seu arquivo `dados.csv` na mesma pasta do script.
2. Instale os pacotes necessários:
   ```bash
   pip install pandas openpyxl

---

## 🏢 Aplicação prática na Sogamax

Este projeto pode ser usado no dia a dia da Sogamax para:

    Importar relatórios brutos exportados de sistemas diversos

    Filtrar apenas os dados relevantes (ex: cliente, bairro, serviço, valor, status, data)

    Padronizar planilhas para análises, envio por e-mail ou arquivamento

    Automatizar tarefas repetitivas de organização de dados que antes eram feitas manualmente

Pode ser aplicado por equipes administrativas, comerciais ou de suporte, sempre que houver necessidade de limpar, organizar e reaproveitar planilhas em processos internos.
