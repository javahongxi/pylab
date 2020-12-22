import loop, internal.internal_variable

for x in loop.a:
    if x > 3:
        break
    print(x)

print("doc: " + (__doc__ or "none doc"))
print("file: " + (__file__ or "none file"))
print("package: " + (__package__ or "none package"))
print("name: " + (__name__ or "none name"))