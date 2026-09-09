import unittest
from unittest.mock import patch, MagicMock

import app as app_module


class TestGerarResposta(unittest.TestCase):
    """Testa a função gerar_resposta() sem chamar a API real do Gemini."""

    @patch("app.client.models.generate_content")
    def test_gerar_resposta_retorna_texto_da_api(self, mock_generate_content):
        resposta_falsa = MagicMock()
        resposta_falsa.text = "Sim, temos arroz em promoção esta semana!"
        mock_generate_content.return_value = resposta_falsa

        resultado = app_module.gerar_resposta("Vocês têm arroz?")

        self.assertEqual(resultado, "Sim, temos arroz em promoção esta semana!")
        mock_generate_content.assert_called_once()

    def test_gerar_resposta_mensagem_vazia(self):
        resultado = app_module.gerar_resposta("")
        self.assertIn("não entendi", resultado.lower())


class TestRotaChat(unittest.TestCase):
    """Testa a rota /chat usando o test client do Flask."""

    def setUp(self):
        app_module.app.testing = True
        self.client = app_module.app.test_client()

    @patch("app.gerar_resposta")
    def test_rota_chat_retorna_json_com_resposta(self, mock_gerar_resposta):
        mock_gerar_resposta.return_value = "Olá! Como posso ajudar?"

        resposta = self.client.post("/chat", json={"mensagem": "oi"})

        self.assertEqual(resposta.status_code, 200)
        dados = resposta.get_json()
        self.assertIn("resposta", dados)
        self.assertEqual(dados["resposta"], "Olá! Como posso ajudar?")


if __name__ == "__main__":
    unittest.main()