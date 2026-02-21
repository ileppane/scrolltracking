
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    # built-in constants
    NAME_IN_URL = 'scrolltracking_demo_twobuttons'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 24
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    choice = models.IntegerField()
    dectime = models.FloatField()
    dectime_end = models.FloatField()
    time_startscrolling = models.FloatField()
    time_endscrolling = models.FloatField()
    scrolltime = models.FloatField()
    x = models.StringField()
    y = models.StringField()
    psiL = models.FloatField()
    psiR = models.FloatField()
    dwelltimeL = models.FloatField()
    dwelltimeR = models.FloatField()
    switchesLR = models.IntegerField()
    switchesRL = models.IntegerField()
    lastdwell = models.IntegerField()
    xdist = models.FloatField()
class Instructions(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
class Decision(Page):
    form_model = 'player'
    form_fields = ['choice', 'x', 'y', 'time_startscrolling', 'time_endscrolling', 'dectime_end', 'lastdwell']
    @staticmethod
    def js_vars(player: Player):
        return dict( choice1 = 'Product 1',  choice2 = 'Product 2' )
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # dectime ends when the button is clicked
        player.dectime = round((player.dectime_end - player.time_startscrolling)/1000,3)
        
        # scrolltime ends when the last x coordinate is recorded
        player.scrolltime = round((player.time_endscrolling - player.time_startscrolling)/1000,3)
        
        
        ### CALCULATING THE PROCESS TRACING METRICS psiL and psiR
        ##
        import ast
        x = ast.literal_eval(player.x)
        y = ast.literal_eval(player.y)
        
        # the below line removes the first element(s) from x; reason: x always has more points than y 
        # this is because the divs are initially blank and show only after scrolling about 3px, but 
        # y starts recording only after divs are shown
        x = x[(len(x)-len(y)):len(x)]
        
        # total distance travelled in x-direction
        player.xdist = sum(abs(x[i+1]-x[i]) for i in range(len(x)-1))
        
        # append the points to make a curve; the right/left "dwell" starts when x crosses 150 and ends when it crosses 150 again
        xyright = []
        xyleft = []
        for j in range(len(x)):
            if (j>0) and (x[j-1]<=150 and x[j]>150) or (x[j-1]>=150 and x[j]<150): xyright.append([150,y[j]])
            if (j>0) and (x[j-1]<=150 and x[j]>150) or (x[j-1]>=150 and x[j]<150): xyleft.append([150,y[j]])
            if x[j]>=150: xyright.append([x[j],y[j]])
            if x[j]<150: xyleft.append([x[j],y[j]])
        
        # add the vertical midpoint line on both
        xyright.append([150,y[-1]])
        xyright.append([150,y[0]])
        xyleft.append([150,y[-1]])
        xyleft.append([150,y[0]])
        
        # add the horizontal lines
        if x[0]<150: xyleft.append([x[0],y[0]])
        if x[0]>=150: xyright.append([x[0],y[0]])
        if x[-1]<150: xyleft.append([x[0],y[0]])
        if x[-1]>=150: xyright.append([x[0],y[0]])
        
        # calculate psiR using xyright
        l = len(xyright)
        s = 0.0
        for i in range(l):
            j = (i+1)%l  # keep index in [0,l)
            s += (xyright[j][0] - xyright[i][0])*(xyright[j][1] + xyright[i][1])
        
        psiR = -0.5*s
        
        # calculate psiL using xyleft
        l = len(xyleft)
        s = 0.0
        for i in range(l):
            j = (i+1)%l  # keep index in [0,l)
            s += (xyleft[j][0] - xyleft[i][0])*(xyleft[j][1] + xyleft[i][1])
        
        psiL = -0.5*s
        
        player.psiL = abs(psiL)
        player.psiR = abs(psiR)
        
        ### CALCULATING PROCESS TRACING METRICS dwelltimeL, dwelltimeR and switchesLR, switchesRL
        ##
        dwelltimeleft = 0
        dwelltimeright = 0
        lr = 0
        rl = 0
        for i in range(1,len(y)):
            # dwelltimes
            if x[i] < 150:
                dwelltimeleft += y[i]-y[i-1]
            if x[i] >= 150:
                dwelltimeright += y[i]-y[i-1]
            # switches
            if i==1: # first switch added separately because stimuli become visible only after a bit of scrolling
                if x[i] > 150: lr += 1 
                if x[i] < 150: rl += 1
            if x[i-1] >= 150 and x[i] < 150: # going from right to left
                rl += 1
            if x[i-1] <= 150 and x[i] > 150: # going from left to right
                lr += 1
        
        player.dwelltimeR = round(.001*dwelltimeright,3)
        player.dwelltimeL = round(.001*dwelltimeleft,3)
        player.switchesLR = lr
        player.switchesRL = rl
        
class ResponseCurve(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        import ast
        x = ast.literal_eval(player.x)
        y = ast.literal_eval(player.y)
        
        return dict(x = x, y = y)
    @staticmethod
    def js_vars(player: Player):
        import ast
        x = ast.literal_eval(player.x)
        y = ast.literal_eval(player.y)
        
        return dict(x = x, y = y)
page_sequence = [Instructions, Decision, ResponseCurve]