# -*- coding: utf-8  -*-

# TASK: Fix accents in words ending with "che"
# USE: python replace.py -log -xml:itwiki-latest-pages-articles.xml -namespace:0 -fix:che -pt:60
# STAT: beta

fixes['che'] = {
    'regex': True,
    'msg': {
        'it':u'Correggo accenti'
    },
    'replacements': [
        (u'\\b([Aa])bbenchè\\b', ur'\1bbenché'),
        (u'\\b([aA])cciocchè\\b', ur'\1cciocché'),
        (u'\\b([aA])ffinchè\\b', ur'\1ffinché'),
        (u'\\b([aA])lcunchè\\b', ur'\1lcunché'),
        (u'\\b([aA])llorchè\\b', ur'\1llorché'),
        (u'\\b([aA])ltrochè\\b', ur'\1ltroché'),
        (u'\\b([aA])ncorchè\\b', ur'\1ncorché'),
        (u'\\b([aA])nzichè\\b', ur'\1nziché'),
        (u'\\b([aA])ttesochè\\b', ur'\1ttesoché'),
        (u'\\b([aA])vvegnachè\\b', ur'\1vvegnaché'),
        #fd
        (u"\\b([aA])vvegnadiochè\\b", ur"\1vvegnadioché"),
        #fd
        (u"\\b([aA])vvengachè\\b", ur"\1vvengaché"),
        #fd
        (u"\\b([aA])vvengadiochè\\b", ur"\1vvengadioché"),
        (u'\\b([bB])enchè\\b', ur'\1enché'),
        (u'\\b([cC])hecchè\\b', ur'\1hecché'),
        #fd
        (u"\\b([cC])iocchè\\b", ur"\1iocché"),
        (u'\\b([cC])omecchè\\b', ur'\1omecché'),
        #fd
        (u"\\b([cC])onciofossechè\\b", ur"\1onciofosseché"),
        (u'\\b([cC])ontuttochè\\b', ur'\1ontuttoché'),
        (u'\\b([cC])osicchè\\b', ur'\1osicché'),
        (u'\\b([cC])otalchè\\b', ur'\1otalché'),
        (u'\\b([dD])acchè\\b', ur'\1acché'),
        (u'\\b([dD])appoichè\\b', ur'\1appoiché'),
        (u'\\b([dD])imodochè\\b', ur'\1imodoché'),
        #fd
        (u"\\b([dD])opochè\\b", ur"\1opoché"),
        #fd
        (u"\\b([dD])opodichè\\b", ur"\1opodiché"),
        (u'\\b([eE])ssendochè\\b', ur'\1ssendoché'),
        (u'\\b([fF])inattantochè\\b', ur'\1inattantoché'),
        (u'\\b([fF])inchè\\b', ur'\1inché'),
        (u'\\b([fF])intantochè\\b', ur'\1intantoché'),
        #fd
        (u"\\b([fF])inacchè\\b", ur"\1inacché"),
        (u"\\b([fF])inattantochè\\b", ur"\1inattantoché"),
        (u'\\b([fF])uorchè\\b', ur'\1uorché'),
        (u'\\b(?<!orgio )([gG])iacchè\\b', ur'\1iacché'), # Piergiorgio Giacchè
        (u'\\b([gG])ranchè\\b', ur'\1ranché'),
        #fd
        (u"\\b([gG])iafossechè\\b", ur"\1iafosseché"),
        #fd
        (u"\\b([gG])iafossecosachè\\b", ur"\1iafossecosaché"),
        #fd
        (u"\\b([iI])nfinattantochè\\b", ur"\1nfinattantoché"),
        (u'\\b([lL])orchè\\b', ur'\1orché'),
        #fd
        (u"\\b([iI])nquantochè\\b", ur"\1nquantoché"),
        (u'\\b([mM])acchè\\b', ur'\1acché'),
        (u'\\b([nN])onchè\\b', ur'\1onché'),
        #fd
        (u"\\b([nN])onsochè\\b", ur"\1onsoché"),
        (u'\\b([oO])ltrechè\\b', ur'\1ltreché'),
        #fd
        (u"\\b([oO])ndechè\\b", ur"\1ndeché"),
        (u'\\b([pP])erchè\\b', ur'\1erché'),
        (u'\\b([pP])erciocchè\\b', ur'\1erciocché'),
        (u'\\b([pP])erlochè\\b', ur'\1erloché'),
        (u'\\b([pP])erocchè\\b', ur'\1erocché'),
        (u'\\b([pP])oichè\\b', ur'\1oiché'),
        #fd
        (u"\\b([pP])osciachè\\b", ur"\1osciaché"),
        (u'\\b([pP])ressochè\\b', ur'\1ressoché'),
        (u'\\b([pP])urchè\\b', ur'\1urché'),
        #fd
        (u"\\b([qQ])uantochè\\b", ur"\1uantoché"),
        #fd
        (u"\\b([qQ])uasichè\\b", ur"\1uasiché"),
        #fd
        (u"\\b([sS])econdochè\\b", ur"\1econdoché"),
        (u'\\b([sS])ennonchè\\b', ur'\1ennonché'),
        (u'\\b([sS])enonchè\\b', ur'\1enonché'),
        (u'\\b([sS])icchè\\b', ur'\1icché'),
        (u'\\b([sS])inattantochè\\b', ur'\1inattantoché'),
        (u'\\b([sS])inchè\\b', ur'\1inché'),
        (u'\\b([sS])intantochè\\b', ur'\1intantoché'),
        (u"\\b([sS])tantechè\\b", ur"\1tanteché"),
        (u'\\b([tT])alchè\\b', ur'\1alché'),
        #fd
        (u"\\b([tT])almentechè\\b", ur"\1almenteché"),
        (u'\\b([tT])antochè\\b', ur'\1antoché'),
        #fd
        (u"\\b([tT])rannechè\\b", ur"\1ranneché"),
        (u'\\b([tT])uttochè\\b', ur'\1uttoché'),
        (u'\\b([nN])è\\b', ur'\1é'),
    ]
}
