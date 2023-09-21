class player:
   def play(self):
     print("the player is playing cricket.")

class batsman(player):
  def play(self):
    print("the batsman is batting.")

class bowler(player):
  def play(self):
    print("the bowler is bowling.")

#create objects of barsman and bowler class and call the play() method for each
batsman=batsman()
bowler=bowler()

batsman.play() # output:"the batsman is batting."
bowler.play() # output:"the bowler is bowling."