// seleciona o formulario pelo ID
const formulario = document.getElementById("formulario");

// aguarda o envio do formulario
formulario.addEventListener("submit", function(event) {
    // impede o recarregamento da pagina
    event.preventDefault();

    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;
    const mensagem = document.getElementById("mensagem").value;

    // verifica se todos os campos foram preenchidos
    if (nome === "" || email === "" || mensagem === "") {
        alert("Preencha todos os campos!");
        return;

    }
    // verifica se o email possui o caractere @
    if (!email.includes("@")) {
        alert("Digite um e-mail válido.");
        return;

    }

    // exibe mensagem de sucesso e limpa o formulario
    alert("Mensagem enviada com sucesso!");
    formulario.reset();

});