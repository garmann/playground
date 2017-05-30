var request = require('request'); 
const cheerio = require('cheerio')


exports.getVisitorName = function(url, cb){
  /*
  with a baisc membership on xing.com you are not able to get the names of your visitors. i found a workaround in the internet with the events page.

  this is my exported function :-)

  usage:
  - right click on the persons image in the visistors pane
  - copy image address
  - run this function with copy data (url)

  Args:
    - url (string)
    - callback

  Returns 
    - callback with name or error

  */

  if (typeof cb !== 'function'){
    throw Error('this is not a callback!')
  }

  if (url.startsWith('https://www.xing.com/img/users/') === false || url.endsWith('.jpg') === false){
    cb(1, 'no valid input');
  }

  const xing_url = 'https://www.xing.com/events/widgets/organized/'

  let pos_begin_userid = url.indexOf('.', 17) + 1;
  let pos_end_userid = url.indexOf(',', 17);
  let visitor_userid = parseInt(url.substring(pos_begin_userid, pos_end_userid))

  if (Number.isInteger(visitor_userid) === false) {
    cb(new Error('cloud not parse userid from visistor'));
  }

  let eventsPageUrl = xing_url + visitor_userid

  console.log('DEBUG: eventsPageUrl: ', eventsPageUrl);

  request(eventsPageUrl, function(error, response, body){
    if (error) cb(new Error(error));

    let $ = cheerio.load(body);
    let title = $('head title').text();
    let pos_start = 11; // string starts with: 'Events von '
    let pos_end = title.indexOf('|') - 1;

    if (typeof title === 'string'){
      cb(null, title.substring(pos_start, pos_end));
    } else {
      cb(new Error('cloud not parse name'));
    }
    
  });



};