# -*- coding: utf-8  -*-

# TASK: Fix Italian region names
# USE: python replace.py -log -xml:itwiki-latest-pages-articles.xml -namespace:0 -fix:regioni -pt:60
# TODO: simplify regex
# STAT: beta

fixes['regioni'] = {
    'regex': True,
    'msg': {
        'it': u'Correggo nomi dei ducati'
    },
    'replacements': [
        # Granducati Italiani in ordine alfabetico
        (u"[Gg]ran[ _-]{0,1,2}[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Tt]oscana", u"Granducato di Toscana"),
        # Ducati Italiani in ordine alfabetico
        (u"[Dd]ucato[ _-]{1,2}[Dd][’`' _]{1,2}[Aa]osta", u"Ducato d'Aosta"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Aa]malfi", u"Ducato di Amalfi"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Aa]sti", u"Ducato di Asti"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Bb]enevento", u"Ducato di Benevento"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Bb]ergamo", u"Ducato di Bergamo"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Bb]rescia", u"Ducato di Brescia"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Cc]amerino", u"Ducato di Camerino"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Cc]astro", u"Ducato di Castro"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Cc]eneda", u"Ducato di Ceneda"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ff]irenze", u"Ducato di Firenze"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]el[ _-]{1,2}[Ff]riuli", ur"Ducato del Friuli"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ff]errara", u"Ducato di Ferrara"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Gg]aeta", u"Ducato di Gaeta"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Gg]uastalla", u"Ducato di Guastalla"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ii]vrea", u"Ducato di Ivrea"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ll]ucca", u"Ducato di Lucca"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Mm]antova", u"Ducato di Mantova"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Mm]assa", u"Ducato di Massa"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Mm]ilano", u"Ducato di Milano"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Mm]irandola", u"Ducato di Mirandola"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Mm]odena", u"Ducato di Modena"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]el[ _-]{1,2}[Mm]onferrato", ur"Ducato del Monferrato"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Nn]apoli", u"Ducato di Napoli"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Pp]arma", u"Ducato di Parma"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Pp]avia", u"Ducato di Pavia"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Pp]ersiceto", u"Ducato di Persiceto"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Pp]iacenza", u"Ducato di Piacenza"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Pp]uglia[ _-]{1,2}[Ee][ _-]{1,2}[Dd]i[ _-]{1,2}[Cc]alabria", u"Ducato di Puglia e di Calabria"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Rr]eggio", u"Ducato di Reggio"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ss]an[ _-]{1,2}[Gg]iulio", u"Ducato di San Giulio"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ss]abbioneta", u"Ducato di Sabbioneta"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ss]avoia", u"Ducato di Savoia"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ss]ora", u"Ducato di Sora"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ss]orrento", u"Ducato di Sorrento"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ss]poleto", u"Ducato di Spoleto"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Tt]orino", u"Ducato di Torino"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Tt]rento", u"Ducato di Trento"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Tt]reviso", u"Ducato di Treviso"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Tt]uscia", u"Ducato di Tuscia"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Uu]rbino", u"Ducato di Urbino"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Vv]enezia", u"Ducato di Venezia"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Vv]erona", u"Ducato di Verona"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Vv]icenza", u"Ducato di Vicenza"),
        # Ducati Tedeschi in ordine alfabetico
        (u"[Dd]ucato[ _-]{1,2}[Dd][’`' _]{1,2}[Aa]ustria", u"Ducato d'Austria"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Bb]aviera", u"Ducato di Baviera"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Bb]ar", u"Ducato di Bar"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Bb]oemia", u"Ducato di Boemia"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Bb]rabante", u"Ducato di Brabante"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ff]ranconia", u"Ducato di Franconia"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ll]orena", u"Ducato di Lorena"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Pp]omerania", u"Ducato di Pomerania"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ss]assonia", u"Ducato di Sassonia"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ss]vevia", u"Ducato di Svevia"),
        (u"[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Vv]estfalia", u"Ducato di Vestfalia"),

    ],
    'exceptions': {
        'inside-tags': [
            'hyperlink',
            'link',
        ],
        'inside': [
            r'{{interprogetto|.*}}',
        ],
    }
}
