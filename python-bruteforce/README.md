# Bruteforcing web app login with Python

Some login applications are still prone to brute force attacks with the lack of any protections and mitigations in place. With that, a malicious actor can utilize any tool or language to perform a bruteforce attack for a working combination of a username + password. 

For this demonstration we will build and utilize Python to script and perform this attack on a local web application.

## Getting Started

Pull public container used in lab 
``` docker pull sjusata/demos:python-bruteforce ```

Run container on your local machine to run on port 8080
``` docker run --name bruteforce-test -it -d -p 8080:8080 python-bruteforce:latest ```

Now start building your attack script(s)! 