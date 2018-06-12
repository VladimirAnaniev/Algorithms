#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

void main(int argc, char *argv[]) {
	if(fork()) {
		wait();
		int file = open(argv[1], O_RDONLY);
		char buff[3];
		while(read(file, buff, 2)) {
			printf("%s ", buff);
		}
		printf("\n");
	} else {
		int file = open(argv[1], O_WRONLY|O_CREAT|O_TRUNC, 0777);
		write(file, "foobar", 6);
	}

}
