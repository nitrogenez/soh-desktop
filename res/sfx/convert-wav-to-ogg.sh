#!/bin/bash

# it just works it just works overpriced open worlds
# use it if you forgot to convert audio.

for i in *.wav; do
	j=$(echo -n $i | sed -e 's/.wav/.ogg/g')
	echo -e "[ \e[36mCONVERTER\e[m ] : Converting:\n	- \e[1;36m$i\e[m\n	to\n	- \e[1;36m$j\e[m"
	ffmpeg -y -i "$i" -strict -2 -acodec vorbis -ac 2 -aq 50 "$j"
done
# EOF
