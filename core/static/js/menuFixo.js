 //Diz para o navegador o que será carregado no momento em que a página é acessada.
jQuery("document").ready(function($){
 
    //Elemento que vai receber os eventos.
    var nav = $('.menu_usuario');
 
    //Ao rolar a página, a função será executada.
    $(window).scroll(function () {
        //Se o tamanho da parte rolada for maior que 136px (pixels) ->
        if ($(this).scrollTop() > 1) {
            nav.addClass("fixed"); //Aplica a classe scrolled_menu no elemento .menu
        } else {
            nav.removeClass("fixed"); //Remove a classe scrolled_menu no elemento .menu
        }
    });
 
});
