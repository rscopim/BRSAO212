import requests

try:
    r = requests.get("https://randomuser.me/api/")
    r.raise_for_status()  # lança erro se status != 200
    u = r.json()['results'][0]
    print(f"Nome: {u['name']['first']} {u['name']['last']}")
    print(f"E-mail: {u['email']}")
    print(f"País: {u['location']['country']}")
except Exception as e:
    print("Falha ao acessar a API:", e)