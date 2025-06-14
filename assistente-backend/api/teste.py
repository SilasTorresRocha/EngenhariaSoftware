from dotenv import dotenv_values
import os

# Caminho absoluto até o .env do mesmo diretório
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
config = dotenv_values(dotenv_path)

print(config)
