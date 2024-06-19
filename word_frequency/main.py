import requests
from typing import List
from collections import Counter, deque
import heapq

class WordFrequency:
    def __init__(self,
                 word: str,
                 freq: int) -> None:
        self.word = word
        self.frequency = freq

    def __lt__(self, other) -> bool:
        """
        Custom less than operator
        If two words have the same frequency, the word with the greater lexicographical order should be ordered first.
        Else the word with the higher frequency should be ordered first.
        """
        if self.frequency == other.frequency:
            return self.word > other.word
        return self.frequency < other.frequency

def download_text(url: str) -> str:
    """Download text from a given URL"""
    response = requests.get(url)
    return response.text

def parse_text(text) -> List[str]:
    """Parse text into a list of words"""
    return text.split()

def main():
    """
    Steps to get the 10th to 20th most frequent words:
    1. Download the text from the given URL
    2. Parse the text into a list of words
    3. Count the frequency of each word
    4. Use a max heap to keep track of the 20 most frequent words
    5. Pop the heap until the 10th most frequent word is reached
    6. Print the words from 10th to 20th most frequent

    Overall time complexity: O(nlogk) where n is the number of words and k is the number of top words frequency to be tracked
    """
    url = "https://www.gutenberg.org/cache/epub/16317/pg16317.txt"
    text = download_text(url)
    word_freq = Counter(parse_text(text))
    start = 10
    stop = 20
    max_heap = []
    for key, val in word_freq.items():
        heapq.heappush(max_heap, WordFrequency(key, val))
        if len(max_heap) > stop:
            heapq.heappop(max_heap)

    result = deque([])
    while stop > start:
        result.appendleft(heapq.heappop(max_heap).word)
        stop -= 1

    print("Words ranked from 10th to 20th by frequency:")
    for word in result:
        print(f"{word}: {word_freq[word]}")

if __name__ == "__main__":
    main()