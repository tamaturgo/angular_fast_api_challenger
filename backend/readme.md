# Sobre o backend

O backend foi desenvolvido utilizando o framework [FastAPI](https://fastapi.tiangolo.com/), que é um framework moderno e rápido para desenvolvimento de APIs.

## Estrutura

A estrutura do backend é a seguinte:

```bash
├── backend
│   ├── app
│   │   ├── categories
│   │   │   ├── model.py
│   │   │   ├── router.py
│   │   ├── products
│   │   │   ├── model.py
│   │   │   ├── router.py
│   │   ├── api.py
│   │   ├── database.py
│   ├── main.py
│   ├── migrations.py
│   ├── requirements.txt
│
```

A pasta `app` contém os módulos da aplicação. Cada módulo possui um arquivo `router.py` que contém as rotas daquele módulo e um arquivo `model.py` que contém o modelo de dados daquele módulo.

O arquivo `api.py` contém a instância da API e o arquivo `database.py` contém a instância do banco de dados.

O arquivo `main.py` contém a inicialização da aplicação.

O arquivo `migrations.py` contém o script de migração do banco de dados.

O arquivo `requirements.txt` contém as dependências do projeto.

## Como rodar

Para rodar o backend, você deve ter o python instalado na sua máquina. Para instalar as dependências, execute o comando:

```bash
pip install -r requirements.txt
```

Para criação do banco de dados, execute o comando:

```bash
python migrations.py
```

Para rodar a api, execute o comando:

```bash
uvicorn main:app --reload
```
