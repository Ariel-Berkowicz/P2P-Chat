# P2P-Chat

* Discovery
  * You register by making yourself findable by others (as in Telegram or Whatsapp)
* Session Initiation
  * Send a message to users who you want to connect with
* Communication and Synchronization
  * You can live connect with any of your friends who is available now.
  * For users who are not available (offline), you can write messages, which are stored on your own client.
  * The data for offline users will be synchronized when both users are discoverable.
* Security
  * All is hashed


## Run the system
  #### To run the system what you need to do is run in on a Linux terminal, if you are on a Windows machine use WSL
  #### Use python3 and run `python3 chat.py` 
  #### If you want to test the local connection of the chat systems; you will need to run more than 2 chat.py files.
  #### One of the users will be used as a server and the other 2 will be chatting between the each other or even more.
  #### If the server ever dies for some unknown reason one of the users will become a server to keep the chat going.