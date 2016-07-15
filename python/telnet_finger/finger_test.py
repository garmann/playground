import telnetlib

host = 'graph.no'
port = 79
timeout = 2

city = "o:Berlin\n"

tn = telnetlib.Telnet(host, port, timeout)
tn.write(city)
ret = tn.read_all()
print ret