Title: On Python Namespace and PIL vs Pillow
Date: 2012-12-03 06:30:00
Category: Python

All python dev know Zen of python, when you type import this at python
console. One of the Zen say:-

> Namespaces are one honking great idea -- let's do more of those!

Namespace is great. It allow you to keep your stuff separate from others.
While namespace such a great thing, you'll surprise that some packages in
Python does not embrace it very well. PIL for example is quite an important
package. The official documentation however does not advertise `PIL` as it
top level namespace. Instead every individual module is imported directly.

This does not pose much problem back then but with people start using
virtualenv to isolate their apps and install the package through pip or
easy_install, we start to realize a problem with how PIL was packaged. Folks
at plone repackaged PIL into [Pillow][1] with a premise to make it easy to
install not through system package manager. I've been using Pillow most of
the time these days.

When working on [Booktype openshift quickstart][2], I'd somehow changed the deps in
`setup.py` to Pillow instead of the original PIL along the way. After sorting
out all action hooks script and was about to call it a day, a final test
showed that an image that uploaded not longer listed. Looking at `MEDIA_ROOT`
confirmed the image was successfully uploaded. My initial thought was could be
some issue with my settings since I split some of it into separate file and
not using the default that come with the release tarball. Debugging was so
painful since no exception happened at all and with all the Ajax call, I'm
lost.

After going through all the Ajax calls, I finally found the url to list the
images. Accessing the url through browser immediately revealed the
error. It was an import error when the code want to import `Image` module. It
work fine before when using PIL because PIL also add path to the top level
directory in `site-packages` effectively making all modules underneath it
being exposed as top level namespace. But Pillow on the other hand only
expose PIL as top level namespace so the code break.

While the ideal thing to do is to fix all code so that they're not
importing modules directly, it not always feasible. I'm quite lucky that
PIL compiled successfully on openshift so I don't have to use Pillow. A
lesson to learn is always publish your packages as single top level
namespace and never misused your language flexibility (in this case
extending path through .pth file) to do something 'clever'.

*2012-11-18 17:54*

[1]:http://pypi.python.org/pypi/Pillow
[2]:https://github.com/k4ml/booktype-openshift
