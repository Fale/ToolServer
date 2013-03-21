#!/bin/bash
#
#A wrapper-script for the Punteggiatura rules.
#$ -l h_rt=23:00:00
#$ -l virtual_free=100M
#$ -l arch=*
#$ -l fs-user-store=1

NDATE=$(date +"%Y%m%d")
NTIME=$(date +"%H%M")

mkdir -p /home/fale/lists/$NDATE

/usr/bin/python $HOME/pywikipedia/replace.py -xml:/mnt/user-store/dumps/itwiki-latest-pages-articles.xml -ns:0 -fix:punteggiatura -pt:60 -savenew:/home/fale/lists/$NDATE/punteggiatura-$NTIME.log -always
 
#EOF