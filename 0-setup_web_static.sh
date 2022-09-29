#!/usr/bin/env bash
### Installs nginx, configures content serving to hbnb_static
### Creates /data/ directories + symlink, index.html page
### Assigns ownership rights of /data/ recursively to ubuntu user + group

new_string="location \/hbnb_static {\n alias \/data\/web_static\/current\/;"

apt-get update -y
apt-get install nginx -y
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i -E "s/^[^#]+location \/ \{/$new_string/" /etc/nginx/sites-available/default
service nginx reload
service nginx restart
