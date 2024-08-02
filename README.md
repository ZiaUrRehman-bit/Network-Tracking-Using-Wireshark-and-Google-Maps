# Netwrok Tracking Using Wireshark and Google Maps
In this project, I will show you Network Traffic visualization using the Python programming language, Wireshark and Google Maps. This tutorial covers the implementation steps needed to take a file of network traffic and convert it into a visual presentation using Google Maps.
## Downloading external material
Besides the Python code that will be created in this tutorial, several external resources and applications is needed to make it work.
## GeoLiteCity
First of you will need to download the GeoLiteCity database as this will be used to translate a IP address into a Geo location(longitude & latitude). The database can be downloaded here: https://github.com/mbcc2006/GeoLiteCity-data
## Wireshark
Besides the GeoLiteCity database you will also be needing the Wireshark application to be able to capture network traffic on your device. The captured traffic will act as input to our Python script and will be the data displayed at the end using Google Maps. The Wireshark application can be downloaded here: https://www.wireshark.org/ 
## Capture Network Traffic
With Wireshark installed it’s time to create our input data which will consist of a captured pcap file. The file will consist of all network traffic going to and from our device in the period we have the capture function activated.

To initialize a capture open wireshark and select a interface which has traffic going through it. e.g
![image](https://github.com/user-attachments/assets/ad017fe0-ecc0-4c7a-88bb-0c42f2c8b177)

When selecting a interface, Wireshark automatically starts a new capture, which is why you immediately gets prompted with network traffic. To stop the capture and save the data you will have to do the following:
![image](https://github.com/user-attachments/assets/89e8a48b-2a6b-4eb6-b593-d2ecb928d879)

Once the capture has been stopped you need to export the captured data in pcap format, this can be done by clicking File -> Export Specified Packets.. and then selecting the following format:
![image](https://github.com/user-attachments/assets/bb6accb4-a96c-4cc8-85bd-f7a32c3df8d7)

With the captured data saved in the correct format, you’re ready to move into the Python Implementation.



