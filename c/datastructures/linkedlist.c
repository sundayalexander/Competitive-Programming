/**
An implementation of a Linkedlist data structure.
Implementation approach can be found here: https://github.com/sundayalexander/coding-interview-university#data-structures
This data structure is for learning purpose only, an optimized implementation is available for production use in the C community.
**/
#include <stdlib.h>
typedef struct node{
    int number;
    struct node *next;

} node;




int main(void){
    node *list = malloc(sizeof(node));
    node *n = malloc(sizeof(node));
    if(n != NULL){
        n->number=1;
        n->next=NULL
    }
    list =  n;

    node *n = malloc(sizeof(node));
    if(n != NULL){
        n->number=1;
        n->next=NULL
    }
    list->next =  n;
    n = NULL;
    return 0;
}
