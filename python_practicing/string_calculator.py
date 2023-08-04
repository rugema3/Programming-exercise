# string_calculator.py

class StringCalculator:
    @staticmethod
    def add(numbers):
        if not numbers:
            return 0

        # Split the input string by commas and newlines
        numbers_list = [int(num) for num in numbers.replace("\n", ",").split(",")]

        # Sum the numbers
        total_sum = sum(numbers_list)

        return total_sum

