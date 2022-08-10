AI 801 - Team 2

There are two ways to run the files:

The first is by double clicking the main_PlayGame.py and playing from the terminal.
This is the prefered method as inputs will be taken properly (Spyder was hanging up for some unknown reason).
    Note:  There is some error catching but not enough that you can't break the game if you wanted to.  
            It was not our primary concern and will be worked out in QA.
    
The file main_BatchTests.py will run through 250 games for board sizes 5, 6, 7, 8, 9, and 10x10.  It will output the results in the TTT_Data.txt file.
  This is *NOT* the prefered way to run the batch tests as you'll need to modify the code if you want to look at different conditions.
  Thus, the second method of running the code is preferable.
  

The second method of running the files is:

1) Open up the IDE of your choice, set your directory path, and run the files:
     a)  main_BatchTests.py
          Authors:
     Brandon Botzer - Penn State AI-801, Summer 2022, TEAM 2
    
      Purpose:
          To run multiple games of TTT for testing results.

      How to use this code:

          Please note, this code was written for tests and as such, a base knowledge
          of how the code should function is needed.  The following information shall
          help you determine what needs to change depending on what test you are running.

          In line 42, select which board sizes you'd like to test.
              NOTE: If testing the 3x3 board, enter: range(3,4)
              NOTE: If testing larger board sizes: range(5,7)
                      This will test board sizes 5 and 6
                      You are able to test boards 5 --> 10
                      To do so, enter: range(5,11)
                      THERE IS NO TEST FOR A BOARD SIZE OF 4

          In line 53, select the number of games you'd like to simulate at each baord size
              NOTE: Large board sizes take considerable amount of time to run tests on
                      It is best practice to run large boards by themselves and at a lower
                      number of games.


          Lines 85 - 95 contain the various move sets for the tests:
              Line 8 contains the AI miniMax Player.
              Line 9 contains the AI miniMax Computer.
              Line 9 continas the random Player.

              These players can be commented out to determine what the AI computer is up against
              They can also be shuffled in their order to determine the starting player


          To assign the proper Depth Limit for the searching algormithm, you must go into 'takeTurns_ab_dls.py'
              in the miniMax function, you will see a value for the depth limit.
              this value represents how deep the search tree will go before it ignores win conditions and returns the heuristic
                  NOTE: FOR LARGE BOARD SIZES, VALUES ABOVE ONE FOR THE DLS WILL CAUSE EXTREAMLY LONG RUNTIMES

          Please ensure that the TTT_Data.txt file has been created in your repository.  This is where the run data will be stored.

          In the last few lines, make sure you have updated your output to reflect what tests you are running.

          Once ready, you are free to run the code and test.
     
     
     
     b)  main_PlayGame.py
     
          This is the main driver for the Tic Tac Topia AI project.

          Author:
              Brandon Botzer-Penn State AI-801, Summer 2022, TEAM 2



          Purpose:
              This code is designed to allow a human player to play against the AI.
              You can play on 3x3, 5x5, 6x6, 7x7, 8x8, 9x9, or 10x10 boards.


          How to use this code:
              Enter the n dimentision of the n x n board you wish to play on.

              Enter if the Player is first (yes) or the AI is first (no)

              For some reason I still do not understand, the text entry sometimes hangs up
              and freezes.  Stopping the program and then rerunning it will often work to fix the problem.
              However, this may mean that you may not be able to finish a game.  Because of this we've decided not
              to put the human moves into a function call as it seems that the functions hang up on the input()
              more often than just leaving them in the main.

              The easier method to run this is to just launch main_PlayGame.py from the file itself and have 
              it play within the terminal.

              Not that it matters because you are unable to win BWAHAHAHAHA
              
              





