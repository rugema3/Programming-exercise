#include <stdio.h>

/* Function declarations */
int add(int a, int b);
int subtract(int a, int b);
int multiply(int a, int b);
float divide(int a, int b);

int main(void) {
	int num1, num2, choice;

	/* Get user input */
	printf("Enter first number: ");
	scanf("%d", &num1);
	printf("Enter second number: ");
	scanf("%d", &num2);

	/* Get operation choice */
	printf("Select operation:\n");
	printf("1. Addition\n");
	printf("2. Subtraction\n");
	printf("3. Multiplication\n");
	printf("4. Division\n");
	printf("Enter your choice (1-4): ");
	scanf("%d", &choice);

	/* Perform the selected operation */
	switch (choice) {
		case 1:
			printf("Result: %d\n", add(num1, num2));
			break;
		case 2:
			printf("Result: %d\n", subtract(num1, num2));
			break;
		case 3:
			printf("Result: %d\n", multiply(num1, num2));
			break;
		case 4:
			printf("Result: %.2f\n", divide(num1, num2));
			break;
		default:
			printf("Invalid choice!\n");
			break;
	}

	return 0;
}

/* Function definitions */

/**
 * add - Adds two numbers
 * @a: First number
 * @b: Second number
 *
 * Return: Result of the addition
 */
int add(int a, int b) {
	return a + b;
}

/**
 * subtract - Subtracts two numbers
 * @a: First number
 * @b: Second number
 *
 * Return: Result of the subtraction
 */
int subtract(int a, int b) {
	return a - b;
}

/**
 * multiply - Multiplies two numbers
 * @a: First number
 * @b: Second number
 *
 * Return: Result of the multiplication
 */
int multiply(int a, int b) {
	return a * b;
}

/**
 * divide - Divides two numbers
 * @a: First number
 * @b: Second number
 *
 * Return: Result of the division
 */
float divide(int a, int b) {
	if (b != 0) {
		return (float) a / b;
	} else {
		printf("Error: Division by zero!\n");
		return 0.0;
	}
}

