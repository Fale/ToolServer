# -*- coding: utf-8  -*-

# TASK: Rimuovere commenti inutili
# USE:: python replace.py -log -xml:itwiki-latest-pages-articles.xml -namespace:0 -fix:commentiHtml -pt:60
# TODO: Capire consenso
# STAT: alpha

fixes['commentiHtml'] = {
    'regex': True,
    'msg': {
        'it': u'Rimuovo commenti inutili'
    },
    'replacements': [
        (u"<!--(.*)-->", ur""),
    ],
    'exceptions': {
        'inside-tags': [
            'hyperlink',
            'link',
        ],
    }
}
