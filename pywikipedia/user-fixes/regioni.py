# -*- coding: utf-8  -*-

# TASK: Fix Italian region names
# USE: python replace.py -log -xml:itwiki-latest-pages-articles.xml -namespace:0 -fix:regioni -pt:60
# TODO: simplify regex
# STAT: alpha

fixes['regioni'] = {
    'regex': True,
    'msg': {
        'it': u'Correggo nome regione'
    },
    'replacements': [
        (u"[Ee]milia [Rr]omagna", ur"Emilia-Romagna"),
#        (u"\[\[([Ee]milia) ([Rr]omagna)\]\]", ur"[[\1-\2]]"),
#        (u"\|([Ee]milia) ([Rr]omagna)\]\]", ur"|\1-\2]]"),
#        (u"\[\[([Ee]milia) ([Rr]omagna)\|", ur"\[\[\1-\2\|"),
#        (u"([Fr]iuli) ([Ve]nezia [Gg]iulia)(?!\])", ur"\1-\2"),
#        (u"\[\[([Fr]iuli) ([Ve]nezia [Gg]iulia)\]\]", ur"[[\1-\2]]"),
#        (u"\|([Fr]iuli) ([Ve]nezia [Gg]iulia)\]\]", ur"|\1-\2]]"),
        (u"([Tt]rentino) ([Aa]lto [Aa]dige)(?!\])", ur"\1-\2"),
        (u"\[\[([Tt]rentino) ([Aa]lto [Aa]dige)\]\]", ur"[[\1-\2]]"),
        (u"\|([Tt]rentino) ([Aa]lto [Aa]dige)\]\]", ur"|\1-\2]]"),
    ],
    'exceptions': {
        'text-contains': [
            r"[Ff]errovie [Ee]milia [Rr]omagna",
            r"[Bb]anca [Pp]opolare dell'[Ee]milia [Rr]omagna",
            r"[Aa]tlante on\-line degli [Aa]nfibi e [Rr]ettili dell'[Ee]milia [Rr]omagna",
            r"[Cc]orpo [Pp]olacco in [Ee]milia [Rr]omagna",
            r"[Mm]afia, [Cc]amorra e '[Nn]drangheta in [Ee]milia [Rr]omagna",
            r"[Cc]onferenza [Ee]piscopale dell'[Ee]milia [Rr]omagna",
            r"[Pp]olitica del [Tt]erritorio in [Ee]milia [Rr]omagna",
            # Categories
            r"[Rr]icette regionali-Emilia Romagna",
            r"[Aa]rchitetture barocche dell'Emilia Romagna",
            # Files
            r'Stemma Comando Regionale Emilia Romagna GDF',
            r'Stemma Comando Regionale Trentino Alto Adige GDF',
        ],
    }
}
