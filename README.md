## Building and upping Docker containers
Primary and two secondary servers in three different docker containers: primary (port 9000), happy_secondary (port 9001), carefree_secondary (port 9002)
Dmytro$ docker-compose up --build
![image](https://github.com/user-attachments/assets/29b58a79-449f-42d6-83f6-ee7cd369101e)

![image](https://github.com/user-attachments/assets/033c5d40-9d89-4fc4-8323-dc300db58cf3)

## Filling the list with data over POST requests to the Primary
Post the first element to the list 
Dmytro$ curl -X POST -d "iOS" http://localhost:9000
Post the second element to the list 
Dmytro$ curl -X POST -d "Android" http://localhost:9000
Post the third element to the list
Dmytro$ curl -X POST -d "Tizen" http://localhost:9000

## Geting sent data over GET request from all three servers
Get data from the Primary running on port 9000
![image](https://github.com/user-attachments/assets/d28a7388-588c-47a1-9e9b-117403f42d18)

Get data from the first Secondary running on port 9001
![image](https://github.com/user-attachments/assets/b5c1ea82-e666-45f0-a351-bdf74679a8d2)

Get data from the second Secondary running on port 9002
![image](https://github.com/user-attachments/assets/63c7b532-2795-4240-9f8f-00cbe99f2ffd)

## Entire look
![image](https://github.com/user-attachments/assets/ab7d9e51-0529-4ed7-b06d-1c4c4e8eff6a)













