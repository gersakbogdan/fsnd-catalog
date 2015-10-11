apt-get -qqy update
apt-get -qqy install git
apt-get -qqy install postgresql python-psycopg2
apt-get -qqy install python-flask python-sqlalchemy
apt-get -qqy install python-pip
apt-get -qqy install python-dev
apt-get -qqy install libjpeg-dev
apt-get -qqy install zlib1g-dev
pip install bleach
pip install oauth2client
pip install requests
pip install httplib2
pip install networkx
pip install virtualenv
su postgres -c 'createuser -dRS vagrant'
su vagrant -c 'createdb'
su vagrant -c 'createdb forum'
su vagrant -c 'psql forum -f /vagrant/forum/forum.sql'

vagrantTip="[35m[1mThe shared directory is located at /vagrant\nTo access your shared files: cd /vagrant(B[m"
echo -e $vagrantTip > /etc/motd
