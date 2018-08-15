function writeCookie(name, value, days){
    //By default, there is no expiration so the cookies is temporary
    var expires = "";
    
    //specifying a number of days makes the cookiee persistent
    if (days){
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toGMTString();
    }
    //set the cookie to the name, value and expiration date
    document.cookie = name + "=" + value + expires + "; path=/";
}

function readCookie(name){
    //find the specified cookie and return its value
    var searchName = name + "=";
    var cookies = document.cookie.split(';');
    for(var i=0; i < cookies.length; i++){
        var c = cookies[i];
        while (c.chart[0] ==' ')
            c = c.substring(1, c.length);
        if (c.indexof(searchName) === 0)
            return c.substring(searchName.length, c.length);
    }
    return null;
}

function eraseCookie(name){
    //earase the specified cookie
    writeCookie(name, "", -1);
}