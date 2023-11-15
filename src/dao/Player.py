class Player:
    def __init__(self, username, nbGamePlayed, nbGameWin, wallet, bankrupt, nbBlackjack):
      self.username = username
      self.nbGamePlayed = nbGamePlayed
      self.nbGameWin = nbGameWin
      self.wallet = wallet
      self.bankrupt = bankrupt
      self.nbBlackjack = nbBlackjack

    def getUsername(self):
       return self.username
    
    def getNbGamePlayed(self):
       return self.nbGamePlayed
    
    def getNbGameWin(self):
       return self.nbGameWin
    
    def getWallet(self):
       return self.wallet
    
    def getBankrupt(self):
       return self.bankrupt
    
    def getNbBlackjack(self):
       return self.nbBlackjack
    
    def setNbGamePlayed(self, new):
       self.nbGamePlayed = new
    
    def setNbGameWin(self, new):
       self.nbGameWin = new
    
    def setWallet(self, new):
       self.wallet = new
    
    def setBankrupt(self, new):
       self.bankrupt = new
    
    def setNbBlackjack(self, new):
       self.nbBlackjack = new
