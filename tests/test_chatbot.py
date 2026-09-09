import unittest
from unittest.mock import MagicMock, patch
from chatbot import SupermercadoBot

class TestSupermercadoBot(unittest.TestCase):
    def setUp(self):
        self.bot = SupermercadoBot()

    def test_mensagem_vazia(self):
        """Teste 1: Validação de entrada sem acionar a API externa."""
        resposta = self.bot.processar_mensagem("   ")
        self.assertEqual(resposta, "Por favor, digite uma pergunta válida.")

    @patch("chatbot.genai.Client")
    def test_resposta_gemini_com_mock(self, mock_client_class):
        """Teste 2: Simula resposta da API do Gemini sem gastar cotas ou depender de internet."""
        # Cria a resposta falsa simulada
        mock_response = MagicMock()
        mock_response.text = "O quilo do feijão custa R$ 8,50."

        # Configura o client falso para devolver a resposta simulada
        mock_instance = mock_client_class.return_value
        mock_instance.models.generate_content.return_value = mock_response

        # Atribui o client falso ao bot
        self.bot.client = mock_instance

        resultado = self.bot.processar_mensagem("Qual o valor do feijão?")

        self.assertIn("R$ 8,50", resultado)
        mock_instance.models.generate_content.assert_called_once()

if __name__ == "__main__":
    unittest.main()