# 0x11-what_happens_when_your_type_google_com_in_your_browser_and_press_enter

## TABLE OF CONTENT
- [Introduction](#Introduction)
- [FULL STACK SE](#FSSE)
- [THE WEB BROWSING EXPERIENCE](#BrowsingExperience)
	- [DNS request](#DNS_Request)
	- [TCP/IP](#TCP_IP)
	- [Firewall](#Firewall)
	- [HTTPS/SSL](#HTTPS)
	- [Load Balancer](#Balancer)
	- [Web server](#WebServer)
	- [Application server](#AppServer)
	- [Database](#Database)
## Introduction <a name="Introduction"></a>
In this article, we'll explore what happens when you type "google.com" into your web browser's address bar and press Enter. We'll take a journey through the various steps involved in the web browsing experience, from DNS requests to the final rendering of the webpage. But first, let's understand what it means to be a Full Stack Software Engineer.
## FULL STACK SE <a name="FSSE"></a>
Full Stack Software Engineers, often referred to as Full Stack Developers, are versatile professionals who are comfortable interacting with any layer of the software stack. They possess a broad range of skills that encompass both front-end and back-end development. Here, we'll outline the knowledge and responsibilities of a Full Stack Software Engineer.
1. Front End Development A Full Stack SE should excel in creating user interfaces using various technologies. They must prioritize creating user-friendly interfaces and ensure cross-browser compatibility.
2. Back-End Development Full Stack SEs are adept at back-end development, creating dynamic applications that communicate with databases using various technologies. They should also have skills in database administration and query writing. Security is paramount, and they must protect their applications from common web vulnerabilities.
3. DevOps Full Stack SEs work with version control systems like Git, enabling collaboration. They also understand deployment strategies and CI/CD (Continuous Integration/Continuous Deployment). Debugging skills are essential.
4. Project Management Knowledge of design patterns and tools, along with Agile methodologies, aids project planning. Effective communication and collaboration skills are critical for group projects.
In summary, Full Stack Software Engineers are passionate problem solvers with a wealth of knowledge and experience in various technologies.
## The Web Browsing Experience <a name="BrowsingExperience"></a>
Let's dive into the web browsing experience by using the example of typing "https://www.google.com" into your browser. Here's what happens:
### DNS Request <a name="DNS_Request"></a>
The first station, the domain name has to be translated into its mapped IP address by the DNS server. Domain names can be easily memorized by humans as to IP addresses, that is the purpose behind DNS servers.
### TCP/IP <a name="TCP_IP"></a>
In order to get the requested page https://www.google.com, The client has to establish a connection to the server. This is done with the help of the protocol TCP/IP. It establishes a connection in a very reliable way.
### Firewall <a name="Firewall"></a>
It is employed to secure the connection between the client and server.
### HTTPS/SSL <a name="HTTPS"></a>
Google.com uses the secure HTTPS protocol, certified by SSL, to protect data during transmission.
### Load Balancer <a name="Balancer"></a>
Google utilizes load balancers to distribute the overwhelming volume of requests efficiently among its servers.
### Web Server <a name="WebServer"></a>
The client's request reaches Google's web server, the Google Web Server (GWS), which handles the requests.
### Application Server <a name="AppServer"></a>
For requests that require specific logical analysis, an application server comes into play.
### Database <a name="Database"></a>
It is pivotal for retrieving various data.

This journey happens seamlessly, and these elements work together to provide us with the famous search engine we all know.
