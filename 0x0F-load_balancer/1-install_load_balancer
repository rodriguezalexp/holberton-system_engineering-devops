#!/usr/bin/env bash
#configuration of the load balancer
sudo apt-get -y update
sudo apt-get -y install haproxy
sudo chmod 777 /etc/haproxy/haproxy.cfg 
echo "frontend firtslb
	bind *:80
	option forwardfor
	default_backend holbi-servers
	
backend holbi-servers
	balance roundrobin
	server 2618-web-01 104.196.141.92:80 check
	server 2618-web-02 75.101.202.218:80 check" > /etc/haproxy/haproxy.cfg
sudo service haproxy restart

