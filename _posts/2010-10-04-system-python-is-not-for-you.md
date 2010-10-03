---
layout: post
title: System python is not for you
---

{{ page.title }}
================

<p class="meta">Mon Oct  4 01:18:09 MYT 2010</p>

If you already did some python development or just getting started, one of the advice you would always get is to never mess with the system python - the python version that come with your distro. For example on Ubuntu or Debian based system, python that was installed by `sudo apt-get install python`. At first I didn't really understand what this mean, why you can't use something that already comes for free ?

The answer to that question is because that version of python actually meant for the distro itself. Most distro would in some place used python, maybe for some configurations script. In Ubuntu, lot of their own applications are written with python. If we upgrade some of the libraries not through the standard package manager, there's a chance it would break these apps. So that's what the python they provided is for. It's for their own use, not us. Once I realized this, I have a feeling that distro should ship the python that they need separately from the python that would be used by the users.

For development purpose, I always run `virtualenv $HOME` to setup virtualenv environment in my home directory. Under Ubuntu, `$HOME/bin` is under `$PATH` so `which python` would always point to `/home/kamal/bin/python` rather than `/usr/bin/python`. This allow me to freely use easy_install and it would install it to my `$HOME/lib/python2.5` instead of system wide lib directory. For something specific like developing a django project, I prefer to use [Buildout][1] to further isolate the environment. More on [Buildout][1] later.

[1]:http://www.buildout.org/
