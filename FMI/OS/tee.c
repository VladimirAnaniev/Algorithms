#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

void main(int argc, char *argv[]) {
	int files[256];
	for(int i = 1; i < argc; i++) {
		files[i] = open(argv[i], O_WRONLY|O_CREAT|O_TRUNC, 0777);	
	}

	char buff[256];
	while(scanf("%s", buff)) {
		printf("%s\n", buff);
		for(int i = 1; i < argc; i++) {
			write(files[i], buff, strlen(buff));
			write(files[i], "\n", 1);
		}
	}

	printf("Closing files");
	for(int i = 1; i < argc; i++) {
		close(files[i]);
	}
}
