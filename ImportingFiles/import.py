# importing a module that i've created
import instances

# importing a built-in python module
import fractions

# importing an external module that i downloaded using pip package manager
import docx

print(instances.band_members)
print(instances.kilometers_to_meters(2))

print(fractions.Fraction(10, 11))
print(fractions.Fraction(42, 12))

print(docx.ImagePart)