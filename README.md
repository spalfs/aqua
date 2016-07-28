# aqua

Installation for Debian:

    Install dependencies -
        "su"
        "apt install python3-flask zlib1g-dev uuid-dev gcc make git autoconf autogen automake pkg-config ipython3 apache2 libapache2-mod-wsgi-py3" 
        "exit"

    Install netdata -
        "su"
        "git clone https://github.com/firehol/netdata"
        "cd netdata"
        "./netdata-installer.sh"
        Enter
        "exit"

    Then run it (if it is not already running)-
        "su"
        "/usr/sbin/netdata"
        "exit"
    
    Or if you want it to run at every boot - 
        "su"
        "nano /etc/rc.local"
        Append "/usr/sbin/netdata" before the exit
        Ctrl-X, Y, Enter
        "exit"

    The python plugins must be moved into netdata's plugin folder - 
    	"su"
        "cp *.plugin /usr/libexec/netdata/plugins.d/"
        "exit"
    
    Now lets set up apache - 
        "cp /apache/run.conf /etc/apache2/sites-available/"
        "a2dissite 000-default"
        "a2ensite run"
        "service apache2 reload"
    
    Final Touches -
        Get local ip
        "ifconfig | grep inet"
        Replace line 15 from templates/*.html to your local ip
        "...src=XXX.XXX.XXX.XXX:19999/dashboard.js"
        Now access within your network with your local ip through the browser :)

    THINGS TO DO - 
        Look into new netdata python plugin system and reimplement ours
        Arduino .ino
        Look if local dns server is worth doing
        Python script to read from usb, write to database, and pipe to netdata (started with .wsgi, server, or rc.local)
        Add matplotlib image generator to server
        Look into making the host a wifi connectable switch
