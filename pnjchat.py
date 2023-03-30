from Constant import PR_AGGRESSIVE
from Constant import PR_FRIENDLY
from Constant import DEBUG

from openaiconnect import message
questtest ="Quete: 'Abbatre 5 membres du gang eau chaude'"
chatjoueur = input(">")
promptaggro =  DEBUG + PR_AGGRESSIVE + chatjoueur +"Je viens te defier !"
promptfriend = DEBUG + questtest + PR_FRIENDLY

# print(promptfriend)
# print (prompt)
message(promptfriend)


