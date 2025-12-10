#include <stdio.h>
#include <string.h>

int main() {
	FILE *fptr;
	
	// Open file
	fptr = fopen("day-1-input.txt", "r");

	// Close file if not found
	if (fptr == NULL) {
		printf("File could not be opened\n");
		fclose(fptr);
		return 1;
	}

	char content[100];

	while (fgets(content, 100, fptr)) {

	}

	struct list {
		
	}

	fclose(fptr);
	return 0;
}
