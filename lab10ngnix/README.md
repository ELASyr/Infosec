Lab 10 — NGINX proxy_pass

Description
-----------
In this lab I created a small Flask API that listens on port 5000.
Nginx is configured to listen on port 8000 and forward requests to the API using the proxy_pass directive.
This hides the API’s internal port and allows Nginx to handle incoming traffic, logging, and potential security rules.
A transient 502 Bad Gateway earlier occurred because nginx tried to proxy while the backend was not yet running — restarting the backend and reloading nginx resolved it.


