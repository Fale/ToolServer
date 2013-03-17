# -*- coding: utf-8  -*-

# TASK: Correggere gli spazi doppi
# USE: python replace.py -log -xml:itwiki-latest-pages-articles.xml -namespace:0 -fix:2spazi -pt:60
# STAT: beta

fixes['spazi'] = {
    'regex': True,
    'msg': {
        'it':u'Correggo gli spazi doppi'
    },
    'replacements': [
        (u'([a-zA-Z]|[,:;!?]|\.\.\.|…)[ ]{2,3}([a-zA-Z]|[,:;!?]|\.\.\.|…)', ur'\1 \2'), #Correggo spazi doppi e tripli
    ],   
    'exceptions': {
        'inside-tags': [
            'hyperlink',    
            'link',
            'template',
            'comment',       
            'nowiki',
            #'startspace',
            'pre',           
            'source',
            'math',
            'table',    
            'gallery',
            'timeline',
        ],
        'inside': [
            #r'\[[^\]]+\]', #Per esagerare colle precauzioni ed evitare errori come in Italo_Calvino#Collegamenti_esterni
            #r'\[http[^ ]+([,:;!?]|\.\.\.|…)[^ ]+ .+\]', #Se si volesse salvare solo l'indirizzo e non il titolo
            u'{{sic|(.*)}}',
            r'[Image|File|Immagine]:.*\.[png|jpg|svg]', #Images
            r'(?s)<[^>]+>',
            r'color:',
            #r'Aiuto:Provincia',
            r'background:',
            r'style="(.*)"',
            r"style='(.*)'",
            r'(?s)\{[^\}]+\}', #Inutile, non produce errori in nessuna voce in Wikiquote; utile per togliere l'exceptinsid template
            r'&[^;]+;',
        ],         
    }
}
