from pylint.lint import Run
main():
  file = input("Enter the name of the file you would like to check the rating of: ")
  score = Run['--errors-only', file]
  final_score = score.linter.stats['global_note']
  if final_score >= 6:
    return True
  else:
    return False

main()
