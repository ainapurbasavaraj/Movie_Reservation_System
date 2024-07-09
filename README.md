# Movie_Reservation_System

Architecture diagram : https://b6f7.short.gy/Yt7zAn

Idempotancy : https://medium.com/@saurav200892/how-to-achieve-idempotency-in-post-method-d88d7b08fcdd

Rest principles : https://github.com/ainapurbasavaraj/REST-Priniciples

REST methods : https://www.restapitutorial.com/lessons/httpmethods.html

flask : https://flask.palletsprojects.com/en/2.3.x/deploying/

AWS instance login details : 
chmod 400 "Basavanagar-key.pem"
ssh -i "Basavanagar-key.pem" ubuntu@ec2-18-204-203-169.compute-1.amazonaws.com
AWS account id : 165178850723
users : basavaraj,girish


postgresql configurations : /opt/homebrew//var/postgresql@16/postgresql.conf
postgresql : allow remote connections
https://blog.devart.com/configure-postgresql-to-allow-remote-connection.html
Adding trust : https://stackoverflow.com/questions/55038942/fatal-password-authentication-failed-for-user-postgres-postgresql-11-with-pg
To connect to remote server : psql -h 34.227.8.22 -p 5432 -U postgres

