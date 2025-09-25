from functions.get_file_content import get_file_content

print(get_file_content("calculator", "main.py"))                   # should include 'def main():'
print(get_file_content("calculator", "pkg/calculator.py"))         # should include 'def _apply_operator(self, operators, values)'
print(get_file_content("calculator", "/bin/cat"))                  # should start with 'Error:'
print(get_file_content("calculator", "pkg/does_not_exist.py"))     # should start with 'Error:'