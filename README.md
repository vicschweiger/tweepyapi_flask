# TweetSearchApp

## Descrição do Projeto

**TweetSearchApp** é uma aplicação web simples que permite pesquisar tweets usando Flask e Tweepy. Ela autentica com a API do Twitter e exibe os resultados da pesquisa de uma forma visualmente amigável.

## Funcionalidades Principais

1. **Pesquisar Tweets:**
   - Formulário para entrada de termos de pesquisa.
   - Integração com a API do Twitter para buscar tweets com base nos termos fornecidos.
   
2. **Exibir Resultados:**
   - Resultados da pesquisa exibidos de maneira organizada e visualmente atraente.
   - Informações exibidas incluem o texto do tweet, o usuário que postou, a data e hora do tweet, e outras informações relevantes.

## Tecnologias Utilizadas

- **Backend:**
  - Flask (framework web em Python)
  - Tweepy (biblioteca para interação com a API do Twitter)

- **Frontend:**
  - HTML5 e CSS3 para a estrutura e estilo das páginas.
  - Jinja2 (template engine do Flask) para renderização dinâmica de páginas.
  - Bootstrap (framework CSS) para design responsivo e estilização.

## Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/vicschweiger/tweepyapi_flask
   cd tweetsearchapp

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt

4. **Configure a API do Twitter:**
   Crie um arquivo config.py na raiz do projeto com as seguintes informações:
   ```bash
   API_KEY = 'sua_api_key'
   API_SECRET_KEY = 'sua_api_secret_key'
   ACCESS_TOKEN = 'seu_access_token'
   ACCESS_TOKEN_SECRET = 'seu_access_token_secret'

5. **Execute a aplicação:**
   ```bash
   flask run
  A aplicação estará disponível em http://127.0.0.1:5000/.

## Futuras Melhorias
* Implementar paginação para os resultados da pesquisa.
* Adicionar filtros avançados de pesquisa, como localização e datas.
* Melhorar a interface do usuário com mais detalhes sobre cada tweet, como número de retweets e curtidas.
