#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def bubble_sort(arr,comparison_function):
  swaps = 0
  sorted = False
  while not sorted:
    sorted = True
    for idx in range(len(arr) - 1):
      if comparison_function(arr[idx], arr[idx + 1]) == True:
        sorted = False
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        swaps += 1
  print("Bubble sort: There were {0} swaps".format(swaps))
  return arr


def quicksort(list, start, end, comparison_function):
  if start >= end:
    return
  pivot_idx = random.randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  less_than_pointer = start
  for i in range(start, end):
    if comparison_function(pivot_element, list[i]):
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  quicksort(list, start, less_than_pointer - 1,comparison_function)
  quicksort(list, less_than_pointer + 1, end,comparison_function)


def merge_sort(items):
  if len(items) <= 1:
    return items

  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]

  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)
  print(left_sorted, right_sorted)
  return merge(left_sorted, right_sorted)


def merge(left, right):
  result = []

  while (left and right):
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)

  if left:
    result += left
  if right:
    result += right

  return result


# In[ ]:


if __name__ = "__main__":
    import csv
    # This code loads the current book
    # shelf data from the csv file
    def load_books(filename):
      bookshelf = []
      with open(filename) as file:
          shelf = csv.DictReader(file)
          for book in shelf:
              # add your code here

              bookshelf.append(book)
      return bookshelf

    # PRINT THE THE BOOKS
    bookshelf = utils.load_books('books_small.csv')
    for book in bookshelf:
      #print(book['title'])
      book['author_lower'] = book['author'].lower()
      book['title_lower'] = book['title'].lower()

    # SORT BY TITLE: BUBBLE_SORT
    def by_title_ascending(book_a, book_b):
      return book_a['title_lower'] > book_b['title_lower']

    sort_1 = sorts.bubble_sort(bookshelf,by_title_ascending)
    for book in sort_1:
      print(book['title'])
    print("")
    
    
    # SORT BY AUTHOR
    def by_author_ascending(book_a, book_b):
      return book_a['author_lower'] > book_b['author_lower']

    # SORT BY AUTHOR: BUBBLE_SORT
    bookshelf_v1 = bookshelf
    sort_2 = sorts.bubble_sort(bookshelf_v1,by_author_ascending)
    for book in sort_2:
      print(book['author'])
    print("")

    # SORT BY AUTHOR: QUICKSORT
    bookshelf_v2 = bookshelf
    sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
    for book in bookshelf_v2:
      print(book['author'])
    print("")

    # SORT BY TOTAL LENGTH: BUBBLE_SORT AND QUICKSORT
    def by_total_length(book_a, book_b):
      return  (len(book_a['author_lower']) + len(book_a['title_lower'])) > (len(book_b['author_lower']) + len(book_b['title_lower']))

    long_bookshelf = utils.load_books('books_small.csv')
    for book in long_bookshelf:
      #print(book['title'])
      book['author_lower'] = book['author'].lower()
      book['title_lower'] = book['title'].lower()

    sort_3 = sorts.bubble_sort(long_bookshelf,by_total_length)
    sort_4 = sorts.quicksort(long_bookshelf,0, len(long_bookshelf)-1,by_total_length)

    
    

