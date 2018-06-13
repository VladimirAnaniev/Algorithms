#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

// реализирайте команда ср, работеща с произволен брой подадена входни параметри

void main(int argc, char *argv[]) {
	char buff[256];
	char new_name[256];
	int len;

	for(int i = 1; i < argc - 1; i++) {
		int orig = open(argv[i], O_RDONLY);
		if(orig == -1) {
			printf("Cannot open %s\n", argv[i]);
			continue;
		}

		strcpy(new_name, argv[argc - 1]);
		strcat(new_name, "/");
		strcat(new_name, argv[i]);

		int cp = open(new_name, O_WRONLY|O_CREAT|O_TRUNC, 0777);
		if(cp == -1) {
			printf("Cannot open or create %s\n", new_name);
			close(orig);
			continue;
		}

		while(len = read(orig, buff, 256)) {
			write(cp, buff, len);
		}

		close(orig);
		close(cp);
	}

}
