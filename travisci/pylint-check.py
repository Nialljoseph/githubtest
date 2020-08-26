from pylint.lint import Run
main():
  file = input("Enter the name of the file you would like to check: ")
  Run['--errors-only', file]

main()
