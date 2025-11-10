###
# A program for printing detailed information.
#
employee = "Mr. John May, born on 1998-02-16"
print(f'Name: {employee[4:8]}')
print(f'Surname: {employee[9:12]}')
print(f'Born: {employee[-10:]}')
print(f'Initials: {employee[4]+employee[9]}')

## bierzemy pod uwagę wszytskie znaki
## [2:4] drugi znak w tym nawiasie nie pokaże się "jest do niego ale bez niego"