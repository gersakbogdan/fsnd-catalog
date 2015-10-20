apt-get -qqy update
apt-get -qqy install git
apt-get -qqy install postgresql
apt-get -qqy install python-psycopg2
apt-get -qqy install python-flask
apt-get -qqy install python-sqlalchemy
apt-get -qqy install python-pip
apt-get -qqy install python-dev
apt-get -qqy install libjpeg-dev
apt-get -qqy install zlib1g-dev

pip install virtualenv

vagrantTip="[35m[1mThe shared directory is located at /vagrant\nTo access your shared files: cd /vagrant(B[m"
echo -e $vagrantTip > /etc/motd
