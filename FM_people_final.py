# -*- coding: utf-8 -*-
__author__ = 'angelinaprisyazhnaya'

import urllib2, re, codecs, wikipedia

people = codecs.open(u'people_NOM.csv', 'r', 'utf-8')
people_final = codecs.open(u'people_final.csv', 'w+', 'utf-8')

dic = {}

url = 'http://www.rvb.ru/dostoevski/04index/name_index.htm'
html = urllib2.urlopen(url).read().decode('cp1251')
#html = unicode(html, 'cp1251')
html = html.replace(u'\n', u' ').replace(u'\r', u'')


for line in people:
    m = re.search(u';(.+?);(.+?);', line, flags=re.U)
    person = m.group(1)
    letter_number = m.group(2)
    if re.search(u'\\w\.\\s\\w\.\\s\\w+', person, flags=re.U) != None:
        if person not in dic:
            #dic[person] = letter_number
            dic[person] = 1
        else:
            #dic[person] += u', ' + letter_number
            dic[person] += 1

    elif re.search(u'(\\w+)\\s(\\w+)', person, flags=re.U) != None:
        ns = re.search(u'(\\w+)\\s(\\w+)', person, flags=re.U)
        name = ns.group(1)
        surname = ns.group(2)

        name_html = re.search(name + u'\\s(\(\\w+\)\\s)?' + surname + u'\\sсм\.\\s(\\w+)\\s(\\w\.)\\s(\\w\.)', html, flags=re.U)

        if name_html != None:
            name_html_final = name_html.group(3) + u' ' + name_html.group(4) + u' ' + name_html.group(2)

            if name_html_final not in dic:
                dic[name_html_final] = 1
                #dic[name_html_final] = letter_number
            else:
                dic[name_html_final] += 1
                #dic[name_html_final] += u', ' + letter_number


for i in dic:

    wikipedia.set_lang(u'ru')

    try:
        name_wiki = wikipedia.page(i)
        link = name_wiki.url
        link = link.encode('ascii')
        link = urllib2.unquote(link).decode('utf8')
        people_final.write(i + u';' + str(dic[i]) + u';' + link + u'\r\n')
    except:
        continue





people.close()
people_final.close()
