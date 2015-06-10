# -*- coding: utf-8 -*-
__author__ = 'angelinaprisyazhnaya'

import re, codecs

people = codecs.open(u'people.csv', 'r', 'utf-8')
people_NOM = codecs.open(u'people_NOM.csv', 'w', 'utf-8')

for line in people:
    line = re.sub(u'(н|г)(ы|у|е|ой)\\s(\\w+)(ны|ну|не|ной)(;|\\s)', u'\\1а \\3на;', line, flags=re.U)
    line = re.sub(u'(р)(ы|у|е|ой)\\s(\\w+)(ны|ну|не|ной)(;|\\s)', u'\\1а \\3на;', line, flags=re.U)

    line = re.sub(u'(а|у)\\s(\\w+)(ч|в)(у|а)(;|\\s)(\\w+)я(;|\\s)', u' \\2\\3\\5\\6ь\\7', line, flags=re.U)
    line = re.sub(u'(а|у)\\s(\\w+)(ч|в)(у|а)(;|\\s)(\\w+)(у|а)(;|\\s)', u' \\2\\3\\5\\6\\8', line, flags=re.U)

    line = re.sub(u'(ая)\\s(\\w+)(ч|в)(у|а)(;|\\s)', u'ай \\2\\3\\5', line, flags=re.U) #Николая Николавевича
    line = re.sub(u'(а|у)\\s(\\w+)(ч|в)(у|а)(;|\\s)', u' \\2\\3\\5', line, flags=re.U)
    line = re.sub(u'ия\\s(\\w+)я', u'ий \\1ь', line, flags=re.U)
    line = re.sub(u'ею\\s(\\w+)у', u'ей \\1', line, flags=re.U)

    line = re.sub(u'(ю)\\s(\\w+)(чу)(;|\\s)', u'й \\2ч\\4', line, flags=re.U)

    line = re.sub(u'(ем|ом)\\s(\\w+)(ом|ем)(;|\\s)', u' \\2\\4', line, flags=re.U)

    line = re.sub(u'(ии|ией|ию)\\s(\\w+)(не|ной|ну|ны)(;|\\s)', u'ия \\2на\\4', line, flags=re.U)

    line = re.sub(u'ь(е|ю|и|ей)\\s(\\w+)(е|ой)(;|\\s)', u'ья \\2а\\4', line, flags=re.U)
    line = re.sub(u'е\\s(\\w+)е(;|\\s)', u'а \\1а\\2', line, flags=re.U)
    people_NOM.write(line)


people.close()
people_NOM.close()
