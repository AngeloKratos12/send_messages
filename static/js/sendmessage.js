var username = localStorage.getItem('user_name')
function store(){
    var message = document.getElementById('write').value;
    window.localStorage.setItem('message',message);
    message = window.localStorage.getItem('message')

    var destination = document.getElementById('enterDest').value;
    window.localStorage.setItem('destination',destination);
    destination = window.localStorage.getItem('destination')
    
                }

window.onload = function(){
    document.getElementById("stock").onsubmit = store;
                    
                }

   