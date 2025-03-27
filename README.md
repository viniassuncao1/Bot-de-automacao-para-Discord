# 🤖 Discord Bot para Sincronizar Membros da Polícia do Metrópole RP com Google Sheets 📊

Este é um bot Discord em Python criado para **facilitar o trabalho manual da Polícia do Metrópole RP**, um servidor de **GTA RP (roleplay, não roleplay de McDonald's 😉)**. No nosso servidor, atualmente, precisamos ir no Discord, verificar manualmente o nome e o ID de cada policial e inserir essas informações em uma planilha. Pensando em otimizar nosso tempo e reduzir essa tarefa repetitiva, desenvolvi esta automação para simplificar tudo!

O bot coleta informações dos membros do servidor Discord do Metrópole RP e as salva automaticamente em uma planilha do Google Sheets. Ele também tenta ordenar os membros com base em uma lista predefinida de patentes encontradas em seus nicks do Discord.

## ✨ Funcionalidades

* **🔗 Conecta-se ao Discord:** Utiliza a biblioteca `discord.py` para interagir com o Discord.
* **🔑 Autenticação Google Sheets:** Usa a biblioteca `gspread` e a `oauth2client` para autenticar e interagir com o Google Sheets através de um arquivo de credenciais JSON.
* **👤 Coleta Dados de Membros:** Obtém o ID, nome de exibição dos membros de um servidor Discord específico.
* **🏷️ Extrai Patente e ID:** Tenta extrair a patente (a primeira palavra do nick) e o ID (a parte após "|") do nome de exibição do membro.
* **<0xF0><0x9F><0xAA><0x96> Ordena por Patente:** Ordena os membros na planilha do Google Sheets com base em uma lista predefinida de patentes. Membros sem uma patente reconhecida são listados por último.
* **💾 Atualiza Google Sheets:** Escreve os dados coletados e ordenados em uma planilha do Google Sheets especificada.

## ⚙️ Pré-requisitos

* **🐍 Python 3.6 ou superior:** Certifique-se de ter o Python instalado em seu sistema.
* **📚 Bibliotecas Python:** Instale as seguintes bibliotecas usando o pip:
    ```bash
    pip install discord.py gspread oauth2client
    ```
* **☁️ Conta Google e Projeto Google Cloud:**
    * Você precisará de uma conta Google.
    * Crie um projeto no [Google Cloud Console](https://console.cloud.google.com/).
    * Ative a API Google Sheets para o seu projeto.
    * Crie uma conta de serviço no seu projeto.
    * Baixe o arquivo de credenciais JSON da conta de serviço e salve-o (renomeie para `metropolerp-455022-cb095f41d364.json` ou atualize o nome no código).
    * 📤 Compartilhe a planilha do Google Sheets com o endereço de e-mail da sua conta de serviço (com permissões de edição).
* **🤖 Bot Discord:**
    * Crie um bot Discord no [Portal de Desenvolvedores do Discord](https://discord.com/developers/applications).
    * 🔑 Obtenha o token do seu bot.
    * ➕ Convide o bot para o seu servidor Discord.
    * ✅ Certifique-se de que o bot tenha as permissões necessárias para visualizar membros no seu servidor.

## 🛠️ Configuração

1.  **🔑 Arquivo de Credenciais do Google Sheets:**
    * Coloque o arquivo JSON de credenciais da sua conta de serviço do Google Cloud na mesma pasta do script Python e renomeie-o para `metropolerp-455022-cb095f41d364.json` (ou mantenha o nome original e atualize a variável `CRED_FILE` no código).

2.  **📝 Nome da Planilha:**
    * Abra o script Python (`seu_script.py`).
    * Na linha `# SHEET_NAME = "Teste 123"`, substitua `"Teste 123"` pelo nome exato da sua planilha do Google Sheets.

3.  **🆔 ID do Servidor Discord:**
    * No script Python, localize a linha `# guild = client.get_guild(1227605216602619994)` e substitua `1227605216602619994` pelo ID do seu servidor Discord. Para obter o ID do servidor, você precisa ativar o "Modo de Desenvolvedor" no Discord (⚙️ Configurações de Usuário -> ➡️ Avançado) e então clicar com o botão direito no ícone do seu servidor e selecionar "Copiar ID".

4.  **🔑 Token do Bot Discord:**
    * Na última linha do script (`client.run("SEU_TOKEN_AQUI")`), substitua `"SEU_TOKEN_AQUI"` pelo token do seu bot Discord que você obteve no Portal de Desenvolvedores.

5.  **🎖️ Ordem das Patentes (Opcional):**
    * A lista `ordem_patentes` define a ordem em que os membros serão listados na planilha. Edite esta lista para corresponder às patentes utilizadas no seu servidor e a ordem desejada.

## ▶️ Execução

1.  Abra um terminal ou prompt de comando.
2.  ➡️ Navegue até a pasta onde você salvou o script Python.
3.  🚀 Execute o script com o comando:
    ```bash
    python seu_script.py
    ```
    (Substitua `seu_script.py` pelo nome do seu arquivo Python).

4.  O bot se conectará ao Discord e, assim que estiver pronto, coletará os dados dos membros do servidor especificado e os escreverá na planilha do Google Sheets. Você verá mensagens no console indicando o sucesso ✅ ou falha ❌ da operação.

## ⚠️ Notas

* Certifique-se de que o nome de exibição dos membros no seu servidor siga um padrão onde a patente (ou cargo) aparece como a primeira palavra e o ID (ou outra informação) aparece após um caractere "|". Exemplo: `Cb. Machado | 2338`.
* O bot precisa ter permissão para "Ler Canais de Texto & Canais de Voz" e "Membros Presentes" no seu servidor para poder listar os membros.
* Em caso de erros, verifique o console para obter informações detalhadas sobre o problema. Certifique-se de que o arquivo de credenciais JSON é válido, o nome da planilha e o ID do servidor estão corretos, e o bot tem as permissões necessárias.

## 🙏 Créditos

Este bot utiliza as seguintes bibliotecas de código aberto:

* [discord.py](https://discordpy.readthedocs.io/en/stable/)
* [gspread](https://docs.gspread.org/en/latest/)
* [oauth2client](https://oauth2client.readthedocs.io/en/latest/)

## 🧑‍💻 Criado por

Vinicius Machado

## 🤝 Contribuições e Participação

Este projeto foi criado por mim. Se você tiver interesse em contribuir com melhorias, novas funcionalidades ou participar do desenvolvimento, entre em contato através de Discord: viniassuncao, E-mail: Viniciusmassuncao@gmail.com.
