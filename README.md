# Grupo zap listings-api

A api foi preparada com o objetivo de participar do processo seletivo do grupo zap para 
uma vaga de gestor de engenharia.


Utilizei como guia as instruções fornecidas no endereço 
https://grupozap.github.io/cultura/challenges/engineering.html.
O problema escolhido foi a Opção B. 

Essa é a minha primeira aplicação desenvolvida em Python 
(na minha carreira sempre fui programador .NET e aceito o blame por isso). 
Talvez vocês encontrem características de outras linguagens em alguns códigos mas tentei 
cuidar ao máximo.


##A API
```python
BASE_URL = "https://zap-listings-api.herokuapp.com/"
```

### Endpoints
* `listings/` : Obtem uma lista com todos os anúncios disponíveis.

Opções de filtro
* `listings/?portal=zap` : Obtem uma lista com todos os anúncios que atendam as regras do 
desafio para o portal Zap.
* `listings/?portal=vivareal` : Obtem uma lista com todos os anúncios que atendam as regras 
do desafio para o portal VivaReal.

##Escolhas de implementação
###Stack e frameworks
Escolhi utilizar a stack Python + Django + DRF. 
Com ele pronto talvez possa parecer um pouco de exagero em termos de framework para as 
regras solicitadas. 
No entanto, uma API de anúncios com certeza novas funcionalidades e abstrações seram 
implementadas (afinal era para fazer um sistema production ready né :p).

###Heroku
Apesar de não ser um requisito queria deixar a aplicação publicada no Heroku. 
Isso exigiu que o request feito ao Json exemplo precisasse rodar em backgroud, 
devido as limitações do host.

###Estrutura do projeto
A estrutura tentei seguir ao máximo o padrão do Django. 
Meu intuito inicial foi sobrescever as Models Django e ao invés de obter de um banco de dados 
utilizar o json.
No fim, fazer dessa forma ficou muito complexo e precisaria sobrescrever muitas funções do Django.


###Cache
Implementar cache em uma api nem sempre é a escolha mais sábia. 
Nesse caso, o problema me "obrigava" a obter os dados da url fornecida 
criei um cache em memória (com uma váriavel global, podia utilizar qualquer outra forma) para
tornar a navegação mais fluída.


## Tutorial de Instalação e execução
### Instalação

```bash
$ git clone 'git@github.com:joaodann/listings-api.git'
$ cd listings-api
$ # Ative o virtual env com a ferramenta de sua escolha /venv
$ virtualenv env -p python3
$ source env/bin/activate
$ # /venv
$ pip3 install -r requirements.txt
```

### Teste

```bash
$ cd listings-api
$ make test
```

### Executar local

```bash
$ cd listings-api
$ make run
```

### Publicar

```bash
$ cd listings-api
$ make deploy
```

## Ambiente de Desenvolvimento

* Laptop MacbookAir i5 8gb MacOS
* macOS Mojave;
* Pycharm;
* Python (latest version);
* virtualenv;


## Histórico de commit
Começei usando feature branch mas achei que mais complicou na leitura da timeline do que ajudou.
Depois dos setup inicial começei a fazer commmit na master (sim, me senti mal por isso) com
os menores ciclos que consegui, considerando minha pouca familiaridade com a linguagem.

## Testes do projeto
Criei todos os testes que julguei necessário para cobrir a regra de negócio.

Podia ter feito mais testes para testar a estrutura do projeto e diretamente as views.
Optei não fazer por ter receio de acabar testando o prório funcionamento do Django/DRF.

