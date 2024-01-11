apt-get install python3 python3-pip -y
apt-get -y install nginx postgresql 
pip3 install -r ./requirements.txt

su postgres psql
CREATE DATABASE organiza_ai WITH ENCODING 'UTF8' LC_COLLATE='en_US.UTF-8' LC_CTYPE='en_US.UTF-8';
su root
