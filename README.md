# scrapy-pat-sjc
*Scrapy das vagas de empregos disponiveis no PAT da cidade de São José dos Campos - SP. 

## O que é necessário instalar?
### Python 3
     
[Link de Instalação do Python3](https://www.python.org/downloads/release/python-364/)
  
### Bibliotecas a serem utilizadas:

    pip install -r requirements.txt

## Executando
### Salvando as vagas em um JSON

    scrapy crawl vagas_pat -o vagas.json
    
### Salvando as vagas no MongoDB Atlas
#### Configurações MongoDB, editar o arquivo setting.py 
    # Descomente a linha: 'vagas.pipelines.MongoPipeline': 300,
    
    ITEM_PIPELINES = {
    'vagas.pipelines.VagasPipeline': 300,
    'vagas.pipelines.MongoPipeline': 300,
    }
    
    # Adicione as configurações da sua conta MongoDB Atlas:
    
    # Configurações MongoDB Atlas - Exemplo:
    MONGO_URI = 'mongodb+srv://<user>:<password>@cluster0-hql3l.mongodb.net/test'
    MONGO_DATABASE = 'Vagas'
    
#### Executando e salvando no MongoDB Atlas
    scrapy crawl vagas_pat
