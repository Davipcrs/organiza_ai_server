su - postgres /var/lib/pgsql CREATE USER $DATABASE_USER WITH ENCRYPTED PASSWORD $DATABASE_PWD; 
su - postgres /var/lib/pgsql GRANT ALL PRIVILEGES ON DATABASE organiza_ai TO $DATABASE_USER;



python main.py