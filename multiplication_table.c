/**
 * main - calling the function
 * print_mult_table:this function prints the multiplication table 
 * of n numbers up to 12.
 * @n: number whose multiplication table is to be printed
 * Return: 0 (success)
 */
#include<stdio.h>
void print_mult_table(int n)
{
	int i, j;
	
	for (i = 0; i <= n; i++)
	{
		for (j = 0; j <= 12; j++)/* we want to print up to times 12 as the max*/
		{
			printf("%d\t", i * j);
			/** adding a table to make the numbers more
			 * visible and neat
			 */
		}
		printf("\n");
	}
}

int main(void)
{
	print_mult_table(12);
	return (0);
}
