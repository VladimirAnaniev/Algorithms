#include <stdio.h>
#include <stdlib.h>

void main(int argc, char *argv[]) {
	int status;
	if(fork()) {
		wait(&status);
		if(status == 0) {
			execlp(argv[2], argv[2], 0);
		} else {
			exit(-1);
		}
	} else {
		execlp(argv[1], argv[1], 0);
		exit(-1);
	}
}
