Title: Hacking on Kratos
Date: 2012-07-08 07:13:00
Status: draft

I'm trying to understand how it actually for someone to get into some new 
technology given any very little guidance and info they have on that particilar 
subject. We have this issue now at work where new hires keep failing getting up 
to speed after their first few months citing the technologies we used as their 
main problem.

So I decided to try something new myself, to see how far I can get into it.  
Finding which project to work on, I decided on [Kratos][1], project from [Sinar 
Project][2] to track Malaysian Member of Parliament.

First problem encountered was with curl SSL cert. Trying several workaround in 
this [stackoverflow question][3], upgrading my rvm seem to work.

    Gem::Installer::ExtensionBuildError: ERROR: Failed to build gem native 
    extension.

            /home/kamal/.rvm/rubies/ruby-1.9.3-p0/bin/ruby extconf.rb 
    checking for pg_config... no
    No pg_config... trying anyway. If building fails, please try again with
     --with-pg-config=/path/to/pg_config
    checking for libpq-fe.h... no
    Can't find the 'libpq-fe.h header
    *** extconf.rb failed ***
    Could not create Makefile due to some reason, probably lack of
    necessary libraries and/or headers.  Check the mkmf.log file for more
    details.  You may need configuration options.

    sudo apt-get install libpq-dev  

Next problem, sqlite3:-

    Gem::Installer::ExtensionBuildError: ERROR: Failed to build gem native extension.

            /home/kamal/.rvm/rubies/ruby-1.9.3-p0/bin/ruby extconf.rb 
    checking for sqlite3.h... no
    sqlite3.h is missing. Try 'port install sqlite3 +universal'
    or 'yum install sqlite-devel' and check your shared library search path (the
    location where your sqlite3 shared library is located).
    *** extconf.rb failed ***

sudo apt-get install libsqlite3-dev


[1]:https://github.com/Sinar/Kratos/
[2]:ahttp://sinarproject.org/
[3]:http://stackoverflow.com/questions/6414232/curl-certificate-error-when-using-rvm-to-install-ruby-1-9-2
