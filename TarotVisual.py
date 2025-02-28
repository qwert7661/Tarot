import random as rng
import pygame as pg
import sys
pg.init()
pg.font.init()

print("Welcome to Celtic Cross Tarot")

# Setting up Screen, Clock & Font
running = True
screen_width = 1800
screen_height = 1000
screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("Celtic Cross Tarot")
clock = pg.time.Clock()
font = pg.font.Font(None,50)
small_font = pg.font.Font(None,30)


######################## SIZES AND COORDINATES #############################
card_size = (145,240)
marker_size = (card_size[0]+8,card_size[1]+8)
marker_width = 5; marker_radius = 10

x_offset = 155
y_offset = 250


coordinates_sig = (screen_width//2-500,screen_height//2 + 125)
coordinates_covers = (coordinates_sig[0]-x_offset,coordinates_sig[1])
coordinates_crosses = (coordinates_sig[0]+x_offset,coordinates_sig[1])
coordinates_crowns = (coordinates_sig[0],coordinates_sig[1]-y_offset)
coordinates_beneath = (coordinates_sig[0],coordinates_sig[1]+y_offset)
coordinates_behind = (coordinates_sig[0]+(x_offset*2),coordinates_sig[1])
coordinates_before = (coordinates_sig[0]-(x_offset*2),coordinates_sig[1])
coordinates_self = (coordinates_sig[0]+(x_offset*3),coordinates_beneath[1])
coordinates_house = (coordinates_self[0],coordinates_self[1]-y_offset)
coordinates_hopes = (coordinates_self[0],coordinates_self[1]-(y_offset*2))
coordinates_outcome = (coordinates_self[0],coordinates_self[1]-(y_offset*3))
coordinates_display_title = 1130,50
coordinates_display_subtitle = 1080,100
coordinates_description = 1070,200

####################### Card Space Rectangles #####################################
marker_significator_surf = pg.Surface(marker_size)
marker_significator_rect = marker_significator_surf.get_rect(center = coordinates_sig)
marker_covers_surf = pg.Surface(marker_size)
marker_covers_rect = marker_covers_surf.get_rect(center = coordinates_covers)
marker_crosses_surf = pg.Surface(marker_size)
marker_crosses_rect = marker_crosses_surf.get_rect(center = coordinates_crosses)
marker_crowns_surf = pg.Surface(marker_size)
marker_crowns_rect = marker_crowns_surf.get_rect(center = coordinates_crowns)
marker_beneath_surf = pg.Surface(marker_size)
marker_beneath_rect = marker_beneath_surf.get_rect(center = coordinates_beneath)
marker_behind_surf = pg.Surface(marker_size)
marker_behind_rect = marker_behind_surf.get_rect(center = coordinates_behind)
marker_before_surf = pg.Surface(marker_size)
marker_before_rect = marker_before_surf.get_rect(center = coordinates_before)
marker_self_surf = pg.Surface(marker_size)
marker_self_rect = marker_self_surf.get_rect(center = coordinates_self)
marker_house_surf = pg.Surface(marker_size)
marker_house_rect = marker_house_surf.get_rect(center = coordinates_house)
marker_hopes_surf = pg.Surface(marker_size)
marker_hopes_rect = marker_hopes_surf.get_rect(center = coordinates_hopes)
marker_outcome_surf = pg.Surface(marker_size)
marker_outcome_rect = marker_outcome_surf.get_rect(center = coordinates_outcome)

###################### BUTTONS ###################
draw_button_text = font.render('DRAW',True,'White')
draw_button_surf = pg.Surface((112,32)); draw_button_surf.fill('Blue')
draw_button_rect = draw_button_surf.get_rect(topleft = (coordinates_hopes[0] + 100,screen_height - 190))

all_button_text = font.render('DRAW ALL',True,'White')
all_button_surf = pg.Surface((188,32)); all_button_surf.fill('blue4')
all_button_rect = all_button_surf.get_rect(topleft = (coordinates_hopes[0] + 100, screen_height - 140))

reset_button_text = font.render('RESET',True,'White')
reset_button_surf = pg.Surface((120,32)); reset_button_surf.fill('red4')
reset_button_rect = reset_button_surf.get_rect(topleft = (coordinates_hopes[0] + 100, screen_height - 90))



################################## TAROT CARD CLASS ######################################
class TarotCard():
    reversed = False

    def __init__(self, name:str, major:bool, rank:int, suit:str, image, desc, gender:str):
        self.name = name
        self.major = major
        self.rank = rank
        self.suit = suit
        self.image = image
        self.image = pg.transform.scale(self.image,(card_size))
        self.rect = self.image.get_rect(center=(0,0))
        self.desc = desc
        self.gender = gender

# Descriptions
if True:
    # Descriptions major
    dscr_0r = "Folly, mania, extravagance, intoxication, delirium, frenzy, bewrayment. Reversed: Negligence, absence, distribution, carelessness, apathy, nullity, vanity."
    dscr_1r = "Skill, diplomacy, address, subtlety; sickness, pain, loss, disaster, snares of enemies; self-confidence, will; the Querent, if male. Reversed: Physician, Magus, mental disease, disgrace, disquiet."
    dscr_2r = "Secrets, mystery, the future as yet unrevealed; the woman who interests the Querent, if male; the Querent herself, if female; silence, tenacity; mystery, wisdom, science. Reversed: Passion, moral or physical ardour, conceit, surface knowledge."
    dscr_3r = "Fruitfulness, action, initiative, length of days; the unknown, clandestine; also difficulty, doubt, ignorance. Reversed: Light, truth, the unravelling of involved matters, public rejoicings; according to another reading, vacillation."
    dscr_4r = "Stability, power, protection, realization; a great person; aid, reason, conviction; also authority and will. Reversed: Benevolence, compassion, credit; also confusion to enemies, obstruction, immaturity."
    dscr_5r = "Marriage, alliance, captivity, servitude; by another account, mercy and goodness; inspiration; the man to whom the Querent has recourse. Reversed: Society, good understanding, concord, overkindness, weakness."
    dscr_6r = "Attraction, love, beauty, trials overcome. Reversed: Failure, foolish designs. Another account speaks of marriage frustrated and contrarieties of all kinds."
    dscr_7r = "Succour, providence; also war, triumph, presumption, vengeance, trouble. Reversed: Riot, quarrel, dispute, litigation, defeat."
    dscr_8r = "Power, energy, action, courage, magnanimity; also complete success and honours. Reversed: Despotism, abuse of power, weakness, discord, sometimes even disgrace."
    dscr_9r = "Prudence, circumspection; also and especially treason, dissimulation, roguery, corruption. Reversed: Concealment, disguise, policy, fear, unreasoned caution."
    dscr_10r = "Destiny, fortune, success, elevation, luck, felicity. Reversed: Increase, abundance, superfluity."
    dscr_11r = "Equity, rightness, probity, executive; triumph of the deserving side in law. Reversed: Law in all its departments, legal complications, bigotry, bias, excessive severity."
    dscr_12r = "Wisdom, circumspection, discernment, trials, sacrifice, intuition, divination, prophecy. Reversed: Selfishness, the crowd, body politic."
    dscr_13r = "End, mortality, destruction, corruption; also, for a man, the loss of a benefactor; for a woman, many contrarieties; for a maid, failure of marriage projects. Reversed: Inertia, sleep, lethargy, petrifaction, somnambulism; hope destroyed."
    dscr_14r = "Economy, moderation, frugality, management, accommodation. Reversed: Things connected with churches, religions, sects, the priesthood, sometimes even the priest who will marry the Querent; also disunion, unfortunate combinations, competing interests."
    dscr_15r = "Ravage, violence, vehemence, extraordinary efforts, force, fatality; that which is predestined but is not for this reason evil. Reversed: Evil fatality, weakness, pettiness, blindness."
    dscr_16r = "Misery, distress, indigence, adversity, calamity, disgrace, deception, ruin. It is a card in particular of unforeseen catastrophe. Reversed: According to one account, the same in a lesser degree; also oppression, imprisonment, tyranny."
    dscr_17r = "Loss, theft, privation, abandonment; another reading says: hope and bright prospects. Reversed: Arrogance, haughtiness, impotence."
    dscr_18r = "Hidden enemies, danger, calumny, darkness, terror, deception, occult forces, error. Reversed: Instability, inconstancy, silence, lesser degrees of deception and error."
    dscr_19r = "Material happiness, fortunate marriage, contentment. Reversed: The same in a lesser sense."
    dscr_20r = "Change of position, renewal, outcome. Another account specifies total loss through lawsuit. Reversed: Weakness, pusillanimity, simplicity; also deliberation, decision, sentence."
    dscr_21r = "Assured success, recompense, voyage, route, emigration, flight, change of place. Reversed: Inertia, fixity, stagnation, permanence."

    # Descriptions minor
    # cups
    if True:
        dscr_Ac = "The waters are beneath, and thereon are water-lilies; the hand issues from the cloud, holding in its palm the cup, from which four streams are pouring; a dove, bearing in its bill a cross-marked Host, descends to place the Wafer in the Cup; the dew of water is falling on all sides. It is an intimation of that which may lie behind the Lesser Arcana. Divinatory Meanings: House of the true heart, joy, content, abode, nourishment, abundance, fertility; Holy Table, felicity hereof. Reversed: House of the false heart, mutation, instability, revolution."
        dscr_2c = "A youth and maiden are pledging one another, and above their cups rises the Caduceus of Hermes, between the great wings of which there appears a lion's head. It is a variant of a sign which is found in a few old examples of this card. Some curious emblematical meanings are attached to it, but they do not concern us in this place. Divinatory Meanings: Love, passion, friendship, affinity, union, concord, sympathy, the interrelation of the sexes, and--as a suggestion apart from all offices of divination--that desire which is not in Nature, but by which Nature is sanctified."
        dscr_3c = "Maidens in a garden-ground with cups uplifted, as if pledging one another. Divinatory Meanings: The conclusion of any matter in plenty, perfection and merriment; happy issue, victory, fulfilment, solace, healing. Reversed: Expedition, dispatch, achievement, end. It signifies also the side of excess in physical enjoyment, and the pleasures of the senses."
        dscr_4c = "A young man is seated under a tree and contemplates three cups set on the grass before him; an arm issuing from a cloud offers him another cup. His expression notwithstanding is one of discontent with his environment. Divinatory Meanings: Weariness, disgust, aversion, imaginary vexations, as if the wine of this world had caused satiety only; another wine, as if a fairy gift, is now offered the wastrel, but he sees no consolation therein. This is also a card of blended pleasure. Reversed: Novelty, presage, new instruction, new relations."
        dscr_5c = "A dark, cloaked figure, looking sideways at three prone cups two others stand upright behind him; a bridge is in the background, leading to a small keep or holding. Divinatory Meanings: It is a card of loss, but something remains over; three have been taken, but two are left; it is a card of inheritance, patrimony, transmission, but not corresponding to expectations; with some interpreters it is a card of marriage, but not without bitterness or frustration. Reversed: News, alliances, affinity, consanguinity, ancestry, return, false projects."
        dscr_6c = "Children in an old garden, their cups filled with flowers. Divinatory Meanings: A card of the past and of memories, looking back, as--for example--on childhood; happiness, enjoyment, but coming rather from the past; things that have vanished. Another reading reverses this, giving new relations, new knowledge, new environment, and then the children are disporting in an unfamiliar precinct. Reversed: The future, renewal, that which will come to pass presently."
        dscr_7c = "Strange chalices of vision, but the images are more especially those of the fantastic spirit. Divinatory Meanings: Fairy favours, images of reflection, sentiment, imagination, things seen in the glass of contemplation; some attainment in these degrees, but nothing permanent or substantial is suggested. Reversed: Desire, will, determination, project."
        dscr_8c = "A man of dejected aspect is deserting the cups of his felicity, enterprise, undertaking or previous concern. Divinatory Meanings: The card speaks for itself on the surface, but other readings are entirely antithetical--giving joy, mildness, timidity, honour, modesty. In practice, it is usually found that the card shews the decline of a matter, or that a matter which has been thought to be important is really of slight consequence--either for good or evil. Reversed: Great joy, happiness, feasting."
        dscr_9c = "A goodly personage has feasted to his heart's content, and abundant refreshment of wine is on the arched counter behind him, seeming to indicate that the future is also assured. The picture offers the material side only, but there are other aspects. Divinatory Meanings: Concord, contentment, physical bien-être; also victory, success, advantage; satisfaction for the Querent or person for whom the consultation is made. Reversed: Truth, loyalty, liberty; but the readings vary and include mistakes, imperfections, etc."
        dscr_10c = "Appearance of Cups in a rainbow; it is contemplated in wonder and ecstasy by a man and woman below, evidently husband and wife. His right arm is about her; his left is raised upward; she raises her right arm. The two children dancing near them have not observed the prodigy but are happy after their own manner. There is a home-scene beyond. Divinatory Meanings: Contentment, repose of the entire heart; the perfection of that state; also perfection of human love and friendship; if with several picture-cards, a person who is taking charge of the Querent's interests; also the town, village or country inhabited by the Querent. Reversed: Repose of the false heart, indignation, violence."
        dscr_Pc = "A fair, pleasing, somewhat effeminate page, of studious and intent aspect, contemplates a fish rising from a cup to look at him. It is the pictures of the mind taking form. Divinatory Meanings: Fair young man, one impelled to render service and with whom the Querent will be connected; a studious youth; news, message; application, reflection, meditation; also these things directed to business. Reversed: Taste, inclination, attachment, seduction, deception, artifice."
        dscr_Nc = "Graceful, but not warlike; riding quietly, wearing a winged helmet, referring to those higher graces of the imagination which sometimes characterize this card. He too is a dreamer, but the images of the side of sense haunt him in his vision. Divinatory Meanings: Arrival, approach--sometimes that of a messenger; advances, proposition, demeanour, invitation, incitement. Reversed: Trickery, artifice, subtlety, swindling, duplicity, fraud."
        dscr_Qc = "Beautiful, fair, dreamy--as one who sees visions in a cup. This is, however, only one of her aspects; she sees, but she also acts, and her activity feeds her dream. Divinatory Meanings: Good, fair woman; honest, devoted woman, who will do service to the Querent; loving intelligence, and hence the gift of vision; success, happiness, pleasure; also wisdom, virtue; a perfect spouse and a good mother. Reversed: The accounts vary; good woman; otherwise, distinguished woman but one not to be trusted; perverse woman; vice, dishonour, depravity."
        dscr_Kc = "He holds a short sceptre in his left hand and a great cup in his right; his throne is set upon the sea; on one side a ship is riding and on the other a dolphin is leaping. The implicit is that the Sign of the Cup naturally refers to water, which appears in all the court cards. Divinatory Meanings: Fair man, man of business, law, or divinity; responsible, disposed to oblige the Querent; also equity, art and science, including those who profess science, law and art; creative intelligence. Reversed: Dishonest, double-dealing man; roguery, exaction, injustice, vice, scandal, pillage, considerable loss."
    # pentacles
    if True:
        dscr_Ap = "A hand--issuing, as usual, from a cloud--holds up a pentacle. Divinatory Meanings: Perfect contentment, felicity, ecstasy; also speedy intelligence; gold. Reversed: The evil side of wealth, bad intelligence; also great riches. In any case it shews prosperity, comfortable material conditions, but whether these are of advantage to the possessor will depend on whether the card is reversed or not."
        dscr_2p = "A young man, in the act of dancing, has a pentacle in either hand, and they are joined by that endless cord which is like the number 8 reversed. Divinatory Meanings: On the one hand it is represented as a card of gaiety, recreation and its connexions, which is the subject of the design; but it is read also as news and messages in writing, as obstacles, agitation, trouble, embroilment. Reversed: Enforced gaiety, simulated enjoyment, literal sense, handwriting, composition, letters of exchange."
        dscr_3p = "A sculptor at his work in a monastery. Compare the design which illustrates the Eight of Pentacles. The apprentice or amateur therein has received his reward and is now at work in earnest. Divinatory Meanings: Métier, trade, skilled labour; usually, however, regarded as a card of nobility, aristocracy, renown, glory. Reversed: Mediocrity, in work and otherwise, puerility, pettiness, weakness."
        dscr_4p = "A crowned figure, having a pentacle over his crown, clasps another with hands and arms; two pentacles are under his feet. He holds to that which he has. Divinatory Meanings: The surety of possessions, cleaving to that which one has, gift, legacy, inheritance. Reversed: Suspense, delay, opposition."
        dscr_5p = "Two mendicants in a snow-storm pass a lighted casement. Divinatory Meanings: The card foretells material trouble above all, whether in the form illustrated--that is, destitution--or otherwise. For some cartomancists, it is a card of love and lovers-wife, husband, friend, mistress; also concordance, affinities. These alternatives cannot be harmonized. Reversed: Disorder, chaos, ruin, discord, profligacy."
        dscr_6p = "A person in the guise of a merchant weighs money in a pair of scales and distributes it to the needy and distressed. It is a testimony to his own success in life, as well as to his goodness of heart. Divinatory Meanings: Presents, gifts, gratification; another account says attention, vigilance, now is the accepted time, present prosperity, etc. Reversed: Desire, cupidity, envy, jealousy, illusion."
        dscr_7p = "A young man, leaning on his staff, looks intently at seven pentacles attached to a clump of greenery on his right; one would say that these were his treasures and that his heart was there. Divinatory Meanings: These are exceedingly contradictory; in the main, it is a card of money, business, barter; but one reading gives altercation, quarrels--and another innocence, ingenuity, purgation. Reversed: Cause for anxiety regarding money which it may be proposed to lend."
        dscr_8p = "An artist in stone at his work, which he exhibits in the form of trophies. Divinatory Meanings: Work, employment, commission, craftsmanship, skill in craft and business, perhaps in the preparatory stage. Reversed: Voided ambition, vanity, cupidity, exaction, usury. It may also signify the possession of skill, in the sense of the ingenious mind turned to cunning and intrigue."
        dscr_9p = "A woman, with a bird upon her wrist, stands amidst a great abundance of grapevines in the garden of a manorial house. It is a wide domain, suggesting plenty in all things. Possibly it is her own possession and testifies to material well-being. Divinatory Meanings: Prudence, safety, success, accomplishment, certitude, discernment. Reversed: Roguery, deception, voided project, bad faith."
        dscr_10p = "A man and woman beneath an archway which gives entrance to a house and domain. They are accompanied by a child, who looks curiously at two dogs accosting an ancient personage seated in the foreground. The child's hand is on one of them. Divinatory Meanings: Gain, riches; family matters, archives, extraction, the abode of a family. Reversed: Chance, fatality, loss, robbery, games of hazard; sometimes gift, dowry, pension."
        dscr_Pp = "A youthful figure, looking intently at the pentacle which hovers over his raised hands. He moves slowly, insensible of that which is about him. Divinatory Meanings: Application, study, scholarship, reflection; another reading says news, messages and the bringer thereof; also rule, management. Reversed: Prodigality, dissipation, liberality, luxury; unfavourable news."
        dscr_Np = "He rides a slow, enduring, heavy horse, to which his own aspect corresponds. He exhibits his symbol, but does not look therein. Divinatory Meanings: Utility, serviceableness, interest, responsibility, rectitude-all on the normal and external plane. Reversed: Inertia, idleness, repose of that kind, stagnation; also placidity, discouragement, carelessness."
        dscr_Qp = "The face suggests that of a dark woman, whose qualities might be summed up in the idea of greatness of soul; she has also the serious cast of intelligence; she contemplates her symbol and may see worlds therein. Divinatory Meanings: Opulence, generosity, magnificence, security, liberty. Reversed: Evil, suspicion, suspense, fear, mistrust."
        dscr_Kp = "The figure calls for no special description. The face is rather dark, suggesting also courage, but somewhat lethargic in tendency. The bull's head should be noted as a recurrent symbol on the throne. The sign of this suit is represented throughout as engraved or blazoned with the pentagram, typifying the correspondence of the four elements in human nature and that by which they may be governed. In many old Tarot packs this suit stood for current coin, money, deniers. I have not invented the substitution of pentacles and I have no special cause to sustain in respect of the alternative. But the consensus of divinatory meanings is on the side of some change, because the cards do not happen to deal especially with questions of money. Divinatory Meanings: Valour, realizing intelligence, business and normal intellectual aptitude, sometimes mathematical gifts and attainments of this kind; success in these paths. Reversed: Vice, weakness, ugliness, perversity, corruption, peril."
    # wands
    if True:
        dscr_Aw = "A hand issuing from a cloud grasps a stout wand or club. Divinatory Meanings: Creation, invention, enterprise, the powers which result in these; principle, beginning, source; birth, family, origin, and in a sense the virility which is behind them; the starting point of enterprises; according to another account, money, fortune, inheritance. Reversed: Fall, decadence, ruin, perdition, to perish; also a certain clouded joy."
        dscr_2w = "A tall man looks from a battlemented roof over sea and shore; he holds a globe in his right hand, while a staff in his left rests on the battlement; another is fixed in a ring. The Rose and Cross and Lily should be noticed on the left side. Divinatory Meanings: Between the alternative readings there is no marriage possible; on the one hand, riches, fortune, magnificence; on the other, physical suffering, disease, chagrin, sadness, mortification. The design gives one suggestion; here is a lord overlooking his dominion and alternately contemplating a globe; it looks like the malady, the mortification, the sadness of Alexander amidst the grandeur of this world's wealth. Reversed: Surprise, wonder, enchantment, emotion, trouble, fear."
        dscr_3w = "A calm, stately personage, with his back turned, looking from a cliff's edge at ships passing over the sea. Three staves are planted in the ground, and he leans slightly on one of them. Divinatory Meanings: He symbolizes established strength, enterprise, effort, trade, commerce, discovery; those are his ships, bearing his merchandise, which are sailing over the sea. The card also signifies able co-operation in business, as if the successful merchant prince were looking from his side towards yours with a view to help you. Reversed: The end of troubles, suspension or cessation of adversity, toil and disappointment."
        dscr_4w = "From the four great staves planted in the foreground there is a great garland suspended; two female figures uplift nosegays; at their side is a bridge over a moat, leading to an old manorial house. Divinatory Meanings: They are for once almost on the surface--country life, haven of refuge, a species of domestic harvest-home, repose, concord, harmony, prosperity, peace, and the perfected work of these. Reversed: The meaning remains unaltered; it is prosperity, increase, felicity, beauty, embellishment."
        dscr_5w = "A posse of youths, who are brandishing staves, as if in sport or strife. It is mimic warfare, and hereto correspond the Divinatory Meanings: Imitation, as, for example, sham fight, but also the strenuous competition and struggle of the search after riches and fortune. In this sense it connects with the battle of life. Hence some attributions say that it is a card of gold, gain, opulence. Reversed: Litigation, disputes, trickery, contradiction."
        dscr_6w = "A laurelled horseman bears one staff adorned with a laurel crown; footmen with staves are at his side. Divinatory Meanings: The card has been so designed that it can cover several significations; on the surface, it is a victor triumphing, but it is also great news, such as might be carried in state by the King's courier; it is expectation crowned with its own desire, the crown of hope, and so forth. Reversed: Apprehension, fear, as of a victorious enemy at the gate; treachery, disloyalty, as of gates being opened to the enemy; also indefinite delay."
        dscr_7w = "A young man on a craggy eminence brandishing a staff; six other staves are raised towards him from below. Divinatory Meanings: It is a card of valour, for, on the surface, six are attacking one, who has, however, the vantage position. On the intellectual plane, it signifies discussion, wordy strife; in business--negotiations, war of trade, barter, competition. It is further a card of success, for the combatant is on the top and his enemies may be unable to reach him. Reversed: Perplexity, embarrassments, anxiety. It is also a caution against indecision."
        dscr_8w = "The card represents motion through the immovable - a flight of wands through an open country; but they draw to the term of their course. That which they signify is at hand; it may be even on the threshold. Divinatory Meanings: Activity in undertakings, the path of such activity, swiftness, as that of an express messenger; great haste, great hope, speed towards an end which promises assured felicity; generally, that which is on the move; also the arrows of love. Reversed: Arrows of jealousy, internal dispute, stingings of conscience, quarrels; and domestic disputes for persons who are married."
        dscr_9w = "The figure leans upon his staff and has an expectant look, as if awaiting an enemy. Behind are eight other staves--erect, in orderly disposition, like a palisade. Divinatory Meanings: The card signifies strength in opposition. If attacked, the person will meet an onslaught boldly; and his build shews, that he may prove a formidable antagonist. With this main significance there are all its possible adjuncts--delay, suspension, adjournment. Reversed: Obstacles, adversity, calamity."
        dscr_10w = "A man oppressed by the weight of the ten staves which he is carrying. Divinatory Meanings: A card of many significances, and some of the readings cannot be harmonized. I set aside that which connects it with honour and good faith. The chief meaning is oppression simply, but it is also fortune, gain, any kind of success, and then it is the oppression of these things. It is also a card of false-seeming, disguise, perfidy. The place which the figure is approaching may suffer from the rods that he carries. Success is stultified if the Nine of Swords follows, and if it is a question of a lawsuit, there will be certain loss. Reversed: Contrarieties, difficulties, intrigues, and their analogies."
        dscr_Pw = "In a scene similar to the former, a young man stands in the act of proclamation. He is unknown but faithful, and his tidings are strange. Divinatory Meanings: Dark young man, faithful, a lover, an envoy, a postman. Beside a man, he will bear favourable testimony concerning him. A dangerous rival, if followed by the Page of Cups; he has the chief qualities of his suit. He may signify family intelligence. Reversed: Anecdotes, announcements, evil news. Also indecision and the instability which accompanies it."
        dscr_Nw = "He is shewn as if upon a journey, armed with a short wand, and although mailed is not on a warlike errand. He is passing mounds or pyramids. The motion of the horse is a key to the character of its rider, and suggests the precipitate mood, or things connected therewith. Divinatory Meanings: Departure, absence, flight, emigration. A dark young man, friendly. Change of residence. Reversed: Rupture, division, interruption, discord."
        dscr_Qw = "The Wands throughout this suit are always in leaf, as it is a suit of life and animation. Emotionally and otherwise, the Queen's personality corresponds to that of the King, but is more magnetic. Divinatory Meanings: A dark woman, countrywoman, friendly, chaste, loving, honourable. If the card beside her signifies a man, she is well disposed towards him; if a woman, she is interested in the Querent. Also, love of money, or a certain success in business. Reversed: Good, economical, obliging, serviceable. Signifies also--but in certain positions and in the neighbourhood of other cards tending in such directions--opposition, jealousy, even deceit and infidelity."
        dscr_Kw = 'The physical and emotional nature to which this card is attributed is dark, ardent, lithe, animated, impassioned, noble. The King uplifts a flowering wand, and wears, like his three correspondences in the remaining suits, what is called a cap of maintenance beneath his crown. He connects with the symbol of the lion, which is emblazoned on the back of his throne. Divinatory Meanings: Dark man, friendly, countryman, generally married, honest and conscientious. The card always signifies honesty, and may mean news concerning an unexpected heritage to fall in before very long. Reversed: Good, but severe; austere, yet tolerant.'
    # swords
    if True:
        dscr_As = "A hand issues from a cloud, grasping a sword, the point of which is encircled by a crown. Divinatory Meanings: Triumph, the excessive degree in everything, conquest, triumph of force. It is a card of great force, in love as well as in hatred. The crown may carry a much higher significance than comes usually within the sphere of fortune-telling. Reversed: The same, but the results are disastrous; another account says: conception, childbirth, augmentation, multiplicity."
        dscr_2s = "A hoodwinked female figure balances two swords upon her shoulders. Divinatory Meanings: Conformity and the equipoise which it suggests, courage, friendship, concord in a state of arms; another reading gives tenderness, affection, intimacy. The suggestion of harmony and other favourable readings must be considered in a qualified manner, as Swords generally are not symbolical of beneficent forces in human affairs. Reversed: Imposture, falsehood, duplicity, disloyalty."
        dscr_3s = "Three swords piercing a heart; cloud and rain behind. Divinatory Meanings: Removal, absence, delay, division, rupture, dispersion, and all that the design signifies naturally, being too simple and obvious to call for specific enumeration. Reversed: Mental alienation, error, loss, distraction, disorder, confusion."
        dscr_4s = "The effigy of a knight in the attitude of prayer, at full length upon his tomb. Divinatory Meanings: Vigilance, retreat, solitude, hermit's repose, exile, tomb and coffin. It is these last that have suggested the design. Reversed: Wise administration, circumspection, economy, avarice, precaution, testament."
        dscr_5s = "A disdainful man looks after two retreating and dejected figures. Their swords lie upon the ground. He carries two others on his left shoulder, and a third sword is in his right hand, point to earth. He is the master in possession of the field. Divinatory Meanings: Degradation, destruction, revocation, infamy, dishonour, loss, with the variants and analogues of these. Reversed: The same; burial and obsequies."
        dscr_6s = "A ferryman carrying passengers in his punt to the further shore. The course is smooth, and seeing that the freight is light, it may be noted that the work is not beyond his strength. Divinatory Meanings: Journey by water, route, way, envoy, commissionary, expedient. Reversed: Declaration, confession, publicity; one account says that it is a proposal of love."
        dscr_7s = "A man in the act of carrying away five swords rapidly; the two others of the card remain stuck in the ground. A camp is close at hand. Divinatory Meanings: Design, attempt, wish, hope, confidence; also quarrelling, a plan that may fail, annoyance. The design is uncertain in its import, because the significations are widely at variance with each other. Reversed: Good advice, counsel, instruction, slander, babbling."
        dscr_8s = "A woman, bound and hoodwinked, with the swords of the card about her. Yet it is rather a card of temporary durance than of irretrievable bondage. Divinatory Meanings: Bad news, violent chagrin, crisis, censure, power in trammels, conflict, calumny; also sickness. Reversed: Disquiet, difficulty, opposition, accident, treachery; what is unforeseen; fatality."
        dscr_9s = "One seated on her couch in lamentation, with the swords over her. She is as one who knows no sorrow which is like unto hers. It is a card of utter desolation. Divinatory Meanings: Death, failure, miscarriage, delay, deception, disappointment, despair. Reversed: Imprisonment, suspicion, doubt, reasonable fear, shame."
        dscr_10s = "A prostrate figure, pierced by all the swords belonging to the card. Divinatory Meanings: Whatsoever is intimated by the design; also pain, affliction, tears, sadness, desolation. It is not especially a card of violent death. Reversed: Advantage, profit, success, favour, but none of these are permanent; also power and authority."
        dscr_Ps = "A lithe, active figure holds a sword upright in both hands, while in the act of swift walking. He is passing over rugged land, and about his way the clouds are collocated wildly. He is alert and lithe, looking this way and that, as if an expected enemy might appear at any moment. Divinatory Meanings: Authority, overseeing, secret service, vigilance, spying, examination, and the qualities thereto belonging. Reversed: More evil side of these qualities; what is unforeseen, unprepared state; sickness is also intimated."
        dscr_Ns = "He is riding in full course, as if scattering his enemies. In the design he is really a prototypical hero of romantic chivalry. He might almost be Galahad, whose sword is swift and sure because he is clean of heart. Divinatory Meanings: Skill, bravery, capacity, defence, address, enmity, wrath, war, destruction, opposition, resistance, ruin. There is therefore a sense in which the card signifies death, but it carries this meaning only in its proximity to other cards of fatality. Reversed: Imprudence, incapacity, extravagance."
        dscr_Qs = "Her right hand raises the weapon vertically and the hilt rests on an arm of her royal chair. The left hand is extended, the arm raised her countenance is severe but chastened; it suggests familiarity with sorrow. It does not represent mercy, and, her sword notwithstanding, she is scarcely a symbol of power. Divinatory Meanings: Widowhood, female sadness and embarrassment, absence, sterility, mourning, privation, separation. Reversed: Malice, bigotry, artifice, prudery, bale, deceit."
        dscr_Ks = "He sits in judgment, holding the unsheathed sign of his suit. He recalls, of course, the conventional Symbol of justice in the Trumps Major, and he may represent this virtue, but he is rather the power of life and death, in virtue of his office. Divinatory Meanings: Whatsoever arises out of the idea of judgment and all its connexions-power, command, authority, militant intelligence, law, offices of the crown, and so forth. Reversed: Cruelty, perversity, barbarity, perfidy, evil intention."

# Major Arcana
if True:
    t0r = TarotCard(name='The Fool', major=True, rank=0, suit='major', image=pg.image.load('graphics/TarotCards/0 The Fool.png'),
        desc=dscr_0r, gender='HIM')
    t1r = TarotCard(name='The Magician', major=True, rank=1, suit='major', image=pg.image.load('graphics/TarotCards/1 - The Magician.png'),
        desc=dscr_1r, gender='HIM')
    t2r = TarotCard(name='The High Priestess', major=True, rank=2, suit='major', image=pg.image.load('graphics/TarotCards/2 - The High Priestess.png'),
        desc=dscr_2r, gender='HER')
    t3r = TarotCard(name='The Empress', major=True, rank=3, suit='major', image=pg.image.load('graphics/TarotCards/3 - The Empress.png'),
        desc=dscr_3r, gender='HER')
    t4r = TarotCard(name='The Emperor', major=True, rank=4, suit='major', image=pg.image.load('graphics/TarotCards/4 - The Emperor.png'),
        desc=dscr_4r, gender='HIM')
    t5r = TarotCard(name='The Hierophant', major=True, rank=5, suit='major', image=pg.image.load('graphics/TarotCards/5 - The Hierophant.png'),
        desc=dscr_5r, gender='HIM')
    t6r = TarotCard(name='The Lovers', major=True, rank=6, suit='major', image=pg.image.load('graphics/TarotCards/6 - The Lovers.png'),
        desc=dscr_6r, gender='THEM')
    t7r = TarotCard(name='The Chariot', major=True, rank=7, suit='major', image=pg.image.load('graphics/TarotCards/7 - The Chariot.png'),
        desc=dscr_7r, gender='HIM')
    t8r = TarotCard(name='Strength', major=True, rank=8, suit='major', image=pg.image.load('graphics/TarotCards/8 - Strength.png'),
        desc=dscr_8r, gender='HER')
    t9r = TarotCard(name='The Hermit', major=True, rank=9, suit='major', image=pg.image.load('graphics/TarotCards/9 - The Hermit.png'),
        desc=dscr_9r, gender='HIM')
    t10r = TarotCard(name='The Wheel of Fortune', major=True, rank=10, suit='major', image=pg.image.load('graphics/TarotCards/10 - The Wheel.png'),
        desc=dscr_10r, gender='IT')
    t11r = TarotCard(name='Justice', major=True, rank=11, suit='major', image=pg.image.load('graphics/TarotCards/11 - Justice.png'),
        desc=dscr_11r, gender='HIM')
    t12r = TarotCard(name='The Handed Man', major=True, rank=12, suit='major', image=pg.image.load('graphics/TarotCards/12 - The Hanged Man.png'),
        desc=dscr_12r, gender='HIM')
    t13r = TarotCard(name='Death', major=True, rank=13, suit='major', image=pg.image.load('graphics/TarotCards/13 - Death.png'),
        desc=dscr_13r, gender='HIM')
    t14r = TarotCard(name='Temperance', major=True, rank=14, suit='major', image=pg.image.load('graphics/TarotCards/14 - Temperance.png'),
        desc=dscr_14r, gender='HER')
    t15r = TarotCard(name='The Devil', major=True, rank=15, suit='major', image=pg.image.load('graphics/TarotCards/15 - The Devil.png'),
        desc=dscr_15r, gender='HIM')
    t16r = TarotCard(name='The Tower', major=True, rank=16, suit='major', image=pg.image.load('graphics/TarotCards/16 - The Tower.png'),
        desc=dscr_16r, gender='IT')
    t17r = TarotCard(name='The Star', major=True, rank=17, suit='major', image=pg.image.load('graphics/TarotCards/17 -The Star.png'),
        desc=dscr_17r, gender='HER')
    t18r = TarotCard(name='The Moon', major=True, rank=18, suit='major', image=pg.image.load('graphics/TarotCards/18 - The Moon.png'),
        desc=dscr_18r, gender='HER')
    t19r = TarotCard(name='The Sun', major=True, rank=19, suit='major', image=pg.image.load('graphics/TarotCards/19 - The Sun.png'),
        desc=dscr_19r, gender='HIM')
    t20r = TarotCard(name='Judgment', major=True, rank=20, suit='major', image=pg.image.load('graphics/TarotCards/20 - Judgment.png'),
        desc=dscr_20r, gender='HIM')
    t21r = TarotCard(name='The World', major=True, rank=21, suit='major', image=pg.image.load('graphics/TarotCards/21 - The World.png'),
        desc=dscr_21r, gender='HER')
# Minor Cups
if True:
    tAc = TarotCard(name='Ace of Cups', major=False, rank=1, suit='cups', image=pg.image.load('graphics/TarotCards/Ace_of_Cups.png'),
        desc=dscr_Ac, gender='IT')
    t2c = TarotCard(name='Two of Cups', major=False, rank=2, suit='cups', image=pg.image.load('graphics/TarotCards/Two_of_Cups.png'),
        desc=dscr_2c, gender='THEM')
    t3c = TarotCard(name='Three of Cups', major=False, rank=3, suit='cups', image=pg.image.load('graphics/TarotCards/Three_of_Cups.png'),
        desc=dscr_3c, gender='THEN')
    t4c = TarotCard(name='Four of Cups', major=False, rank=4, suit='cups', image=pg.image.load('graphics/TarotCards/Four_of_Cups.png'),
        desc=dscr_4c, gender='HIM')
    t5c = TarotCard(name='Five of Cups', major=False, rank=5, suit='cups', image=pg.image.load('graphics/TarotCards/Five_of_Cups.png'),
        desc=dscr_5c, gender='HIM')
    t6c = TarotCard(name='Six of Cups', major=False, rank=6, suit='cups', image=pg.image.load('graphics/TarotCards/Six_of_Cups.png'),
        desc=dscr_6c, gender='THEM')
    t7c = TarotCard(name='Seven of Cups', major=False, rank=7, suit='cups', image=pg.image.load('graphics/TarotCards/Seven_of_Cups.png'),
        desc=dscr_7c, gender='HIM')
    t8c = TarotCard(name='Eight of Cups', major=False, rank=8, suit='cups', image=pg.image.load('graphics/TarotCards/Eight_of_Cups.png'),
        desc=dscr_8c, gender='HIM')
    t9c = TarotCard(name='Nine of Cups', major=False, rank=9, suit='cups', image=pg.image.load('graphics/TarotCards/Nine_of_Cups.png'),
        desc=dscr_9c, gender='HIM')
    t0c = TarotCard(name='Ten of Cups', major=False, rank=10, suit='cups', image=pg.image.load('graphics/TarotCards/Ten_of_Cups.png'),
        desc=dscr_10c, gender='THEM')
    tPc = TarotCard(name='Page of Cups', major=False, rank=11, suit='cups', image=pg.image.load('graphics/TarotCards/Page_of_Cups.png'),
        desc=dscr_Pc, gender='HIM')
    tNc = TarotCard(name='Knight of Cups', major=False, rank=12, suit='cups', image=pg.image.load('graphics/TarotCards/Knight_of_Cups.png'),
        desc=dscr_Nc, gender='HIM')
    tQc = TarotCard(name='Queen of Cups', major=False, rank=13, suit='cups', image=pg.image.load('graphics/TarotCards/Queen_of_Cups.png'),
        desc=dscr_Qc, gender='HER')
    tKc = TarotCard(name='King of Cups', major=False, rank=14, suit='cups', image=pg.image.load('graphics/TarotCards/King_of_Cups.png'),
        desc=dscr_Kc, gender='HIM')
# Minor Pentacles
if True:
    tAp = TarotCard(name='Ace of Pentacles', major=False, rank=1, suit='pentacles', image=pg.image.load('graphics/TarotCards/Ace_of_Pentacles.png'),
        desc=dscr_Ap, gender='IT')
    t2p = TarotCard(name='Two of Pentacles', major=False, rank=2, suit='pentacles', image=pg.image.load('graphics/TarotCards/Two_of_Pentacles.png'),
        desc=dscr_2p, gender='HIM')
    t3p = TarotCard(name='Three of Pentacles', major=False, rank=3, suit='pentacles', image=pg.image.load('graphics/TarotCards/Three_of_Pentacles.png'),
        desc=dscr_3p, gender='HIM')
    t4p = TarotCard(name='Four of Pentacles', major=False, rank=4, suit='pentacles', image=pg.image.load('graphics/TarotCards/Four_of_Pentacles.png'),
        desc=dscr_4p, gender='HIM')
    t5p = TarotCard(name='Five of Pentacles', major=False, rank=5, suit='pentacles', image=pg.image.load('graphics/TarotCards/Five_of_Pentacles.png'),
        desc=dscr_5p, gender='THEM')
    t6p = TarotCard(name='Six of Pentacles', major=False, rank=6, suit='pentacles', image=pg.image.load('graphics/TarotCards/Six_of_Pentacles.png'),
        desc=dscr_6p, gender='HIM')
    t7p = TarotCard(name='Seven of Pentacles', major=False, rank=7, suit='pentacles', image=pg.image.load('graphics/TarotCards/Seven_of_Pentacles.png'),
        desc=dscr_7p, gender='HIM')
    t8p = TarotCard(name='Eight of Pentacles', major=False, rank=8, suit='pentacles', image=pg.image.load('graphics/TarotCards/Eight_of_Pentacles.png'),
        desc=dscr_8p, gender='HIM')
    t9p = TarotCard(name='Nine of Pentacles', major=False, rank=9, suit='pentacles', image=pg.image.load('graphics/TarotCards/Nine_of_Pentacles.png'),
        desc=dscr_9p, gender='HER')
    t0p = TarotCard(name='Ten of Pentacles', major=False, rank=10, suit='pentacles', image=pg.image.load('graphics/TarotCards/Ten_of_Pentacles.png'),
        desc=dscr_10p, gender='THEM')
    tPp = TarotCard(name='Page of Pentacles', major=False, rank=11, suit='pentacles', image=pg.image.load('graphics/TarotCards/Page_of_Pentacles.png'),
        desc=dscr_Pp, gender='HIM')
    tNp = TarotCard(name='Knight of Pentacles', major=False, rank=12, suit='pentacles', image=pg.image.load('graphics/TarotCards/Knight_of_Pentacles.png'),
        desc=dscr_Np, gender='HIM')
    tQp = TarotCard(name='Queen of Pentacles', major=False, rank=13, suit='pentacles', image=pg.image.load('graphics/TarotCards/Queen_of_Pentacles.png'),
        desc=dscr_Qp, gender='HER')
    tKp = TarotCard(name='King of Pentacles', major=False, rank=14, suit='pentacles', image=pg.image.load('graphics/TarotCards/King_of_Pentacles.png'),
        desc=dscr_Kp, gender='HIM')
# Minor Wands
if True:
    tAw = TarotCard(name='Ace of Wands', major=False, rank=1, suit='wands', image=pg.image.load('graphics/TarotCards/Ace_of_Wands.png'),
        desc=dscr_Aw, gender='IT')
    t2w = TarotCard(name='Two of Wands', major=False, rank=2, suit='wands', image=pg.image.load('graphics/TarotCards/Two_of_Wands.png'),
        desc=dscr_2w, gender='HIM')
    t3w = TarotCard(name='Three of Wands', major=False, rank=3, suit='wands', image=pg.image.load('graphics/TarotCards/Three_of_Wands.png'),
        desc=dscr_3w, gender='HIM')
    t4w = TarotCard(name='Four of Wands', major=False, rank=4, suit='wands', image=pg.image.load('graphics/TarotCards/Four_of_Wands.png'),
        desc=dscr_4w, gender='THEM')
    t5w = TarotCard(name='Five of Wands', major=False, rank=5, suit='wands', image=pg.image.load('graphics/TarotCards/Five_of_Wands.png'),
        desc=dscr_5w, gender='THEM')
    t6w = TarotCard(name='Six of Wands', major=False, rank=6, suit='wands', image=pg.image.load('graphics/TarotCards/Six_of_Wands.png'),
        desc=dscr_6w, gender='HIM')
    t7w = TarotCard(name='Seven of Wands', major=False, rank=7, suit='wands', image=pg.image.load('graphics/TarotCards/Seven_of_Wands.png'),
        desc=dscr_7w, gender='HIM')
    t8w = TarotCard(name='Eight of Wands', major=False, rank=8, suit='wands', image=pg.image.load('graphics/TarotCards/Eight_of_Wands.png'),
        desc=dscr_8w, gender='THEM')
    t9w = TarotCard(name='Nine of Wands', major=False, rank=9, suit='wands', image=pg.image.load('graphics/TarotCards/Nine_of_Wands.png'),
        desc=dscr_9w, gender='HIM')
    t0w = TarotCard(name='Ten of Wands', major=False, rank=10, suit='wands', image=pg.image.load('graphics/TarotCards/Ten_of_Wands.png'),
        desc=dscr_10w, gender='HIM')
    tPw = TarotCard(name='Page of Wands', major=False, rank=11, suit='wands', image=pg.image.load('graphics/TarotCards/Page_of_Wands.png'),
        desc=dscr_Pw, gender='HIM')
    tNw = TarotCard(name='Knight of Wands', major=False, rank=12, suit='wands', image=pg.image.load('graphics/TarotCards/Knight_of_Wands.png'),
        desc=dscr_Nw, gender='HIM')
    tQw = TarotCard(name='Queen of Wands', major=False, rank=13, suit='wands', image=pg.image.load('graphics/TarotCards/Queen_of_Wands.png'),
        desc=dscr_Qw, gender='HER')
    tKw = TarotCard(name='King of Wands', major=False, rank=14, suit='wands', image=pg.image.load('graphics/TarotCards/King_of_Wands.png'),
        desc=dscr_Kw, gender='HIM')
# Minor Swords
if True:
    tAs = TarotCard(name='Ace of Swords', major=False, rank=1, suit='swords', image=pg.image.load('graphics/TarotCards/Ace_of_Swords.png'),
        desc=dscr_As, gender='IT')
    t2s = TarotCard(name='Two of Swords', major=False, rank=2, suit='swords', image=pg.image.load('graphics/TarotCards/Two_of_Swords.png'),
        desc=dscr_2s, gender='HER')
    t3s = TarotCard(name='Three of Swords', major=False, rank=3, suit='swords', image=pg.image.load('graphics/TarotCards/Three_of_Swords.png'),
        desc=dscr_3s, gender='IT')
    t4s = TarotCard(name='Four of Swords', major=False, rank=4, suit='swords', image=pg.image.load('graphics/TarotCards/Four_of_Swords.png'),
        desc=dscr_4s, gender='HIM')
    t5s = TarotCard(name='Five of Swords', major=False, rank=5, suit='swords', image=pg.image.load('graphics/TarotCards/Five_of_Swords.png'),
        desc=dscr_5s, gender='HIM')
    t6s = TarotCard(name='Six of Swords', major=False, rank=6, suit='swords', image=pg.image.load('graphics/TarotCards/Six_of_Swords.png'),
        desc=dscr_6s, gender='HIM')
    t7s = TarotCard(name='Seven of Swords', major=False, rank=7, suit='swords', image=pg.image.load('graphics/TarotCards/Seven_of_Swords.png'),
        desc=dscr_7s, gender='HIM')
    t8s = TarotCard(name='Eight of Swords', major=False, rank=8, suit='swords', image=pg.image.load('graphics/TarotCards/Eight_of_Swords.png'),
        desc=dscr_8s, gender='HER')
    t9s = TarotCard(name='Nine of Swords', major=False, rank=9, suit='swords', image=pg.image.load('graphics/TarotCards/Nine_of_Swords.png'),
        desc=dscr_9s, gender='HER')
    t0s = TarotCard(name='Ten of Swords', major=False, rank=10, suit='swords', image=pg.image.load('graphics/TarotCards/Ten_of_Swords.png'),
        desc=dscr_10s, gender='HIM')
    tPs = TarotCard(name='Page of Swords', major=False, rank=11, suit='swords', image=pg.image.load('graphics/TarotCards/Page_of_Swords.png'),
        desc=dscr_Ps, gender='HIM')
    tNs = TarotCard(name='Knight of Swords', major=False, rank=12, suit='swords', image=pg.image.load('graphics/TarotCards/Knight_of_Swords.png'),
        desc=dscr_Ns, gender='HIM')
    tQs = TarotCard(name='Queen of Swords', major=False, rank=13, suit='swords', image=pg.image.load('graphics/TarotCards/Queen_of_Swords.png'),
        desc=dscr_Qs, gender='HER')
    tKs = TarotCard(name='King of Swords', major=False, rank=14, suit='swords', image=pg.image.load('graphics/TarotCards/King_of_Swords.png'),
        desc=dscr_Ks, gender='HIM')

class Reading():
    full_deck = [t0r,t1r,t2r,t3r,t4r,t5r,t6r,t7r,t8r,t9r,t10r,
                 t11r,t12r,t14r,t15r,t16r,t17r,t18r,t19r,t20r,t21r,
                 tAc,t2c,t3c,t4c,t5c,t6c,t7c,t8c,t9c,t0c,tPc,tNc,tQc,tKc,
                 tAp,t2p,t3p,t4p,t5p,t6p,t7p,t8p,t9p,t0p,tPp,tNp,tQp,tKp,
                 tAw,t2w,t3w,t4w,t5w,t6w,t7w,t8w,t9w,t0w,tPw,tNw,tQw,tKw,
                 tAs,t2s,t3s,t4s,t5s,t6s,t7s,t8s,t9s,t0s,tPs,tNs,tQs,tKs]
    deck = full_deck
    board = []
    c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 = 0,0,0,0,0,0,0,0,0,0,0
    stage = -1

    def reset(self):
        global display_significator,display_covers,display_crosses,display_crowns,display_beneath,display_behind
        global display_before, display_self, display_house, display_hopes, display_outcome

        # Resetting the images so cards dont get wrongly flipped
        if True:
            # Major Arcana
            t0r.image = pg.image.load('graphics/TarotCards/0 The Fool.png')
            t1r.image = pg.image.load('graphics/TarotCards/1 - The Magician.png')
            t2r.image = pg.image.load('graphics/TarotCards/2 - The High Priestess.png')
            t3r.image = pg.image.load('graphics/TarotCards/3 - The Empress.png')
            t4r.image = pg.image.load('graphics/TarotCards/4 - The Emperor.png')
            t5r.image = pg.image.load('graphics/TarotCards/5 - The Hierophant.png')
            t6r.image = pg.image.load('graphics/TarotCards/6 - The Lovers.png')
            t7r.image = pg.image.load('graphics/TarotCards/7 - The Chariot.png')
            t8r.image = pg.image.load('graphics/TarotCards/8 - Strength.png')
            t9r.image = pg.image.load('graphics/TarotCards/9 - The Hermit.png')
            t10r.image = pg.image.load('graphics/TarotCards/10 - The Wheel.png')
            t11r.image = pg.image.load('graphics/TarotCards/11 - Justice.png')
            t12r.image = pg.image.load('graphics/TarotCards/12 - The Hanged Man.png')
            t13r.image = pg.image.load('graphics/TarotCards/13 - Death.png')
            t14r.image = pg.image.load('graphics/TarotCards/14 - Temperance.png')
            t15r.image = pg.image.load('graphics/TarotCards/15 - The Devil.png')
            t16r.image = pg.image.load('graphics/TarotCards/16 - The Tower.png')
            t17r.image = pg.image.load('graphics/TarotCards/17 -The Star.png')
            t18r.image = pg.image.load('graphics/TarotCards/18 - The Moon.png')
            t19r.image = pg.image.load('graphics/TarotCards/19 - The Sun.png')
            t20r.image = pg.image.load('graphics/TarotCards/20 - Judgment.png')
            t21r.image = pg.image.load('graphics/TarotCards/21 - The World.png')

            # Minor Cups
            tAc.image = pg.image.load('graphics/TarotCards/Ace_of_Cups.png')
            t2c.image = pg.image.load('graphics/TarotCards/Two_of_Cups.png')
            t3c.image = pg.image.load('graphics/TarotCards/Three_of_Cups.png')
            t4c.image = pg.image.load('graphics/TarotCards/Four_of_Cups.png')
            t5c.image = pg.image.load('graphics/TarotCards/Five_of_Cups.png')
            t6c.image = pg.image.load('graphics/TarotCards/Six_of_Cups.png')
            t7c.image = pg.image.load('graphics/TarotCards/Seven_of_Cups.png')
            t8c.image = pg.image.load('graphics/TarotCards/Eight_of_Cups.png')
            t9c.image = pg.image.load('graphics/TarotCards/Nine_of_Cups.png')
            t0c.image = pg.image.load('graphics/TarotCards/Ten_of_Cups.png')
            tPc.image = pg.image.load('graphics/TarotCards/Page_of_Cups.png')
            tNc.image = pg.image.load('graphics/TarotCards/Knight_of_Cups.png')
            tQc.image = pg.image.load('graphics/TarotCards/Queen_of_Cups.png')
            tKc.image = pg.image.load('graphics/TarotCards/King_of_Cups.png')

            # Minor Pentacles
            tAp.image = pg.image.load('graphics/TarotCards/Ace_of_Pentacles.png')
            t2p.image = pg.image.load('graphics/TarotCards/Two_of_Pentacles.png')
            t3p.image = pg.image.load('graphics/TarotCards/Three_of_Pentacles.png')
            t4p.image = pg.image.load('graphics/TarotCards/Four_of_Pentacles.png')
            t5p.image = pg.image.load('graphics/TarotCards/Five_of_Pentacles.png')
            t6p.image = pg.image.load('graphics/TarotCards/Six_of_Pentacles.png')
            t7p.image = pg.image.load('graphics/TarotCards/Seven_of_Pentacles.png')
            t8p.image = pg.image.load('graphics/TarotCards/Eight_of_Pentacles.png')
            t9p.image = pg.image.load('graphics/TarotCards/Nine_of_Pentacles.png')
            t0p.image = pg.image.load('graphics/TarotCards/Ten_of_Pentacles.png')
            tPp.image = pg.image.load('graphics/TarotCards/Page_of_Pentacles.png')
            tNp.image = pg.image.load('graphics/TarotCards/Knight_of_Pentacles.png')
            tQp.image = pg.image.load('graphics/TarotCards/Queen_of_Pentacles.png')
            tKp.image = pg.image.load('graphics/TarotCards/King_of_Pentacles.png')

            # Minor Wands
            tAw.image = pg.image.load('graphics/TarotCards/Ace_of_Wands.png')
            t2w.image = pg.image.load('graphics/TarotCards/Two_of_Wands.png')
            t3w.image = pg.image.load('graphics/TarotCards/Three_of_Wands.png')
            t4w.image = pg.image.load('graphics/TarotCards/Four_of_Wands.png')
            t5w.image = pg.image.load('graphics/TarotCards/Five_of_Wands.png')
            t6w.image = pg.image.load('graphics/TarotCards/Six_of_Wands.png')
            t7w.image = pg.image.load('graphics/TarotCards/Seven_of_Wands.png')
            t8w.image = pg.image.load('graphics/TarotCards/Eight_of_Wands.png')
            t9w.image = pg.image.load('graphics/TarotCards/Nine_of_Wands.png')
            t0w.image = pg.image.load('graphics/TarotCards/Ten_of_Wands.png')
            tPw.image = pg.image.load('graphics/TarotCards/Page_of_Wands.png')
            tNw.image = pg.image.load('graphics/TarotCards/Knight_of_Wands.png')
            tQw.image = pg.image.load('graphics/TarotCards/Queen_of_Wands.png')
            tKw.image = pg.image.load('graphics/TarotCards/King_of_Wands.png')

            # Minor Swords
            tAs.image = pg.image.load('graphics/TarotCards/Ace_of_Swords.png')
            t2s.image = pg.image.load('graphics/TarotCards/Two_of_Swords.png')
            t3s.image = pg.image.load('graphics/TarotCards/Three_of_Swords.png')
            t4s.image = pg.image.load('graphics/TarotCards/Four_of_Swords.png')
            t5s.image = pg.image.load('graphics/TarotCards/Five_of_Swords.png')
            t6s.image = pg.image.load('graphics/TarotCards/Six_of_Swords.png')
            t7s.image = pg.image.load('graphics/TarotCards/Seven_of_Swords.png')
            t8s.image = pg.image.load('graphics/TarotCards/Eight_of_Swords.png')
            t9s.image = pg.image.load('graphics/TarotCards/Nine_of_Swords.png')
            t0s.image = pg.image.load('graphics/TarotCards/Ten_of_Swords.png')
            tPs.image = pg.image.load('graphics/TarotCards/Page_of_Swords.png')
            tNs.image = pg.image.load('graphics/TarotCards/Knight_of_Swords.png')
            tQs.image = pg.image.load('graphics/TarotCards/Queen_of_Swords.png')
            tKs.image = pg.image.load('graphics/TarotCards/King_of_Swords.png')


        self.deck = [t0r, t1r, t2r, t3r, t4r, t5r, t6r, t7r, t8r, t9r, t10r,
                     t11r, t12r, t14r, t15r, t16r, t17r, t18r, t19r, t20r, t21r,
                     tAc, t2c, t3c, t4c, t5c, t6c, t7c, t8c, t9c, t0c, tPc, tNc, tQc, tKc,
                     tAp, t2p, t3p, t4p, t5p, t6p, t7p, t8p, t9p, t0p, tPp, tNp, tQp, tKp,
                     tAw, t2w, t3w, t4w, t5w, t6w, t7w, t8w, t9w, t0w, tPw, tNw, tQw, tKw,
                     tAs, t2s, t3s, t4s, t5s, t6s, t7s, t8s, t9s, t0s, tPs, tNs, tQs, tKs]
        for card in self.deck:
            card.reversed = False
            card.image = pg.transform.scale(card.image, (card_size))
            card.rect = card.image.get_rect(center=(0, 0))

        self.board = []
        self.c0, self.c1, self.c2, self.c3, self.c4, self.c5 = 0,0,0,0,0,0
        self.c6, self.c7, self.c8, self.c9, self.c10 = 0,0,0,0,0
        self.stage = -1
        display_significator = False; display_covers = False; display_crosses = False; display_crowns = False;
        display_beneath = False; display_behind = False; display_before = False; display_self = False;
        display_house = False; display_hopes = False; display_outcome = False

    def draw_all(self):
        for n in range(11 - len(game.board)):
            self.draw_card()

    def draw_card(self):
        self.stage += 1
        if self.stage == 0: self.draw_significator()
        if self.stage == 1: self.draw_covers()
        if self.stage == 2: self.draw_crosses()
        if self.stage == 3: self.draw_crowns()
        if self.stage == 4: self.draw_beneath()
        if self.stage == 5: self.draw_behind()
        if self.stage == 6: self.draw_before()
        if self.stage == 7: self.draw_self()
        if self.stage == 8: self.draw_house()
        if self.stage == 9: self.draw_hopes()
        if self.stage == 10: self.draw_outcome()


    def draw_significator(self):
        global display_significator_desc, c0_bigcard_surf
        while self.c0 == 0 or self.c0 in [t1r,t2r]:
            self.c0 = rng.choice(self.deck)
        self.deck.remove(self.c0)
        self.board.append(self.c0)
        self.c0.reversed = False
        display_significator_desc = f'{self.c0.desc}'
        self.c0.rect.center = (coordinates_sig)
        c0_bigcard_surf = pg.transform.scale(self.c0.image, bigcard_size)

    def draw_covers(self):
        global display_covers_desc, c1_bigcard_surf
        self.c1 = rng.choice(self.deck)
        self.deck.remove(self.c1)
        self.board.append(self.c1)
        self.c1.reversed = rng.choice([True,False])
        if self.c1.reversed:
            self.c1.image = pg.transform.rotate(self.c1.image, 180)
        display_covers_desc = f'{self.c1.desc}'
        self.c1.rect.center = (coordinates_covers)
        c1_bigcard_surf = pg.transform.scale(self.c1.image, bigcard_size)

    def draw_crosses(self):
        global display_crosses_desc, c2_bigcard_surf
        self.c2 = rng.choice(self.deck)
        self.deck.remove(self.c2)
        self.board.append(self.c2)
        self.c2.reversed = False
        display_crosses_desc = f'{self.c2.desc}'
        self.c2.rect.center = (coordinates_crosses)
        c2_bigcard_surf = pg.transform.scale(self.c2.image, bigcard_size)

    def draw_crowns(self):
        global display_crowns_desc, c3_bigcard_surf
        self.c3 = rng.choice(self.deck)
        self.deck.remove(self.c3)
        self.board.append(self.c3)
        self.c3.reversed = rng.choice([True,False])
        if self.c3.reversed:
            self.c3.image = pg.transform.rotate(self.c3.image, 180)
        display_crowns_desc = f'{self.c3.desc}'
        self.c3.rect.center = (coordinates_crowns)
        c3_bigcard_surf = pg.transform.scale(self.c3.image, bigcard_size)

    def draw_beneath(self):
        global display_beneath_desc, c4_bigcard_surf
        self.c4 = rng.choice(self.deck)
        self.deck.remove(self.c4)
        self.board.append(self.c4)
        self.c4.reversed = rng.choice([True,False])
        if self.c4.reversed:
            self.c4.image = pg.transform.rotate(self.c4.image, 180)
        display_beneath_desc = f'{self.c4.desc}'
        self.c4.rect.center = (coordinates_beneath)
        c4_bigcard_surf = pg.transform.scale(self.c4.image, bigcard_size)

    def draw_behind(self):
        global display_behind_desc, c5_bigcard_surf
        self.c5 = rng.choice(self.deck)
        self.deck.remove(self.c5)
        self.board.append(self.c5)
        self.c5.reversed = rng.choice([True,False])
        if self.c5.reversed:
            self.c5.image = pg.transform.rotate(self.c5.image, 180)
        display_behind_desc = f'{self.c5.desc}'
        self.c5.rect.center = (coordinates_behind)
        c5_bigcard_surf = pg.transform.scale(self.c5.image, bigcard_size)

    def draw_before(self):
        global display_before_desc, c6_bigcard_surf
        self.c6 = rng.choice(self.deck)
        self.deck.remove(self.c6)
        self.board.append(self.c6)
        self.c6.reversed = rng.choice([True,False])
        if self.c6.reversed:
            self.c6.image = pg.transform.rotate(self.c6.image, 180)
        display_before_desc = f'{self.c6.desc}'
        self.c6.rect.center = (coordinates_before)
        c6_bigcard_surf = pg.transform.scale(self.c6.image, bigcard_size)

    def draw_self(self):
        global display_self_desc, c7_bigcard_surf
        self.c7 = rng.choice(self.deck)
        self.deck.remove(self.c7)
        self.board.append(self.c7)
        self.c7.reversed = rng.choice([True,False])
        if self.c7.reversed:
            self.c7.image = pg.transform.rotate(self.c7.image, 180)
        display_self_desc = f'{self.c7.desc}'
        self.c7.rect.center = (coordinates_self)
        c7_bigcard_surf = pg.transform.scale(self.c7.image, bigcard_size)

    def draw_house(self):
        global display_house_desc, c8_bigcard_surf
        self.c8 = rng.choice(self.deck)
        self.deck.remove(self.c8)
        self.board.append(self.c8)
        self.c8.reversed = rng.choice([True,False])
        if self.c8.reversed:
            self.c8.image = pg.transform.rotate(self.c8.image, 180)
        display_house_desc = f'{self.c8.desc}'
        self.c8.rect.center = (coordinates_house)
        c8_bigcard_surf = pg.transform.scale(self.c8.image, bigcard_size)

    def draw_hopes(self):
        global display_hopes_desc, c9_bigcard_surf
        self.c9 = rng.choice(self.deck)
        self.deck.remove(self.c9)
        self.board.append(self.c9)
        self.c9.reversed = rng.choice([True,False])
        if self.c9.reversed:
            self.c9.image = pg.transform.rotate(self.c9.image, 180)
        display_hopes_desc = f'{self.c9.desc}'
        self.c9.rect.center = (coordinates_hopes)
        c9_bigcard_surf = pg.transform.scale(self.c9.image, bigcard_size)

    def draw_outcome(self):
        global display_outcome_desc, c10_bigcard_surf
        self.c10 = rng.choice(self.deck)
        self.deck.remove(self.c10)
        self.board.append(self.c10)
        self.c10.reversed = rng.choice([True,False])
        if self.c10.reversed:
            self.c10.image = pg.transform.rotate(self.c10.image, 180)
        display_outcome_desc = f'{self.c10.desc}'
        self.c10.rect.center = (coordinates_outcome)
        c10_bigcard_surf = pg.transform.scale(self.c10.image, bigcard_size)


game = Reading()


################################ DESCRIPTIONS ###############################


display_desc_surf = pg.Surface((100,10))
display_desc_rect = display_desc_surf.get_rect(center = coordinates_description)



display_significator = False;display_covers = False;display_crosses = False;display_crowns = False;display_beneath = False
display_behind = False;display_before = False;display_self = False;display_house = False;display_hopes = False;display_outcome = False

############# WRAPAROUND??? ###################################
def draw_wrapped_text(surface, text, font, color, rect, line_spacing=5):
    """Draws wrapped text inside a given rect on the Pygame surface."""
    words = text.split(' ')
    space_width, space_height = font.size(' ')
    x, y = rect.topleft
    max_width = rect.width
    line = ""

    for word in words:
        test_line = line + word + " "
        test_width, _ = font.size(test_line)

        if test_width <= max_width:
            line = test_line
        else:
            rendered_line = font.render(line, True, color)
            surface.blit(rendered_line, (x, y))
            y += space_height + line_spacing
            line = word + " "

    if line:
        rendered_line = font.render(line, True, color)
        surface.blit(rendered_line, (x, y))

description_rect = pg.Rect(980, 300, 600, 200)


####################################### BIG CARD ON MOUSEOVER ##################################################
bigcard_size = (card_size[0]*2,card_size[1]*2)
bigcard_rect = (490,10)

############################### GAME LOOOP ######################################
counter = 5
while running:
    counter += 1

    # Names and descriptions for mouseover
    if game.c0:
        display_significator_text = font.render(f'THE SIGNIFICATOR:', True, 'Black')
        if game.c0.reversed: display_significator_subtext = font.render(f'{game.c0.name} Reversed', True, 'Black')
        else: display_significator_subtext = font.render(f'{game.c0.name}', True, 'Black')
        display_significator_surf = pg.Surface((100, 10))
        display_significator_rect = display_significator_surf.get_rect(center=coordinates_display_title)
    if game.c1:
        display_covers_text = font.render(f'WHAT COVERS {game.c0.gender}:', True, 'Black')
        if game.c1.reversed: display_covers_subtext = font.render(f'{game.c1.name} Reversed', True, 'Black')
        else: display_covers_subtext = font.render(f'{game.c1.name}', True, 'Black')
        display_covers_surf = pg.Surface((100, 10))
        display_covers_rect = display_covers_surf.get_rect(center=coordinates_display_title)
    if game.c2:
        display_crosses_text = font.render(f'WHAT CROSSES {game.c0.gender}:', True, 'Black')
        if game.c2.reversed: display_crosses_subtext = font.render(f'{game.c2.name} Reversed', True, 'Black')
        else: display_crosses_subtext = font.render(f'{game.c2.name}', True, 'Black')
        display_crosses_surf = pg.Surface((100, 10))
        display_crosses_rect = display_crosses_surf.get_rect(center=coordinates_display_title)
    if game.c3:
        display_crowns_text = font.render(f'WHAT CROWNS {game.c0.gender}:', True, 'Black')
        if game.c3.reversed: display_crowns_subtext = font.render(f'{game.c3.name} Reversed', True, 'Black')
        else: display_crowns_subtext = font.render(f'{game.c3.name}', True, 'Black')
        display_crowns_surf = pg.Surface((100, 10))
        display_crowns_rect = display_crowns_surf.get_rect(center=coordinates_display_title)
    if game.c4:
        display_beneath_text = font.render(f'WHAT SITS BENEATH {game.c0.gender}:', True, 'Black')
        if game.c4.reversed: display_beneath_subtext = font.render(f'{game.c4.name} Reversed', True, 'Black')
        else: display_beneath_subtext = font.render(f'{game.c4.name}', True, 'Black')
        display_beneath_surf = pg.Surface((100, 10))
        display_beneath_rect = display_beneath_surf.get_rect(center=coordinates_display_title)
    if game.c5:
        display_behind_text = font.render(f'WHAT WAITS BEHIND {game.c0.gender}:', True, 'Black')
        if game.c5.reversed: display_behind_subtext = font.render(f'{game.c5.name} Reversed', True, 'Black')
        else: display_behind_subtext = font.render(f'{game.c5.name}', True, 'Black')
        display_behind_surf = pg.Surface((100, 10))
        display_behind_rect = display_behind_surf.get_rect(center=coordinates_display_title)
    if game.c6:
        display_before_text = font.render(f'WHAT LIES BEFORE {game.c0.gender}:', True, 'Black')
        if game.c6.reversed: display_before_subtext = font.render(f'{game.c6.name} Reversed',True,'Black')
        else: display_before_subtext = font.render(f'{game.c6.name}',True,'Black')
        display_before_surf = pg.Surface((100, 10))
        display_before_rect = display_before_surf.get_rect(center=coordinates_display_title)
    if game.c7:
        display_self_text = font.render(f'WHAT REPRESENTS {game.c0.gender}:', True, 'Black')
        if game.c7.reversed: display_self_subtext = font.render(f'{game.c7.name} Reversed', True, 'Black')
        else: display_self_subtext = font.render(f'{game.c7.name}', True, 'Black')
        display_self_surf = pg.Surface((100, 10))
        display_self_rect = display_self_surf.get_rect(center=coordinates_display_title)
    if game.c8:
        display_house_text = font.render(f'WHAT HOUSES {game.c0.gender}:', True, 'Black')
        if game.c8.reversed: display_house_subtext = font.render(f'{game.c8.name} Reversed', True, 'Black')
        else: display_house_subtext = font.render(f'{game.c8.name}', True, 'Black')
        display_house_surf = pg.Surface((100, 10))
        display_house_rect = display_house_surf.get_rect(center=coordinates_display_title)
    if game.c9:
        if game.c0.gender == 'HIM':
            display_hopes_text = font.render(f'FOR WHAT HE HOPES:', True, 'Black')
        elif game.c0.gender == 'HER':
            display_hopes_text = font.render(f'FOR WHAT SHE HOPES:', True, 'Black')
        elif game.c0.gender == 'THEM':
            display_hopes_text = font.render(f'FOR WHAT THEY HOPE:', True, 'Black')
        else:
            display_hopes_text = font.render(f'FOR WHAT IT HOPES:', True, 'Black')
        if game.c9.reversed: display_hopes_subtext = font.render(f'{game.c9.name} Reversed', True, 'Black')
        else: display_hopes_subtext = font.render(f'{game.c9.name}', True, 'Black')
        display_hopes_surf = pg.Surface((100, 10))
        display_hopes_rect = display_hopes_surf.get_rect(center=coordinates_display_title)
    if game.c10:
        display_outcome_text = font.render(f'THE FINAL OUTCOME:', True, 'Black')
        if game.c10.reversed: display_outcome_subtext = font.render(f'{game.c10.name} Reversed', True, 'Black')
        else: display_outcome_subtext = font.render(f'{game.c10.name}', True, 'Black')
        display_outcome_surf = pg.Surface((100, 10))
        display_outcome_rect = display_outcome_surf.get_rect(center=coordinates_display_title)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        else:
            mouse_pos = pg.mouse.get_pos()
            if event.type == pg.MOUSEBUTTONDOWN:
                # Clicking Buttons
                if draw_button_rect.collidepoint(mouse_pos):
                    game.draw_card()
                if all_button_rect.collidepoint(mouse_pos):
                    game.draw_all()
                if reset_button_rect.collidepoint(mouse_pos):
                    game.reset()
            if event.type == pg.MOUSEMOTION:
                # Mouseover Cards
                if game.c0 != 0:
                    if game.c0.rect.collidepoint(mouse_pos):
                        display_significator = True
                        display_covers = False
                        display_crosses = False
                        display_crowns = False
                        display_beneath = False
                        display_behind = False
                        display_before = False
                        display_self = False
                        display_house = False
                        display_hopes = False
                        display_outcome = False
                if game.c1 != 0:
                    if game.c1.rect.collidepoint(mouse_pos):
                        display_significator = False
                        display_covers = True
                        display_crosses = False
                        display_crowns = False
                        display_beneath = False
                        display_behind = False
                        display_before = False
                        display_self = False
                        display_house = False
                        display_hopes = False
                        display_outcome = False
                if game.c2 != 0:
                    if game.c2.rect.collidepoint(mouse_pos):
                        display_significator = False
                        display_covers = False
                        display_crosses = True
                        display_crowns = False
                        display_beneath = False
                        display_behind = False
                        display_before = False
                        display_self = False
                        display_house = False
                        display_hopes = False
                        display_outcome = False
                if game.c3 != 0:
                    if game.c3.rect.collidepoint(mouse_pos):
                        display_significator = False
                        display_covers = False
                        display_crosses = False
                        display_crowns = True
                        display_beneath = False
                        display_behind = False
                        display_before = False
                        display_self = False
                        display_house = False
                        display_hopes = False
                        display_outcome = False
                if game.c4 != 0:
                    if game.c4.rect.collidepoint(mouse_pos):
                        display_significator = False
                        display_covers = False
                        display_crosses = False
                        display_crowns = False
                        display_beneath = True
                        display_behind = False
                        display_before = False
                        display_self = False
                        display_house = False
                        display_hopes = False
                        display_outcome = False
                if game.c5 != 0:
                    if game.c5.rect.collidepoint(mouse_pos):
                        display_significator = False
                        display_covers = False
                        display_crosses = False
                        display_crowns = False
                        display_beneath = False
                        display_behind = True
                        display_before = False
                        display_self = False
                        display_house = False
                        display_hopes = False
                        display_outcome = False
                if game.c6 != 0:
                    if game.c6.rect.collidepoint(mouse_pos):
                        display_significator = False
                        display_covers = False
                        display_crosses = False
                        display_crowns = False
                        display_beneath = False
                        display_behind = False
                        display_before = True
                        display_self = False
                        display_house = False
                        display_hopes = False
                        display_outcome = False
                if game.c7 != 0:
                    if game.c7.rect.collidepoint(mouse_pos):
                        display_significator = False
                        display_covers = False
                        display_crosses = False
                        display_crowns = False
                        display_beneath = False
                        display_behind = False
                        display_before = False
                        display_self = True
                        display_house = False
                        display_hopes = False
                        display_outcome = False
                if game.c8 != 0:
                    if game.c8.rect.collidepoint(mouse_pos):
                        display_significator = False
                        display_covers = False
                        display_crosses = False
                        display_crowns = False
                        display_beneath = False
                        display_behind = False
                        display_before = False
                        display_self = False
                        display_house = True
                        display_hopes = False
                        display_outcome = False
                if game.c9 != 0:
                    if game.c9.rect.collidepoint(mouse_pos):
                        display_significator = False
                        display_covers = False
                        display_crosses = False
                        display_crowns = False
                        display_beneath = False
                        display_behind = False
                        display_before = False
                        display_self = False
                        display_house = False
                        display_hopes = True
                        display_outcome = False
                if game.c10 != 0:
                    if game.c10.rect.collidepoint(mouse_pos):
                        display_significator = False
                        display_covers = False
                        display_crosses = False
                        display_crowns = False
                        display_beneath = False
                        display_behind = False
                        display_before = False
                        display_self = False
                        display_house = False
                        display_hopes = False
                        display_outcome = True
                    


    # Background
    screen.fill((69, 145, 19))

    # Buttons
    screen.blit(draw_button_surf,draw_button_rect)
    screen.blit(draw_button_text,draw_button_rect)
    screen.blit(all_button_surf,all_button_rect)
    screen.blit(all_button_text,all_button_rect)
    screen.blit(reset_button_surf,reset_button_rect)
    screen.blit(reset_button_text,reset_button_rect)

    # Blitting title display on mouseover
    if display_significator:
        screen.blit(display_significator_text,display_significator_rect)
        draw_wrapped_text(screen,display_significator_desc,small_font,'Black',description_rect)
        screen.blit(display_significator_subtext,coordinates_display_subtitle)
        screen.blit(c0_bigcard_surf,bigcard_rect)
    if display_covers:
        screen.blit(display_covers_text,display_covers_rect)
        draw_wrapped_text(screen,display_covers_desc,small_font,'Black',description_rect)
        screen.blit(display_covers_subtext, coordinates_display_subtitle)
        screen.blit(c1_bigcard_surf, bigcard_rect)
    if display_crosses:
        screen.blit(display_crosses_text,display_crosses_rect)
        draw_wrapped_text(screen,display_crosses_desc,small_font,'Black',description_rect)
        screen.blit(display_crosses_subtext, coordinates_display_subtitle)
        screen.blit(c2_bigcard_surf, bigcard_rect)
    if display_crowns:
        screen.blit(display_crowns_text,display_crowns_rect)
        draw_wrapped_text(screen,display_crowns_desc,small_font,'Black',description_rect)
        screen.blit(display_crowns_subtext, coordinates_display_subtitle)
        screen.blit(c3_bigcard_surf, bigcard_rect)
    if display_beneath:
        screen.blit(display_beneath_text,display_beneath_rect)
        draw_wrapped_text(screen,display_beneath_desc,small_font,'Black',description_rect)
        screen.blit(display_beneath_subtext, coordinates_display_subtitle)
        screen.blit(c4_bigcard_surf, bigcard_rect)
    if display_behind:
        screen.blit(display_behind_text,display_behind_rect)
        draw_wrapped_text(screen,display_behind_desc,small_font,'Black',description_rect)
        screen.blit(display_behind_subtext, coordinates_display_subtitle)
        screen.blit(c5_bigcard_surf, bigcard_rect)
    if display_before:
        screen.blit(display_before_text,display_before_rect)
        draw_wrapped_text(screen,display_before_desc,small_font,'Black',description_rect)
        screen.blit(display_before_subtext, coordinates_display_subtitle)
        screen.blit(c6_bigcard_surf, bigcard_rect)
    if display_self:
        screen.blit(display_self_text,display_self_rect)
        draw_wrapped_text(screen,display_self_desc,small_font,'Black',description_rect)
        screen.blit(display_self_subtext, coordinates_display_subtitle)
        screen.blit(c7_bigcard_surf, bigcard_rect)
    if display_house:
        screen.blit(display_house_text,display_house_rect)
        draw_wrapped_text(screen,display_house_desc,small_font,'Black',description_rect)
        screen.blit(display_house_subtext, coordinates_display_subtitle)
        screen.blit(c8_bigcard_surf, bigcard_rect)
    if display_hopes:
        screen.blit(display_hopes_text,display_hopes_rect)
        draw_wrapped_text(screen,display_hopes_desc,small_font,'Black',description_rect)
        screen.blit(display_hopes_subtext, coordinates_display_subtitle)
        screen.blit(c9_bigcard_surf, bigcard_rect)
    if display_outcome:
        screen.blit(display_outcome_text,display_outcome_rect)
        draw_wrapped_text(screen,display_outcome_desc,small_font,'Black',description_rect)
        screen.blit(display_outcome_subtext, coordinates_display_subtitle)
        screen.blit(c10_bigcard_surf, bigcard_rect)

    # Blitting Cards on Board
    if game.c0 != 0:
        screen.blit(game.c0.image,game.c0.rect)
    if game.c1 != 0:
        screen.blit(game.c1.image, game.c1.rect)
    if game.c2 != 0:
        screen.blit(game.c2.image, game.c2.rect)
    if game.c3 != 0:
        screen.blit(game.c3.image, game.c3.rect)
    if game.c4 != 0:
        screen.blit(game.c4.image, game.c4.rect)
    if game.c5 != 0:
        screen.blit(game.c5.image, game.c5.rect)
    if game.c6 != 0:
        screen.blit(game.c6.image, game.c6.rect)
    if game.c7 != 0:
        screen.blit(game.c7.image, game.c7.rect)
    if game.c8 != 0:
        screen.blit(game.c8.image, game.c8.rect)
    if game.c9 != 0:
        screen.blit(game.c9.image, game.c9.rect)
    if game.c10 != 0:
        screen.blit(game.c10.image, game.c10.rect)

    # Blitting Card-Space Markers
    pg.draw.rect(screen,'brown4',marker_significator_rect,marker_width,marker_radius)
    pg.draw.rect(screen, 'brown4', marker_covers_rect, marker_width,marker_radius)
    pg.draw.rect(screen, 'brown4', marker_crosses_rect, marker_width,marker_radius)
    pg.draw.rect(screen, 'brown4', marker_crowns_rect, marker_width,marker_radius)
    pg.draw.rect(screen, 'brown4', marker_beneath_rect, marker_width,marker_radius)
    pg.draw.rect(screen, 'brown4', marker_behind_rect, marker_width,marker_radius)
    pg.draw.rect(screen, 'brown4', marker_before_rect, marker_width,marker_radius)
    pg.draw.rect(screen, 'brown4', marker_self_rect, marker_width,marker_radius)
    pg.draw.rect(screen, 'brown4', marker_house_rect, marker_width,marker_radius)
    pg.draw.rect(screen, 'brown4', marker_hopes_rect, marker_width,marker_radius)
    pg.draw.rect(screen, 'brown4', marker_outcome_rect, marker_width,marker_radius)

    # Updating display and limiting FPS
    pg.display.flip()
    clock.tick(60)
# ================================================================================================================= #
#                                                     end of code                                                   #
# ================================================================================================================= #
pg.quit()
sys.exit()
