function store(){
    var user_name = document.getElementById('user_name').value;
    window.localStorage.setItem('user_name',user_name);
    
                }

    window.onload = function(){
        document.getElementById("store").onsubmit = store;
        
    }


