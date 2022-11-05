Setup in Production:

0.Switch media files from racine/app/static/media to racine/static/media
1.Create new user by cmd: adduser username sudo
2.Activate virtualenv by cmd: source /home/udoms/env/md/bin/activate
3.Go to project main directory by cmd: cd ........./.........
4.Restart NGINX web server by cmd: sudo /etc/init.d/nginx restart
5.Run web server interface by cmd: sudo uwsgi --ini microdomains_uwsgi.ini
6.Change max upload size at : /etc/nginx/sites-available/_nginx.conf