#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

void main(int argc, char *argv[]) {
	int file = open("file", O_RDWR|O_CREAT|O_TRUNC, 0777);
	
	if(fork()) {
		wait();
		write(file, "bar", 3);
	} else {
		write(file, "foo", 3);
	}

	close(file);
}
