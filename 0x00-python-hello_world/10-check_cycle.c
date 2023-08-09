#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if list contains a cycle
 * @list: singly-linked list
 *
 * Return: 1 if cycle, 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *x, *y;

	if (list->next == NULL || list == NULL)
		return (0);

	x = list->next;
	y = list->next->next;
	while (x && y && y->next)
	{
		if (x == y)
			return (1);

		x = x->next;
		y = y->next->next;
	}
	return (0);
}
