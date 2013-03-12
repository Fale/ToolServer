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
        #(u"[Fr]iuli[ -][Ve]nezia [Gg]iulia", ur"Friuli Venezia Giulia"), # Not sure about the consense
        #(u"[Fr]iuli [Ve]nezia[ -][Gg]iulia", ur"Friuli Venezia Giulia"), # Not sure about the consense
        (u"[Tt]rentino [Aa]lto [Aa]dige", ur"Trentino-Alto Adige"),
        (u"[Tt]rentino[ -][Aa]lto-[Aa]dige", ur"Trentino-Alto Adige"),
    ],
    'exceptions': {
        'inside-tags': [
            'hyperlink',
            'link',
        ],
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
            r"[Aa]rchitetture gotiche dell'Emilia Romagna",
            r"[Aa]rchitetture rinascimentali dell'Emilia Romagna",
            r"[Aa]rchitetture romaniche dell'Emilia-Romagna",
            # Files
            r'Stemma Comando Regionale Emilia Romagna GDF',
            r'Stemma Comando Regionale Trentino Alto Adige GDF',
            # Templates
            r'[Pp]iste ciclabili del Trentino-Alto Adige',
        ],
    }
}
