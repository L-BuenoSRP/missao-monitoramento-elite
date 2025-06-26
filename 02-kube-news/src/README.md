# Monitoramento Elite - Estrutura MVC

Este projeto foi refatorado seguindo o padrão MVC (Model-View-Controller) para melhorar a organização, manutenibilidade e escalabilidade do código.

## Estrutura do Projeto

```
src/
├── app.py                 # Arquivo principal da aplicação
├── config/               # Configurações
│   ├── __init__.py
│   └── database.py       # Configuração do banco de dados
├── models/               # Modelos de dados
│   ├── __init__.py
│   └── post.py          # Modelo Post
├── controllers/          # Lógica de negócio
│   ├── __init__.py
│   ├── post_controller.py    # Controller para Posts
│   └── health_controller.py  # Controller para Health Checks
├── views/               # Rotas e endpoints
│   ├── __init__.py
│   ├── post_routes.py   # Rotas relacionadas a Posts
│   └── health_routes.py # Rotas de Health Check
├── middleware/          # Middlewares
│   ├── __init__.py
│   └── health_middleware.py # Middleware de Health Check
├── templates/           # Templates HTML
├── static/             # Arquivos estáticos
└── requirements.txt    # Dependências
```

## Componentes MVC

### Models (Modelos)
- **`models/post.py`**: Define o modelo Post com métodos para operações no banco de dados
- Responsável pela estrutura de dados e interação com o banco

### Views (Visualizações)
- **`views/post_routes.py`**: Rotas relacionadas a posts (listagem, criação, visualização)
- **`views/health_routes.py`**: Rotas de health check e readiness
- Responsáveis por receber requisições HTTP e retornar respostas

### Controllers (Controladores)
- **`controllers/post_controller.py`**: Lógica de negócio para posts (validação, criação)
- **`controllers/health_controller.py`**: Lógica para health checks
- Responsáveis pela lógica de negócio e coordenação entre models e views

## Benefícios da Refatoração

1. **Separação de Responsabilidades**: Cada componente tem uma responsabilidade específica
2. **Manutenibilidade**: Código mais organizado e fácil de manter
3. **Testabilidade**: Componentes isolados facilitam testes unitários
4. **Escalabilidade**: Estrutura preparada para crescimento do projeto
5. **Reutilização**: Controllers e models podem ser reutilizados em diferentes views

## Como Executar

```bash
cd src
python app.py
```

A aplicação estará disponível em `http://localhost:5000`

## Endpoints Disponíveis

### Posts
- `GET /` - Lista todos os posts
- `GET /post` - Formulário de criação
- `POST /post` - Cria novo post
- `GET /post/<id>` - Visualiza post específico
- `POST /api/post` - API para criação em massa

### Health Check
- `GET /health` - Status de saúde
- `GET /ready` - Status de readiness
- `PUT /unhealth` - Define como não saudável
- `PUT /unreadyfor/<seconds>` - Define como não pronto por X segundos 