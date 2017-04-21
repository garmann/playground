var mysql = require('mysql');
var con = mysql.createConnection({
  host: '192.168.178.60',
  user: 'root',
  password: 'x'
});

con.connect(function(err){
  if (err) {
    console.error('error connecting', err.stack);
    return;
  }

  console.log('connected', con.threadId);
});

con.query('SHOW PROCESSLIST', function(err, results, fields){
  if (err) throw err;
  console.log(0, results);
  console.log(1, fields);

});

con.end(function(err){
  if (err) console.log(err);
});