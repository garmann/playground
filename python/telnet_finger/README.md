# weather information in terminal or python

i found a tool (graph.no) to get weather informations on the command line. you can do something like this:

```
finger berlin@graph.no
or 
finger o:berlin@graph.no
```

this results into (finger berlin@graph.no):

```
                   -= Meteogram for germany/berlin/berlin =-
 'C                                                                   Rain (mm)
 24======
 23      ^^^^^^                                                       9 mm
 22            ^^^^^^^^^                                              8 mm
 21                     ===                                         ' 7 mm
 20                        ===^^^                                   ' 6 mm
 19                              ^^^                                ' 5 mm
 18                                 ===        '  '  '           '  ' 4 mm
 17                                    ^^^^^^  '  '  '  '     '  '  ' 3 mm
 16  '                                       =='  '  '  '  |=='=='==' 2 mm
 15  |  |                 |  |        |        |==|==|==|==|  |  |  | 1 mm
   _15_16_17_18_19_20 21 22 23 00 01 02 03 04_05_06_07_08_09_10_11_12 Hour

     N NW NW NW  N NE NE NE NE NE NE NE NE  N  N  N  N  N NW NW NW NW Wind dir.
     2  4  5  5  6  5  4  4  4  5  7  6  6  7  8  8  9  9 10 10 12 10 Wind(mps)

Legend left axis:   - Sunny   ^ Scattered   = Clouded   =V= Thunder   # Fog
Legend right axis:  | Rain    ! Sleet       * Snow
[Rate limited to survive twitter storm. Max 3 connections pr. 30 seconds.]
```


or this results into (finger o:berlin@graph.no):

```
berlin at 19:00: 19 C, 7.9 mps wind from WNW.
```

## python code

```
>>> import telnetlib
>>> tn = telnetlib.Telnet('graph.no', 79, 2)
>>> tn.write('o:berlin\n')
>>> print tn.read_all()
berlin at 19:00: 19 C, 7.9 mps wind from WNW.
```

parameters:

- telnetlib.Telnet(host, port, timeout)
	- host = hostname of service, like 'graph.no'
	- port = finger protocol uses 79
	- timeout = client timeout in seconds
- tn.write('o:berlin\n')
	- \n is needed


## python script
- see finger_test.py


## more info


- [https://0p.no/2014/12/13/graph_no___weather_forecast_via_finger.html](https://0p.no/2014/12/13/graph_no___weather_forecast_via_finger.html)
- [https://github.com/ways/pyyrascii](https://github.com/ways/pyyrascii)
- [https://github.com/ways/pyyrlib](https://github.com/ways/pyyrlib)
- [https://docs.python.org/2/library/telnetlib.html](https://docs.python.org/2/library/telnetlib.html)
