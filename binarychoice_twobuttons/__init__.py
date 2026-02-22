
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    # built-in constants
    NAME_IN_URL = 'binarychoice_twobuttons'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 120
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    prolificcode = models.StringField()
    gender = models.StringField(choices=[['male', "men's trainers"], ['female', "women's trainers"]], label='<p>I would like to see ...</p>', widget=widgets.RadioSelect)
    shoeorder = models.StringField()
    shoeratings = models.StringField()
    shoepairs = models.StringField()
    thisround_shoepair = models.StringField()
    choice = models.IntegerField()
    lastdwell = models.IntegerField()
    dectime_end = models.FloatField()
    dectime = models.FloatField()
    scrolltime = models.FloatField()
    time_startscrolling = models.FloatField()
    time_endscrolling = models.FloatField()
    x = models.StringField()
    y = models.StringField()
    psiL = models.FloatField()
    psiR = models.FloatField()
    thisround_shoe1rating = models.IntegerField()
    thisround_shoe2rating = models.IntegerField()
    thisround_valuedifference = models.IntegerField()
    ismobile_touchstart = models.IntegerField(blank=True, initial=0)
    screenwidth = models.StringField(blank=True, initial='')
    screenheight = models.StringField(blank=True, initial='')
    dwelltimeL = models.FloatField()
    dwelltimeR = models.FloatField()
    switchesLR = models.IntegerField()
    switchesRL = models.IntegerField()
    xdist = models.FloatField()
def stimuliorder(player: Player):
    pass
class MobileCheck(Page):
    form_model = 'player'
    form_fields = ['ismobile_touchstart', 'screenwidth', 'screenheight']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    @staticmethod
    def vars_for_template(player: Player):
        session = player.session
        return dict( pilot = session.config['pilot'] )
class Information(Page):
    form_model = 'player'
    form_fields = ['prolificcode']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
class Instructions(Page):
    form_model = 'player'
    form_fields = ['gender']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        session = player.session
        ###
        # Randomise the order of shoes
        ##
        import random
        
        
        maleshoes = ['13106703','13120641','13120626','12118603','16105642','12167703','16105601','12126118','12102103','12126140','13115602','13107203','12167727','16105627','12167740','13110701','13120603','12102140','12105303','16106101','13110703','12156040','12118630','12126103','21300503','12102167','21127840','12100403','21310803','21201127','12105340','12344303','12100418','21127803','12167702','21223903','12167718','12102144','12126172','12116803','12126147','12100430','12105301','13110730','13120703','12100540','12102174','12139947','12156027','21233703','12134603','21158040','12192203','12100503','12100440','13118503','12167746','12100427','12141003','12139902','21141240','12141025','12100522','21313803','13100903','21116240','12100469','13107201','16105640','11484401','12134630','12105403','12121025','12118640','15129641','12114503','21233907','12134640','11003201','15133302','11044501','21144303','12227401','12134602','21303008','16105030','16106203','12327127','21303018','12121022','12121041','16105637','16105003','12192218','12100415','16105669','12105331','12599702','15129630','12128127','12103340','12105408','21127801','12192241','21157801','12115340','12103308','12327103','12116002','14532403','15100903']
        
        if session.config['pilot'] == 1:
            maleshoes = maleshoes[0:10]
        
        femaleshoes = ['27316903','27403330','27403303','27116503','21523003','27415901','27116540','27116501','27434132','27458003','21523007','27434101','27401667','21611503','27315203','27410901','27400303','27304603','27410902','27403340','27417640','27415927','27313803','27400340','27400301','21410803','21408340','21610503','27314003','27400335','27306543','21610524','27400370','27417603','27405642','27417641','27419403','27434131','27128303','21482506','27116525','27116544','27314025','21411406','27419401','27300712','27047602','27016940','27419427','27419440','27402441','27116040','14615701','27403840','27159840','21473907','27423569','27315227','27402430','21410806','27074327','27405640','27012903','27401603','27315103','27428801','27405636','27401601','27401636','27405027','21414906','27458306','27304307','27405630','27033018','27121002','27435032','21415407','27456831','21411403','27116572','21622203','27116569','27151640','27400330','21408324','27313830','27458001','27410931','27400337','27405631','21473901','21411430','21414903','27428803','27116571','27411030','27116519','27401607','27417642','27400367','27400203','21611524','27306303','27124640','21601002','27423501','27415903','21414942','27314006','27409141']
        
        random.shuffle(maleshoes)
        random.shuffle(femaleshoes)
        
        maleshoes = [eval(i) for i in maleshoes]
        femaleshoes = [eval(i) for i in femaleshoes]
        
        if player.gender == 'male':
            player.shoeorder = str(maleshoes)
        else:
            player.shoeorder = str(femaleshoes)
        
class Preference(Page):
    form_model = 'player'
    form_fields = ['shoeratings']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    @staticmethod
    def vars_for_template(player: Player):
        import ast
        shoeorder = ast.literal_eval(player.shoeorder)
        
        divs = ''
        for i in range(len(shoeorder)):
            #divs += 'shoe' + str(i) + ': ' +  # used for testing
            divs += '<span id=\"shoe' + str(i) + 'rating\" hidden></span>'
        
        return dict( divs = divs, shoeorder = shoeorder )
    @staticmethod
    def js_vars(player: Player):
        import ast
        
        shoeorder = ast.literal_eval(player.shoeorder)
        
        imagelist = ["https://www.sportsdirect.com/images/products/" + str(x) + "_h.jpg" for x in shoeorder]
        
        return dict( numberofshoes = len(shoeorder), shoeorder = shoeorder, imagelist = imagelist )
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        ###
        # Here the pairs are created based on preference ratings
        ###
        import random
        import ast
        shoeorder = ast.literal_eval(player.shoeorder)
        shoeratings = ast.literal_eval(player.shoeratings)
        
        ###
        # PHILIASTIDES & RATCLIFF: CONTINUUM OF DIFFERENCE RATINGS, VALUES BETWEEN -3 TO 3,
        # WHO HAD 50 TRIALS PER DIFFERENCE RATING = TOTAL 350 PAIRS FOR EACH BLOCK (700 TRIALS)
        
        # make two long shoelists as pair candidates
        shoelist1 = []
        shoelist2 = []
        for i in range(len(shoeorder)):
            shoelist1 += [shoeorder[i]] * (len(shoeorder)-1)
            shoelist2 += [x for x in shoeorder if x != shoeorder[i]]
        
        # calculate value differences in these long shoelists
        valuediff = []
        for i in range(len(shoelist1)):
            shoe1rating = shoeratings[shoeorder.index(shoelist1[i])] # rating of shoe in shoelist1
            shoe2rating = shoeratings[shoeorder.index(shoelist2[i])] # rating of shoe in shoelist1
            # value difference shoe1 - shoe2
            valuediff.append(shoe1rating - shoe2rating)
        
        # create a long pair list
        # NOTE: 105 PAIRS WILL BE FORMED, SO 105 IS THE MAXIMUM POSSIBLE NUMBER OF ROUNDS
        # BELOW HAS CHANGED 9/10/2024: 15 REPLACD BY 20
        longpairs = []
        for i in range(len(shoelist1)):
            longpairs.append([shoelist1[i],shoelist2[i]])
        
        # then choose 20*7=140 values uniformly from the valuediff list to form the final pairings 
        # do not use value differences < -3 or > 3
        shoepairs = []
        for diff in range(-3,4):
            indices = [i for i in range(len(valuediff)) if valuediff[i] == diff]
            longpairs_diff = [longpairs[i] for i in indices]
            if len(longpairs_diff) >= 20:
                shoepairs += random.sample(longpairs_diff, 20) # sample without replacement
            elif len(longpairs_diff) > 0:
                shoepairs += random.choices(longpairs_diff, k=20) # if there are less than 20, sample with replacement
            else:
                shoepairs += [] # if there are no longpairs with a specific value difference, then this will remain shorter
        
        # in an exceptional case add pairs so that total number of shoepairs is 20*7
        if len(shoepairs) < 20*7:
            shoepairs += random.choices(longpairs, k=(20*7 - len(shoepairs)))
        
        
        # randomise the order of shoepairs presented during the study
        random.shuffle(shoepairs)
        
        # the pair for each shoe can now be found in this variable: player.in_round(1).shoepairs
        player.shoepairs = str(shoepairs)
class Instructions2(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
class PreDecision(Page):
    form_model = 'player'
    timeout_seconds = 1
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        session = player.session
        # 7/10/2024 removed: 21307202, 12156043, 15128203, 13120630
        # this leaves 111 shoes 
        maleshoes = ['13106703','13120641','13120626','12118603','16105642','12167703','16105601','12126118','12102103','12126140','13115602','13107203','12167727','16105627','12167740','13110701','13120603','12102140','12105303','16106101','13110703','12156040','12118630','12126103','21300503','12102167','21127840','12100403','21310803','21201127','12105340','12344303','12100418','21127803','12167702','21223903','12167718','12102144','12126172','12116803','12126147','12100430','12105301','13110730','13120703','12100540','12102174','12139947','12156027','21233703','12134603','21158040','12192203','12100503','12100440','13118503','12167746','12100427','12141003','12139902','21141240','12141025','12100522','21313803','13100903','21116240','12100469','13107201','16105640','11484401','12134630','12105403','12121025','12118640','15129641','12114503','21233907','12134640','11003201','15133302','11044501','21144303','12227401','12134602','21303008','16105030','16106203','12327127','21303018','12121022','12121041','16105637','16105003','12192218','12100415','16105669','12105331','12599702','15129630','12128127','12103340','12105408','21127801','12192241','21157801','12115340','12103308','12327103','12116002','14532403','15100903']
        
        if session.config['pilot'] == 1:
            maleshoes = maleshoes[0:10]
        
        
        # 7/10/2024 removed: 27406969, 21610502, 27316969, 27423506
        # this leaves 111 shoes
        femaleshoes = ['27316903','27403330','27403303','27116503','21523003','27415901','27116540','27116501','27434132','27458003','21523007','27434101','27401667','21611503','27315203','27410901','27400303','27304603','27410902','27403340','27417640','27415927','27313803','27400340','27400301','21410803','21408340','21610503','27314003','27400335','27306543','21610524','27400370','27417603','27405642','27417641','27419403','27434131','27128303','21482506','27116525','27116544','27314025','21411406','27419401','27300712','27047602','27016940','27419427','27419440','27402441','27116040','14615701','27403840','27159840','21473907','27423569','27315227','27402430','21410806','27074327','27405640','27012903','27401603','27315103','27428801','27405636','27401601','27401636','27405027','21414906','27458306','27304307','27405630','27033018','27121002','27435032','21415407','27456831','21411403','27116572','21622203','27116569','27151640','27400330','21408324','27313830','27458001','27410931','27400337','27405631','21473901','21411430','21414903','27428803','27116571','27411030','27116519','27401607','27417642','27400367','27400203','21611524','27306303','27124640','21601002','27423501','27415903','21414942','27314006','27409141']
        
        for i in range(0, len(maleshoes)): maleshoes[i] = int(maleshoes[i])
        for i in range(0, len(femaleshoes)): femaleshoes[i] = int(femaleshoes[i])
        
        # THE maleshoes, femaleshoes VARIABLES ABOVE DON'T DO ANYTHING???
        
        # Determine the pair of shoes for this round and calculate their ratings and valuedifference
        import ast
        shoepairs = ast.literal_eval(player.in_round(1).shoepairs)
        thisround_shoepair = shoepairs[player.round_number-1]
        shoeorder = ast.literal_eval(player.in_round(1).shoeorder)
        shoeratings = ast.literal_eval(player.in_round(1).shoeratings) # ratings = subjective preferences givien by player
        
        player.thisround_shoepair = str(thisround_shoepair)
        player.thisround_shoe1rating = int(shoeratings[shoeorder.index(thisround_shoepair[0])])
        player.thisround_shoe2rating = int(shoeratings[shoeorder.index(thisround_shoepair[1])])
        player.thisround_valuedifference = player.thisround_shoe1rating - player.thisround_shoe2rating
        
class Decision(Page):
    form_model = 'player'
    form_fields = ['choice', 'dectime_end', 'x', 'y', 'time_startscrolling', 'time_endscrolling', 'lastdwell']
    @staticmethod
    def vars_for_template(player: Player):
        import ast
        shoepair = ast.literal_eval(player.thisround_shoepair)
        
        return dict( 
            shoeimage1 = 'https://www.sportsdirect.com/images/products/' + str(shoepair[0]) + '_h.jpg',
            shoeimage2 = 'https://www.sportsdirect.com/images/products/' + str(shoepair[1]) + '_h.jpg',
            beginning = player.round_number <=3
        )
    @staticmethod
    def js_vars(player: Player):
        return dict( choice1 = 'Product A',  choice2 = 'Product B' )
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
    def is_displayed(player: Player):
        session = player.session
        # display in pilot only for the first 3 rounds
        return session.config['pilot'] == 1 and player.round_number <=3
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
class Results(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS
    @staticmethod
    def vars_for_template(player: Player):
        session = player.session
        return dict(
            prolificurl = session.config['prolificurl']
        )
page_sequence = [MobileCheck, Information, Instructions, Preference, Instructions2, PreDecision, Decision, ResponseCurve, Results]