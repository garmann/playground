# play with syslog-ng
(see vagrant file for vm configuration and ip)

## vagrant setup
- open terminal and cd into the directory
- (virtualbox/vagrant installed)
- (select own config.vm.box image)
- shell: vagrant up

## install syslog-ng
```
apt-get update
apt-get install syslog-ng syslog-ng-core
```

## config syntax check
```
syslog-ng -s -f /etc/syslog-ng/syslog-ng.conf
```

## create log event
```
logger foobar
```

## log to remote
````
destination d_net { tcp("192.168.50.8" port(1000) log_fifo_size(1000)); };
log { source(s_src); destination(d_net); };
````

## receive remote logs
```
source s_net { tcp(ip(0.0.0.0) port(1000)); };
destination d_net { file("/var/log/remote.log"); };
log { source(s_net); destination(d_net); };
```

## filtering remote logs

### filtering based on hostnames
(this shows an easy way with local dns resolution at the log server)

- add ip and hostnames to /etc/hosts

```
192.168.50.5 app1
192.168.50.6 app2
192.168.50.7 web1
```

- change "use_dns(no)" to "yes" in main configuration

```
options { chain_hostnames(off); flush_lines(0); use_dns(yes); use_fqdn(no);
          owner("root"); group("adm"); perm(0640); stats_freq(0);
          bad_hostname("^gconfd$");
};
```
- add/change filtering rules, this is only for app servers

```
filter app { host(app); };
source s_net { tcp(ip(0.0.0.0) port(1000)); };
destination d_net { file("/var/log/remote.log"); };
log { source(s_net); filter(app); destination(d_net); };
```

### filtering based on regex
(on log server)

```
filter f_ntp { match("adjust time server", value("MESSAGE")); };
source s_net { tcp(ip(0.0.0.0) port(1000)); };
destination d_ntp { file("/var/log/remote_ntp.log"); }
log { source(s_net); filter(f_ntp); destination(d_ntp); };
```

- value("MESSAGE") will scan the whole line

### add external logfiles
(on log client)

```
destination d_net { tcp("192.168.50.8" port(1000) log_fifo_size(1000)); };
source s_test { file("/tmp/logfile"); };
log { source(s_test); destination(d_net); };
```

## links
- [https://www.balabit.com/sites/default/files/documents/syslog-ng-ose-latest-guides/en/syslog-ng-ose-guide-admin/html/index.html](https://www.balabit.com/sites/default/files/documents/syslog-ng-ose-latest-guides/en/syslog-ng-ose-guide-admin/html/index.html)
- [https://pzolee.blogs.balabit.com/2009/12/troubleshooting-and-debugging-syslog-ng/](https://pzolee.blogs.balabit.com/2009/12/troubleshooting-and-debugging-syslog-ng/)
- [http://www.syslog.org/logged/reading-logs-from-a-file-in-syslog-ng/](http://www.syslog.org/logged/reading-logs-from-a-file-in-syslog-ng/)