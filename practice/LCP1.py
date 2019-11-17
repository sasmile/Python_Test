class Solution:
    def game(self, guess=list[int], answer=list[int]):
        return sum(guess[i] == answer[i] for i in range(len(guess)))