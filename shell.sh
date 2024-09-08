#! /bin/bash
read -p $'(\033[0;31mchero\033[0m)-\033[0;32m~\033[0m' cmd
echo "./$cmd">cmd.sh
cd 
cd chero
cd bin
bash cmd.sh
cd chero
cd home
bash wh.sh