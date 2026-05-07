class Solution:
    def totalFruit(self, fruits):

        left = 0
        max_fruits = 0
        count = {}

        for right in range(len(fruits)):

            fruit = fruits[right]

            if fruit in count:
                count[fruit] += 1
            else:
                count[fruit] = 1

            while len(count) > 2:

                left_fruit = fruits[left]
                count[left_fruit] -= 1

                if count[left_fruit] == 0:
                    del count[left_fruit]

                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
        