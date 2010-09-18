#!/bin/bash

if [ -z $1 ]; then
    echo "No title"
    exit 1
fi

DATE_META=`date`
TITLE=$1
TPL=$( cat <<EOL
---
layout: post
title: $TITLE
---

{{ page.title }}
================

<p class="meta">$DATE_META</p>
EOL)

POST=_posts/`date +"%Y-%m-%d"`-"$TITLE".md
echo "$TPL" > $POST && vim $POST
