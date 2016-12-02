# aqua

Installation for Debian:

    Install dependencies -
        "apt update"
        "apt dist-upgrade"
        "apt install dselect"
        "dselect update"
        "dpkg --set-selections < configs/Package.list"
        "apt deslect-upgrade -y"

    Install netdata -
        "git clone https://github.com/firehol/netdata"
        "./netdata-installer.sh"

    The aqua plugin must be moved into netdata's python plugin folder - 
        "cp scripts/aqua.chart.py /usr/libexec/netdata/python.d/"
    
    Now lets set up apache - 
        "cp /apache/run.conf /etc/apache2/sites-available/"
        "a2dissite 000-default"
        "a2ensite run"
        "service apache2 reload"

    Move configs to correct locations - 
        "cp configs/interfaces      /etc/network/interfaces"
        "cp configs/dhcpd.conf      /etc/dhcp/dhcpd.conf"
        "cp configs/fstab           /etc/fstab"
        "cp configs/hostapd.conf    /etc/hostapd/hostapd.conf"
        "cp configs/isc-dhcp-server /etc/default/isc-dhcp-server"
        "cp configs/sysctl.conf     /etc/sysctl.conf"

    To have data transmitted to the server - 
        "./scripts/transceiver.py"

    Final Touches -
        You should now be able to access the server via its local IP
        The getIP() function has only been tested if the the host is connected to the network over "wlan0"
        If you are having issues, goto line 31 of server.py and set the ip yourself
