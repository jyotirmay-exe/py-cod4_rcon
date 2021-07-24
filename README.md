
<h1>Simple CLI RCON Tool for Call of Duty 4 Servers</h1>
  

This is a command-line interface to communicate with a CoD4 server's RCON without even having access to the server's dedicated console or the linux terminal. The program creates a socket object with IPv4 and UDP connection (`socket.AF_INET & socket.SOCK_DGRAM`) to initialize the connection. All you have to do is run the script, put in your connection details and the rcon password and your are good to go!



<h1>Prerequisites</h1>

  

Your computer needs to have the following:<br>

1.  &nbsp;[Python 3]("https://python.org") (made with Python 3.9.1)

2.  &nbsp;pip (used pip 21.1.2 at the time of making this project)

3.  &nbsp;Open ports in your firewall to allow incoming and outgoing packets



<h1>How to use it?</h1>

First off you need to install a package called ```stdiomask``` which masks your input password during the runtime... Just in case :)
To install it, open your terminal and type in:
```
python -m pip install --upgrade pip
python -m pip install stdiomask
```
Rest all modules used are included in <b>The Python Standard Library.</b>

Now clone this repo:
`git clone https://github.com/jyotirmay-exe/py-cod4_rcon.git`

Execute the script:
`python run.py`

If the ip:port combination and the rcon password are correct, you should be able to type in the rcon commands just like you do in-game or in the dedicated console, and the respective responses from the server will be displayed in the terminal. You may provide the ip address or the domain name as you wish.
<h1>Features</h1>

 1. The first time you run this script, it would ask for ip, port and rcon password as inputs. But after the first execution, it saves the connection object and the parameters the the `data` folder. Upon re-executing, it will ask you if you want to load the server connection from the previous session. If you type in `y` you don't need to provide the connection details again, unless, you want to change the connection to a different server or have changed your rcon password.
 2. Commands sent and responses received and new connections are logged in the `logs` folder in a txt file.
 
That's it till now. Hope you find it helpful!