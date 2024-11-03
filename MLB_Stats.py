def main():
  hitting = open("MLB_Hitting.csv", 'r')
  pitching = open("MLB_Pitching.csv", 'r')

  for line in hitting:
    info = line.split(",")
    runsS = info[3]

  for line in pitching:
    info = line.split(",")
    team = info[0]
    runsA = info[3]
    wins = info[4]
    losses = info[5]
    era = info[7]

    print(team, "had", runsS, "runs per game versus", runsA, "runs allowed. Their earned run average was", era, "ending the season with", wins, "wins and",losses, "losses.")
    
  hitting.close()
  pitching.close()

if __name__ == '__main__':
  main()