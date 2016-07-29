#!/bin/bash

# Installing dependencies
apt update
apt install -y python3 python3-flask zlib1g-dev uuid-dev gcc make git autoconf autogen
apt install -y automake pkg-config ipython3 apache2 libapache2-mod-wsgi-py3 sed 

# Installing netdata
cd ~
git clone https://github.com/firehol/netdata
netdata/netdata-installer.sh

# Running netdata
/usr/sbin/netdata

# Making sure it runs at every boot
sed -i '13i/usr/sbin/netdata' /etc/rc.local

# Setting up config files
cp ~/aqua/scripts/*.plugin /usr/libexec/netdata/plugins.d/
cp ~/aqua/apache/run.conf /etc/apache2/sites-available/

# Setting up apache
a2dissite 000-default
a2ensite run
service apache2 reload
