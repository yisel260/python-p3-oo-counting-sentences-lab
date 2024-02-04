#!/usr/bin/env python3
import re

class MyString:
  def __init__(self,value =""):
        self.value = value

  @property
  def value(self):
        return self._value
  @value.setter
  def value (self, string):
        if isinstance(string, str):
            self._value = string
        else:
             print("The value must be a string.")

  def is_sentence(self):
    return self.value.endswith(".")

  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
    print("Value:", self.value)
    if not self.value.strip():
        return 0
    sentences = re.split(r'[.?!]', self.value)
    non_empty_sentences = [sentence for sentence in sentences if sentence.strip()]
    return len(non_empty_sentences)