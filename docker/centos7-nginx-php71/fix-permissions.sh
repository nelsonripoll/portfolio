#!/bin/bash
if [[ ! -d "app/tmp" ]]; then
  mkdir app/tmp
  mkdir app/tmp/cache
  mkdir app/tmp/cache/models
  mkdir app/tmp/cache/persistent
  mkdir app/tmp/cache/views
  mkdir app/tmp/sessions
  mkdir app/tmp/tests
fi

if [[ ! -d "app/logs" ]]; then
  mkdir app/logs
fi

sudo chown -R nginx /usr/share/nginx
sudo chgrp -R nginx /usr/share/nginx

sudo chmod -R ug=rwx app/tmp
sudo chmod -R ug=rwx app/logs
