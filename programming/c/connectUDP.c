int connectsock(const char *host, const char *service, const char *transport)
int connectUDP(const char *host, const char *service){
	return connectsock(host, service, "udp");
}

