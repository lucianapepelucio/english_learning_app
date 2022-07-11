# Desafio a cumprir:

Você precisa construir uma plataforma educacional que oferece um simulado para alunos que tem interesse em testar seus conhecimentos no inglês.

Todos os dados deverão ser salvos em memória (variáveis), não é necessário a configuração de um database.


## Alguns requisitos que sua aplicação deverá ter:

- [x] Utilizar a versão 3.9 de python
- [x] Utilizar o git para gerenciamento de código
- [ ] async / await .
- [ ] Utilizar os métodos corretos para cada requisição, put, get, delete, patch, post
- [ ] Fazer a validação de tipos nas funções
- [ ] Retornar o status code correto para cada resposta
- [ ] Semântica nas rotas. Ex:. /user /user/<user_id>
- [ ] Utilizar a tipagem para melhor entendimento do código. Ex:. soma(num: int)


## Para acessar o projeto:
```
cd desafio-back
```
## Para rodar o projeto:
```
python3 -m venv venv
source venv/bin/activate
uvicorn main:app --reload
```
 ## Acessar os seguintes endereços no navegador:
 - http://127.0.0.1:8000
 - http://127.0.0.1:8000/docs
 - http://127.0.0.1:8000/redoc
 - http://127.0.0.1:8000/openapi.json (ver schemas)
