"""Lesson 1.7: Route a task to an AI model and estimate its cost."""

task = input("Task (code / private / chat): ").strip().lower()
tokens = int(input("Estimated tokens: "))

# Why: private data stays on the laptop, so route it to the local model.
if task == "private":
    model = "llama3.2 (local, Ollama)"
    price = 0
elif task == "code":
    model = "claude (cloud, strong at code)"
    price = 0.8
else:
    model = "small cloud model (cheap for chat)"
    price = 0.2

cost = tokens / 1000 * price

# Why: long requests cost more, so warn before sending them.
if tokens > 4000:
    print("Warning: long request, consider shortening it.")
else:
    print("Length is fine.")

print(f"Chosen model: {model}")
print(f"Estimated cost: {cost:.2f} PKR")
