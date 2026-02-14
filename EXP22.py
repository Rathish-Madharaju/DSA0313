text = "Ravi has a car. He loves it."
words = text.split()

last_noun = ""
resolved = []

for w in words:
    if w.lower() in ["ravi", "car"]:
        last_noun = w
        resolved.append(w)
    elif w.lower() in ["he", "it"]:
        resolved.append(last_noun)
    else:
        resolved.append(w)

print("Resolved Text:")
print(" ".join(resolved))
