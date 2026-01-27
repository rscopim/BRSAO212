# =========================================================
# IMPORTAÇÕES
# =========================================================

import boto3                     # SDK da AWS para Python (comunicação com serviços AWS)
import json                      # Manipulação de JSON (Bedrock exige JSON)
import uuid                      # Geração de IDs únicos para os arquivos no S3
from datetime import datetime, timezone  # Datas com timezone UTC (boa prática moderna)
from botocore.exceptions import ClientError  # Tratamento de erros da AWS


# =========================================================
# CONFIGURAÇÕES PADRÃO DO SCRIPT
# =========================================================

REGION = "us-east-1"
# Região AWS onde o Bedrock está disponível

DEFAULT_BUCKET_NAME = "bucket-bedrock-logs-interacao-rss23"
# Bucket padrão sugerido pelo script

PREFIX = "interacoes-bedrock/"
# Prefixo lógico para organização dos arquivos no S3


# =========================================================
# CRIAÇÃO DOS CLIENTES AWS
# =========================================================

bedrock_control = boto3.client("bedrock", region_name=REGION)
# Cliente de CONTROLE do Bedrock (listar modelos, metadados)

bedrock_runtime = boto3.client("bedrock-runtime", region_name=REGION)
# Cliente de EXECUÇÃO do Bedrock (invoke_model)

s3 = boto3.client("s3", region_name=REGION)
# Cliente do Amazon S3 (armazenamento dos logs)


# =========================================================
# FUNÇÃO: GARANTIR QUE O BUCKET EXISTA
# =========================================================

def garantir_bucket(bucket):
    """
    Verifica se o bucket existe no S3.
    Se não existir, cria o bucket automaticamente.
    """
    try:
        s3.head_bucket(Bucket=bucket)
        print(f"Bucket '{bucket}' já existe.")

    except ClientError as e:
        if e.response["Error"]["Code"] == "404":
            print(f"Bucket '{bucket}' não encontrado. Criando...")
            s3.create_bucket(Bucket=bucket)
            print(f"Bucket '{bucket}' criado com sucesso.")
        else:
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

    response = bedrock_control.list_foundation_models()

    for model in response["modelSummaries"]:
        if (
            model["providerName"] == "Amazon"
            and "TEXT" in model.get("inputModalities", [])
            and "TEXT" in model.get("outputModalities", [])
        ):
            return model["modelId"], model["modelName"]

    raise Exception("Nenhum modelo Amazon de TEXTO disponível.")


# =========================================================
# INTERAÇÃO: ESCOLHA / CRIAÇÃO DO BUCKET
# =========================================================

print("\n=== Configuração do Bucket S3 ===")
print(f"Bucket padrão: {DEFAULT_BUCKET_NAME}")

opcao = input("Deseja usar o bucket padrão? (s/n): ").strip().lower()

if opcao == "n":
    BUCKET_NAME = input("Digite o nome do novo bucket S3: ").strip()
    print(f"Bucket informado: {BUCKET_NAME}")
else:
    BUCKET_NAME = DEFAULT_BUCKET_NAME
    print(f"Usando bucket padrão: {BUCKET_NAME}")

# Garante que o bucket escolhido exista
garantir_bucket(BUCKET_NAME)


# =========================================================
# INICIALIZAÇÃO DO SISTEMA BEDROCK
# =========================================================

MODEL_ID, MODEL_NAME = obter_modelo_amazon_texto()

print("\n=== Chat com Amazon Bedrock (Modelos Amazon) ===")
print(f"Modelo em uso: {MODEL_NAME}")
print(f"Model ID: {MODEL_ID}")
print("Digite 'sair' para encerrar.\n")


# =========================================================
# LOOP PRINCIPAL DO CHAT
# =========================================================

while True:
    pergunta = input("Digite 'sair' para encerrar ou envie nova pergunta: ")

    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Encerrando o chat. Até logo!")
        break

    # =====================================================
    # PAYLOAD PARA MODELOS AMAZON NOVA
    # =====================================================

    body = {
        "messages": [
            {
                "role": "user",
                "content": [{"text": pergunta}]
            }
        ],
        "inferenceConfig": {
            "maxTokens": 300,
            "temperature": 0.7
        }
    }

    # =====================================================
    # INVOCANDO O MODELO NO BEDROCK
    # =====================================================

    response = bedrock_runtime.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body)
    )

    response_body = json.loads(response["body"].read())
    resposta = response_body["output"]["message"]["content"][0]["text"]

    print(f"\nBedrock: {resposta}\n")


    # =====================================================
    # REGISTRO DA INTERAÇÃO
    # =====================================================

    registro = {
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "provider": "Amazon",
        "model_id": MODEL_ID,
        "model_name": MODEL_NAME,
        "pergunta": pergunta,
        "resposta": resposta
    }

    # =====================================================
    # ESTRUTURA DA KEY NO S3
    # =====================================================

    key = (
        f"{PREFIX}"
        f"{datetime.now(timezone.utc).strftime('%Y/%m/%d')}/"
        f"{uuid.uuid4()}.json"
    )

    # =====================================================
    # SALVANDO NO AMAZON S3
    # =====================================================

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=json.dumps(registro, ensure_ascii=False, indent=2),
        ContentType="application/json"
    )
