/*Validações do Login*/
$(function() {
    $('#login').submit(function() {
        var obj = this;
        var form = $(obj);
        var dados = new FormData(obj);
        $.ajax({
            url: form.attr('action'),
            type: form.attr('method'),
            data: dados,
            processData: false,
            cache: false,
            contentType: false,
            success: function(data) {
                if (data == "ErroUsuarioVazio") {
                    let usuario = document.getElementById('usuario');
                    usuario.className = 'form-control col-7 is-invalid';
                    usuario.focus();
                    let erroUsuario = window.document.getElementById('erroUsuario');
                    erroUsuario.className = 'col-7 invalid-feedback d-block';
                }
                else{
                    let usuario = document.getElementById('usuario');
                    usuario.className = 'form-control col-7';
                    let erroUsuario = window.document.getElementById('erroUsuario');
                    erroUsuario.className = 'col-7 invalid-feedback';
                }
                if (data == "ErroSenhaVazio") {
                    let senha = document.getElementById('senha');
                    senha.className = 'form-control col-7 is-invalid';
                    senha.focus();
                    let erroSenha = window.document.getElementById('erroSenha');
                    erroSenha.className = 'col-7 invalid-feedback d-block';
                }
                else{
                    let senha = document.getElementById('senha');
                    senha.className = 'form-control col-7';
                    let erroSenha = window.document.getElementById('erroSenha');
                    erroSenha.className = 'col-7 invalid-feedback';
                }
            }
        })
        return false;
    })
});