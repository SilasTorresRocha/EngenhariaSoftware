import google.generativeai as genai
from dotenv import dotenv_values
import os

config = dotenv_values(os.path.join(os.path.dirname(__file__), ".env"))
GEMINI_API_KEY = config.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Erro: variável de ambiente GEMINI_API_KEY não está definida")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash") 

def gerar_planejamento_semana(dados_usuario: dict) -> dict:
    try:
        # Transforma o dicionário em texto json
        json_texto = str(dados_usuario).replace("'", '"')  # simples, mas funcional
        prompt = (
            f"Gere um planejamento semanal baseado na seguinte rotina do estudante.\n"
            f"Formato da entrada:\n{json_texto}\n"
            f"Devolva APENAS um JSON com o planejamento. Não inclua explicações ou comentários."
        )

        response = model.generate_content(prompt)

        if response.text:
            import json
            return json.loads(response.text)  # Retorna como dicionário
        else:
            return {"erro": "Resposta vazia do Gemini"}

    except Exception as e:
        return {"erro": f"Erro na comunicação com o Gemini: {str(e)}"}
