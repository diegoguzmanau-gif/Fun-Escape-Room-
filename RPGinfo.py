class RPGInfo():
    author = "Diego Guzman" #what a handsome cool name!
    
    def __init__(self, game_title):
        self.title = game_title
    
    def welcome(self):
        print("Welcome to " + self.title)

    @staticmethod
    def info():
        print("I definitely did not copy this code from the teacher :)")
        print("there are 2 ways to finish the game, good luck!") #should i add more? no ones going to see this anyways...

    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print("Created by " + cls.author)
        print("""
         _____
        /     \\
       |  o o  |
       |   ^   |
        \\ \\_/ /
         \\___/
        """)#hahahahahaahhaha