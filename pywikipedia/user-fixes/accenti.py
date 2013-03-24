# -*- coding: utf-8  -*-

# TASK: Correggere accenti
# USE: python replace.py -log -xml:itwiki-latest-pages-articles.xml -namespace:0 -fix:accenti -pt:60
# STAT: alpha

fixes['accenti'] = {
    'regex': True,
    'nocase': False,
    'msg': {
        'it':u'Correzione dei simboli di punteggiatura'
    },
    'replacements': [
        (u"([ ]{1}[^'’`]{1}[a-zA-Z ]*)a['’`]([ ,.]{1})", ur"\1à\2"),
        (u"([ ]{1}[^'’`]{1}[a-zA-Z ]*)e['’`]([ ,.]{1})", ur"\1è\2"),
        (u"([ ]{1}[^'’`]{1}[a-zA-Z ]*)i['’`]([ ,.]{1})", ur"\1ì\2"),
        (u"([ ]{1}[^'’`]{1}[a-zA-Z ]*)o['’`]([ ,.]{1})", ur"\1ò\2"),
        (u"([ ]{1}[^'’`]{1}[a-zA-Z ]*)u['’`]([ ,.]{1})", ur"\1ù\2"),
        (u" pò[ ,.]", ur" po'\1"),
        (u" mò[ ,.]", ur" mo'\1"),
        (u"([ \"'_][Dd])è ", ur"\1e' "),
        (u"([ \"'_][Cc])à ", ur"\1a' "),
    ],
    'exceptions': {
        'inside': [
            r'\[\[.{2,3}:.*\]\]', #Interwiki
            r'[Image|File|Immagine]:.*\.[png|jpg|svg]', #Images
        ],
        'inside-tags': [
            'nowiki',
            'comment',
            'math',
            'pre',
            'source',        # because of code examples
            'startspace',    # because of code examples
        ],
    }
}
