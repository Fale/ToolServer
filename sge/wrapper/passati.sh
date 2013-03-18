#!/bin/bash
#
#A wrapper-script for the Passati rules.
#$ -l h_rt=23:00:00
#$ -l virtual_free=100M
#$ -l arch=*
#$ -l fs-user-store=1

NDATE=$(date +"%Y%m%d")
NTIME=$(date +"%H%M")

mkdir -p /home/fale/lists/$NDATE

/usr/bin/python $HOME/pywikipedia/replace.py -xml:/mnt/user-store/dumps/itwiki-latest-pages-articles.xml -ns:0 -fix:passati -pt:60 -savenew:/home/fale/lists/$NDATE/passati-$NTIME.log -always
 
#EOF
