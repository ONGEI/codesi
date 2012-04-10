$(document).ready(function(){
    var menu = $('#menua');
    var year = new Date().getFullYear();
    var years = year - 2007;
    //var a = years <= 5 ? years : 5;
    for (var i = 0; i <= years; i++){
        menu.append('<li><a href="#">'+(Number(year)-Number(i))+'</a></li>');
        }
    /*if(years > (4)){
        years = years - 4;
        year = year - years;
        menu.append('<li class="divider"></li>');
        menu.append('<li class="dropdown">'+
        '<a class="dropdown-toggle" data-toggle="dropdown">Más<b class="caret"></b></a>'+
        '<ul id="menu-mas" class="dropdown-menu"></ul></li>');
        menu_mas = $("#menu-mas");
        for(var i = 0; i < years; i++){
            menu_mas.append('<li><a href="#">'+(Number(year)-(Number(i)+4))+'</a></li>');
        }
    }*/
    });
