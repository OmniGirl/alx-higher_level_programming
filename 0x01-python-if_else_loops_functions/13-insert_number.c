#include <stdio.h>
#include <stdlib.h>

/* Definition of singly linked list node */
typedef struct listint_s
{
int n;
struct listint_s *next;
} 
listint_t;

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to the head of the list
 * @number: number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node, *current;
/* Allocate memory for new node */
new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
return NULL;

/* Set the value of the new node */
new_node->n = number;
new_node->next = NULL;

/* If the list is empty or the new node should be the first node */
if (*head == NULL || number < (*head)->n)
{
new_node->next = *head;
*head = new_node;
return new_node;
}
/* Traverse the list to find the correct position to insert the new node */
current = *head;
while (current->next != NULL && current->next->n < number)
current = current->next;
/* Insert the new node */
new_node->next = current->next;
current->next = new_node;
return new_node;
}
