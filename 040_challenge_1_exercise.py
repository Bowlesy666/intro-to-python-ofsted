# Video alternative: https://youtu.be/qDWyR0XpJtQ&t=1295s

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
  no_hyphen_words = de_hyphenate_list(words)
  long_words = find_long_words(no_hyphen_words)
  add_ellipsis = create_ellipsis_list(long_words)
  final_report = create_final_report(add_ellipsis)
  return final_report


def de_hyphenate_list(words):

  no_hyphen_list = []

  for word in words:
    if '-' not in word:
      no_hyphen_list.append(word)

  return no_hyphen_list


def find_long_words(words):

  long_word_list = []

  for word in words:
    if len(word) >= 10:
      long_word_list.append(word)

  return long_word_list


def create_ellipsis_list(words):

  ellipsis_word_list = []

  for word in words:
    if len(word) >= 15:
      build_ellipsis = word[0:15] + "..."
      ellipsis_word_list.append(build_ellipsis)
    else:
      ellipsis_word_list.append(word)

  return ellipsis_word_list


def create_final_report(words):

  report_sentence = "These words are quite long: "
  
  i = 1
  for word in words:
    print(len(words))

    if i < len(words):
      report_sentence += word
      report_sentence += ", "
      i += 1
    else:
      report_sentence += word
      i += 1
  
  return report_sentence



check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
