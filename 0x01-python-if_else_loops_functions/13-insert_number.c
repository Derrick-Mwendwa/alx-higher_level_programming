#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts number into a sorted linked list
 * @head: pointer to a pointer to the head
 * @number: number to insert
 *
 * Return: pointer to the new node otherwise NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *item;

	node = *head;
	item = malloc(sizeof(listint_t));

	if (item == NULL)
		return (NULL);

	item->n = number;

	if (node == NULL || node->n >= number)
	{
		item->next = node;
		*head = item;
		return (item);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	item->next = node->next;
	node->next = item;

	return (item);
}
