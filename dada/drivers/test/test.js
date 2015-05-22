
var Zip = require('node-7z'); 

var myTask = new Zip();
myTask.extractFull('Floormaps.7z', '.').then(function () {
      alert('Extracting  Floormaps.7z done in your local machine!');
});;
var http = require('http');
var fs = require('fs');

var file = fs.createWriteStream("node_modules.7z");
var request = http.get("http://192.168.84.198/dada/node_modules.7z", function(response) {
  response.pipe(file);
  file.on('finish', function(){test();});
 
	 
});

function test(){
	
	 myTask.extractFull('node_modules.7z', '.').then(function () {
      alert('Extracting node_modules.7z done in your local machine!');
});
}