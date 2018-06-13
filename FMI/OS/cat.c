#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

void main(int argc, char *argv[]) {
	char buff;
	for(int i = 1; i < argc; i++) {
		int file = open(argv[i], O_RDONLY);
		if(file == -1) {
			printf("Could not open %s\n", argv[i]);
		}		

		//int len;
		while(read(file, &buff, 1)) {
			printf("%c", buff);
		}

		close(file);
	}

}
