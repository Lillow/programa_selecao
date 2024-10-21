# Programa de Seleção

Este é um programa desenvolvido em Django que permite gerenciar movimentos financeiros.

## Requisitos

- Python 3.8 ou superior
- Django 5.1.2 ou superior

## Instalação

Siga os passos abaixo para configurar o ambiente e executar o programa:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/Lillow/programa_selecao.git
   
   ```
2. **Navegue até o diretório do projeto:**

   ```bash
   
    cd programa_selecao
  
   ```

3. **Crie um ambiente virtual**:

   ```bash
   
    python -m venv venv
   
   ```
   
4. **Ative o ambiente virtual**:

    No Windows:

   ```bash
   
    venv\Scripts\activate
   
   ```
    No macOS/Linux:
   
   ```bash
   
    source venv/bin/activate
   
   ```

5. **Instale as dependências**:

   ```bash
   
    pip install -r requirements.txt
   
   ```

6. **Migre o banco de dados**:

   ```bash
   
    python manage.py migrate
   
   ```

7. **Crie um superusuário (opcional)**:

   ```bash
   
    python manage.py createsuperuser
   
   ```


8. **Inicie o servidor**:

   ```bash
   
    python manage.py runserver
   
   ```

9. **Acesse a aplicação**:

   ```bash
   
     Abra um navegador e acesse http://127.0.0.1:8000/movements/ para visualizar a lista de movimentos.
   
   ```
## Uso

Após iniciar o servidor, você poderá gerenciar seus movimentos financeiros através da interface da web. Algumas funcionalidades disponíveis incluem:

   - Visualizar a lista de movimentos
   - Adicionar novos movimentos
   - Editar ou excluir movimentos existentes
