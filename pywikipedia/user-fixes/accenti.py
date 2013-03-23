
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
    
        'graphsymb': {
        'regex': True,
        'nocase': True,
        'msg': {
               'it':u'Correzione dei simboli di punteggiatura'
              },
        'replacements': [
(ur"(\.\s*)E'", ur"\1È"),
(ur"([^ \t\n\r\f\v0-9]+),([^ \t\n\r\f\v0-9\):]+)", ur"\1, \2"),
(ur"(\s+),(\s+)", ur", "),
(ur"([^ \t\n\r\f\v']+)['’`] (\S+)", ur"\1'\2"),
(ur"([^ \t\n\r\f\v']+)[’`](\S+)", ur"\1'\2"),
(ur"po['’`](\S+)", ur"po' \1"),
(ur"Guns N['’`]Roses", ur"Guns N' Roses"),
(ur"www,", ur"www."),
(u" po'([^ ,.]{1})", ur" po' \1"),
(u" mo'([^ ,.]{1})", u" mo' \1"),
(u" ([Dd])e'([^ ,.]{1})'", ur" \1e' \2"),
(u" ([Cc])a'([^ ,.]{1})'", ur" \1a' \2"),
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
    },
}
