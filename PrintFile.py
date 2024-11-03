def main():
  myFile = open("qbdata.txt", 'r')

  for line in myFile:
    info = line.split("	")
    td = info[7]
    name = info[0]
    rate = info[9]
    print(name, "had a rating of", rate, "and threw", td, "touchdowns.")
    
  myFile.close()

if __name__ == '__main__':
  main()
