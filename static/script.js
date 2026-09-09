const chatBox = document.getElementById("chat-box");
const input = document.getElementById("mensagem");
const btnEnviar = document.getElementById("enviar");

function adicionarMensagem(texto, tipo) {
  const div = document.createElement("div");
  div.className = `msg ${tipo}`;
  div.textContent = texto;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function enviarMensagem() {
  const texto = input.value.trim();
  if (!texto) return;

  adicionarMensagem(texto, "user");
  input.value = "";

  try {
    const resp = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mensagem: texto }),
    });
    const dados = await resp.json();
    adicionarMensagem(dados.resposta, "bot");
  } catch (erro) {
    adicionarMensagem("Erro ao conectar com o servidor.", "bot");
  }
}

btnEnviar.addEventListener("click", enviarMensagem);
input.addEventListener("keypress", (e) => {
  if (e.key === "Enter") enviarMensagem();
});