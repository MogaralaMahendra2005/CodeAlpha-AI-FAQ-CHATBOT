function sendMessage(){


let input=document.getElementById("message");


let message=input.value;



if(message.trim()=="")
return;



chat(message);


input.value="";


}





function askQuestion(question){


chat(question);


}




function chat(message){


let box=document.getElementById("chat-box");



box.innerHTML +=

"<div class='user'>"+message+"</div>";



fetch("/chat",{


method:"POST",


headers:{

"Content-Type":"application/json"

},


body:JSON.stringify({

message:message

})


})



.then(response=>response.json())


.then(data=>{


box.innerHTML +=

"<div class='bot'>"+data.answer+"</div>";



box.scrollTop=box.scrollHeight;


});


}