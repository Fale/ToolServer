#!/bin/sh

qcronsub -N regioni $HOME/ToolServer/sge/wrapper/regioni.sh
qcronsub -N ducati $HOME/ToolServer/sge/wrapper/ducati.sh
qcronsub -N si $HOME/ToolServer/sge/wrapper/si.sh
qcronsub -N spazi $HOME/ToolServer/sge/wrapper/spazi.sh
qcronsub -N passati $HOME/ToolServer/sge/wrapper/passati.sh
