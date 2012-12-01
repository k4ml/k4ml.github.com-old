Title: Webdev Pattern - Shortcircuit
Date: 2012-11-11 03:13:00
Category: Webdev Pattern
Status: Draft

This will be the first installment to what I hope a series of common pattern 
used in web development.

In web development, we always in client-server model where we have the website 
on the server and a client (most of the time will be a web browser) accessing 
the website on the server. The browser will ask the server for a page it need 
(a Resource in REST speak) and the server will return a Response. While on 
development this might just happened on our local computer or laptop but it 
still client-server model nonetheless. So in short, one of most frequent thing 
we did in web development is entering url in the browser address bar to access 
our website for testing.

As I said earlier, we mostly did development on our local computer or laptop 
and to access the website on our local machine, usually we will use a loopback 
address in form of `http://127.0.0.1/` or `http://localhost/` or anything like 
that. But there's a case that we want to fully simulate how the website will be 
accessed by real users on the live server. For example let say the website is 
at `http://www.mywebsite.com/`. Now when testing, we will access the website in 
development on our local machine using url `http://127.0.0.1/`. Not really nice 
and in some cases, not desirable at all.

Since domain name is just a mapping from a name (that we can easiliy memorise) 
to an IP address handled by DNS servers sitting at every corner of this world 
we can actually provide the mapping that we want. So we want that when we type 
`http://www.mywebsite.com/` on our laptop, it will retrieve the website sitting 
in our laptop instead of the one on live server. Every network stack on 
operating system (at least that we commonly used) has what it called a host 
file which simply a text file that map a name to an IP address. On Unix/Linux 
system this will be at `/etc/hosts` while on Windows, the location a bit 
obscure but you can easily search for it using the Explorer. It should be 
somewhere in your `C:\Windows\` folder. By default it maybe called `hosts.sam` 
which mean it's not used yet and you have to rename it to remove the '`.sam`' 
extension.

Once you have that file in place, the mapping is simply:-

    localhost           127.0.0.1
    www.mywebsite.com   127.0.0.1
    othersite.com       127.0.0.1
    myexample.net       192.168.0.5

All the network stack will look into this file first before querying DNS server 
in order to resolve the domain name. The IP address can be any IP that you want 
the domain pointing to. This is why I call this a short-circuit. Instead of the 
usual hop of going from `your machine => ISP DNS server => Another DNS Server` 
to get what is the IP address, it goes straight to the hosts file on the same 
machine.
