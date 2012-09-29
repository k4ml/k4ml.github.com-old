Title: Android: Phonegap with existing sqlite database
Date: 2012-09-30

Just started my journey into android development and one thing I quickly found 
along the way is that shipping existing sqlite database with your phonegap app 
is non-trivial. Not sure this is problem with android directly or just 
phonegap. While you can put the sqlite database in your `assets/` directory, 
phonegap apparently try to read the database from other fix location on the 
phone. Failing to read that, it will create new empty database.

There's workaround scattered in blogpost and mailing-list posts and I finally 
managed to get it working after hours of hunting and try and error session. If 
you search around you probably end up on some of these sites:-

* 
<http://www.raymondcamden.com/index.cfm/2012/7/27/Guest-Blog-Post-Shipping-a-populated-SQLite-DB-with-PhoneGap>
* <http://www.corporatezen.com/shipping_prepopulated_database_with_phonegap>
* <http://gauravstomar.blogspot.ca/2011/08/prepopulate-sqlite-in-phonegap.html>

The fix involved few steps:-

* You have to move the sqlite database file to location that phonegap expected. 
Have to write some java for this but luckily the code we found on those site 
still working on latest phonegap release.
* The built-in sqlite driver (if I can call it as such) does not support 
reading from existing sqlite database so we have to use 3rd party sqlite 
plugin.
* The 3rd party sqlite plugin turn out to have issue with android < 2.3.3 and 
since I plan to also include support for froyo based phone, I have to fix this 
too.

You can get the code to move the db from this [gist][2].

Next grab the sqlite plugin from 
<https://github.com/chbrody/Cordova-SQLitePlugin> and copy the folder under 
`Android/src` to our `src/` directory. Then we have to tell phonegap about this 
plugin by editing `res/xml/config.xml` and include the following line:-

    <plugin name="SQLitePlugin" 
    value="com.phonegap.plugin.sqlitePlugin.SQLitePlugin"/>

Finally we have to remove some lines from 
`src/com/phonegap/plugin/sqlitePlugin.java`. The dev already marked the files 
to be deleted so we just need to find and remove it. You can see the [diff][1] 
from my app repo. To open the database from our app code, make sure to omit the 
.db extension since phonegap seem to automatically append that to db name.

You can also clone [my app on github][3] which has (hopefully) everything in 
place and you just need to load it into your Eclipse project.


[1]:https://github.com/k4ml/halal-android/commit/f6bbf52a5504367a0e5aaeae8b8ea24068403f4a#src/com/phonegap/plugin/sqlitePlugin/SQLitePlugin.java
[2]:https://gist.github.com/3805152
[3]:https://github.com/k4ml/halal-android
