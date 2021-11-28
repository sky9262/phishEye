window.onload = () => {
   function httpGet(theUrl) {
       var xmlHttp = new XMLHttpRequest();
       xmlHttp.open("GET", theUrl, false);
       xmlHttp.send(null);
       return xmlHttp.responseText;
   }

   ip = httpGet("https://api.ipify.org/")
   data = httpGet("https://ipapi.co/" + ip + "/json/")
   var url = "/";
   var xhr = new XMLHttpRequest();
   xhr.open("POST", url);
   xhr.setRequestHeader("Accept", "application/json");
   xhr.setRequestHeader("Content-Type", "application/json");
   xhr.onreadystatechange = function() {
       if (xhr.readyState === 4) {
           console.log(xhr.status);
           console.log(xhr.responseText);
       }
   };
   useragent = ',"useragent":"' + navigator.userAgent + '"'
   new_data = data.slice(0, -1) + useragent + data.slice(-1);
   console.log(new_data)
   xhr.send(new_data);

}
