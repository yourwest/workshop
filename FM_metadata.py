# -*- coding: utf-8 -*-
__author__ = 'angelinaprisyazhnaya'

import urllib2, re, codecs

url = 'http://rvb.ru/dostoevski/tocvol15.htm' 
html = urllib2.urlopen(url).read()
html = unicode(html, 'cp1251')
html = html.replace(u'\n', u'').replace(u'\r', u'')

def find_links(mainHtml):
    links = re.findall(u'<a\\s+href="(01.+?)"', mainHtml)
    return links

def find_text(mainHtml):
    try:
        letterText = re.search(u'adressee">(.+?)<div class="navigation">', mainHtml)
        finalText = letterText.group(1)
    except:
        letterText = re.search(u'<p\\s+id="p1">(.+?)<div class="navigation">', mainHtml)
        finalText = letterText.group(1)
    
    finalText = finalText.replace(u'&lt;', u'').replace(u'&gt;', u'').replace(u'</p>', u'\r\n')
    finalText = finalText.replace(u'&egrave;', u'è').replace(u'&Egrave;', u'È')
    finalText = finalText.replace(u'&agrave;', u'à').replace(u'&Agrave;', u'À')
    finalText = finalText.replace(u'&ecirc;', u'ê').replace(u'&Ecirc;', u'Ê')
    finalText = finalText.replace(u'&acirc;', u'â').replace(u'&Acirc;', u'Â')
    finalText = finalText.replace(u'&eacute;', u'é').replace(u'&Eacute;', u'É')
    finalText = finalText.replace(u'&ccedil;', u'ç').replace(u'&Ccedil;', u'Ç')
    finalText = finalText.replace(u'&oelig;', u'œ').replace(u'&OElig;', u'Œ')
    finalText = finalText.replace(u'&euml;', u'ë').replace(u'&Euml;', u'Ë')
    finalText = finalText.replace(u'&iuml;', u'ï').replace(u'&Iuml;', u'Ï')
    
    toBeCut = re.findall(u'\\d+?</div>', finalText)
    for i in toBeCut:
        finalText = finalText.replace(i, u'')
        
    toBeCut = re.findall(u'\\d+?</a>', finalText)
    for i in toBeCut:
        finalText = finalText.replace(i, u'')     

    toBeCut = re.findall(u'<.+?>', finalText)
    for i in toBeCut:
        finalText = finalText.replace(i, u'')
        
    return finalText

def main(text):
    links = find_links(html)
    ID = 1
    for i in links:
        letterUrl = u'http://rvb.ru/dostoevski/' + i
        letterHtml = urllib2.urlopen(letterUrl).read()
        letterHtml = unicode(letterHtml, 'cp1251')
        letterHtml = letterHtml.replace(u'\n', u'').replace(u'\r', u'')

        text = codecs.open(u'./texts/' + str(ID) + u'.txt', 'w', 'utf-8-sig')
        text.write(find_text(letterHtml))
        text.close()
        ID += 1

if __name__ == u'__main__':
    main(u'page.html')
