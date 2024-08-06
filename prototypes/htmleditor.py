import htmlgenerator as hgen

title = "9-best-beaches"

# Open a file for writing
file = open(f"{title}.html", "w")

# Write content to the file

a = hgen.initial(title)
b = hgen.boilerplate()
d = hgen.page('TRA00201','Baia-do-Sancho','Baia do Sancho, Brazil',"Located in the Fernando de Noronha archipelago, Baia do Sancho is consistently ranked as one of the world's best beaches for its pristine white sand, clear blue waters, and dramatic cliffs.",1)
n = hgen.ending()

file.write(a)
file.write(b)
file.write(d)
file.write(n)


# Close the file
file.close()