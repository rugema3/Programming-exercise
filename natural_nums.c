/**
 * naturals - This function prints the natural numbers from 1 to 50
 * @n: highest number to be printed
 * The program is using recursion as a method of printing
 * the first 50 natural numbers
 * Return: nothing to return here
 */
#include<stdio.h>
int naturals(int n)
{
	if (n <= 50)
	{
		printf("%d\t", n);
		naturals(n + 1);
	}
}

/**
 * main - the main calls the recursive function.
 * Return: 0 (success).
 */
int main(void)
{
	int n = 1;

	naturals(n);
	printf("\n");
	return (0);
}
