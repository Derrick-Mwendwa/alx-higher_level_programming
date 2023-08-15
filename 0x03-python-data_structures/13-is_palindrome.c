#include <stdio.h>
#include "lists.h"

listint_t *reverse(listint_t **head);

/**
 * is_palindrome - checks if singly linked list is a palindrome
 * @head: pointer to the head of list
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	size_t len, i;
	listint_t *rev, *temp, *x;

	len = 0;

	if ((*head)->next == NULL || *head == NULL)
		return (1);

	temp = *head;

	while (temp)
	{
		++len;
		temp = temp->next;
	}

	temp = *head;

	for (i = 0; i < ((len / 2) - 1); i++)
		temp = temp->next;

	if ((len % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	rev = reverse(&temp);
	x = rev;

	temp = *head;

	while (rev)
	{
		if (temp->n != rev->n)
			return (0);

		temp = temp->next;
		rev = rev->next;
	}

	reverse(&x);

	return (1);
}

/**
 * reverse - reverse a singly-linked list
 * @head: pointer to the head node
 *
 * Return: pointer to the new head node
 */
listint_t *reverse(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}
