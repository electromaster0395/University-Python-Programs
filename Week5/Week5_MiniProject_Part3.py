frames = ["*    ",
          " *   ",
          "  *  ",
          "   * ",
          "    *",
          "   * ",
          "  *  ",
          " *   ",
          "*    ",]

def printPattern(pattern, times):
    if(times == None):
        while True:
            for j in range(len(frames)-1):
                print(frames[j])

    else:
        for i in range(0, times):
            for j in range(len(frames)-1):
                print(frames[j])
    print(frames[len(frames) - 1])

printPattern(frames, None)
