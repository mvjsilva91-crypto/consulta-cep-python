import pandas as pd
import requests

cep = input("Digite o CEP: ").strip()

url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = requests.get(url)
dados = resposta.json()

if "erro" in dados:
    print("❌ CEP não encontrado!")
else:
    print("\n📍 Endereço encontrado:")
    print("Logradouro:", dados["logradouro"])
    print("Bairro:", dados["bairro"])
    print("Localidade:", dados["localidade"])
    print("UF:", dados["uf"])

    # opcional: salvar em tabela
    df = pd.DataFrame([{
        "CEP": cep,
        "Logradouro": dados["logradouro"],
        "Bairro": dados["bairro"],
        "Cidade": dados["localidade"],
        "UF": dados["uf"]
    }])

    df.to_csv("endereco.csv", index=False)
    print("\n💾 Dados salvos em endereco.csv")
