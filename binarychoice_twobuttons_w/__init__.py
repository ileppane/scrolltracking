
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    # built-in constants
    NAME_IN_URL = 'binarychoice_twobuttons_w'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 120
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    prolificcode = models.StringField()
    gender = models.StringField(choices=[['male', "men's products"], ['female', "women's products"]], label='<p>I would like to see ...</p>', widget=widgets.RadioSelect)
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
def watchid(player: Player):
    malewatches = ['watch-collection-flagship-heritage-l4-815-4-52-2-1726053625-thumbnail.png?w=2400',
     'watch-collection-flagship-heritage-l4-815-4-52-2-1726053625-thumbnail.png?w=2400',
     'watch-collection-longines-legend-diver-l3-764-4-99-6-1726058741-thumbnail.png?w=2400',
     'watch-collection-longines-legend-diver-l3-764-4-50-7-1726058723-thumbnail.png?w=2400',
     'watch-collection-longines-legend-diver-l3-764-4-50-7-1726058723-thumbnail.png?w=2400',
     'watch-collection-longines-legend-diver-l3-764-4-90-7-1726058741-thumbnail.png?w=2400',
     'watch-collection-longines-legend-diver-l3-764-4-06-6-1726058739-thumbnail.png?w=2400',
     'watch-collection-longines-legend-diver-l3-764-4-96-6-1726058752-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-835-4-32-9-1726058719-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-790-4-06-6-1726058081-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-843-4-93-2-1726058079-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-919-4-92-0-1726057243-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-919-4-92-6-1726055254-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-782-4-06-9-1726055300-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-782-4-06-6-1726055299-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-909-4-97-6-1726055251-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-909-4-97-0-1726057241-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-909-4-77-6-1726055248-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-909-4-77-3-1726057239-thumbnail.png?w=2400',
     'watch-collection-flagship-heritage-l4-815-4-62-2-1726053626-thumbnail.png?w=2400',
     'watch-collection-flagship-heritage-l4-815-4-02-2-1726053625-thumbnail.png?w=2400',
     'watch-collection-flagship-heritage-l4-815-4-78-2-1726058068-thumbnail.png?w=2400',
     'watch-collection-flagship-heritage-l4-815-4-92-2-1726058069-thumbnail.png?w=2400',
     'watch-collection-flagship-heritage-l4-815-4-72-2-1726058067-thumbnail.png?w=2400',
     'watch-collection-la-grande-classique-de-longines-l4-755-4-51-6-1726057322-thumbnail.png?w=2400',
     'watch-collection-longines-legend-diver-l3-764-4-90-2-1726058138-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-802-1-53-6-1726058753-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-802-1-53-6-1726058753-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-802-5-53-6-1726058054-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-802-5-53-6-1726058054-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-802-5-53-2-1726058053-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-802-5-53-2-1726058053-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-802-4-63-6-1726058050-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-802-4-63-6-1726058050-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-802-4-63-2-1726058049-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-802-4-93-6-1726058052-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-821-5-53-2-1726058754-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-821-5-59-2-1726058754-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-821-4-53-6-1726058016-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-821-4-53-2-1726058015-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-821-4-93-6-1726058019-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-821-4-93-2-1726058018-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-781-4-96-6-1726055166-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-781-4-96-9-1726055167-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-781-4-56-6-1726057312-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-780-4-56-9-1726056419-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-781-4-05-6-1726058027-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-781-4-05-2-1726058026-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-890-4-96-6-1726058153-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-890-4-96-9-1726058154-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-890-4-56-6-1726058152-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-890-4-56-9-1726058153-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-890-4-06-6-1726058151-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-790-4-06-2-1726058115-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-830-4-02-6-1726058046-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-830-4-02-6-1726058046-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-830-4-92-6-1726058031-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-830-4-92-6-1726058031-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-830-4-52-6-1726058028-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-830-4-52-6-1726058028-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-835-4-32-6-1726058071-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-835-4-32-6-1726058071-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-835-4-02-6-1726058177-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-835-4-91-2-1726058145-thumbnail.png?w=2400',
     'watch-collection-ultra-chron-l2-836-4-52-6-1726057409-thumbnail.png?w=2400',
     'watch-collection-ultra-chron-l2-836-4-52-2-1726057408-thumbnail.png?w=2400',
     'watch-collection-longines-legend-diver-l3-374-4-90-2-1726057336-thumbnail.png?w=2400',
     'watch-collection-longines-pilot-majetek-l2-838-1-53-2-1726058746-thumbnail.png?w=2400',
     'watch-collection-longines-pilot-majetek-l2-838-4-53-0-1726058011-thumbnail.png?w=2400',
     'watch-collection-longines-pilot-majetek-l2-838-4-53-8-1726058012-thumbnail.png?w=2400',
     'watch-collection-longines-pilot-majetek-l2-838-4-53-2-1726058012-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-793-4-73-2-1726057985-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-773-4-71-2-1726058076-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-773-4-78-3-1726057220-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-919-4-78-3-1726057246-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-909-4-92-6-1726055250-thumbnail.png?w=2400',
     'watch-collection-conquest-heritage-l1-648-4-78-2-1726058142-thumbnail.png?w=2400',
     'watch-collection-conquest-heritage-l1-648-4-62-2-1726058141-thumbnail.png?w=2400',
     'watch-collection-conquest-heritage-l1-648-4-52-2-1727115413-thumbnail.png?w=2400',
     'watch-collection-flagship-heritage-l4-795-4-78-2-1726055044-thumbnail.png?w=2400',
     'watch-collection-conquest-heritage-l1-649-4-72-2-1726058131-thumbnail.png?w=2400',
     'watch-collection-conquest-heritage-l1-649-4-52-2-1726058111-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-793-5-72-7-1726058760-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-793-5-72-7-1726058760-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-793-5-70-7-1726058759-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-793-5-70-7-1726058759-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-793-5-70-2-1726058758-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-793-5-70-2-1726058758-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-835-4-98-9-1726058745-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-835-4-98-9-1726058745-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-835-4-02-9-1726058745-thumbnail.png?w=2400',
     'watch-collection-la-grande-classique-de-longines-l4-908-4-51-6-1726055371-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-835-4-98-6-1726058720-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-720-4-92-6-1726058196-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-793-5-72-2-1726058776-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-720-4-62-6-1726058195-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-720-4-52-6-1726058195-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-720-4-02-6-1726058194-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-720-4-72-6-1726058177-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-844-8-71-2-1726058147-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-844-6-71-2-1726058146-thumbnail.png?w=2400',
     'watch-collection-la-grande-classique-de-longines-l4-755-2-11-7-1726055034-thumbnail.png?w=2400',
     'watch-collection-la-grande-classique-de-longines-l4-755-4-11-2-1726055034-thumbnail.png?w=2400',
     'watch-collection-longines-legend-diver-l3-764-4-50-0-1726058135-thumbnail.png?w=2400',
     'watch-collection-conquest-heritage-l1-650-4-72-2-1726058132-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-821-1-53-2-1726058130-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-821-1-53-6-1726058128-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-790-4-66-2-1726058117-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-790-4-56-9-1726058116-thumbnail.png?w=2400',
     'watch-collection-conquest-heritage-l1-650-4-52-2-1726058112-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-843-4-73-2-1726058110-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-843-4-73-2-1726058110-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-773-4-71-6-1726058095-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-773-4-71-6-1726058095-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-773-4-61-6-1726058094-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-773-4-61-6-1726058094-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-773-4-61-2-1726058093-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-773-4-61-2-1726058093-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-673-4-61-6-1726058092-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-673-4-61-2-1726058091-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-835-4-72-6-1726058088-thumbnail.png?w=2400',
     'watch-collection-la-grande-classique-de-longines-l4-755-2-11-2-1726055033-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-673-4-71-6-1726058087-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-790-4-96-9-1726058086-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-790-4-96-6-1726058084-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-790-4-66-6-1726058083-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-790-4-56-6-1726058082-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-843-4-63-2-1726058077-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-673-4-71-2-1726058075-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-835-4-92-6-1726058073-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-835-4-52-6-1726058072-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-812-5-53-9-1726058059-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-812-5-53-6-1726058058-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-812-5-53-2-1726058057-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-802-5-53-9-1726058055-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-802-4-93-2-1726058051-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-802-4-53-6-1726058048-thumbnail.png?w=2400']
    
    # remove duplicates
    malewatches = list(set(malewatches))
    
    # use the first 111
    malewatches = malewatches[0:111]
    #malewatches = malewatches[0:10]
    
    
    femalewatches = ['watch-collection-conquest-l3-430-5-72-9-1726058175-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-430-5-72-9-1726058175-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-430-4-99-6-1726058717-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-430-4-99-6-1726058717-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-430-4-92-6-1726058716-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-430-4-92-6-1726058716-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-430-4-02-6-1726058714-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-430-4-02-6-1726058714-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-410-4-53-6-1726056383-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-410-4-63-6-1726057202-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-410-4-53-0-1726056382-thumbnail.png?w=2400',
     'watch-collection-longines-legend-diver-l3-374-4-80-0-1726055151-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-410-4-63-2-1726056384-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-410-4-93-6-1726056386-thumbnail.png?w=2400',
     'watch-collection-longines-legend-diver-l3-374-4-40-2-1726057335-thumbnail.png?w=2400',
     'watch-collection-longines-legend-diver-l3-374-4-50-0-1726055147-thumbnail.png?w=2400',
     'watch-collection-longines-legend-diver-l3-374-4-30-2-1726057284-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-512-4-71-4-1726055436-thumbnail.png?w=2400',
     'watch-collection-longines-legend-diver-l3-374-4-90-2-1726057336-thumbnail.png?w=2400',
     'watch-collection-longines-legend-diver-l3-374-4-50-6-1726055148-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-780-4-96-6-1726056421-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-512-4-11-6-1726055291-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-780-4-96-9-1726056422-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-512-4-93-6-1726055305-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-780-4-56-9-1726056419-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-512-5-71-7-1726055102-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-128-4-77-6-1726054809-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-780-4-56-6-1726056418-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-512-5-79-7-1726055103-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-512-5-79-7-1726055103-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-128-4-78-3-1726057203-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-128-4-78-3-1726057203-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-512-0-71-7-1726057333-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-512-0-71-7-1726057333-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-377-4-58-6-1726054903-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-377-4-58-6-1726054903-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-128-4-78-6-1726054810-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-376-3-87-7-1726055326-thumbnail.png?w=2400',
     'watch-collection-longines-primaluna-l8-116-4-87-6-1726057314-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-128-4-87-6-1726054811-thumbnail.png?w=2400',
     'watch-collection-flagship-l4-974-4-12-6-1726055208-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-376-4-76-6-1726054901-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-376-4-96-6-1726055153-thumbnail.png?w=2400',
     'watch-collection-flagship-l4-974-3-22-7-1726055203-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-128-4-97-6-1726054812-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-128-5-37-7-1726057344-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-257-5-87-7-1726055346-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-257-8-87-3-1726057209-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-257-4-87-6-1726054827-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-257-4-78-6-1726054826-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-128-5-77-7-1726054814-thumbnail.png?w=2400',
     'watch-collection-record-l2-321-5-72-7-1726055132-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-128-5-79-7-1726054814-thumbnail.png?w=2400',
     'watch-collection-record-l2-321-4-57-6-1726054840-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-128-5-89-7-1726054815-thumbnail.png?w=2400',
     'watch-collection-longines-evidenza-l2-155-4-71-6-1726054822-thumbnail.png?w=2400',
     'watch-collection-the-longines-heritage-classic-l2-828-4-53-6-1726055463-thumbnail.png?w=2400',
     'watch-collection-the-longines-heritage-classic-l2-828-4-53-6-1726055463-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-128-8-78-3-1726057205-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-128-8-78-3-1726057205-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-128-8-87-3-1726057206-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-128-8-87-3-1726057206-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-810-4-73-6-1726055309-thumbnail.png?w=2400',
     'watch-collection-longines-spirit-l3-810-4-53-6-1726055307-thumbnail.png?w=2400',
     'watch-collection-longines-evidenza-l2-142-0-70-4-1726054817-thumbnail.png?w=2400',
     'watch-collection-hydroconquest-l3-781-4-76-6-1726055163-thumbnail.png?w=2400',
     'watch-collection-longines-evidenza-l2-142-0-70-6-1726054818-thumbnail.png?w=2400',
     'watch-collection-longines-legend-diver-l3-374-4-80-6-1726055152-thumbnail.png?w=2400',
     'watch-collection-longines-evidenza-l2-142-4-73-4-1726054819-thumbnail.png?w=2400',
     'watch-collection-longines-evidenza-l2-142-4-73-6-1726054820-thumbnail.png?w=2400',
     'watch-collection-conquest-classic-l2-386-3-87-7-1726055356-thumbnail.png?w=2400',
     'watch-collection-longines-evidenza-l2-142-8-73-2-1726054821-thumbnail.png?w=2400',
     'watch-collection-conquest-classic-l2-386-3-72-7-1726055355-thumbnail.png?w=2400',
     'watch-collection-conquest-classic-l2-386-4-88-6-1726055240-thumbnail.png?w=2400',
     'watch-collection-conquest-classic-l2-386-4-87-6-1726055239-thumbnail.png?w=2400',
     'watch-collection-conquest-classic-l2-386-4-72-6-1726057319-thumbnail.png?w=2400',
     'watch-collection-longines-evidenza-l2-155-4-71-5-1726054821-thumbnail.png?w=2400',
     'watch-collection-conquest-classic-l2-386-4-52-6-1726055238-thumbnail.png?w=2400',
     'watch-collection-conquest-classic-l2-386-0-87-6-1726055237-thumbnail.png?w=2400',
     'watch-collection-conquest-classic-l2-386-0-72-6-1726055236-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-767-4-73-9-1726055430-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-377-3-87-7-1726055327-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-767-4-73-6-1726055429-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-767-4-73-6-1726055429-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-377-4-76-6-1726054904-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-377-4-76-6-1726054904-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-767-4-73-3-1726055428-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-767-4-73-3-1726055428-thumbnail.png?w=2400',
     'watch-collection-longines-evidenza-l2-175-0-71-6-1726054823-thumbnail.png?w=2400',
     'watch-collection-longines-evidenza-l2-175-0-71-6-1726054823-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-767-4-73-0-1726055428-thumbnail.png?w=2400',
     'watch-collection-conquest-l3-377-4-96-6-1726055153-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-767-4-71-9-1726055294-thumbnail.png?w=2400',
     'watch-collection-longines-evidenza-l2-175-4-71-6-1726054824-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-767-4-71-6-1726055293-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-767-4-71-0-1726055292-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-757-4-73-9-1726055427-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-757-4-73-6-1726055426-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-757-4-73-3-1726055425-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-757-4-73-0-1726055423-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-757-4-71-9-1726055212-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-757-4-71-6-1726055110-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-257-4-77-6-1726054825-thumbnail.png?w=2400',
     'watch-collection-longines-dolcevita-l5-757-4-71-0-1726055109-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-257-4-78-3-1726057207-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-257-4-97-0-1726057207-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-257-4-97-6-1726054829-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-257-5-37-7-1726057345-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-257-5-77-7-1726054830-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-257-5-79-7-1726054831-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-257-5-79-7-1726054831-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-257-5-89-7-1726054832-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-257-5-89-7-1726054832-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-257-8-78-3-1726057209-thumbnail.png?w=2400',
     'watch-collection-longines-master-collection-l2-257-8-78-3-1726057209-thumbnail.png?w=2400',
     'watch-collection-record-l2-320-0-57-6-1726054835-thumbnail.png?w=2400',
     'watch-collection-record-l2-320-0-57-6-1726054835-thumbnail.png?w=2400',
     'watch-collection-record-l2-320-0-87-6-1726054836-thumbnail.png?w=2400',
     'watch-collection-record-l2-320-4-11-2-1726054837-thumbnail.png?w=2400',
     'watch-collection-record-l2-320-4-11-6-1726054837-thumbnail.png?w=2400',
     'watch-collection-record-l2-320-4-57-6-1726054838-thumbnail.png?w=2400',
     'watch-collection-record-l2-320-4-87-6-1726054838-thumbnail.png?w=2400',
     'watch-collection-record-l2-321-0-87-6-1726054839-thumbnail.png?w=2400',
     'watch-collection-record-l2-321-4-11-2-1726054839-thumbnail.png?w=2400',
     'watch-collection-record-l2-321-4-11-6-1726054840-thumbnail.png?w=2400',
     'watch-collection-record-l2-321-4-87-6-1726054842-thumbnail.png?w=2400',
     'watch-collection-record-l2-321-4-96-6-1726054842-thumbnail.png?w=2400',
     'watch-collection-la-grande-classique-de-longines-l4-209-1-91-2-1726054944-thumbnail.png?w=2400',
     'watch-collection-la-grande-classique-de-longines-l4-209-1-91-7-1726054944-thumbnail.png?w=2400',
     'watch-collection-la-grande-classique-de-longines-l4-209-1-97-7-1726054946-thumbnail.png?w=2400',
     'watch-collection-la-grande-classique-de-longines-l4-209-1-97-8-1726054947-thumbnail.png?w=2400',
     'watch-collection-la-grande-classique-de-longines-l4-209-2-11-2-1726054948-thumbnail.png?w=2400',
     'watch-collection-la-grande-classique-de-longines-l4-209-2-11-7-1726054949-thumbnail.png?w=2400',
     'watch-collection-la-grande-classique-de-longines-l4-209-2-11-8-1726054949-thumbnail.png?w=2400',
     'watch-collection-la-grande-classique-de-longines-l4-209-2-87-7-1726054950-thumbnail.png?w=2400',
     'watch-collection-la-grande-classique-de-longines-l4-209-2-87-8-1726054951-thumbnail.png?w=2400',
     'watch-collection-la-grande-classique-de-longines-l4-209-4-11-2-1726054952-thumbnail.png?w=2400']
    
    # remove duplicates
    femalewatches = list(set(femalewatches))
    
    # use the first 111
    femalewatches = femalewatches[0:111]
    
    
    if player.in_round(1).gender == 'male':
        return malewatches
    else:
        return femalewatches
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
        ###
        # Randomise the order of products
        ##
        import random
        malewatches = watchid(player)
        random.shuffle(malewatches)
        femalewatches = watchid(player)
        random.shuffle(femalewatches)
        
        # represent the list as a big string in player.shoeorder, using indices of the original list given by watchid(player)
        if player.gender == 'male':
            watchlist = "["
            for i in range(len(malewatches)):
                watchlist += str(watchid(player).index(malewatches[i])) + ','
            watchlist = watchlist[:-1]
            watchlist = watchlist + "]"
            player.shoeorder = watchlist
        else:
            watchlist = "["
            for i in range(len(femalewatches)):
                watchlist += str(watchid(player).index(femalewatches[i])) + ','
            watchlist = watchlist[:-1]
            watchlist = watchlist + "]"
            player.shoeorder = watchlist
        
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
        
        imagelist = ['https://api.ecom.longines.com/media/catalog/product/w/a/' + watchid(player)[x] for x in shoeorder]
        
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
            shoeimage1 = 'https://api.ecom.longines.com/media/catalog/product/w/a/' + watchid(player)[shoepair[0]],
            shoeimage2 = 'https://api.ecom.longines.com/media/catalog/product/w/a/' + watchid(player)[shoepair[1]],
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