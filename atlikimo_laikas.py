import datetime
import sys
 
arguments = sys.argv[1:]

first_argument = arguments[0]
second_argument = arguments[1]

now = str(datetime.datetime.now())

if first_argument == 'pradeti':
    f = open('task-%s.txt'%second_argument, mode = 'w')
    f.write(now)
    f.close()

if first_argument == 'pabaigti':
    f = open('task-%s.txt'%second_argument)
    pradeti = f.read()
    print(pradeti)
    print(now)
    trukme = None
    f.close()
    now = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S.%f')
    pradeti = datetime.datetime.strptime(pradeti, '%Y-%m-%d %H:%M:%S.%f')
    print(now - pradeti)
    

    #i stringa ideti papild reiksme
