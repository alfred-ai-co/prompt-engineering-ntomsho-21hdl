CHAIN_OF_THOUGHT_PROMPT = """
Write a quiz about the topic of {input}. It should have 3 to 5 questions, each with 3 to 5 choices and one correct answer.
The answers should be similar enough to each other that the quiz is not too easy, but avoid trick questions where the answer could be ambiguous.
Let's go through it step by step:

1. Write a question about the topic. Make sure the question has a single correct answer that is not up for interpretation.
  Example: don't ask "What is the most famous city in the world?" as that is subjective and could have many answers. Ask something like "What is the northernmost capital city in the world?" instead.
2. Write 3 to 5 choices for the question.
3. Go through the wrong answers and, if any of them are obviously incorrect, try to make them more plausible by making them something similar to the correct answer.
  Example 1: if asking "What is the nickname for Pittsburgh, PA?" don't use "The Moon" as that is clearly not a nickname for a city and is too obviously wrong. Instead, use another city's nickname.
  Example 2: if asking "What is the nickname for Pittsburgh, PA?" don't use "The Big Apple" as that is famously the nickname for New York City. Instead, use something like "Music City" as that is a less well known nickname for another city.
4. Make sure that none of the wrong answers are the same as the correct answer or that could be the answer if the question were worded differently.
  Example: if asking "What is the nickname for Pittsburgh, PA?" don't include both "Steel City" and "City of Bridges" in the choices as both of them are famous nicknames for Pittsburgh. Instead use something like another city's nickname.

{format_instructions}

"""