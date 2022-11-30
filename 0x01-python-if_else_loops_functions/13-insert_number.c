#include "list.h"
/**
 *insert_node - inserta a number node into a sorted linked list
 *@head: pointer to the first nide of the list
 *@number: number to be inserted
 *Return: adress of bew node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current = *head;
	listint_t *former;
	int diff = 0;
	
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;	
	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next)
		{
			diff = new->n - current ->n;
			if (diff >= 0 && (new->n - (current->next->n)) > 0)
				current = current->next;
			else
				break;
		}
		if (current == *head)
			new->next = current;
		else
		{
			former = current->next;
			current->next = new;
			new->next = former;
		}
	}
	return (&*new);
}
