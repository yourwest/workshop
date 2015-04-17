# -*- coding: utf-8 -*-

import urllib2, re, codecs

metadata = codecs.open(u'metadata.csv', 'r', 'utf-8')
people = codecs.open(u'people.csv', 'w', 'utf-8')
number = 1

for line in metadata:
    inf = re.search(u'\\b(\\d+?);(.+?);(.+?);', line)
    ID = inf.group(1)
    author = inf.group(2)
    addressee = inf.group(3)
    letter = codecs.open(u'./texts/' + ID + u'.txt', 'r', 'utf-8')
    people.write(str(number) + u';' + author + u';' + ID + u';' + u'автор' + u'\r\n')
    number += 1
    people.write(str(number) + u';' + addressee + u';' + ID + u';' + u'адресат' + u'\r\n')
    number += 1
    for i in letter:
        person = re.findall(u'[^.?!]\\s([А-Я][а-я]+\\s[А-Я][а-я]+(\\s[А-Я][а-я]+)?)|(\\w\.\\s\\w\.\\s)((\\w)+)', i)
        for ii in person:
            if re.search(u'(Бо(г(а((ми?)|х)?|и|у|е|о(м|в))?)|ж)|(В((а(с|ми?|ш(\\w)*?))|ы))', ii[0]) == None:
                people.write(str(number) + u';' + ii[0] + u';' + ID + u';' + u'упоминат' + u'\r\n')
                number += 1

metadata.close()
people.close()
