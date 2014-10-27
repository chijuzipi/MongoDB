var server = require("./server");
var router = require("./router");
var requestHandlers = require("./requestHandler");

var handle = {
                "/" : requestHandlers.normal,
                "/start" : requestHandlers.normal,
                "/upload" : requestHandlers.upload
            };
console.log(handle);

server.start(router.route, handle);
