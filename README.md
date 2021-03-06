# sampeIoTData
This fires JSON payloads of fake IoT data to an ORDS endpoint. The endpoint does not require authentication, the endpoint has been editted to remove its base url. 

# How to get your ORDS base url


![](/screenshots/1.png)

From your OCI console, press the upper left hamburger menu and select your autonomous database. 

![](/screenshots/2.png)

Press your database. 

![](/screenshots/3.png)

Go to the Service console. 

![](/screenshots/4.png)

Open the Development tab, and your ORDS base url is on the right. 

![](/screenshots/5.png)

Now the dashboards on this apex application will be able to update in real-time, simulating real sensor data. 

[Inspired by sbs-iot-data-generator](https://github.com/aws-samples/sbs-iot-data-generator)

[Click here to see how you can use API Gateway to protect your ORDS endpoints](https://github.com/GaryHostt/OCI_DevOps/blob/master/Lab301.md)
