#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <libconfig.h>
#include <curl/curl.h>
#include "sakisafecli.h"

size_t
write_data(void *buffer, size_t size, size_t nmemb, void *userp)
{
	memcpy(userp, buffer, nmemb * size);
	return 0;
}

void
print_usage()
{
	printf("USAGE: sakisafecli [-p socks proxy|-P http proxy] [-x] [-s] "
		  "[-6|-4] [--server] FILE\n");
	return;
}

void
print_help()
{
	printf("-s|--server: specifies the sakisafe "
		  "server\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s",
		  "-t|--token: Authentication token (https://u.kalli.st)",
		  "-P|--http-proxy: http proxy to use e.g. http://127.0.0.1:4444",
		  "-p|--socks-proxy: SOCK proxy to use e.g.I 127.0.0.1:9050",
		  "-6|--ipv6: uses IPv6 only",
		  "-4|--ipv6: uses IPv4 only", 
		  "-S|--silent: doesn't print progress",
		  "-x|--paste: read file from stdin",
		  "-C: print current settings",
		  "-h|--help: print this message.\n");
	return;
}

void
progress(
	void *clientp, double dltotal, double dlnow, double ultotal, double ulnow)
{
	/* So I don't get a warning */
	dltotal += 1;
	dlnow += 1;
	printf("\r%0.f uploaded of %0.f (\033[32;1m%0.f%%\033[30;0m)",
		  ulnow,
		  ultotal,
		  ulnow * 100 / ultotal);
	fflush(stdout);
}
