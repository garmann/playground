var mysql = require('mysql');
var amount_queries = 10;
var pool = mysql.createPool({
  connectionLimit: 5,
  host     : '192.168.178.60',
  user     : 'root',
  password : 'x',
  database : 'mysql'
});

function databaseWorkker(){

  var promise = new Promise(

    function(resolve, reject){
      pool.getConnection(function(err, con){
        if (err) console.log('mysql error', err);

        console.log('starting conn id:', con.threadId);
        con.query('select sleep(5)', function(err, results, fields){
          console.log('ending conn id:', con.threadId);
          if (err) console.log('mysql error', err);
          con.release();
          resolve();
        });  
          
      });

    }

  );

  return promise;
}


function runDatabaseWorkers(){
  connections = [];

  for (var x = 0;x<=amount_queries -1;x++){
    connections.push(databaseWorkker());
  }

  Promise.all(connections).then(function(){
    pool.end();
  });

}

runDatabaseWorkers();


