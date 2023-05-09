#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/* Struct for a singly linked list node */
typedef struct listint_s listint_t;
struct listint_s
{
    int m;
    listint_t *next;
};
/* Function prototypes */
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int m);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */

