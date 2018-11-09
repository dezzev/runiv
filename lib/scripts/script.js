var link = "ИЗМЕНИТЕ ССЫЛКУ В SCRIPT.JS  ";

var $short = document.querySelector("#short");
var $url = document.querySelector("#url");

function copyToClipboard(text){
    var dobroipozitiv = document.createElement("input");
    document.body.appendChild(dobroipozitiv);
    dobroipozitiv.setAttribute('value', text);
    dobroipozitiv.select();
    document.execCommand("copy");
    document.body.removeChild(dobroipozitiv);
}

$short.addEventListener("click", function(e){
  var $not = document.querySelector("#notify");
  var $out = document.querySelector("#shorturl");
  var $hint = document.querySelector("#hint");
  
  $not.style.display = 'inherit';
  
  if ($url.value.includes("file://") || $url.value.includes(link)){
    $out.innerHTML = "Ошибка, попробуйте еще раз.";
  }
  
  if ($url.value == ""){
    $out.innerHTML = "Ошибка, попробуйте еще раз.";
    $hint.style.display = "none";
  }
  
  else {
  fetch('/link_gen', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    },
    body: "url=" + document.querySelector("#url").value
  })
  .then(function(response) {
    return response.json();
   })
  .then(function(res) {
      var url  = res.tourl;
      
      function copy() {
        copyToClipboard(link + url);
        $hint.style.display = 'inherit';
        $hint.innerHTML = "Ссылка была скопирована в буфер обмена";
        $url.focus();
	  }
	  
	  $url.blur(); 
      $out.innerHTML = ("Ваша ссылка : " + link + url);
      $out.addEventListener("click", function(a){
          copy();
      });
      
      document.body.addEventListener('keypress', function (b) {
        if (b.which === 99) {
          copy();
        }
	else if (b.which === 1089){
	  copy();
        }
      });
      
    });
  }
});

$url.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        $short.click();
    }});
