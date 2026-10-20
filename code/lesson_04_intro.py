print("Assalam O Alaikum, AI world!")
print("I am learning Python.")
print(100)
print("Model:", "Gemma")
print("Python", "for", "AI", sep="-")
print("Thinking", end="... ")
print("done")
model = "deepseek"
tokens = 120

print(f"{model} used {tokens} tokens")
name = input("Your name: ")
print(f"Welcome, {name}!")
age = int(input("Age: "))
print(f"Next year, you will be {age + 1}")
# AI ke liye model ka naam
model = "gemma"
print("Welcome to my AI app!")

"""Lesson 1.4: Business Prompt Builder"""

# Collect information from the user
name = input("Your name: ")
business = input("Business type: ")
problem = input("Business problem: ")

prompt = (f"You are an AI business assistant for a {business}. "
    f"Help solve this problem: {problem}. "
    f"Give 3 simple and practical solutions."
)

print(f"\nWelcome, {name}!")
print("\n--- Your AI Prompt ---")
print(prompt)
