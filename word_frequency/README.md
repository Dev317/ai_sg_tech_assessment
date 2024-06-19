### Overview
https://github.com/Dev317/ai_sg_tech_assessment/assets/70529335/6a6a72ea-feed-4eb2-8e81-b561d2fe4daf

This is a simple program that prints out the top 10th to 20th words in a text file from a given link.
The solution utilises the max heap as the core data structure to do the word fequency sorting.
Most of the packages used are from the python standard library.
Overall time complexity: O(nlogk) where n is the number of words and k is the number of top words frequency to be tracked.

### Program flow
1. Download the text from the given URL. Store the text in memory since it is a relatively small size data.
2. Parse the text into a list of words, assuming that a valid word has an empty space before and after.
3. Count the frequency of each word via using `Counter` class from `collections` module.
4. Use a max heap via `heapq` module to keep track of the 20 most frequent words
5. Pop the heap until the 10th most frequent word is reached
6. Print the words from 10th to 20th most frequent
