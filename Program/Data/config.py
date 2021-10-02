import Advert_Cycle
import Classes
import Data_Access
import Fund_Transfer
import Loading_Screen
import Message_Windows
import PIN_Screen
import Select_Card
import Select_Options_Window
import Window
import Withdraw_Cash



BLUE = "#3380cc"
DARK_BLUE = '#123546'

win = None
screen = None

TIMER = True
EN_NUMPAD = False
NEXT_WINDOW = False
ENTRY_BOX = False
TEXT_LIMIT = 0

CURR_USER_ACC = None
RECEIVER_ACC = None
CURR_CARD = False
CARD_REMOVE = False
CAN_TERMINATE = False

CH_PINS = [0,0]



#Advert SCreen Control
CYCLE = True
