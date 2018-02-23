#!/usr/bin/python
# -*- coding: utf-8 -*-
def scrapBfx():
	from selenium import webdriver
	from bs4 import BeautifulSoup
	from time import sleep
	
	print "はじめ"
	driver = webdriver.PhantomJS()
	driver.get('https://bfxdata.com/orderbooks/btcusd')
	html = driver.page_source
	
	# ラズパイで動かしていたのでページ読み込みに3秒くらい時間を空けた
	sleep(3)
	soup = BeautifulSoup(html,"lxml")

	tbody =soup.find("tbody", id= "volume1hTableBody")
	vols = tbody.find_all("td", class_="volumTableValue")

	sellVol = vols[0].text
	buyVol = vols[1].text
	totalVol = vols[2].text
	driver.save_screenshot('bfx.png')
	driver.quit()
	print "DELETE comma"
	sell = sellVol.replace(',', '')
	buy = buyVol.replace(',', '')
	total = totalVol.replace(',', '')

	sell = float(sell)
	buy = float(buy)
	total = float(total)
	
	# 売ボリューム, 買ボリューム, 合計	
	return sell,buy,total

def genText():
	sell,buy,total = scrapBfx()
	if sell == 0.0:
		sell,buy,total = scrapBfx()
		
	print sell,buy,total
	print "-----------"
	if sell > buy:
		if sell < 80:
			strong = "かなり売"
		else:
			strong = "売"
	else:
		if buy < 80:
			strong = "かなり買"
		else:
			strong = "買"
	sellretio = round((sell / total), 2) * 100
	buyretio = round((buy / total), 2) * 100

	sell = str(sell)
	buy = str(buy)
	total = str(total)

	sellretio = str(sellretio)
	buyretio = str(buyretio)
	text = ""+strong+"優勢) SELLVOL "+sell+" ("+sellretio+"%) BUYVOL "+buy+" ("+buyretio+"%)"
	
	print text
	
	return
