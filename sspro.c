#include <stdio.h>
#include <stdlib.h>

// Function to link object files and generate the executable
void link(const char* objectFiles[], int numFiles, const char* outputFile) {
    // Open the output file in binary mode
    FILE* output = fopen(outputFile, "wb");
    if (output == NULL) {
        printf("Error: Could not open output file for writing.\n");
        return;
    }

    // Loop through each object file
    for (int i = 0; i < numFiles; i++) {
        // Open the object file in binary mode
        FILE* input = fopen(objectFiles[i], "rb");
        if (input == NULL) {
            printf("Error: Could not open object file '%s'.\n", objectFiles[i]);
            fclose(output);
            return;
        }

        // Read the object file contents and write them to the output file
        int ch;
        while ((ch = fgetc(input)) != EOF) {
            fputc(ch, output);
        }

        // Close the object file
        fclose(input);
    }

    // Close the output file
    fclose(output);

    printf("Linking successful. Executable file '%s' generated.\n", outputFile);
}

int main() {
    const char* objectFiles[] = {
        "file1.o",
        "file2.o",
        "file3.o"
    };
    int numFiles = sizeof(objectFiles) / sizeof(objectFiles[0]);

    const char* outputFile = "output.exe";

    link(objectFiles, numFiles, outputFile);

    return 0;
}