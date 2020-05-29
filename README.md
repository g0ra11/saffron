# Saffron Banking System
![](saff_logo.png)
### The project expose a Banking API, a Web Server and an Android Studio App 
 1. The API server is capable of transforming the clients requests into internal messages and put on a rabbit queue. Then, one or more workers will consume the messages from queue and respond. Available requests are: 
 * Check balance
 * Transfer to another client
 * Online payment 

 Python Libraries
* flask 
* pymongo
* PyRSMQ 
* hashlib

2. Web Server is a Dummy Shop where the user is able to buy and pay using Saffron Banking. In order to pay, the user have to introduce a generated token by API which contains a specific amount of money.
* ReactJS web framework

3. Android Studio App represents the user account control and comes with following facilities: 
* Finger signature login
* Register 
* Chech balance
* Transfer to another user 
* Online payment