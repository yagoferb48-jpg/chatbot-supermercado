import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

CONTEXTO_SISTEMA = (
    "Você é o assistente virtual do Super Mercado Fictício ExemploMart. "
    "Ajude os clientes com dúvidas sobre produtos, preços, promoções, "
    "horário de funcionamento (Seg a Sáb, 8h às 22h) e localização das seções da loja. "
    "Seja educado, direto e use um tom simpático."
)


def gerar_resposta(mensagem_usuario: str) -> str:
    """Gera a resposta do chatbot usando a API do Gemini."""
    if not mensagem_usuario or not mensagem_usuario.strip():
        return "Desculpe, não entendi sua mensagem. Pode repetir?"

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=f"{CONTEXTO_SISTEMA}\n\nCliente: {mensagem_usuario}",
        )
        return response.text
    except Exception as e:
        return f"Desculpe, ocorreu um erro ao processar sua mensagem: {e}"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    dados = request.get_json(silent=True) or {}
    mensagem = dados.get("mensagem", "")
    resposta = gerar_resposta(mensagem)
    return jsonify({"resposta": resposta})


if __name__ == "__main__":
    app.run(debug=True)