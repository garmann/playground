# infos

simple test for npm mysql lib with parallel connections build with promises.

## run docker mysql

```
docker run -it -e MYSQL_ROOT_PASSWORD=x -p 3306:3306 mysql
```

## check for mysql on localhost

```
lsof -i :3306
```

there should be an open mysql process

## run pooling or connect

```
npm install
node pooling.js
node connect.js
```