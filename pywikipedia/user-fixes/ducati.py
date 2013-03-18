# -*- coding: utf-8  -*-

# TASK: Fix names of Dacati (Dukes)
# USE: python replace.py -log -xml:itwiki-latest-pages-articles.xml -namespace:0 -fix:ducati -pt:60
# STAT: alpha

fixes['ducati'] = {
    'regex': True,
    'msg': {
        'it': u'Correggo nomi dei ducati'
    },
    'replacements': [
        # Granducati Italiani in ordine alfabetico
        (u"\\b[Gg]ran[ _-]{0,1,2}[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Tt]oscana", u"Granducato di Toscana"),
        (u"\\b[Gg]ran[ _-]{0,1,2}[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ll]ucca", u"Granducato di Lucca"),
        # Ducati Italiani in ordine alfabetico
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd][’`' _]{1,2}[Aa]osta", u"Ducato d'Aosta"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Aa]malfi", u"Ducato di Amalfi"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Aa]sti", u"Ducato di Asti"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Bb]enevento", u"Ducato di Benevento"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Bb]ergamo", u"Ducato di Bergamo"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Bb]rescia", u"Ducato di Brescia"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Cc]amerino", u"Ducato di Camerino"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Cc]astro", u"Ducato di Castro"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Cc]eneda", u"Ducato di Ceneda"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ff]irenze", u"Ducato di Firenze"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]el[ _-]{1,2}[Ff]riuli", ur"Ducato del Friuli"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ff]errara", u"Ducato di Ferrara"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Gg]aeta", u"Ducato di Gaeta"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Gg]uastalla", u"Ducato di Guastalla"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ii]vrea", u"Ducato di Ivrea"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ll]ucca", u"Ducato di Lucca"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Mm]antova", u"Ducato di Mantova"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Mm]assa", u"Ducato di Massa"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Mm]ilano", u"Ducato di Milano"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Mm]irandola", u"Ducato di Mirandola"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Mm]odena", u"Ducato di Modena"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]el[ _-]{1,2}[Mm]onferrato", ur"Ducato del Monferrato"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Nn]apoli", u"Ducato di Napoli"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Pp]arma", u"Ducato di Parma"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Pp]avia", u"Ducato di Pavia"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Pp]ersiceto", u"Ducato di Persiceto"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Pp]iacenza", u"Ducato di Piacenza"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Pp]uglia[ _-]{1,2}[Ee][ _-]{1,2}[Dd]i[ _-]{1,2}[Cc]alabria", u"Ducato di Puglia e di Calabria"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Rr]eggio", u"Ducato di Reggio"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ss]an[ _-]{1,2}[Gg]iulio", u"Ducato di San Giulio"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ss]abbioneta", u"Ducato di Sabbioneta"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ss]avoia", u"Ducato di Savoia"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ss]ora", u"Ducato di Sora"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ss]orrento", u"Ducato di Sorrento"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ss]poleto", u"Ducato di Spoleto"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Tt]orino", u"Ducato di Torino"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Tt]rento", u"Ducato di Trento"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Tt]reviso", u"Ducato di Treviso"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Tt]uscia", u"Ducato di Tuscia"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Uu]rbino", u"Ducato di Urbino"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Vv]enezia", u"Ducato di Venezia"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Vv]erona", u"Ducato di Verona"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Vv]icenza", u"Ducato di Vicenza"),
        # Granducati Tedeschi in ordine alfabetico
        (u"\\b[Gg]ran[ _-]{0,1,2}[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ss]assonia[ _-][Ww]eimar[ _-][Ee]isenach", u"Granducato di Sassonia-Weimar-Eisenach"),
        # Ducati Tedeschi in ordine alfabetico
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd][’`' _]{1,2}[Aa]ustria", u"Ducato d'Austria"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Bb]aviera", u"Ducato di Baviera"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Bb]ar", u"Ducato di Bar"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Bb]oemia", u"Ducato di Boemia"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Bb]rabante", u"Ducato di Brabante"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ff]ranconia", u"Ducato di Franconia"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ll]orena", u"Ducato di Lorena"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Pp]omerania", u"Ducato di Pomerania"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ss]assonia", u"Ducato di Sassonia"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Ss]vevia", u"Ducato di Svevia"),
        (u"\\b[Dd]ucato[ _-]{1,2}[Dd]i[ _-]{1,2}[Vv]estfalia", u"Ducato di Vestfalia"),

        (u'([a-zA-Z]|[,:;!?]|\.\.\.|…)[ ]{2,3}([a-zA-Z]|[,:;!?]|\.\.\.|…)', ur'\1 \2'), #Correggo spazi doppi e tripli
    ],
    'exceptions': {
        'inside-tags': [
            'hyperlink',
            'link',
        ],
        'inside': [
            r'{{interprogetto|.*}}',
            r'[Ii]mmagine[ ]*=[ ]*(.*)\.[gif|jpg|png|svg]',
            r'[Ll]inkBandiera[ ]*=[ ]*(.*)\.[gif|jpg|png|svg]',
            r'[Pp]aginaBandiera[ ]*=[ ]*(.*)',
            r"\*[ ]?(.*)''(.*)''(.*)",
            r'[Image|File|Immagine]:.*\.[gif|jpg|png|svg]', #Images
        ],
    }
}
