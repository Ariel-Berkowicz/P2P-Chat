# P2P-Chat
A peer-to-peer python chat application using a centralized server.

## How to run
1. To add a new peer, run the following command:
```
python3 chat.py
```

2. For the first peer it will make it the server:
![1](https://user-images.githubusercontent.com/61075964/162983906-acc68e1d-7370-4552-9384-1b6438c22b59.png)

3. Then for the next peers it will add them as clients:
![2](https://user-images.githubusercontent.com/61075964/162984080-a724b94f-eef4-40e8-b2a9-fb3b32f9074c.png)

4. You can send messages using command line as:
![3](https://user-images.githubusercontent.com/61075964/162984218-ed5c2b4d-1468-42ae-982c-815ffd23fdee.png)

5. Now if you kill the server peer then it will make one of the other peers a server (using random wait time):
![6](https://user-images.githubusercontent.com/61075964/162984633-22887f91-1eb2-42ea-8311-cbf5a9b2d356.png)

## Discovery
You register by making yourself findable by others (as in Telegram or Whatsapp)

## Session Initiation
Send a message to users who you want to connect with

## Communication and Synchronization
  * You can live connect with any of your friends who is available now.
  * For users who are not available (offline), you can write messages, which are stored on your own client.
  * The data for offline users will be synchronized when both users are discoverable.
## Security
All is hashed
