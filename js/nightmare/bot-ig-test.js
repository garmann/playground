var Nightmare = require('nightmare');
var nightmare = Nightmare({
  show: true,
  debug: true,
  typeInterval: 100
  /*,
    openDevTools: {
      mode: 'detach'
    }
  */
  });

var username ='X';
var password = 'X';
var searchuser = 'X';


nightmare
  .viewport(1000, 1000)
  .useragent("Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36")
  .goto('https://www.instagram.com/')

  // click login link
  .click('._fcn8k')

  // fill input fields
  .type('input[name="username"]', username)
  .type('input[name="password"]', password)

  // click login button
  .click('._ah57t')

  // wait for document loaded means:
  // - wait until DOM content with .coreSpriteSearchIcon
  // - and then type into searchbox
  .wait('.coreSpriteSearchIcon')
  .type('._9x5sw', searchuser)

  // wait for dropdown menu is loaded and click it
  .wait('._oluat') //dropdown
  .click('._oluat')

  //wait for document load
  .wait()

  // test screenshot and scrolldown
  .screenshot('test1.png')
  .scrollTo(500,0)

  .wait(2000)

  // click on followers button from searched user
  .click('a[href="/' + searchuser + '/followers/"]')

  //wait for modal is loaded
  .wait('._gzjax')

  // wait 10 seconds so you can have a look around
  .wait(10000)

  // uncommend this for no exit
  .wait('.thisclassdoesnotexist')

  // end process
  .end()
  .then(function (result) {
    console.log(result);
  })
  .catch(function (error) {
    console.error('Search failed:', error);
  })
  ;