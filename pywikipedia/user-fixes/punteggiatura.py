fixes['punteggiatura'] = {
    'regex': True,
    'nocase': True,
    'msg': {
        'it':'Correggo punteggiatura'
    },
    'replacements': [
        (u"([^ \t\n\r\f\v0-9'\"\.:,<])\.([^ \t\n\r\f\v0-9'\"\)\.:\],<])",ur"\1. \2"),
        (u"(\S) \. (\S)",ur"\1. \2 "),
        (u"([a|d])\. c\.", ur"\1.C."), #a.C. e d.C.
        (u"\s\.([png|svg|jpg|jpeg])", ur".\1"),
        (u"([']{2,3,5}) (\S+)",ur" \1\2"),
        (u"(\S+) ([']{2,3,5})",ur"\1\2 "),
        (u"([^ \t\n\r\f\v0-9=]+)([,])([^ \t\n\r\f\v0-9\):\]<]+)", ur"\1\2 \3"),
        (u"(\s+)([,.])(\s+)", ur"\2\3"),
        # URLs
        (u"www,", u"www\."),
        (u"([^ ,]*),it", ur"\1.it"),
        (u"([^ ,]*),org", ur"\1.org"),
        (u"([^ ,]*),com", ur"\1.com"),
        (u"([^ ,]*),net", ur"\1.net"),
        (u"([^ ,]*),co", ur"\1.co"),
        (u"([^ ,]*),uk", ur"\1.uk"),

    ],
    'exceptions': {
        'inside': [
            r'\[\[.{2,3}:.*\]\]', #Interwiki
            r'[Image|File|Immagine]:.*\.[png|jpg|svg]', #Images
            r'http://.*[ ]', #URLs, broken -.-
            r'<sub>.*</sub>',
            r'{{familytree.*}}',
        ],
        'inside-tags': [
            'nowiki',
            'comment',
            'hyperlink',
            'math',
            'pre',
            'source',        # because of code examples
            'startspace',    # because of code examples
        ],
    }
}
