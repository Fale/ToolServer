#!/bin/sh

CURRENT=$(readlink -f /mnt/user-store/dumps/itwiki-latest-pages-articles.xml)
LAST=$(readlink -f $HOME/lists/itwiki-last-known.xml)

if [ $CURRENT != $LAST ]; then
    ln -s $CURRENT $HOME/lists/itwiki-last-known.xml
    # Execute the scripts needed
fi
