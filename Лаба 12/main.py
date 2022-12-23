import json
import functools


class Solution:
    def sum_number_in_string(self, number_string: str) -> int:
        num1 = 0
        number_string = number_string
        for word in str(number_string):
            num1 += int(word)
        return num1

    def get_leader_string(self, steps: int) -> str:
        result = ""
        for i in range(steps + 1):
            str = ""
            for k in range(steps - i):
                str += ' '
            for k in range(i):
                str += '#'
            result += str + '\n'
        return result

    def to_json(self, func):
            @functools.wraps(func)
            def wrapped(*args, **kwargs):
                result = func(*args, **kwargs)
                return json.dumps(result)

            return wrapped




if __name__ == '__main__':
    solution = Solution()

    solution.sum_number_in_string('12345')
    solution.sum_number_in_string('160438521039')

    print(solution.get_leader_string(3))
    print(solution.get_leader_string(5))

    @solution.to_json
    def get_data():
        return {
            'data': 42
        }