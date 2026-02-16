# 🏠 Orçamento de Aluguel -- Imobiliária R.M (Flask + Tailwind)

Aplicação web desenvolvida em **Python (Flask)** com **frontend em
TailwindCSS**, criada para automatizar a geração de orçamento de aluguel
mensal conforme regras acadêmicas da disciplina *Algorithmic Thinking &
Introduction to Object-Oriented Programming*.

------------------------------------------------------------------------

## 🎯 Objetivo

Permitir que o usuário informe os dados do imóvel e receba
automaticamente:

-   ✔ Valor do aluguel mensal
-   ✔ Valor do contrato (R\$ 2.000,00)
-   ✔ Parcelamento do contrato (até 5x)
-   ✔ Download de arquivo CSV com 12 mensalidades

------------------------------------------------------------------------

## 🧮 Regras de Negócio

### 🏢 Apartamento

-   Base: R\$ 700,00 (1 quarto)
-   2 quartos: + R\$ 200,00
-   Garagem: + R\$ 300,00
-   Desconto de 5% se não possuir crianças

### 🏠 Casa

-   Base: R\$ 900,00 (1 quarto)
-   2 quartos: + R\$ 250,00
-   Garagem: + R\$ 300,00

### 🏙 Estúdio

-   Base: R\$ 1.200,00
-   2 vagas: + R\$ 250,00
-   Vagas extras: + R\$ 60,00 cada

### 📄 Contrato

-   Valor fixo: R\$ 2.000,00
-   Parcelamento: 1x até 5x

------------------------------------------------------------------------

## 🏗 Arquitetura do Projeto

    calculadoraDeAluguel/
    │
    ├── run.py
    ├── README.MD
    ├── requirements.txt
    ├── config.py
    ├── .env
    ├── .gitignore
    │
    ├── app/
    │   ├── __init__.py
    │   ├── models.py
    │   ├── services.py
    │   ├── routes/
    │   │   └── __init__.py
    │   │   └── main.py
    │   ├── templates/
    │   │   ├── base.html
    │   │   ├── index.html
    │   │   └── resultado.html
    │   └── static/
    │
    └── exports/

------------------------------------------------------------------------

## ⚙️ Tecnologias Utilizadas

-   Python 3.10+
-   Flask
-   TailwindCSS (CDN)
-   HTML5
-   CSV (exportação de dados)

------------------------------------------------------------------------

## 🚀 Como Executar

### 1️⃣ Clonar repositório

    git clone <URL_DO_REPOSITORIO>
    cd calculadoraDeAluguel

### 2️⃣ Criar ambiente virtual

Windows:

    python -m venv .venv
    .venv\Scripts\activate

Linux/Mac:

    python -m venv .venv
    source .venv/bin/activate

### 3️⃣ Instalar dependências

    pip install -r requirements.txt

### 4️⃣ Criar arquivo .env

    FLASK_APP=run:app
    FLASK_ENV=development
    FLASK_DEBUG=1
    SECRET_KEY=sua-chave-aqui

### 5️⃣ Rodar aplicação

    python -m flask run

Acesse:

    http://127.0.0.1:5000

------------------------------------------------------------------------

## 📁 Exportação CSV

Ao clicar em **Baixar CSV (12 meses)**, será gerado:

    orcamento_12_parcelas.csv

Formato:

    parcela;valor
    1;700.00
    2;700.00
    ...
    12;700.00

------------------------------------------------------------------------

## 🧠 Conceitos Aplicados

-   Pensamento algorítmico (Entrada → Processamento → Saída)
-   Programação Orientada a Objetos
-   Estruturas condicionais
-   Separação de responsabilidades
-   Arquitetura organizada (Blueprints + Application Factory)

------------------------------------------------------------------------

## 🛡 Boas Práticas

-   Uso de `.env` para variáveis sensíveis
-   `.gitignore` configurado
-   Estrutura modular
-   Separação entre camada web e regras de negócio

------------------------------------------------------------------------

## 👨‍💻 Autor
Juan Henrique
Projeto desenvolvido para fins acadêmicos.
