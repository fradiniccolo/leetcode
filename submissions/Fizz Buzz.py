class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        array = []
        for number in range(1, n+1):
            item = ''
            if number % 3 == 0:
                item += "Fizz"
            if number % 5 == 0:
                item += "Buzz"
            if item == '':
                item = str(number)
            array.append(item)
        return array
