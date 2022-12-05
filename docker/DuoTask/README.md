# Duo Task

This is a basic Flask application that serves a simple static website that returns the machine's hostname.

It is directly accessible on port `5500`.

Set the environment variable `YOUR_NAME` to your name to have the app display your name in its welcome message. Otherwise, it will refer to you as "friend".

The `nginx.conf` file can be used to configure an NGINX container to run as a reverse proxy to the Flask app container, effectively making the Flask application accessible on port `80`. You will need to know how to configure networks in Docker in order to achieve this.


# from QA
You should currently be able to:

    Containerise the Flask application in this repository
        You will have to write a Dockerfile to build the image - a Dockerfile template has been provided for you
    Create a network and connect the Flask app container to it.

You can try to:

    Create an NGINX container to and connect it to the network:
        You will need to either bind mount the nginx.conf file to /etc/nginx/nginx.conf on the container, or create a custom NGINX image which copys the file there instead.
