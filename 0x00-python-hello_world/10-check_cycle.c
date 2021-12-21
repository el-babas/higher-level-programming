#include "lists.h"

/**
 * check_cycle -  singly linked list has a cycle in it
 * @list: structut
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *l_flash, *l_zoom;

	l_flash = l_zoom = list;

	if (list == NULL)
		return (0);

	while (l_zoom && l_zoom->next && l_zoom->next->next)
	{
		l_flash = l_flash->next;
		l_zoom = l_zoom->next->next;
		/* check if flash reached zoom */
		if (l_flash == l_zoom)
			return (1);
	}
	return (0);
}
