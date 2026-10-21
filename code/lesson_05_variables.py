"""Lesson 1.5: AI model profile card and token cost estimate."""

MODEL = "gemini-4-argon"
temperature = 0.2
max_tokens = 300
stream = False
system_prompt = "You are a helpful Python tutor."

# Example price for practice, not a real price list.
price_per_1k_tokens = 0.5

tokens_used = int(input("Tokens used: "))
cost = tokens_used / 1000 * price_per_1k_tokens

print("\n--- AI Model Profile Card ---")
print(f"Model: {MODEL} ({type(MODEL).__name__})")
print(f"Temperature: {temperature} ({type(temperature).__name__})")
print(f"Max tokens: {max_tokens} ({type(max_tokens).__name__})")
print(f"Streaming: {stream} ({type(stream).__name__})")
print(f"System prompt: {system_prompt} ({type(system_prompt).__name__})")
print(f"Estimated cost: {round(cost, 2)} PKR")
