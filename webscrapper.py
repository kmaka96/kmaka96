import http.cookiejar
import random
import os
from colored import fg
import urllib.request
import requests
import bs4
import time
color = fg('light_green')
color1 = fg('light_blue')
color2 = fg('light_red')
color3 = fg('yellow')

print(color3+'_______________________________________')
print(color+ 'Created by Nikhil Rathore')
print(color3+'_______________________________________')

class scrap():
    count1 = 0
    link = ''
    def vpn():
        codeList = [ "US-C", "US", "US-W"]
        try:
    	    # connect to VPN
    	    #os.system("windscribe connect")

    	    # assigning a random VPN server code
    	    choiceCode = random.choice(codeList)
    	    # connecting to a different VPN server
    	    print("!!! Changing the IP Address........")
    	    os.system("windscribe connect ")#+ choiceCode)
                #os.system("windscribe disconnect")
        except Exception as e:
            #print(e)
    	    os.system("windscribe disconnect")
    	    print("sorry, some error has occurred..!!")

    def comment_scrape(url):
        commen = 0
        blue = True
        count1 = 0

        url = url.replace('https://www.facebook.com','https://mbasic.facebook.com')
        print('--------------------------------------------------------------')
        while blue:
                blue = False
                try:
                    data = requests.get(url)#,cookies=cj)
                    soup = bs4.BeautifulSoup(data.content,'html.parser')
                #print(soup.prettify())
                except Exception as e:
                    print('Retrying...')
                    continue
                for i in soup.find_all('a',href=True):
                    print(i.text)
                    if 'पिछली टिप्पणियाँ देखें…' in i.text:
                        #print(i.text)
                        #pages += i['href']+'\n'
                        url = i['href']
                        blue = True

                    if 'उत्तर' in i.text:
                        #print(i.text)
                        #print(i['href'])
                        if 'https://mbasic.facebook.com' not in i['href']:
                            commen = 'https://mbasic.facebook.com'+(i['href'])
                            with open("comments.txt","a",encoding="utf-8")as f:
                                f.write('\n')
                                f.write(str(commen))
                                f.write('\n')
                                f.write(i.text)
                                f.close()
                        else:
                            with open("comments.txt","a",encoding="utf-8")as f:
                                f.write('\n')
                                f.write(str(commen))
                                f.write('\n')
                                f.write(i.text)
                                f.close()
                    if 'जवाब' in i.text:
                        #print(i.text)
                        if 'https://mbasic.facebook.com' not in i['href']:
                            commen = 'https://mbasic.facebook.com'+(i['href'])
                            with open("comments.txt","a",encoding="utf-8")as f:
                                f.write('\n')
                                f.write(str(commen))
                                f.write('\n')
                                f.write(i.text)
                                f.close()
                        else:
                            with open("comments.txt","a",encoding="utf-8")as f:
                                f.write('\n')
                                f.write(str(commen))
                                f.write('\n')
                                f.write(i.text)
                                f.close()            
                    if 'https://chat.whatsapp.com' in i.text:
                        if (i.text) not in scrap.link:
                            scrap.count1 = scrap.count1+1
                            scrap.link += (i.text)+'\n'
                            print(color + 'found',i.text,scrap.count1)
                            with open("links.txt","a", encoding="utf-8")as f:
                                f.write('\n')
                                f.write(i.text)
                    if i.text == 'Forgotten password?':
                        print('You are logged out')
                        scrap.vpn()
                        time.sleep(2)
                        os.system("windscribe disconnect")
                    if i.text == 'पासवर्ड भूल गए?':
                        print('You are logged out')
                        scrap.vpn()
                        time.sleep(2)
                        os.system("windscribe disconnect")
                    if i.text == 'टाइमलाइन देखें':
                        break

    count = 0
    def search_url():
        tri = ''
        comment = ''
       
        a_file = open("url.txt",encoding='utf-8')
        lines = a_file.readlines()
        url = input("enter Your Group URL:" + color1)
        url = url.replace('https://www.facebook.com','https://mbasic.facebook.com')
        count = int(input(color1 +'Enter pages in no:'))
        print(url)
        a_file = open("url.txt",encoding='utf-8')
        lines = a_file.readlines()
        for line in lines:
            if url in line:
                answer = input("You have used this url do you still wan't to continue (y/n):")
                if answer ==  'y':
                    pass
                else:
                    scrap.search_url()
                break
            else:
                if url not in tri:
                    tri += url
                    with open("test.txt","a", encoding="utf-8")as f:
                        f.write('\n')
                        f.write(url)


        index = 0
        while(index < count):   
            data = requests.get(url)#,cookies=cj)
            soup = bs4.BeautifulSoup(data.content,'html.parser')
            for i in soup.find_all('a',href=True):
                print(i.text)
                if 'Comments' in i.text:
                    #print(i.text)
                    if (i['href']) not in comment:
                         scrap.comment_scrape(i['href'])  
                         comment += (i['href'])
                         print(color1 + '--------------------------------------------------------------')


                if 'टिप्पणियाँ' in i.text:
                    #print(i.text)
                    if (i['href']) not in comment:
                         scrap.comment_scrape(i['href'])  
                         comment += (i['href'])
                         print(color3 + i.text)
                         print('--------------------------------------------------------------')


                if 'https://chat.whatsapp.com/' in i.text:
                    if (i.text) not in scrap.link:
                        scrap.count1 = scrap.count1+1
                        scrap.link += (i.text)+'\n'
                        print(color + 'found',i.text,scrap.count1)
                        with open("links.txt","a", encoding="utf-8")as f:
                            f.write('\n')
                            f.write(i.text)
                if i.text == 'Forgotten password?':
                    print('You are logged out')
                    break

                if i.text == 'पासवर्ड भूल गए?':
                    print('You are logged out') 
                    break

                if i.text == 'let us know':
                    print(i.text)
                    break

                if i.text == 'See more posts':
                    url = 'https://mbasic.facebook.com' +i['href']
                    break
                if i.text == 'ଅଧିକ ପୋଷ୍ଟ ଦେଖନ୍ତୁ':
                    url = 'https://mbasic.facebook.com' +i['href']
                    break
            index = index+1
            if index == count:
                print(index)
                
                count = int(input(color1+"Do you wan't to add more page? add NUMBER:"+color2))

while True:
  scrap.search_url()
      
    




