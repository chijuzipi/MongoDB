function normal(){
  console.log("request handler 'normal' was called");
}

function upload(){
  console.log("request handler 'upload' was called");
}

exports.normal = normal;
exports.upload = upload;
