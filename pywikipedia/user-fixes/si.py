# -*- coding: utf-8  -*-

# TASK: Correggere unità di misura SI
# USE: python replace.py -log -xml:itwiki-latest-pages-articles.xml -namespace:0 -fix:si -pt:60
# TODO: testing
# TODO: incrementare le regex
# STAT: alpha

fixes['si'] = {
    'regex': True,
    'msg': {
        'it':u'Correggo unità di misura'
    },
    'replacements': [
        #(u"(\s|\|)([1-9]{1,3}( [0-9]{3})*)(\s)", ur"\1\2 \3"), # Sostituzione spazio tra cifre
        (u'([0-9])[°º]( ?[\-–—a] ?[0-9]+)°C\\b', ur'\1\2 °C'), # Sostituzione di x°C con x °C
        (u'([0-9])[°º]( ?[\-–—a] ?[0-9]+)°F\\b', ur'\1\2 °F'), # Sostituzione di x°C con x °C
        (u'([0-9])[°º]C\\b', ur'\1 °C'), # Sostituzione di x°C con x °C
        (u'([0-9])[°º]F\\b', ur'\1 °F'), # Sostituzione di x°C con x °C
        (u"([0-9]) gr(\s)", ur"\1 g\2"), # Da gr a g
        (u"([0-9]) gr(\b)", ur"\1 g\2"), # Da gr a g
        (u"\|gr\]\]", ur"|g]]"), # Da gr a g
        (u"([0-9]) Kg", ur"\1 kg"), # Kg a kg, attenzione alle voci di scacchi
        (u"([0-9]) [Kk]g\. ([a-z])", ur"\1 kg \2"), # Kg a kg, attenzione alle voci di scacchi
    ],   
    'exceptions': {
        'title': [
            u'Studio 4°C', # Per °C
            u'Difesa siciliana, variante Svešnikov', # Per Kg
        ],
        'inside-tags': [
            'hyperlink',    
            'link',
            'comment',       
            'source',
            'math',
        ],
        'inside': [
            u'Studio 4°C', # Per °C
            u'groszy', # Da gr a g
            u'groschen', # Da gr a g
        ],         
    }
}
