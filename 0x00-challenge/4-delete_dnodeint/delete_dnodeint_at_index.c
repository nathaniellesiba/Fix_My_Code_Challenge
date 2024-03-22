#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - Delete a node at a specific index from a list
 *
 * @head: A pointer to the first element of a list
 * @index: The index of the node to delete
 *
 * Return: 1 on success, -1 on failure
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *current = *head;
	unsigned int i;

	if (*head == NULL)  /*Check if the list is empty*/
	{
		return (-1);
	}

	if (index == 0)  /*If the node to be deleted is the first node*/
	{
		*head = current->next;
		if (current->next != NULL)
		{
			current->next->prev = NULL;
		}
		free(current);
		return (1);
	}

	for (i = 0; current != NULL && i < index; i++)  /*Traverse to the node at the specified index*/
	{
		current = current->next;
	}

	if (current == NULL)  /*If the index is out of range*/
	{
		return (-1);
	}

	current->prev->next = current->next;  /*Adjust the next pointer of the previous node*/
	if (current->next != NULL)  /*If the node to be deleted is not the last node*/
	{
		current->next->prev = current->prev;  /*Adjust the prev pointer of the next node*/
	}
	free(current);
	return (1);
}
