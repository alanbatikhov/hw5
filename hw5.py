# list = [ 1, 2, 3, 4, 5]
# maximum = max(list)
# minimum = min(list)
# print(minimum, maximum)

# def minimum(list):
#     min_val = None
#     for val in list:
#         if min_val == None or min_val > val:
#             min_val = val
#     return min_val
# def maximum(list):
#     max_val = None
#     for val in list:
#         if max_val == None or max_val<val:
#             max_val = val
#     return max_val
# def main():
#     list = [1,2,3,4,5,6,7]
#     print("Наименьшее значение это ", minimum(list))
#     print("Наибольшее значение это ", maximum(list))
# main()



class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        """
        sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
        """
        most_words_found: int = 0
        for sentence in sentences:
            list_of_words: list[str] = sentence.split(" ")
            num_of_words: int = len(list_of_words)
            most_words_found = max(most_words_found, num_of_words)
        return most_words_found