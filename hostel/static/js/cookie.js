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
        while (c.charAt(0) ==' ')
            c = c.substring(1, c.length);
        if (c.indexOf(searchName) === 0)
            return c.substring(searchName.length, c.length);
    }
    return null;
}

function eraseCookie(name){
    //earase the specified cookie
    writeCookie(name, "", -1);
}


/*

        function validateRegFormData(){
            //validates the inputed data in the registration form for homes match
            //validates the inputed string of name if empty or number included
            if (document.getElementById("firstname").value === "")
                alert("Please provide your firstname");
            //validates the inputed string of name if empty or number included
            else if (document.getElementById("lastname").value === "")
                alert("Please provide your lastname");
            //validates the inputed string of name if empty or number included
            else if (document.getElementById("username").value === "")
                alert("Please provide a username");
            //validates the inputed password if its empty, length, and matches "confirm password"
            else if (document.getElementById("password").value === "")
                alert("Please provide a password");
            else if (document.getElementById("password").value.length < 8)
                alert("Password must be minimum of 8 characters");
            else if (document.getElementById("password2").value !== ""){
                if ((document.getElementById("password").value) != (document.getElementById("password2").value))
                alert("Passwords did not match, please check again");
            }
            //validates that the inputed password2 is not empty, length, and matches "password"
            else if (document.getElementById("password2").value === "")
                alert("Please confirm your password");
            else if (document.getElementById("password2").value.length < 8)
                alert("Password must be minimum of 8 characters");
            else if (document.getElementById("password").value !== ""){
                if ((document.getElementById("password").value) != (document.getElementById("password2").value))
                alert("Passwords did not match, please check again");
            }
            //validates the inputed email address if its empty, or @, .com is present 
            else if (document.getElementById("email").value === "")
                alert("Please provide your email address");
            else if ((document.getElementById("email").value.indexOf("@")) == -1 || (document.getElementById("email").value.indexOf(".com")) == -1)
                alert("Please enter a valid email address");
        }
        
        
        
        function validateContact(){
            //validates the inputed contact is a string of numbers and length
            if (isNaN(parseInt(document.getElementById("contact").value)))
                alert("Please enter a valid phone number");
        }
        
        function calcPrice(){
            //a function to calculate annual income to match home (need working)
            var maxprice = parseInt(document.getElementById("annual_income").value) * 4;
            document.getElementById("annual_income").value = "Annually, you can afford N" + maxprice.toFixed(2);
            
        }
        
	

*/