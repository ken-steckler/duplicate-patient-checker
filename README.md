# Duplicate Patient Checker

---

### Description
A duplicate patient checker that uses the CSV Python library to return a list of names that are duplicates.

### Purpose
Duplicate patient profiles are an issue and can cause problems down the road, such as billing the wrong insurance or not knowing what
other medications the patient is taking. I was tasked to merge all duplicate patients in our pharmacy software so that there
would be no more duplicate profiles.

### Process
I used the Python's CSV library to iterate through a CSV file that is exported from the pharmacy software. The program first
sorts the names by alphabetical order and then checks to see if there are any duplicates by comparing the current name to the next.
If the names and date of births match, then it returrns the names.

---

### Note
This was created using the RXQ pharmacy software. Line 12 depends on the location of first name, last name and date of birth, so it
may be different with other softwares and may need to adjusted. Additionally, this program does not account for nicknames (for example,
it will not recognize "Tom" vs "Thomas").

---

### Technology Used
Python <br />
Pycharm
