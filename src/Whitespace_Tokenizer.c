#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define MAX_LENGTH 50
#define MAX_TOKENS 10

int get_line(char *ptr){
    int ch, n = 0;
    while ((ch = getchar()) != '\n'){
        *(ptr++) = (char)ch;
        n++;
    }
    *ptr = '\0';
    return n;
}

int read_input(char *input){
    int count = 0;
    printf("\n> ");
    return count = get_line(input);
}

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

void print_tokens(char **tokens, int n){
    for(int i = 0; i < n; i++) printf("%s\n", tokens[i]);
}

int main(){
    char input[MAX_LENGTH];
    char *tokens[MAX_TOKENS];
    int num_of_tokens;
    while(true){
        read_input(input);
        num_of_tokens = parse(input, tokens);
        print_tokens(tokens, num_of_tokens);
    }
    return 0;
}

// > Machine learning is fascinating   
// Machine
// learning
// is
// fascinating