import google.generativeai as genai
from dotenv import dotenv_values
import os
import json
import re

config = dotenv_values(os.path.join(os.path.dirname(__file__), ".env"))
GEMINI_API_KEY = config.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Erro: variável de ambiente GEMINI_API_KEY não está definida")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash") 

def gerar_planejamento_com_ia(dados_usuario: dict) -> dict:
    prompt = f"""Gere um planejamento semanal baseado na rotina abaixo. Retorne apenas um JSON puro, sem explicações ou comentários.

Aqui estão os dados do usuário:
{json.dumps(dados_usuario, indent=2, ensure_ascii=False)}

Cada dia da semana deve conter: "horario": "07:00-07:30", "atividade": "descrição da atividade"

Formato de saída esperado:
{{
  "horarios": {{
    "Segunda": [],
    "Terça": [],
    "Quarta": [],
    "Quinta": [],
    "Sexta": [],
    "Sábado": [],
    "Domingo": []
  }}
}}
"""


    try:
        response = model.generate_content(prompt)
        texto = response.text or ""

        # 🔧 Remove blocos de markdown ```json ... ``` se existirem
        if texto.strip().startswith("```"):
            texto = re.sub(r"^```[a-zA-Z]*\n", "", texto.strip())  # remove início ```json
            texto = re.sub(r"\n```$", "", texto.strip())           # remove final ```

        planejamento = json.loads(texto)
        return planejamento

    except Exception as e:
        return {"erro": f"Erro na comunicação com o Gemini: {str(e)}"}