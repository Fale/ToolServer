# -*- coding: utf-8  -*-

# TASK: Correggere spazi e punteggiatura
# USE: python replace.py -log -xml:itwiki-latest-pages-articles.xml -namespace:0 -fix:spazi -pt:60
# FIXME: migliorare le exceptions
# TODO: aggiungere gestione parentesi
# STAT: beta

fixes['spazi'] = {
    'regex': True,
    'msg': {
        'it':u'Correggo spazi'
    },
    'replacements': [
        (u"([a-zA-Z]) ?([,:;!?]|\.\.\.|…)(\w)", ur"\1\2 \3"),
        (u"([a-zA-Z]) ?([\"»]) ?([,:;!?]|\.\.\.|…)(\w)", ur"\1\2\3 \4"),
        (u"([a-z]) ?\.([A-Z][a-z]+\\b)", ur"\1. \2"),   
    ],   
    'exceptions': {
        'inside-tags': [
            'hyperlink',    
            'link',
            #'template',
            'comment',       
            #'nowiki',
            #'startspace',
            #'pre',           
            'source',
            'math',
            #'table',    
            #'gallery',
            #'timeline',
        ],
        'inside': [
            #r'\[[^\]]+\]', #Per esagerare colle precauzioni ed evitare errori come in Italo_Calvino#Collegamenti_esterni
            #r'\[http[^ ]+([,:;!?]|\.\.\.|…)[^ ]+ .+\]', #Se si volesse salvare solo l'indirizzo e non il titolo
            r'(?s)<[^>]+>',
            r'[Ff]ile:',
            r'[Ii]mage:',
            r'[Ii]mmagine:',
            r'color:',
            r'Aiuto:Provincia',
            r'background:',
            r'style="(.*)"',
            r"style='(.*)'",
            r'(?s)\{[^\}]+\}', #Inutile, non produce errori in nessuna voce in Wikiquote; utile per togliere l'exceptinsid template
            r'&[^;]+;',
        ],         
    }
}
