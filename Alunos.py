import requests


chav2 = ''
with open('token.txt', 'r') as file:
    chav2 += file.read()

   
headers = {
    'token': chav2
}

url = requests.get("https://portal.sophia.com.br/SophiAWebAPI/3055/api/v1/Alunos", headers=headers).json()

CodAluno = []


for aluno in url:
    CodAluno.append(aluno['codigo'])

for rm in CodAluno:
     
    BoletinsA = requests.get(f"https://portal.sophia.com.br/SophiAWebAPI/3055/api/v1/alunos/{rm}/Boletins", headers=headers)
    with open('Boletim.pdf', 'ab') as file:
        file.write(BoletinsA.content) 
    