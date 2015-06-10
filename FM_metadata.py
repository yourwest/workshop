# -*- coding: utf-8 -*-
__author__ = 'angelinaprisyazhnaya'

import urllib2, re, codecs

url = 'http://rvb.ru/dostoevski/tocvol15.htm' 
html = urllib2.urlopen(url).read().decode('cp1251')
#html = unicode(html, 'cp1251')
html = html.replace(u'\n', u'').replace(u'\r', u'')

def find_links(mainHtml):
    links = re.findall(u'<a\\s+href="(01.+?)"', mainHtml, flags=re.U)
    return links

def find_number(letter):
    letterNumber = re.search(u'<h1>(\\d+)\.', letter, flags=re.U)
    return letterNumber.group(1)

def find_addressee(letter):
    letterAddressee = re.search(u'<h1>\\d+\.\\s(.+?)<', letter, flags=re.U)
    Addressee = letterAddressee.group(1)
    
    if Addressee.endswith(u'КОЙ'):
        Addressee = Addressee.replace(u'КОЙ', u'КАЯ')
    elif Addressee.endswith(u'НОЙ'):
        Addressee = Addressee.replace(u'НОЙ', u'НА')
    elif Addressee.endswith(u'ВОЙ'):
        Addressee = Addressee.replace(u'ВОЙ', u'ВА')
    elif Addressee.endswith(u'КОМУ'):
        Addressee = Addressee.replace(u'КОМУ', u'КИЙ')
    elif Addressee.endswith(u'ЫМ'):
        Addressee = Addressee.replace(u'ЫМ', u'Ы')
    elif Addressee.endswith(u'НУ'):
        Addressee = Addressee.replace(u'НУ', u'Н')
    elif Addressee.endswith(u'ЛЮ'):
        Addressee = Addressee.replace(u'ЛЮ', u'ЛЬ')
    elif Addressee.endswith(u'ВУ'):
        Addressee = Addressee.replace(u'ВУ', u'В')
    elif Addressee.endswith(u'ЧУ'):
        Addressee = Addressee.replace(u'ЧУ', u'Ч')

    if re.search(u'(\\w\.\\s\\w\.\\s)((\\w)+)', Addressee, flags=re.U) != None:
        addressee1 = re.search(u'(\\w\.\\s\\w\.\\s)((\\w)+)', Addressee, flags=re.U)
        Addressee = addressee1.group(1) + addressee1.group(2).lower().capitalize()

    return Addressee

def find_date(letter):
    try:
        letterDate = re.search(u'subhead">(.+?)(\.|,)', letter, flags=re.U)
        return letterDate.group(1)
    except:
        letterDate = u''
        return letterDate

def find_place(letter):
    try:
        letterPlace = re.search(u'subhead">.+?(\.|,)\\s(.+?)<', letter, flags=re.U)
        return letterPlace.group(2)
    except:
        letterPlace = u''
        return letterPlace

def find_page(mainHtml, number):
    try:
        letterPage = re.search(u'<td><a\\s+href=".+?">' + number + u'\.\\s+.+?</a>.+?(\\d+)<', mainHtml, flags=re.U)
        return letterPage.group(1)
    except:
        letterPage = u''
        return letterPage

def find_note_link(letter):
    try:
        letterNoteLink = re.search (u'(02comm/.+?)">Примечания', letter, flags=re.U)
        return letterNoteLink.group(1)
    except:
        letterNoteLink = u''
        return letterNoteLink


def main(text):
    links = find_links(html)
    ID = 1
    metadata = codecs.open(u'metadata.csv', 'w', 'utf-8')
    for i in links:
        letterUrl = u'http://rvb.ru/dostoevski/' + i
        letterHtml = urllib2.urlopen(letterUrl).read().decode('cp1251')
        #letterHtml = unicode(letterHtml, 'cp1251')
        
        number = find_number(letterHtml)
        addressee = find_addressee(letterHtml)
        date = find_date(letterHtml)
        place = find_place(letterHtml)
        page = find_page(html,number)
        noteLink = u'http://rvb.ru/dostoevski/' + find_note_link(letterHtml)
        metadata.write(str(ID) + u';' + u'Ф.М.Достоевский' + u';' + addressee + u';' +
                       date + u';' + place + u';' + u'русский' + u';' +
                       u'Институт русской литературы РАН' + u';' +
                       u'Собрание сочинений в 15 томах' + u';'+ u'15' + u';' +
                       number + u';' + page + u';' + noteLink + u'\r\n')

        
        ID += 1
    metadata.close()
    
if __name__ == u'__main__':
    main(u'page.html')
