# inotify

inotify is an api in the linux kernel for keeping track of file changes. its in the kernel since 2.6.13 and replaces the old dnotify.

wiki:

- [https://en.wikipedia.org/wiki/Inotify](https://en.wikipedia.org/wiki/Inotify)

## iwatch
iwatch is a program which gives the user the possibility to monitor file changes. iwatch will talk with the inotify api. by any event you can make subcalls to scripts or reporting.

project:

- [http://iwatch.sourceforge.net/index.html](http://iwatch.sourceforge.net/index.html)

install:

- apt-get install iwatch

### run on comandline

- mkdir /testing
- iwatch -r /testing
- in a second terminal: echo "bar" >> /testing/foo

```
(on first terminal)
[29/Oct/2015 15:28:18] IN_CREATE /testing/foo
[29/Oct/2015 15:28:18] IN_CLOSE_WRITE /testing/foo
[29/Oct/2015 15:28:18] * /testing/foo is closed
```

### run as daemon

- in /etc/default/iwatch set START_DAEMON to "true"
- make changes to /etc/iwatch/iwatch.xml
- restart service

config example (first part is default, see second):

```
<config>
  <guard email="root@localhost" name="IWatch"/>
  <watchlist>
    <title>Operating System</title>
    <contactpoint email="root@localhost" name="Administrator"/>
    <path type="single" syslog="on">/bin</path>
    <path type="single" syslog="on">/sbin</path>
    <path type="single">/etc</path>
    <path type="recursive">/lib</path>
    <path type="exception">/lib/modules</path>
  </watchlist>
  <watchlist>
  <title>monitor /testing</title>
  <contactpoint email="admin@localhost" name="Administrator"/>
    <path type="recursive" alert="off" exec="logger iwatch %f">/testing</path>
  </watchlist>
</config>
```

on event this happens in syslog:

```
Oct 29 15:51:59 packer-virtualbox-iso-1445953545 vagrant: iwatch /testing/fooasd
```

### more info for configration and knowhow

- there are types of events and lots of stuff for configuration
 - [http://manpages.ubuntu.com/manpages/utopic/man1/iwatch.1.html](http://manpages.ubuntu.com/manpages/utopic/man1/iwatch.1.html)
 - [https://wiki.debianforum.de/Iwatch](https://wiki.debianforum.de/Iwatch)
 - [http://www.linux-magazin.de/Ausgaben/2007/03/Unter-der-Lupe](http://www.linux-magazin.de/Ausgaben/2007/03/Unter-der-Lupe)
 - [http://manpages.ubuntu.com/manpages/utopic/man1/iwatch.1.html](http://manpages.ubuntu.com/manpages/utopic/man1/iwatch.1.html)


### general thoughts
- queue events if you trigger a script after a lot of events
- does it run good on large filesystems? lots of files, usage and io? 

## more fun
- apt-cache search inotify|grep python

```
python-pyinotify - simple Linux inotify Python bindings
python-pyinotify-doc - simple Linux inotify Python bindings -- documentation
python3-pyinotify - simple Linux inotify Python bindings
python-inotifyx - simple Python binding to the Linux inotify
```

## other
- Gamin -> [https://en.wikipedia.org/wiki/Gamin](https://en.wikipedia.org/wiki/Gamin)
- fschange -> [http://stefan.buettcher.org/cs/fschange/](http://stefan.buettcher.org/cs/fschange/)
- find -ctime | -atime | -mtime
