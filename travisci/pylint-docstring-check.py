from pylint.lint import Run
main():
  file = input("Enter the name of the file you would like to check for missing docstrings: ")
  #missing-docstring (C0111)
  score = Run['missing-docstring', file]

main()
