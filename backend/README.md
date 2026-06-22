# Task Manager

## 🛠️ Tecnologias Utilizadas

<div align="center">

### Backend & Framework
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)

### Frontend
[![HTML5](https://img.shields.io/badge/HTML5-E34C26?style=for-the-badge&logo=html5&logoColor=white)](https://www.w3.org/html/)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://www.w3.org/Style/CSS/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://www.javascript.com/)

### Bancos de Dados
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![MySQL](https://img.shields.io/badge/MySQL-00758F?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

### Processamento de Linguagem Natural
[![TextBlob](https://img.shields.io/badge/TextBlob-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://textblob.readthedocs.io/)
[![NLTK](https://img.shields.io/badge/NLTK-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.nltk.org/)

### Infraestrutura & Ambiente
[![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Anaconda](https://img.shields.io/badge/Anaconda-44A833?style=for-the-badge&logo=anaconda&logoColor=white)](https://www.anaconda.com/)

</div>

---

## 📋 Descrição

Projeto de gerenciador de tarefas desenvolvido com as melhores práticas e tecnologias modernas.

## API RESTful de Feira

Este projeto tambem expoe uma API com Django REST Framework para gerenciamento de boxes de feira e recomendacoes de clientes com analise de sentimento.

### Instalar dependencias

```bash
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe -m textblob.download_corpora
```

### Preparar banco de dados

```bash
.\venv\Scripts\python.exe manage.py makemigrations
.\venv\Scripts\python.exe manage.py migrate
```

O projeto esta usando SQLite por padrao. Para MySQL, instale `mysqlclient` e troque `DATABASES` em `setup/settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "nome_do_banco",
        "USER": "usuario",
        "PASSWORD": "senha",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

### Endpoints

- `GET/POST /api/categorias-box/`
- `GET/POST /api/boxes/`
- `GET/PUT/PATCH/DELETE /api/boxes/{id}/`
- `GET /api/boxes/{id}/estatisticas/`
- `GET/POST /api/recomendacoes/`
- `GET /api/estatisticas/boxes/`
- `POST /api/token/`
- `GET /swagger/`
- `GET /redoc/`

### Autenticacao

A API aceita session authentication e token authentication. Para gerar token, crie um usuario e envie `username` e `password` para `/api/token/`.

```bash
.\venv\Scripts\python.exe manage.py createsuperuser
```
