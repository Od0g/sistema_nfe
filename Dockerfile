# Dockerfile

FROM python:3.12-slim

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos para o container
COPY . .

# Instala dependências
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Expõe a porta padrão do Flask
EXPOSE 5000

# Executa o app
CMD ["python", "run.py"]
