# -*- coding: utf-8  -*-

# TASK: Fix Italian region names
# USE: python replace.py -log -xml:itwiki-latest-pages-articles.xml -namespace:0 -fix:regioni -pt:60
# TODO: simplify regex
# STAT: beta

fixes['regioni'] = {
    'regex': True,
    'msg': {
        'it': u'Correggo nome regione'
    },
    'replacements': [
         #Abruzzo
            (u"\babruzzo\b", u"Abruzzo"),
        #Basilicata
            (u"\bbasilicata\b", u"Basilicata"),
        #Calabria
            (u"\bcalabria\b", u"Calabria"),
            (u"\b[Rr]eggio [Cc]alabria\b", u"Reggio Calabria"),
        #Campania
            (u"\bcampania\b", u"Campania"),
            (u"\bnapoli\b", u"Napoli"),
        #Emilia-Romagna
            (u"[Ee]milia[ _-][Rr]omagna", ur"Emilia-Romagna"),
            (u"Ferrovi[ae] Emilia-Romagna", u"Ferrovie Emilia Romagna"),
            (u"Banca Popolare [Dd]ell[’']Emilia[ -]Romagna", u"Banca Popolare dell'Emilia Romagna"),
            (u"Anfibi e Rettili dell'Emilia-Romagna", u"Anfibi e Rettili dell'Emilia Romagna"),
            (u"Emilia-Romagna Teatro", u"Emilia Romagna Teatro"),
            (u"Istituto Zooprofilattico Sperimentale della Lombardia e dell[’']Emilia[ -]Romagna", u"Istituto Zooprofilattico Sperimentale della Lombardia e dell'Emilia Romagna"),
            (u"Ispettorato Regionale Pionieri dell[’']Emilia[ -]Romagna", u"Ispettorato Regionale Pionieri dell'Emilia Romagna"),
            (u"Ispettorato Regionale Pionieri Emilia[ -]Romagna", u"Ispettorato Regionale Pionieri dell'Emilia Romagna"),
            (u"Ispettorato Regionale Volontari del Soccorso dell[’']Emilia[ -]Romagna", u"Ispettorato Regionale Volontari del Soccorso dell'Emilia Romagna"),
            (u"ADMO Emilia-Romagna", u"ADMO Emilia Romagna"),
        #Friuli Venezia Giulia
            #(u"[Ff]riuli[ _-][Vv]enezia[ _-][Gg]iulia", u"Friuli Venezia Giulia"),
            #(u"Friuli-Venezia Giulia Strade S.p.A.", u"Friuli Venezia Giulia Strade S.p.A."),
            #(u"FVG-IX - Friuli-Venezia Giulia Internet eXchange", u"FVG-IX - Friuli Venezia Giulia Internet eXchange"),
        #Lazio
            (u"\blazio\b", u"Lazio"),
        #Liguria
            (u"\bliguria\b", u"Liguria"),
        #Lombardia
            (u"\blombardia\b", u"Lombardia"),
        #Marche
            #(u"\\bMarche\\b", u"Marche"),
        #Molise
            (u"\bmolise\b", u"Molise"),
        #Piemonte
            (u"\bpiemonte\b", ur"Piemonte"),
            (u"[Dd]ucato[ _-]{1,2}[Dd]i [Ss]avoia", u"Ducato di Savoia"),
        #Puglia
            (u"\bpuglia\b", u"Puglia"),
        #Sardegna
            (u"\bsardegna\b", u"Sardegna"),
        #Sicilia
            (u"\bsicilia\b", u"Sicilia"),
        #Toscana
            #(u"\bToscana\b", u"Toscana"),
        #Trentino-Alto Adige
            (u"[Tt]rentino[ _-][Aa]lto[ _-][Aa]dige", u"Trentino-Alto Adige"),
        #Umbria
            (u"\bumbria\b", u"Umbria"),
        #Valle d'Aosta
            (u"[Vv]alle[ _-]d[’`' _][Aa]osta", ur"Valle d'Aosta"),
            (u"[Dd]ucato[ _-]d[’`' _][Aa]osta", u"Ducato d'Aosta"),
        #Veneto
            (u"\bveneto\b", u"Veneto"),

    ],
    'exceptions': {
        'inside-tags': [
            'hyperlink',
            'link',
        ],
        'inside': [
            r"[Ff]errovie [Ee]milia [Rr]omagna",
            r"[Bb]anca [Pp]opolare dell'[Ee]milia [Rr]omagna",
            r"[Bb]anca [Pp]opolare [Ee]milia [Rr]omagna",
            r"[Aa]tlante on\-line degli [Aa]nfibi e [Rr]ettili dell'[Ee]milia [Rr]omagna",
            r"[Cc]orpo [Pp]olacco in [Ee]milia [Rr]omagna",
            r"[Mm]afia, [Cc]amorra e '[Nn]drangheta in [Ee]milia [Rr]omagna",
            r"[Cc]onferenza [Ee]piscopale dell'[Ee]milia [Rr]omagna",
            r"[Pp]olitica del [Tt]erritorio in [Ee]milia [Rr]omagna",
            r'Almanacco del calcio regionale Trentino Alto Adige',
            r'Indipendenti Per Emilia-Romagna e Lombardia',
            r'Orchestra Regionale dell’Emilia Romagna',
            r"L'Emilia Romagna paese per paese",
            r'Emilia Romagna Teatro',
            r'Individuazione delle rete stradale di interesse regionale - Regione Emilia Romagna',
            r'Associazione Teatrale Emilia Romagna',
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
            r'[Pp]iste ciclabili del Trentino Alto Adige',
            r'[Rr]eti TV Emilia Romagna',
            # Interprogetto
            r'Ricette regionali-Trentino Alto Adige',
            # Old
            r'{{interprogetto|.*}}',
            r'\[\[.{2,3}:.*\]\]', #Interwiki
            r'[Image|File|Immagine]:.*\.[png|jpg|svg]', #Images
            r'@postacert\.umbria\.it', # mails
            r'@rete\.basilicata\.it', # mails
            r'regione\.basilicata\.it',
            r'regione\.calabria\.it',
            r'lombardia\.indettaglio\.it', #crappy used website
            r'airport\.umbria\.it',
            r'montitrasimeno\.umbria\.it',
        ],
    }
}
