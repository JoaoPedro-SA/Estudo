

import google.generativeai as genai

def main():
    try:
        # Substitua "YOUR_API_KEY" pela sua chave de API
        genai.configure(api_key="AIzaSyCQgeKNvrcHCwt4fj9682n9_mFrfS5bjg8")

        # Configurações do modelo
        generation_config = {
            "temperature": 1, 
            "top_p": 0.95, 
            "max_output_tokens": 8192
        }

        # Configurações de segurança
        safety_settings = [
            {"category": cat, "threshold": "BLOCK_MEDIUM_AND_ABOVE"} 
            for cat in genai.HarmCategory
        ]

        # Inicializa o modelo
        model = genai.GenerativeModel(
            model_name="gemini-1.5-pro-latest",
            generation_config=generation_config,
            safety_settings=safety_settings
        )

        # Inicia a conversa
        convo = model.start_chat(history=[])

        print("Olá! Sou o Gemini, seu assistente de IA. Como posso ajudar?")

        while True:
            user_input = input("Você: ")
            convo.send_message(user_input)
            response = convo.last.text
            print(f"Gemini: {response}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()