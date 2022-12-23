"""
Problem: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit
numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

if __name__ == "__main__":

    number1 = 999
    solution = 0
    while number1 > 100:
        number2 = 999
        while number2 > 100:
            product = str(number1 * number2)

            if len(product) == 6:
                if product[0] == product[-1] and product[1] == product[-2] and product[2] == product[-3]:
                    if solution < int(product):
                        solution = int(product)
            elif len(product) == 5 or len(product) == 4:
                if product[0] == product[-1] and product[1] == product[-2]:
                    if solution < int(product):
                        solution = int(product)

            number2 -= 1

        number1 -= 1

    print(solution)
