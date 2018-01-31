#!/usr/bin/python
# -*- coding: utf-8 -*-
def scrapBfx():
	from selenium import webdriver
	from bs4 import BeautifulSoup
	from time import sleep
	
	print "BFX�X�N���C�s���O�J�n"
	driver = webdriver.PhantomJS()
	driver.get('https://bfxdata.com/orderbooks/btcusd')
	html = driver.page_source
	
	# ���Y�p�C�œ������Ă����̂Ńy�[�W�ǂݍ��݂�3�b���炢���Ԃ��󂯂�
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
	
	# ���{�����[��, ���{�����[��, ���v	
	return sell,buy,total

def genText():
	sell,buy,total = scrapBfx()
	if sell == 0.0:
		sell,buy,total = scrapBfx()
		
		
	print "FLOAT�ϊ��に"
	print sell,buy,total
	print "-----------"
	if sell > buy:
		if sell < 80:
			strong = "���Ȃ蔄"
		else:
			strong = "��"
	else:
		if buy < 80:
			strong = "���Ȃ蔃"
		else:
			strong = "��"
	sellretio = round((sell / total), 2) * 100
	buyretio = round((buy / total), 2) * 100

	sell = str(sell)
	buy = str(buy)
	total = str(total)

	sellretio = str(sellretio)
	buyretio = str(buyretio)
	text = ""+strong+"�D��) SELLVOL "+sell+" ("+sellretio+"%) BUYVOL "+buy+" ("+buyretio+"%)"
	
	return text