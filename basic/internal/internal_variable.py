"""内置变量
"""

a = 1
print(dir())

print("doc: " + (__doc__ or "none doc"))
print("file: " + (__file__ or "none file"))
print("package: " + (__package__ or "none package"))
print("name: " + (__name__ or "none name"))
