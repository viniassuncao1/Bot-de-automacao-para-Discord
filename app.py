import discord
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuração do bot do Discord
intents = discord.Intents.default()
intents.members = True  # Permissão para acessar membros
client = discord.Client(intents=intents)

# Configuração do Google Sheets
CRED_FILE = "mcaminho.json"  # Substitua pelo caminho do seu JSON
SHEET_NAME = "Teste 123"  # Substitua pelo nome da planilha no Google Sheets

# Autenticação no Google Sheets
scope = ["", ""]
creds = ServiceAccountCredentials.from_json_keyfile_name(CRED_FILE, scope)
client_gs = gspread.authorize(creds)
sheet = client_gs.open(SHEET_NAME).sheet1  # Abre a primeira aba da planilha

@client.event
async def on_ready():
    print(f'✅ Bot conectado como {client.user}!')

    # Obtém o servidor do Discord
    guild = client.get_guild(1227605216602619994)  # Substitua pelo ID do seu servidor
    if not guild:
        print("❌ Não foi possível encontrar o servidor. Verifique o ID.")
        return

    # Lista de membros
    membros_data = [["ID", "Nome", "ID"]]  # Cabeçalho

    # Ordem das patentes
    ordem_patentes = ["Cel.", "Ten. cel", "Cap.", "1° Ten.", "2° Ten.", "Sub.", "1° Sgt.", "2° Sgt.", "3° Sgt.", "Cb.", "Sd.", "Rec."]

    # Busca membros do servidor
    members = [member async for member in guild.fetch_members()]  # Coleta todos os membros
    membros_processados = []

    for member in members:
        nome_completo = member.display_name  # Nome completo no servidor (ex: "Cb. Machado | 2338")
        partes = nome_completo.split("|")  # Divide o nome em partes usando "|"
        nome = partes[0].strip()  # Pega o nome antes do "|", removendo espaços extras
        passaporte = partes[1].strip() if len(partes) > 1 else "Sem ID"  # Pega o ID após o "|", se existir

        # Extrai a patente do nome
        patente = nome.split(" ")[0]  # Pega a primeira palavra do nome (ex: "Cb.")
        membros_processados.append((patente, nome, passaporte))  # Adiciona a lista com a patente

    # Ordena os membros com base na ordem das patentes
    membros_processados.sort(key=lambda x: ordem_patentes.index(x[0]) if x[0] in ordem_patentes else len(ordem_patentes))

    # Adiciona os membros ordenados à lista final
    for _, nome, passaporte in membros_processados:
        membros_data.append([passaporte, nome, passaporte])  # Adiciona ID, Nome, ID

    # Escreve os dados na planilha
    try:
        sheet.update("A1", membros_data)
        print("✅ Dados salvos no Google Planilhas com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao atualizar a planilha: {e}")

# Substitua pelo token do seu bot do Discord
client.run("Token do bot")
