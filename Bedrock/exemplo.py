# =========================================================
# IMPORTAÇÕES
# =========================================================

import boto3                     # SDK da AWS para Python (comunicação com serviços AWS)
import json                      # Manipulação de JSON (Bedrock exige JSON)
import uuid                      # Geração de IDs únicos para os arquivos no S3
from datetime import datetime, timezone  # Datas com timezone UTC (boa prática moderna)
from botocore.exceptions import ClientError  # Tratamento de erros da AWS


# =========================================================
# CONFIGURAÇÕES GERAIS DO SCRIPT
# =========================================================

REGION = "us-east-1"
# Região AWS onde:
# - Bedrock está disponível
# - O bucket S3 será criado/utilizado

BUCKET_NAME = "bucket-bedrock-logs-interacao-rss23"
# Nome globalmente único do bucket S3
# Esse bucket armazenará TODAS as interações com o Bedrock

PREFIX = "interacoes-bedrock/"
# Prefixo lógico (não é pasta real)
# Ajuda a organizar os arquivos no S3 por data


# =========================================================
# CRIAÇÃO DOS CLIENTES AWS
# =========================================================

bedrock_control = boto3.client(
    "bedrock",
    region_name=REGION
)
# Cliente de CONTROLE do Bedrock
# Usado para listar modelos disponíveis, metadados, etc.

bedrock_runtime = boto3.client(
    "bedrock-runtime",
    region_name=REGION
)
# Cliente de EXECUÇÃO do Bedrock
# Usado para invocar modelos (invoke_model)

s3 = boto3.client(
    "s3",
    region_name=REGION
)
# Cliente do Amazon S3
# Usado para criar bucket e salvar logs


# =========================================================
# FUNÇÃO: GARANTIR QUE O BUCKET EXISTA
# =========================================================

def garantir_bucket(bucket):
    """
    Verifica se o bucket existe.
    - Se existir: segue o fluxo normal
    - Se não existir: cria o bucket
    """
    try:
        # Faz uma chamada simples ao S3 para verificar existência
        s3.head_bucket(Bucket=bucket)
        print(f"Bucket '{bucket}' já existe.")

    except ClientError as e:
        # Se o erro for 404, o bucket não existe
        if e.response["Error"]["Code"] == "404":
            print(f"Bucket '{bucket}' não encontrado. Criando...")
            s3.create_bucket(Bucket=bucket)
            print(f"Bucket '{bucket}' criado com sucesso.")
        else:
            # Qualquer outro erro é relançado
            raise


# =========================================================
# FUNÇÃO: OBTÉM AUTOMATICAMENTE UM MODELO AMAZON DE TEXTO
# =========================================================

def obter_modelo_amazon_texto():
    """
    Lista os modelos disponíveis no Bedrock
    e retorna automaticamente um modelo da Amazon
    que aceite TEXTO como entrada e saída.
    """

    # Chamada à API de controle do Bedrock
    response = bedrock_control.list_foundation_models()

    # Percorre todos os modelos disponíveis
    for model in response["modelSummaries"]:

        # Filtra apenas modelos:
        # - do provedor Amazon
        # - que aceitam texto como entrada
        # - que retornam texto como saída
        if (
            model["providerName"] == "Amazon"
            and "TEXT" in model.get("inputModalities", [])
            and "TEXT" in model.get("outputModalities", [])
        ):
            return model["modelId"], model["modelName"]

    # Se nenhum modelo válido for encontrado
    raise Exception("Nenhum modelo Amazon de TEXTO disponível.")


# =========================================================
# INICIALIZAÇÃO DO SISTEMA
# =========================================================

# Garante que o bucket exista antes de iniciar o chat
garantir_bucket(BUCKET_NAME)

# Obtém automaticamente o modelo Amazon de texto
MODEL_ID, MODEL_NAME = obter_modelo_amazon_texto()

print("\n=== Chat com Amazon Bedrock (Modelos Amazon) ===")
print(f"Modelo em uso: {MODEL_NAME}")
print(f"Model ID: {MODEL_ID}")
print("Digite 'sair' para encerrar.\n")


# =========================================================
# LOOP PRINCIPAL DO CHAT
# =========================================================

while True:
    # Entrada do usuário
    pergunta = input("Digite 'sair' para encerrar ou envie nova pergunta: ")

    # Condição de saída do chat
    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Encerrando o chat. Até logo!")
        break

    # =====================================================
    # PAYLOAD CORRETO PARA MODELOS AMAZON NOVA
    # =====================================================

    body = {
        # Estrutura de mensagens no formato de chat
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "text": pergunta
                    }
                ]
            }
        ],

        # Configurações de inferência do modelo
        "inferenceConfig": {
            "maxTokens": 300,     # Limite máximo da resposta
            "temperature": 0.7    # Grau de criatividade
        }
    }

    # =====================================================
    # INVOCANDO O MODELO NO AMAZON BEDROCK
    # =====================================================

    response = bedrock_runtime.invoke_model(
        modelId=MODEL_ID,             # Modelo selecionado automaticamente
        body=json.dumps(body)         # Payload convertido para JSON
    )

    # Lê o corpo da resposta retornada pelo Bedrock
    response_body = json.loads(response["body"].read())

    # Extrai o texto final da resposta do modelo
    resposta = response_body["output"]["message"]["content"][0]["text"]

    # Exibe a resposta no terminal
    print(f"\nBedrock: {resposta}\n")


    # =====================================================
    # REGISTRO DA INTERAÇÃO (LOG)
    # =====================================================

    registro = {
        # Timestamp em UTC (timezone-aware, sem warning)
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),

        "provider": "Amazon",
        "model_id": MODEL_ID,
        "model_name": MODEL_NAME,

        "pergunta": pergunta,
        "resposta": resposta
    }

    # =====================================================
    # ESTRUTURA DA CHAVE (KEY) NO S3
    # =====================================================

    key = (
        f"{PREFIX}"
        f"{datetime.now(timezone.utc).strftime('%Y/%m/%d')}/"
        f"{uuid.uuid4()}.json"
    )
    # Exemplo final:
    # interacoes-bedrock/2026/01/27/uuid.json

    # =====================================================
    # SALVANDO O LOG NO AMAZON S3
    # =====================================================

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=json.dumps(registro, ensure_ascii=False, indent=2),
        ContentType="application/json"
    )
