$(document).ready(function(){
    var menu = $('#menu');
    var year = new Date().getFullYear();
    var years = year - 2007;
    for (var i = 0; i <= years; i++){
        if (app == 'evento')
            menu.append('<li><a href="/actividad/eventos/'+(Number(year)-Number(i))+'/">'+(Number(year)-Number(i))+'</a></li>');
        else if (app == 'noticia')
            menu.append('<li><a href="/actividad/noticias/'+(Number(year)-Number(i))+'/">'+(Number(year)-Number(i))+'</a></li>');
        else if (app == 'informe')
            menu.append('<li><a href="/actividad/informes/'+(Number(year)-Number(i))+'/">'+(Number(year)-Number(i))+'</a></li>');
        }
    });
