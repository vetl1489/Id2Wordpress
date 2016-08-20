// Generated by CoffeeScript 1.10.0

/*
KVdir v. 1.0.1
NodeJS script
vetl1489
 */

(function() {
  var dirs, fs;

  fs = require('fs');

  dirs = ['1', '2', '3', '4', '5', '8', '9', '10', 'PDF', 'WEB', 'Реклама'];

  dirs.forEach(function(dir) {
    return fs.access(dir, fs.R_OK | fs.W_OK, function(err) {
      if (err) {
        fs.mkdirSync(dir);
        return console.log("Папка '" + dir + "' создана.");
      }
    });
  });

}).call(this);

//# sourceMappingURL=kvdir.js.map
