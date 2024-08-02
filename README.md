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
