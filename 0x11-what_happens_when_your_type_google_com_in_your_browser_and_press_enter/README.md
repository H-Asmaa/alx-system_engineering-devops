## TABLE OF CONTENT

- [INTRODUCTION](#INTRODUCTION)
- [FULL_STACK_SE](#full_stack_se)
- [THE_WEB_BROWSING_EXPERIENCE](#the_web_browsing_experience)`
	- [DNS_request](#dns_request)
	- [TCP_IP](#tcp_ip)
	- [Firewall](#firewall)
	- [HTTPS_SSL](#https_ssl)
	- [Load_Balancer](#load_balancer)
	- [Web_server](#web_server)
	- [Application_server](#application_server)
	- [Database](#database)

## INTRODUCTION

In this article, we'll explore what happens when you type "google.com" into your web browser's address bar and press Enter. We'll take a journey through the various steps involved in the web browsing experience, from DNS requests to the final rendering of the web page. But first, let's understand what it means to be a Full Stack Software Engineer.

## FULL_STACK_SE

Full Stack Software Engineers, often referred to as Full Stack Developers, are versatile professionals who are comfortable interacting with any layer of the software stack. They possess a broad range of skills that encompass both front-end and back-end development. Here, we'll outline the knowledge and responsibilities of a Full Stack Software Engineer.

1. Front End Development A Full Stack SE should excel in creating user interfaces using various technologies. They must prioritize creating user-friendly interfaces and ensure cross-browser compatibility.

2. Back-End Development Full Stack SEs are adept at back-end development, creating dynamic applications that communicate with databases using various technologies. They should also have skills in database administration and query writing. Security is paramount, and they must protect their applications from common web vulnerabilities.

3. DevOps Full Stack SEs work with version control systems like Git, enabling collaboration. They also understand deployment strategies and CI/CD (Continuous Integration/Continuous Deployment). Debugging skills are essential.

4. Project Management Knowledge of design patterns and tools, along with Agile methodologies, aids project planning. Effective communication and collaboration skills are critical for group projects.

In summary, Full Stack Software Engineers are passionate problem solvers with a wealth of knowledge and experience in various technologies.

## THE_WEB_BROWSING_EXPERIENCE

Let's dive into the web browsing experience by using the example of typing "https://www.google.com" into your browser. Here's what happens:

### DNS_Request

The first station, the domain name has to be translated into its mapped IP address by the DNS server. Domain names can be easily memorized by humans as to IP addresses, that is the purpose behind DNS servers.

### TCP_IP

In order to get the requested page https://www.google.com, The client has to establish a connection to the server. This is done with the help of the protocol TCP/IP. It establishes a connection in a very reliable way.

### Firewall

It is employed to secure the connection between the client and server.

### HTTPS_SSL

Google.com uses the secure HTTPS protocol, certified by SSL, to protect data during transmission.

### Load_Balancer

Google utilizes load balancers to distribute the overwhelming volume of requests efficiently among its servers.

### Web_Server

The client's request reaches Google's web server, the Google Web Server (GWS), which handles the requests.

### Application_Server

For requests that require specific logical analysis, an application server comes into play.

### Database

It is pivotal for retrieving various data.

##### This journey happens seamlessly, and these elements work together to provide us with the famous search engine we all know.
