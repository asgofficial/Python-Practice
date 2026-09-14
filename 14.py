a = "Python Programming."

print("1.", a[:6])

print("2.", a[7:18])

if "Java" not in a:
    text = a.replace("Programming", "Java Programming")

print("3.", text)

print("4. Length:", len(text))

print("5.", text.upper())

print("6. Number of words:", len(text.split()))

print("7.", text.replace(" ", ""))

print("8.")
print("A =", text.upper().count("A"))
print("P =", text.upper().count("P"))
print("R =", text.upper().count("R"))
print("M =", text.upper().count("M"))