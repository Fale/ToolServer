#!/bin/bash
#
#A wrapper-script for the SI rules.
#$ -l h_rt=12:00:00
#$ -l virtual_free=100M
#$ -l arch=*
#$ -l fs-user-store=1

/usr/bin/python $HOME/pywikipedia/replace.py -xml:/mnt/user-store/dumps/itwiki-latest-pages-articles.xml -ns:0 -fix:si -pt:60 -savenew:/home/fale/si.log -always
 
#EOF
