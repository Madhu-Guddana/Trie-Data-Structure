"""
Copyright (c) 2018. All rights reserved.

Author: Madhu.Guddana@gmail.com

This package gives simple implementation of Trie data structure.
"""

from __future__ import print_function
class Node(object):
  """Class of each node present in the Trie tree."""
  def __init__(self, data, is_word=False):
    """
    :param data: The character value stored in the node.
    :param is_word: Boolean, True if this node is char of end of word.
    :return: None
    """

    # Child node is dictionary, where key is a character and
    # value is Node constructed using the character.
    self.childNodes = {}
    self.data=data
    self.is_word = is_word

class Trie(object):
  """The Trie data structure implemented using class."""
  def __init__(self):
    self.root = Node(data=None)

  def insert(self, string):
    """Method to insert a word into trie data structure.
    New node will be created per character iff new word is inserted."""
    cur_node = self.root
    for char in string:

      # Case where substring already exists.
      child = cur_node.childNodes.get(char)
      if not child:

        # Case where character swquence is a new entry.
        child = Node(char)
        cur_node.childNodes[char] = child
      cur_node = child

    # Mark the sequence as new word, regardless of node for characters are created.
    cur_node.is_word=True

  def depth_first(self, root):
    """Just to display content of the tree"""
    if root.is_word:
      print (root.data)
    for child in root.childNodes.values():
      if root.data !=None:
        print (root.data, end="")
      self.depth_first(child)

  def retrieve(self, word):
    """Check for the word in tree.
    Returns true only if word found and it is stored as
    complete word and not just as prefix of other word.
    Example: Word "Madhu" is inserted and
    searching for word "Mad" will result in failure."""

    current = self.root
    for char in word:
      if char in current.childNodes:
        current = current.childNodes[char]
      else:
        return False
    return current.is_word

if __name__ == "__main__":
  string = ("Let us see how search engines work. "
            "Consider the following simple auto complete feature. "
            "When you type some characters in the text bar, "
            "the engine automatically gives best matching options "
            "among it's database. Your job is simple. Given an "
            "incomplete search text, output the best search result.")

  tree = Trie()
  for word in string.split(" "):
    tree.insert(word)
  print (tree.retrieve("incomplete"))
  print (tree.retrieve("bar,"))
