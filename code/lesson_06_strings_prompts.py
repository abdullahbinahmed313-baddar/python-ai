"""Lesson 1.6: Clean a messy user question before sending it to an AI model."""

name = input("Your name: ")
question = input("Your question: ")

clean_name = name.strip().title()
clean_question = question.strip().capitalize()

# Why: removing extra spaces makes the name look clean in the prompt.
# Why: estimating tokens helps keep track of the cost of an AI request.
character_count = len(clean_question)
estimated_tokens = round(character_count / 4)
mentions_python = "python" in clean_question.lower()
short_question = clean_question[:150]

print("=" * 30)
print(f"Cleaned question: {clean_question}")
print(f"Characters: {character_count}, about {estimated_tokens} tokens")
print(f"Mentions Python: {mentions_python}")
print("=" * 30)

prompt = f"""You are a friendly Python tutor.
Greet {clean_name} by name and answer in 3 short lines.
Question: {short_question}"""

print(prompt)
