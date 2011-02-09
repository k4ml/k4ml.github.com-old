---
layout: post
title: Load Django custom filters/tags on all templates
---

{{ page.title }}
==========

<p class="meta">Wed Feb 9 13:39:58 MYT 2011</p>

To load your custom template tags or filters in your template, you use the following:-

<pre>
{% load custom_filters %}
</pre>

In your template files. But this mean doing this in each template files that need to use the filters. You can't even put this in a base template and make it available to any templates that extend the base template. Kind of violating the DRY.

Looking around (google), I found [1] which use `add_to_builtins` function from `django.template`. Digged into Django source code, I found out how it being used to load the default tags and filters:-

<pre>
def add_to_builtins(module):
    builtins.append(import_library(module))

add_to_builtins('django.template.defaulttags')
add_to_builtins('django.template.defaultfilters')
</pre>

That around line 1048 inside `django/template/__init__.py`. So this is how I used it in [kecupuapp_base][2]:-

https://github.com/k4ml/kecupuapp_base/commit/b9c62736ebabffa7e972ca00d6a6a1bace47931b

Along the way, also found out this links:-

http://www.b-list.org/weblog/2007/dec/04/magic-tags/
http://stackoverflow.com/questions/1118183/how-to-debug-in-django-the-good-way/2324210#2324210

[1]:http://d-w.me/blog/2010/2/18/11/
[2]:https://github.com/k4ml/kecupuapp_base
