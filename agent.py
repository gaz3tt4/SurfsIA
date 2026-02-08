import os
from dotenv import load_dotenv
from google import genai

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()
def process(information):
    client = genai.Client(api_key=os.getenv('GEMINI_KEY'))

    prompt = "Processe as informações abaixo  " + information

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents= prompt
    ) 

    information_return = response.content


    return  information_return


