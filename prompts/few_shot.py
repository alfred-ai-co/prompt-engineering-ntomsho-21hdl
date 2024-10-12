FEW_SHOT_PROMPT = """
Given the following topic {input}, generate a quiz with 3 to 5 questions. It should be formatted as a json object with
an array of questions,
each Question should have a question string which is the text of the question,
a choices array which is an array of strings for the possible answers,
and an answer string which is the index of the correct answer in the choices array.

Here is an example:
The question is "What is the fluffiest kind of bunny?"
The answers are "A) Angora", "B) Flemish Giant", "C) Lionhead", "D) Netherland Dwarf"
The correct answer is A.
"""