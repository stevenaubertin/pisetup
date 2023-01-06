#!/bin/bash

let upSeconds="$(/usr/bin/cut -d. -f1 /proc/uptime)"
let secs=$((${upSeconds}%60))
let mins=$((${upSeconds}/60%60))
let hours=$((${upSeconds}/3600%24))
let days=$((${upSeconds}/86400))
let cpu=$(</sys/class/thermal/thermal_zone0/temp)
let cpufreq=$(</sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq)
ipprivate="$(ifconfig eth0 | grep inet | awk 'NR==1 {print $2}')"
UPTIME=`printf "%d days, %02dh%02dm%02ds" "$days" "$hours" "$mins" "$secs"`

# get the load averages
read one five fifteen rest < /proc/loadavg

echo "$(tput setaf 2)
   .~~.   .~~.    `date +"%A, %e %B %Y, %r"`
  '. \ ' ' / .'   `uname -srmo`$(tput setaf 1)
   .~ .~~~..~.    
  : .~.'~'.~. :   Uptime.............: ${UPTIME}
 ~ (   ) (   ) ~  Memory.............: `cat /proc/meminfo | grep MemFree | awk {'print $2'}`kB (Free) / `cat /proc/meminfo | grep MemTotal | awk {'print $2'}`kB (Total)
( : '~'.~.'~' : ) Free Space.........: `df | grep root | awk '{print $5}'`
 ~ .~ ( ${ipprivate: -1} ) ~. ~  CPU................: $((cpu/1000))'C (TMP) $((cpufreq/1000))Mhz (FREQ)
  (  : '~' :  )   Load Averages......: ${one}, ${five}, ${fifteen} (1, 5, 15 min)
   '~ .~~~. ~'    IP Addresses.......: ${ipprivate} (Private) `wget -q -O - http://icanhazip.com/ | tail` (Public)
       '~'        Containers.........: `docker container ls | awk '{print $2}' | grep -v ID`
$(tput sgr0)"
