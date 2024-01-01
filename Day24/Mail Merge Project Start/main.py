PLACEHOLDER = '[name]'

with open("C:\\Users\\Dell\\Desktop\\100 days of code\\Day24\\Mail Merge Project Start\\Input\\Names\\person_name", "r") as name_filter:
   names = name_filter.readlines()  # Call the read() method


with open("C:\\Users\\Dell\\Desktop\\100 days of code\\Day24\\Mail Merge Project Start\\Input\\Letters\\letter", "r") as letter_file:
      letter = letter_file.read()
      for name in names:
         name = name.strip()
         new_letters =letter.replace(PLACEHOLDER, name)

         with open (f"Day24/Mail Merge Project Start/All_letter/{name}letter.txt" , mode="w") as new_letter:
               new_letter.write(new_letters)