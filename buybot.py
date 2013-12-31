# -*- coding: utf-8 -*-
import cexapi
import os
from time import sleep
print 'Started Buybot V1.0 Buys at 0.00001 or more BTC'
print 'Loading Config...'
print ''
confg = open('buybot.ini','r')
refresh = int(confg.readline().split(':')[1])
usrname = confg.readline().split(':')[1].rstrip()
api_pub = confg.readline().split(':')[1].rstrip()
api_pri = confg.readline().split(':')[1].rstrip()
confg.close()
cex = cexapi.api(usrname, api_pub, api_pri)
loopcount = 1.0
print 'Now Starting up!'
sleep(2)
os.system('cls')
while(loopcount < 100000):
	f = open('buybot.log','w')
	print 'Loop number %10.0f' % loopcount
	print '\n\n\n\n\n\n\n\n\n'
	btcf = float(cex.balance()['BTC']['available'])
	buyp = float(cex.ticker('GHS/BTC')['last'])
	print 'BTC Balance %6.6F' % btcf
	if(btcf > 0.00001):
		buyamount = btcf/buyp	
		print cex.place_order('buy',buyamount,buyp,'GHS/BTC')
		print 'Bought %2.8F GH/s at %1.8F BTC' % buyamount,buyp
		f.write('Bought %2.8F GH/s at %1.8F BTC' % buyamount,buyp)
	else:
		print 'Not Enough BTC'
	timem = float(refresh)/float(60)
	print 'Next try in about %3.2f minutes' % timem
	print ''
	loopcount = loopcount + 1
	f.close()
	sleep(refresh)
	os.system('cls')
print 'Done'