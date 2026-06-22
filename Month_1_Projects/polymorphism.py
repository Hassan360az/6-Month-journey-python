class Instruction:
    def call_them(self):
        print ("Please come all the members 0 !")


class User1:
    def call_them (self):
        print("please come all the members 1 !")

class User2:
    def call_them (self):
        print ("Please come all the membebrs 2 !")


members_list = [Instruction(), User1(), User2()]

for members in members_list:
    members.call_them()