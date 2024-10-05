#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define MAX_LENGTH 50
#define MAX_TOKENS 10

char input[MAX_LENGTH];
char *tokens[MAX_TOKENS];

int parse(char *input, char **tokens){
    int count = 0;
    char *token = strtok(input, " ");
    while (token != NULL && count < MAX_TOKENS-1){
        
        *tokens++ = token;
        count++;
        token = strtok(NULL, " ");
    }  
    *tokens = '\0';
    return  count;
}