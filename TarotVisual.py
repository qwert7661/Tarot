import random as rng
import pygame as pg
import sys
pg.init()
pg.font.init()

print("Welcome to Celtic Cross Tarot")

#=======================================================================================================================
# STARTUP | DISPLAY, CLOCK, FONT                                                          STARTUP | DISPLAY, CLOCK, FONT
#=======================================================================================================================
# Startup variables
if True:
    running = True
    screen_width = 1800
    screen_height = 1000
    screen = pg.display.set_mode((screen_width,screen_height),pg.FULLSCREEN,pg.SCALED)
    pg.display.set_caption("Celtic Cross Tarot")
    clock = pg.time.Clock()
    font = pg.font.Font(None,50)
    small_font = pg.font.Font(None,30)

#=======================================================================================================================
# COORDINATES: CARDS, MARKERS, DESCRIPTIONS                                    COORDINATES: CARDS, MARKERS, DESCRIPTIONS
#=======================================================================================================================
# Card & Marker Sizes
if True:
    card_size = (145,240)
    marker_size = (card_size[0]+8,card_size[1]+8)
    marker_width = 5; marker_radius = 10
# Card Coordinates
if True:
    x_offset = 155
    y_offset = 250
    coordinates_sig = (screen_width//2-500,screen_height//2 + 155)
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
# Creating Card-Space Rectangles
if True:
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
# Card Description Coordinates & Rectangles
if True:
    coordinates_display_title = 1030, 50
    coordinates_display_subtitle = 980, 95
    description_rect = pg.Rect(980, 150, 800, 200)
# Big Card on Mouseover Coordinates, Rectangle
if True:
    bigcard_size = (card_size[0]*2,card_size[1]*2)
    bigcard_rect = (490,40)

#=======================================================================================================================
# BUTTONS & TEXT                                                                                          BUTTONS & TEXT
#=======================================================================================================================
# Buttons
if True:
    # Draw Button
    draw_button_text = font.render('DRAW',True,'White')
    draw_button_surf = pg.Surface((130,40)); draw_button_surf.fill('Blue')
    draw_button_rect = draw_button_surf.get_rect(topleft = (coordinates_hopes[0] - 375,screen_height - 210))
    # Fill Button
    all_button_text = font.render('FILL',True,'White')
    all_button_surf = pg.Surface((130,40)); all_button_surf.fill('blue4')
    all_button_rect = all_button_surf.get_rect(topleft = (coordinates_hopes[0] - 220, screen_height - 210))
    # Reset Button
    reset_button_text = font.render('RESET',True,'White')
    reset_button_surf = pg.Surface((135,40)); reset_button_surf.fill('red4')
    reset_button_rect = reset_button_surf.get_rect(topleft = (coordinates_hopes[0] - 375, screen_height - 30))

#=======================================================================================================================
# TAROT CARD CLASS                                                                                      TAROT CARD CLASS
#=======================================================================================================================
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

# Card Descriptions
if True:
    # Major Arcana Descriptions
    if True:
        dscr_0r = "With light step, as if earth and its trammels had little power to restrain him, a young man in gorgeous vestments pauses at the brink of a precipice among the great heights of the world; he surveys the blue distance before him - its expanse of sky rather than the prospect below. His act of eager walking is still indicated, though he is stationary at the given moment; his dog is still bounding. The edge which opens on the depth has no terror; it is as if angels were waiting to uphold him, if it came about that he leaped from the height. His countenance is full of intelligence and expectant dream. He has a rose in one hand and in the other a costly wand, from which depends over his right shoulder a wallet curiously embroidered. He is a prince of the other world on his travels through this one - all amidst the morning glory, in the keen air. The sun, which shines behind him, knows whence he came, whither he is going, and how he will return by another path after many days. He is the spirit in search of experience. Many symbols of the Instituted Mysteries are summarized in this card, which reverses, under high warrants, all the confusions that have preceded it. In his Manual of Cartomancy, Grand Orient has a curious suggestion of the office of Mystic Fool, as a part of his process in higher divination; but it might call for more than ordinary gifts to put it into operation. We shall see how the card fares according to the common arts of fortune-telling, and it will be an example, to those who can discern, of the fact, otherwise so evident, that the Trumps Major had no place originally in the arts of psychic gambling, when cards are used as the counters and pretexts. Of the circumstances under which this art arose we know, however, very little. The conventional explanations say that the Fool signifies the flesh, the sensitive life, and by a peculiar satire its subsidiary name was at one time the alchemist, as depicting folly at the most insensate stage. REPRESENTS: Folly, mania, extravagance, intoxication, delirium, frenzy, bewrayment. REVERSED: Negligence, absence, distribution, carelessness, apathy, nullity, vanity."
        dscr_1r = "A youthful figure in the robe of a magician, having the countenance of divine Apollo, with smile of confidence and shining eyes. Above his head is the mysterious sign of the Holy Spirit, the sign of life, like an endless cord, forming the figure 8 in a horizontal position. About his waist is a serpent-cincture, the serpent appearing to devour its own tail. This is familiar to most as a conventional symbol of eternity, but here it indicates more especially the eternity of attainment in the spirit. In the Magician's right hand is a wand raised towards heaven, while the left hand is pointing to the earth. This dual sign is known in very high grades of the Instituted Mysteries; it shows the descent of grace, virtue and light, drawn from things above and derived to things below. The suggestion throughout is therefore the possession and communication of the Powers and Gifts of the Spirit. On the table in front of the Magician are the symbols of the four Tarot suits, signifying the elements of natural life, which lie like counters before the adept, and he adapts them as he wills. Beneath are roses and lilies, the flos campi and lilium convallium, changed into garden flowers, to show the culture of aspiration. This card signifies the divine motive in man, reflecting God, the will in the liberation of its union with that which is above. It is also the unity of individual being on all planes, and in a very high sense it is thought, in the fixation thereof. With further reference to what I have called the sign of life and its connection with the number 8, it may be remembered that Christian Gnosticism speaks of rebirth in Christ as a change 'unto the Ogdoad.' The mystic number is termed Jerusalem above, the Land flowing with Milk and Honey, the Holy Spirit and the Land of the Lord. According to Martinism, 8 is the number of Christ. REPRESENTS: Skill, diplomacy, address, subtlety; sickness, pain, loss, disaster, snares of enemies; self-confidence, will; the Querent, if male. REVERSED: Physician, Magus, mental disease, disgrace, disquiet."
        dscr_2r = "She has the lunar crescent at her feet, a horned diadem on her head, with a globe in the middle place, and a large solar cross on her breast. The scroll in her hands is inscribed with the word Tora, signifying the Greater Law, the Secret Law and the second sense of the Word. It is partly covered by her mantle, to show that some things are implied and some spoken. She is seated between the white and black pillars of the mystic Temple, and the veil of the Temple is behind her: it is embroidered with palms and pomegranates. The vestments are flowing and gauzy, and the mantle suggests light - a shimmering radiance. She has been called occult Science on the threshold of the Sanctuary of Isis, but she is really the Secret Church, the House which is of God and man. She represents also the Second Marriage of the Prince who is no longer of this world; she is the spiritual Bride and Mother, the daughter of the stars and the Higher Garden of Eden. She is, in fine, the Queen of the borrowed light, but this is the light of all. She is the Moon nourished by the milk of the Supernal Mother. In a manner, she is also the Supernal Mother herself - that is to say, she is the bright reflection. It is in this sense of reflection that her truest and highest name in symbolism is Shekinah - the co-habiting glory. According to Kabalism, there is a Shekinah both above and below. In the superior world it is called Binah, the Supernal Understanding which reflects to the emanations that are beneath. In the lower world it is Malkuth - that world being, for this purpose, understood as a blessed Kingdom that with which it is made blessed being the Indwelling Glory. Mystically speaking, the Shekinah is the Spiritual Bride of the just man, and when he reads the Law she gives the Divine meaning. There are some respects in which this card is the highest and holiest of the Greater Arcana. REPRESENTS: Secrets, mystery, the future as yet unrevealed; the woman who interests the Querent, if male; the Querent herself, if female; silence, tenacity; mystery, wisdom, science. REVERSED: Passion, moral or physical ardour, conceit, surface knowledge."
        dscr_3r = "A stately figure, seated, having rich vestments and royal aspect, as of a daughter of heaven and earth. Her diadem is of twelve stars, gathered in a cluster. The symbol of Venus is on the shield which rests near her. A field of corn is ripening in front of her, and beyond there is a fall of water. The sceptre which she bears is surmounted by the globe of this world. She is the inferior Garden of Eden, the Earthly Paradise, all that is symbolized by the visible house of man. She is not Regina coeli, but she is still refugium peccatorum, the fruitful mother of thousands. There are also certain aspects in which she has been correctly described as desire and the wings thereof, as the woman clothed with the sun, as Gloria Mundi and the veil of the Sanctum Sanctorum; but she is not, I may add, the soul that has attained wings, unless all the symbolism is counted up another and unusual way. She is above all things universal fecundity and the outer sense of the Word. This is obvious, because there is no direct message which has been given to man like that which is borne by woman; but she does not herself carry its interpretation. In another order of ideas, the card of the Empress signifies the door or gate by which an entrance is obtained into this life, as into the Garden of Venus; and then the way which leads out therefrom, into that which is beyond, is the secret known to the High Priestess: it is communicated by her to the elect. Most old attributions of this card are completely wrong on the symbolism - as, for example, its identification with the Word, Divine Nature, the Triad, and so forth. REPRESENTS: Fruitfulness, action, initiative, length of days; the unknown, clandestine; also difficulty, doubt, ignorance. REVERSED: Light, truth, the unravelling of involved matters, public rejoicings; according to another reading, vacillation."
        dscr_4r = "He has a form of the Crux ansata for his sceptre and a globe in his left hand. He is a crowned monarch - commanding, stately, seated on a throne, the arms of which are fronted by rams' heads. He is executive and realization, the power of this world, here clothed with the highest of its natural attributes. He is occasionally represented as seated on a cubic stone, which, however, confuses some of the issues. He is the virile power, to which the Empress responds, and in this sense is he who seeks to remove the Veil of Isis; yet she remains virgo intacta. It should be understood that this card and that of the Empress do not precisely represent the condition of married life, though this state is implied. On the surface, as I have indicated, they stand for mundane royalty, uplifted on the seats of the mighty; but above this there is the suggestion of another presence. They signify also - and the male figure especially - the higher kingship, occupying the intellectual throne. Hereof is the lordship of thought rather than of the animal world. Both personalities, after their own manner, are full of strange experience, but theirs is not consciously the wisdom which draws from a higher world. The Emperor has been described as (a) will in its embodied form, but this is only one of its applications, and (b) as an expression of virtualities contained in the Absolute Being - but this is fantasy. REPRESENTS: Stability, power, protection, realization; a great person; aid, reason, conviction; also authority and will. REVERSED: Benevolence, compassion, credit; also confusion to enemies, obstruction, immaturity."
        dscr_5r = "He wears the triple crown and is seated between two pillars, but they are not those of the Temple which is guarded by the High Priestess. In his left hand he holds a sceptre terminating in the triple cross, and with his right hand he gives the well-known ecclesiastical sign which is called that of esotericism, distinguishing between the manifest and concealed part of doctrine. It is noticeable in this connection that the High Priestess makes no sign. At his feet are the crossed keys, and two priestly ministers in albs kneel before him. He has been usually called the Pope, which is a particular application of the more general office that he symbolizes. He is the ruling power of external religion, as the High Priestess is the prevailing genius of the esoteric, withdrawn power. The proper meanings of this card have suffered woeful admixture from nearly all hands. Grand Orient says truly that the Hierophant is the power of the keys, exoteric orthodox doctrine, and the outer side of the life which leads to the doctrine; but he is certainly not the prince of occult doctrine, as another commentator has suggested. He is rather the summa totius theologiæ, when it has passed into the utmost rigidity of expression; but he symbolizes also all things that are righteous and sacred on the manifest side. As such, he is the channel of grace belonging to the world of institution as distinct from that of Nature, and he is the leader of salvation for the human race at large. He is the order and the head of the recognized hierarchy, which is the reflection of another and greater hierarchic order; but it may so happen that the pontiff forgets the significance of this his symbolic state and acts as if he contained within his proper measures all that his sign signifies or his symbol seeks to show forth. He is not, as it has been thought, philosophy - except on the theological side; he is not inspiration; and he is not religion, although he is a mode of its expression. REPRESENTS: Marriage, alliance, captivity, servitude; by another account, mercy and goodness; inspiration; the man to whom the Querent has recourse. REVERSED: Society, good understanding, concord, overkindness, weakness."
        dscr_6r = "The sun shines in the zenith, and beneath is a great winged figure with arms extended, pouring down influences. In the foreground are two human figures, male and female, unveiled before each other, as if Adam and Eve when they first occupied the paradise of the earthly body. Behind the man is the Tree of Life, bearing twelve fruits, and the Tree of the Knowledge of Good and Evil is behind the woman; the serpent is twining round it. The figures suggest youth, virginity, innocence and love before it is contaminated by gross material desire. This is in all simplicity the card of human love, here exhibited as part of the way, the truth and the life. It replaces, by recourse to first principles, the old card of marriage, which I have described previously, and the later follies which depicted man between vice and virtue. In a very high sense, the card is a mystery of the Covenant and Sabbath. The suggestion in respect of the woman is that she signifies that attraction towards the sensitive life which carries within it the idea of the Fall of Man, but she is rather the working of a Secret Law of Providence than a willing and conscious temptress. It is through her imputed lapse that man shall arise ultimately, and only by her can he complete himself. The card is therefore in its way another intimation concerning the great mystery of womanhood. The old meanings fall to pieces of necessity with the old pictures, but even as interpretations of the latter, some of them were of the order of commonplace and others were false in symbolism. REPRESENTS: Attraction, love, beauty, trials overcome. REVERSED: Failure, foolish designs. Another account speaks of marriage frustrated and contrarieties of all kinds."
        dscr_7r = "An erect and princely figure carrying a drawn sword and corresponding, broadly speaking, to the traditional description which I have given in the first part. On the shoulders of the victorious hero are supposed to be the Urim and Thummim. He has led captivity captive; he is conquest on all planes - in the mind, in science, in progress, in certain trials of initiation. He has thus replied to the sphinx, and it is on this account that I have accepted the variation of Éliphas Lévi; two sphinxes thus draw his chariot. He is above all things triumph in the mind. It is to be understood for this reason (a) that the question of the sphinx is concerned with a Mystery of Nature and not of the world of Grace, to which the charioteer could offer no answer; (b) that the planes of his conquest are manifest or external and not within himself; (c) that the liberation which he effects may leave himself in the bondage of the logical understanding; (d) that the tests of initiation through which he has passed in triumph are to be understood physically or rationally; and (e) that if he came to the pillars of that Temple between which the High Priestess is seated, he could not open the scroll called Tora, nor if she questioned him could he answer. He is not hereditary royalty and he is not priesthood. REPRESENTS: Succour, providence; also war, triumph, presumption, vengeance, trouble. REVERSED: Riot, quarrel, dispute, litigation, defeat."
        dscr_8r = "A woman, over whose head there broods the same symbol of life which we have seen in the card of the Magician, is closing the jaws of a lion. The only point in which this design differs from the conventional presentations is that her beneficent fortitude has already subdued the lion, which is being led by a chain of flowers. For reasons which satisfy myself, this card has been interchanged with that of justice, which is usually numbered eight. As the variation carries nothing with it which will signify to the reader, there is no cause for explanation. Fortitude, in one of its most exalted aspects, is connected with the Divine Mystery of Union; the virtue, of course, operates in all planes, and hence draws on all in its symbolism. It connects also with innocentia inviolata, and with the strength which resides in contemplation. These higher meanings are, however, matters of inference, and I do not suggest that they are transparent on the surface of the card. They are intimated in a concealed manner by the chain of flowers, which signifies, among many other things, the sweet yoke and the light burden of Divine Law, when it has been taken into the heart of hearts. The card has nothing to do with self-confidence in the ordinary sense, though this has been suggested - but it concerns the confidence of those whose strength is God, who have found their refuge in Him. There is one aspect in which the lion signifies the passions, and she who is called Strength is the higher nature in its liberation. It has walked upon the asp and the basilisk and has trodden down the lion and the dragon. REPRESENTS: Power, energy, action, courage, magnanimity; also complete success and honours. REVERSED: Despotism, abuse of power, weakness, discord, sometimes even disgrace."
        dscr_9r = "The variation from the conventional models in this card is only that the lamp is not enveloped partially in the mantle of its bearer, who blends the idea of the Ancient of Days with the Light of the World. It is a star which shines in the lantern. I have said that this is a card of attainment, and to extend this conception the figure is seen holding up his beacon on an eminence. Therefore the Hermit is not, as Court de Gebelin explained, a wise man in search of truth and justice; nor is he, as a later explanation proposes, an especial example of experience. His beacon intimates that 'where I am, you also may be.' It is further a card which is understood quite incorrectly when it is connected with the idea of occult isolation, as the protection of personal magnetism against admixture. This is one of the frivolous renderings which we owe to Éliphas Lévi. It has been adopted by the French Order of Martinism and some of us have heard a great deal of the Silent and Unknown Philosophy enveloped by his mantle from the knowledge of the profane. In true Martinism, the significance of the term Philosophe Inconnu was of another order. It did not refer to the intended concealment of the Instituted Mysteries, much less of their substitutes, but - like the card itself - to the truth that the Divine Mysteries secure their own protection from those who are unprepared. REPRESENTS: Prudence, circumspection; also and especially treason, dissimulation, roguery, corruption. REVERSED: Concealment, disguise, policy, fear, unreasoned caution."
        dscr_10r = "In this symbol I have again followed the reconstruction of Éliphas Lévi, who has furnished several variants. It is legitimate - as I have intimated - to use Egyptian symbolism when this serves our purpose, provided that no theory of origin is implied therein. I have, however, presented Typhon in his serpent form. The symbolism is, of course, not exclusively Egyptian, as the four Living Creatures of Ezekiel occupy the angles of the card, and the wheel itself follows other indications of Lévi in respect of Ezekiel's vision, as illustrative of the particular Tarot Key. With the French occultist, and in the design itself, the symbolic picture stands for the perpetual motion of a fluidic universe and for the flux of human life. The Sphinx is the equilibrium therein. The transliteration of Taro as Rota is inscribed on the wheel, counterchanged with the letters of the Divine Name - to show that Providence is implied through all. But this is the Divine intention within, and the similar intention without is exemplified by the four Living Creatures. Sometimes the sphinx is represented couchant on a pedestal above, which defrauds the symbolism by stultifying the essential idea of stability amidst movement. Behind the general notion expressed in the symbol there lies the denial of chance and the fatality which is implied therein. It may be added that, from the days of Lévi onward, the occult explanations of this card are - even for occultism itself - of a singularly fatuous kind. It has been said to mean principle, fecundity, virile honour, ruling authority, etc. The findings of common fortune-telling are better than this on their own plane. REPRESENTS: Destiny, fortune, success, elevation, luck, felicity. REVERSED: Increase, abundance, superfluity."
        dscr_11r = "As this card follows the traditional symbolism and carries above all its obvious meanings, there is little to say regarding it outside the few considerations collected in the first part, to which the reader is referred. It will be seen, however, that the figure is seated between pillars, like the High Priestess, and on this account it seems desirable to indicate that the moral principle which deals unto every man according to his works - while, of course, it is in strict analogy with higher things - differs in its essence from the spiritual justice which is involved in the idea of election. The latter belongs to a mysterious order of Providence, in virtue of which it is possible for certain men to conceive the idea of dedication to the highest things. The operation of this is like the breathing of the Spirit where it wills, and we have no canon of criticism or ground of explanation concerning it. It is analogous to the possession of the fairy gifts and the high gifts and the gracious gifts of the poet: we have them or have not, and their presence is as much a mystery as their absence. The law of Justice is not however involved by either alternative. In conclusion, the pillars of Justice open into one world and the pillars of the High Priestess into another. REPRESENTS: Equity, rightness, probity, executive; triumph of the deserving side in law. REVERSED: Law in all its departments, legal complications, bigotry, bias, excessive severity."
        dscr_12r = "The gallows from which he is suspended forms a Tau cross, while the figure - from the position of the legs - forms a fylfot cross. There is a nimbus about the head of the seeming martyr. It should be noted (1) that the tree of sacrifice is living wood, with leaves thereon; (2) that the face expresses deep entrancement, not suffering; (3) that the figure, as a whole, suggests life in suspension, but life and not death. It is a card of profound significance, but all the significance is veiled. One of his editors suggests that Éliphas Lévi did not know the meaning, which is unquestionable, nor did the editor himself. It has been called falsely a card of martyrdom, a card of prudence, a card of the Great Work, a card of duty; but we may exhaust all published interpretations and find only vanity. I will say very simply on my own part that it expresses the relation, in one of its aspects, between the Divine and the Universe. He who can understand that the story of his higher nature is embedded in this symbolism will receive intimations concerning a great awakening that is possible, and will know that after the sacred Mystery of Death there is a glorious Mystery of Resurrection. REPRESENTS: Wisdom, circumspection, discernment, trials, sacrifice, intuition, divination, prophecy. REVERSED: Selfishness, the crowd, body politic."
        dscr_13r = "The veil or mask of life is perpetuated in change, transformation and passage from lower to higher, and this is more fitly represented in the rectified Tarot by one of the apocalyptic visions than by the crude notion of the reaping skeleton. Behind it lies the whole world of ascent in the spirit. The mysterious horseman moves slowly, bearing a black banner emblazoned with the Mystic Rose, which signifies life. Between two pillars on the verge of the horizon there shines the sun of immortality. The horseman carries no visible weapon, but king and child and maiden fall before him, while a prelate with clasped hands awaits his end. There should be no need to point out that the suggestion of death which I have made in connection with the previous card is, of course, to be understood mystically, but this is not the case in the present instance. The natural transit of man to the next stage of his being either is or may be one form of his progress, but the exotic and almost unknown entrance, while still in this life, into the state of mystical death is a change in the form of consciousness and the passage into a state to which ordinary death is neither the path nor gate. The existing occult explanations of the 13th card are, on the whole, better than usual, rebirth, creation, destruction, renewal, and the rest. REPRESENTS: End, mortality, destruction, corruption; also, for a man, the loss of a benefactor; for a woman, many contrarieties; for a maid, failure of marriage projects. REVERSED: Inertia, sleep, lethargy, petrification, somnambulism; hope destroyed."
        dscr_14r = "A winged angel, with the sign of the sun upon his forehead and on his breast the square and triangle of the septenary. I speak of him in the masculine sense, but the figure is neither male nor female. It is held to be pouring the essences of life from chalice to chalice. It has one foot upon the earth and one upon waters, thus illustrating the nature of the essences. A direct path goes up to certain heights on the verge of the horizon, and above there is a great light, through which a crown is seen vaguely. Hereof is some part of the Secret of Eternal Life, as it is possible to man in his incarnation. All the conventional emblems are renounced herein. So also are the conventional meanings, which refer to changes in the seasons, perpetual movement of life and even the combination of ideas. It is, moreover, untrue to say that the figure symbolizes the genius of the sun, though it is the analogy of solar light, realized in the third part of our human triplicity. It is called Temperance fantastically, because, when the rule of it obtains in our consciousness, it tempers, combines and harmonises the psychic and material natures. Under that rule we know in our rational part something of whence we came and whither we are going. REPRESENTS: Economy, moderation, frugality, management, accommodation. REVERSED: Things connected with churches, religions, sects, the priesthood, sometimes even the priest who will marry the Querent; also disunion, unfortunate combinations, competing interests."
        dscr_15r = "The design is an accommodation, mean or harmony, between several motives mentioned in the first part. The Horned Goat of Mendes, with wings like those of a bat, is standing on an altar. At the pit of the stomach there is the sign of Mercury. The right hand is upraised and extended, being the reverse of that benediction which is given by the Hierophant in the fifth card. In the left hand there is a great flaming torch, inverted towards the earth. A reversed pentagram is on the forehead. There is a ring in front of the altar, from which two chains are carried to the necks of two figures, male and female. These are analogous with those of the fifth card, as if Adam and Eve after the Fall. Hereof is the chain and fatality of the material life. The figures are tailed, to signify the animal nature, but there is human intelligence in the faces, and he who is exalted above them is not to be their master for ever. Even now, he is also a bondsman, sustained by the evil that is in him and blind to the liberty of service. With more than his usual derision for the arts which he pretended to respect and interpret as a master therein, Éliphas Lévi affirms that the Baphometic figure is occult science and magic. Another commentator says that in the Divine world it signifies predestination, but there is no correspondence in that world with the things which below are of the brute. What it does signify is the Dweller on the Threshold without the Mystical Garden when those are driven forth therefrom who have eaten the forbidden fruit. REPRESENTS: Ravage, violence, vehemence, extraordinary efforts, force, fatality; that which is predestined but is not for this reason evil. REVERSED: Evil fatality, weakness, pettiness, blindness."
        dscr_16r = "Occult explanations attached to this card are meagre and mostly disconcerting. It is idle to indicate that it depicts man in all its aspects, because it bears this evidence on the surface. It is said further that it contains the first allusion to a material building, but I do not conceive that the Tower is more or less material than the pillars which we have met with in three previous cases. I see nothing to warrant Papus in supposing that it is literally the fall of Adam, but there is more in favour of his alternative - that it signifies the materialization of the spiritual word. The bibliographer Christian imagines that it is the downfall of the mind, seeking to penetrate the mystery of God. I agree rather with Grand Orient that it is the ruin of the House of Woe, when evil has prevailed therein, and above all that it is the rending of a House of Doctrine. I understand that the reference is, however, to a House of Falsehood. It illustrates also in the most comprehensive way the old truth that 'except the Lord build the house, they labour in vain that build it.' There is a sense in which the catastrophe is a reflection from the previous card, but not on the side of the symbolism which I have tried to indicate therein. It is more correctly a question of analogy; one is concerned with the fall into the material and animal state, while the other signifies destruction on the intellectual side. The Tower has been spoken of as the chastisement of pride and the intellect overwhelmed in the attempt to penetrate the Mystery of God; but in neither case do these explanations account for the two persons who are the living sufferers. The one is the literal word made void and the other its false interpretation. In yet a deeper sense, it may signify also the end of a dispensation, but there is no possibility here for the consideration of this involved question. REPRESENTS: Misery, distress, indigence, adversity, calamity, disgrace, deception, ruin. It is a card in particular of unforeseen catastrophe. REVERSED: According to one account, the same in a lesser degree; also oppression, imprisonment, tyranny."
        dscr_17r = "A great, radiant star of eight rays, surrounded by seven lesser stars - also of eight rays. The female figure in the foreground is entirely naked. Her left knee is on the land and her right foot upon the water. She pours Water of Life from two great ewers, irrigating sea and land. Behind her is rising ground and on the right a shrub or tree, whereon a bird alights. The figure expresses eternal youth and beauty. The star is l'étoile flamboyante, which appears in Masonic symbolism, but has been confused therein. That which the figure communicates to the living scene is the substance of the heavens and the elements. It has been said truly that the mottoes of this card are 'Waters of Life freely' and 'Gifts of the Spirit.' The summary of several tawdry explanations says that it is a card of hope. On other planes it has been certified as immortality and interior light. For the majority of prepared minds, the figure will appear as the type of Truth unveiled, glorious in undying beauty, pouring on the waters of the soul some part and measure of her priceless possession. But she is in reality the Great Mother in the Kabalistic Sephira Binah, which is supernal Understanding, who communicates to the Sephiroth that are below in the measure that they can receive her influx. REPRESENTS: Loss, theft, privation, abandonment; another reading says: hope and bright prospects. REVERSED: Arrogance, haughtiness, impotence."
        dscr_18r = "The distinction between this card and some of the conventional types is that the moon is increasing on what is called the side of mercy, to the right of the observer. It has sixteen chief and sixteen secondary rays. The card represents life of the imagination apart from life of the spirit. The path between the towers is the issue into the unknown. The dog and wolf are the fears of the natural mind in the presence of that place of exit, when there is only reflected light to guide it. The last reference is a key to another form of symbolism. The intellectual light is a reflection and beyond it is the unknown mystery which it cannot show forth. It illuminates our animal nature, types of which are represented below - the dog, the wolf and that which comes up out of the deeps, the nameless and hideous tendency which is lower than the savage beast. It strives to attain manifestation, symbolized by crawling from the abyss of water to the land, but as a rule it sinks back whence it came. The face of the mind directs a calm gaze upon the unrest below; the dew of thought falls; the message is: Peace, be still; and it may be that there shall come a calm upon the animal nature, while the abyss beneath shall cease from giving up a form. REPRESENTS: Hidden enemies, danger, calumny, darkness, terror, deception, occult forces, error. REVERSED: Instability, inconstancy, silence, lesser degrees of deception and error."
        dscr_19r = "The naked child mounted on a white horse and displaying a red standard has been mentioned already as the better symbolism connected with this card. It is the destiny of the Supernatural East and the great and holy light which goes before the endless procession of humanity, coming out from the walled garden of the sensitive life and passing on the journey home. The card signifies, therefore, the transit from the manifest light of this world, represented by the glorious sun of earth, to the light of the world to come, which goes before aspiration and is typified by the heart of a child. But the last allusion is again the key to a different form or aspect of the symbolism. The sun is that of consciousness in the spirit - the direct as the antithesis of the reflected light. The characteristic type of humanity has become a little child therein - a child in the sense of simplicity and innocence in the sense of wisdom. In that simplicity, he bears the seal of Nature and of Art; in that innocence, he signifies the restored world. When the self-knowing spirit has dawned in the consciousness above the natural mind, that mind in its renewal leads forth the animal nature in a state of perfect conformity. REPRESENTS: Material happiness, fortunate marriage, contentment. REVERSED: The same in a lesser sense."
        dscr_20r = "I have said that this symbol is essentially invariable in all Tarot sets, or at least the variations do not alter its character. The great angel is here encompassed by clouds, but he blows his bannered trumpet, and the cross as usual is displayed on the banner. The dead are rising from their tombs - a woman on the right, a man on the left hand, and between them their child, whose back is turned. But in this card there are more than three who are restored, and it has been thought worth while to make this variation as illustrating the insufficiency of current explanations. It should be noted that all the figures are as one in the wonder, adoration and ecstasy expressed by their attitudes. It is the card which registers the accomplishment of the great work of transformation in answer to the summons of the Supernal - which summons is heard and answered from within. Herein is the intimation of a significance which cannot well be carried further in the present place. What is that within us which does sound a trumpet and all that is lower in our nature rises in response - almost in a moment, almost in the twinkling of an eye? Let the card continue to depict, for those who can see no further, the Last judgment and the resurrection in the natural body; but let those who have inward eyes look and discover therewith. They will understand that it has been called truly in the past a card of eternal life, and for this reason it may be compared with that which passes under the name of Temperance. REPRESENTS: Change of position, renewal, outcome. Another account specifies total loss through lawsuit. REVERSED: Weakness, pusillanimity, simplicity; also deliberation, decision, sentence."
        dscr_21r = "As this final message of the Major Trumps is unchanged - and indeed unchangeable - in respect of its design, it has been partly described already regarding its deeper sense. It represents also the perfection and end of the Cosmos, the secret which is within it, the rapture of the universe when it understands itself in God. It is further the state of the soul in the consciousness of Divine Vision, reflected from the self-knowing spirit. But these meanings are without prejudice to that which I have said concerning it on the material side. It has more than one message on the macrocosmic side and is, for example, the state of the restored world when the law of manifestation shall have been carried to the highest degree of natural perfection. But it is perhaps more especially a story of the past, referring to that day when all was declared to be good, when the morning stars sang together and all the Sons of God shouted for joy. One of the worst explanations concerning it is that the figure symbolizes the Magus when he has reached the highest degree of initiation; another account says that it represents the absolute, which is ridiculous. The figure has been said to stand for Truth, which is, however, more properly allocated to the seventeenth card. Lastly, it has been called the Crown of the Magi. REPRESENTS: Assured success, recompense, voyage, route, emigration, flight, change of place. REVERSED: Inertia, fixity, stagnation, permanence."
    # Cups Descriptions
    if True:
        dscr_Ac = "REPRESENTS: The waters are beneath, and thereon are water-lilies; the hand issues from the cloud, holding in its palm the cup, from which four streams are pouring; a dove, bearing in its bill a cross-marked Host, descends to place the Wafer in the Cup; the dew of water is falling on all sides. It is an intimation of that which may lie behind the Lesser Arcana. Divinatory Meanings: House of the true heart, joy, content, abode, nourishment, abundance, fertility; Holy Table, felicity hereof. REVERSED: House of the false heart, mutation, instability, revolution."
        dscr_2c = "REPRESENTS: A youth and maiden are pledging one another, and above their cups rises the Caduceus of Hermes, between the great wings of which there appears a lion's head. It is a variant of a sign which is found in a few old examples of this card. Some curious emblematical meanings are attached to it, but they do not concern us in this place. Divinatory Meanings: Love, passion, friendship, affinity, union, concord, sympathy, the interrelation of the sexes, and - as a suggestion apart from all offices of divination - that desire which is not in Nature, but by which Nature is sanctified."
        dscr_3c = "REPRESENTS: Maidens in a garden-ground with cups uplifted, as if pledging one another. Divinatory Meanings: The conclusion of any matter in plenty, perfection and merriment; happy issue, victory, fulfilment, solace, healing. REVERSED: Expedition, dispatch, achievement, end. It signifies also the side of excess in physical enjoyment, and the pleasures of the senses."
        dscr_4c = "REPRESENTS: A young man is seated under a tree and contemplates three cups set on the grass before him; an arm issuing from a cloud offers him another cup. His expression notwithstanding is one of discontent with his environment. Divinatory Meanings: Weariness, disgust, aversion, imaginary vexations, as if the wine of this world had caused satiety only; another wine, as if a fairy gift, is now offered the wastrel, but he sees no consolation therein. This is also a card of blended pleasure. REVERSED: Novelty, presage, new instruction, new relations."
        dscr_5c = "REPRESENTS: A dark, cloaked figure, looking sideways at three prone cups two others stand upright behind him; a bridge is in the background, leading to a small keep or holding. Divinatory Meanings: It is a card of loss, but something remains over; three have been taken, but two are left; it is a card of inheritance, patrimony, transmission, but not corresponding to expectations; with some interpreters it is a card of marriage, but not without bitterness or frustration. REVERSED: News, alliances, affinity, consanguinity, ancestry, return, false projects."
        dscr_6c = "REPRESENTS: Children in an old garden, their cups filled with flowers. Divinatory Meanings: A card of the past and of memories, looking back, as - for example - on childhood; happiness, enjoyment, but coming rather from the past; things that have vanished. Another reading reverses this, giving new relations, new knowledge, new environment, and then the children are disporting in an unfamiliar precinct. REVERSED: The future, renewal, that which will come to pass presently."
        dscr_7c = "REPRESENTS: Strange chalices of vision, but the images are more especially those of the fantastic spirit. Divinatory Meanings: Fairy favours, images of reflection, sentiment, imagination, things seen in the glass of contemplation; some attainment in these degrees, but nothing permanent or substantial is suggested. REVERSED: Desire, will, determination, project."
        dscr_8c = "REPRESENTS: A man of dejected aspect is deserting the cups of his felicity, enterprise, undertaking or previous concern. Divinatory Meanings: The card speaks for itself on the surface, but other readings are entirely antithetical - giving joy, mildness, timidity, honour, modesty. In practice, it is usually found that the card shows the decline of a matter, or that a matter which has been thought to be important is really of slight consequence - either for good or evil. REVERSED: Great joy, happiness, feasting."
        dscr_9c = "REPRESENTS: A goodly personage has feasted to his heart's content, and abundant refreshment of wine is on the arched counter behind him, seeming to indicate that the future is also assured. The picture offers the material side only, but there are other aspects. Divinatory Meanings: Concord, contentment, physical bien-être; also victory, success, advantage; satisfaction for the Querent or person for whom the consultation is made. REVERSED: Truth, loyalty, liberty; but the readings vary and include mistakes, imperfections, etc."
        dscr_10c = "REPRESENTS: Appearance of Cups in a rainbow; it is contemplated in wonder and ecstasy by a man and woman below, evidently husband and wife. His right arm is about her; his left is raised upward; she raises her right arm. The two children dancing near them have not observed the prodigy but are happy after their own manner. There is a home-scene beyond. Divinatory Meanings: Contentment, repose of the entire heart; the perfection of that state; also perfection of human love and friendship; if with several picture-cards, a person who is taking charge of the Querent's interests; also the town, village or country inhabited by the Querent. REVERSED: Repose of the false heart, indignation, violence."
        dscr_Pc = "REPRESENTS: A fair, pleasing, somewhat effeminate page, of studious and intent aspect, contemplates a fish rising from a cup to look at him. It is the pictures of the mind taking form. Divinatory Meanings: Fair young man, one impelled to render service and with whom the Querent will be connected; a studious youth; news, message; application, reflection, meditation; also these things directed to business. REVERSED: Taste, inclination, attachment, seduction, deception, artifice."
        dscr_Nc = "REPRESENTS: Graceful, but not warlike; riding quietly, wearing a winged helmet, referring to those higher graces of the imagination which sometimes characterize this card. He too is a dreamer, but the images of the side of sense haunt him in his vision. Divinatory Meanings: Arrival, approach - sometimes that of a messenger; advances, proposition, demeanour, invitation, incitement. REVERSED: Trickery, artifice, subtlety, swindling, duplicity, fraud."
        dscr_Qc = "REPRESENTS: Beautiful, fair, dreamy - as one who sees visions in a cup. This is, however, only one of her aspects; she sees, but she also acts, and her activity feeds her dream. Divinatory Meanings: Good, fair woman; honest, devoted woman, who will do service to the Querent; loving intelligence, and hence the gift of vision; success, happiness, pleasure; also wisdom, virtue; a perfect spouse and a good mother. REVERSED: The accounts vary; good woman; otherwise, distinguished woman but one not to be trusted; perverse woman; vice, dishonour, depravity."
        dscr_Kc = "REPRESENTS: He holds a short sceptre in his left hand and a great cup in his right; his throne is set upon the sea; on one side a ship is riding and on the other a dolphin is leaping. The implicit is that the Sign of the Cup naturally refers to water, which appears in all the court cards. Divinatory Meanings: Fair man, man of business, law, or divinity; responsible, disposed to oblige the Querent; also equity, art and science, including those who profess science, law and art; creative intelligence. REVERSED: Dishonest, double-dealing man; roguery, exaction, injustice, vice, scandal, pillage, considerable loss."
    # Pentacles Descriptions
    if True:
        dscr_Ap = "REPRESENTS: A hand - issuing, as usual, from a cloud - holds up a pentacle. Divinatory Meanings: Perfect contentment, felicity, ecstasy; also speedy intelligence; gold. REVERSED: The evil side of wealth, bad intelligence; also great riches. In any case it shows prosperity, comfortable material conditions, but whether these are of advantage to the possessor will depend on whether the card is reversed or not."
        dscr_2p = "REPRESENTS: A young man, in the act of dancing, has a pentacle in either hand, and they are joined by that endless cord which is like the number 8 reversed. Divinatory Meanings: On the one hand it is represented as a card of gaiety, recreation and its connexions, which is the subject of the design; but it is read also as news and messages in writing, as obstacles, agitation, trouble, embroilment. REVERSED: Enforced gaiety, simulated enjoyment, literal sense, handwriting, composition, letters of exchange."
        dscr_3p = "REPRESENTS: A sculptor at his work in a monastery. Compare the design which illustrates the Eight of Pentacles. The apprentice or amateur therein has received his reward and is now at work in earnest. Divinatory Meanings: Métier, trade, skilled labour; usually, however, regarded as a card of nobility, aristocracy, renown, glory. REVERSED: Mediocrity, in work and otherwise, puerility, pettiness, weakness."
        dscr_4p = "REPRESENTS: A crowned figure, having a pentacle over his crown, clasps another with hands and arms; two pentacles are under his feet. He holds to that which he has. Divinatory Meanings: The surety of possessions, cleaving to that which one has, gift, legacy, inheritance. REVERSED: Suspense, delay, opposition."
        dscr_5p = "REPRESENTS: Two mendicants in a snow-storm pass a lighted casement. Divinatory Meanings: The card foretells material trouble above all, whether in the form illustrated - that is, destitution - or otherwise. For some cartomancists, it is a card of love and lovers-wife, husband, friend, mistress; also concordance, affinities. These alternatives cannot be harmonized. REVERSED: Disorder, chaos, ruin, discord, profligacy."
        dscr_6p = "REPRESENTS: A person in the guise of a merchant weighs money in a pair of scales and distributes it to the needy and distressed. It is a testimony to his own success in life, as well as to his goodness of heart. Divinatory Meanings: Presents, gifts, gratification; another account says attention, vigilance, now is the accepted time, present prosperity, etc. REVERSED: Desire, cupidity, envy, jealousy, illusion."
        dscr_7p = "REPRESENTS: A young man, leaning on his staff, looks intently at seven pentacles attached to a clump of greenery on his right; one would say that these were his treasures and that his heart was there. Divinatory Meanings: These are exceedingly contradictory; in the main, it is a card of money, business, barter; but one reading gives altercation, quarrels - and another innocence, ingenuity, purgation. REVERSED: Cause for anxiety regarding money which it may be proposed to lend."
        dscr_8p = "REPRESENTS: An artist in stone at his work, which he exhibits in the form of trophies. Divinatory Meanings: Work, employment, commission, craftsmanship, skill in craft and business, perhaps in the preparatory stage. REVERSED: Voided ambition, vanity, cupidity, exaction, usury. It may also signify the possession of skill, in the sense of the ingenious mind turned to cunning and intrigue."
        dscr_9p = "REPRESENTS: A woman, with a bird upon her wrist, stands amidst a great abundance of grapevines in the garden of a manorial house. It is a wide domain, suggesting plenty in all things. Possibly it is her own possession and testifies to material well-being. Divinatory Meanings: Prudence, safety, success, accomplishment, certitude, discernment. REVERSED: Roguery, deception, voided project, bad faith."
        dscr_10p = "REPRESENTS: A man and woman beneath an archway which gives entrance to a house and domain. They are accompanied by a child, who looks curiously at two dogs accosting an ancient personage seated in the foreground. The child's hand is on one of them. Divinatory Meanings: Gain, riches; family matters, archives, extraction, the abode of a family. REVERSED: Chance, fatality, loss, robbery, games of hazard; sometimes gift, dowry, pension."
        dscr_Pp = "REPRESENTS: A youthful figure, looking intently at the pentacle which hovers over his raised hands. He moves slowly, insensible of that which is about him. Divinatory Meanings: Application, study, scholarship, reflection; another reading says news, messages and the bringer thereof; also rule, management. REVERSED: Prodigality, dissipation, liberality, luxury; unfavourable news."
        dscr_Np = "REPRESENTS: He rides a slow, enduring, heavy horse, to which his own aspect corresponds. He exhibits his symbol, but does not look therein. Divinatory Meanings: Utility, serviceableness, interest, responsibility, rectitude-all on the normal and external plane. REVERSED: Inertia, idleness, repose of that kind, stagnation; also placidity, discouragement, carelessness."
        dscr_Qp = "REPRESENTS: The face suggests that of a dark woman, whose qualities might be summed up in the idea of greatness of soul; she has also the serious cast of intelligence; she contemplates her symbol and may see worlds therein. Divinatory Meanings: Opulence, generosity, magnificence, security, liberty. REVERSED: Evil, suspicion, suspense, fear, mistrust."
        dscr_Kp = "REPRESENTS: The figure calls for no special description. The face is rather dark, suggesting also courage, but somewhat lethargic in tendency. The bull's head should be noted as a recurrent symbol on the throne. The sign of this suit is represented throughout as engraved or blazoned with the pentagram, typifying the correspondence of the four elements in human nature and that by which they may be governed. In many old Tarot packs this suit stood for current coin, money, deniers. I have not invented the substitution of pentacles and I have no special cause to sustain in respect of the alternative. But the consensus of divinatory meanings is on the side of some change, because the cards do not happen to deal especially with questions of money. Divinatory Meanings: Valour, realizing intelligence, business and normal intellectual aptitude, sometimes mathematical gifts and attainments of this kind; success in these paths. REVERSED: Vice, weakness, ugliness, perversity, corruption, peril."
    # Wands Descriptions
    if True:
        dscr_Aw = "REPRESENTS: A hand issuing from a cloud grasps a stout wand or club. Divinatory Meanings: Creation, invention, enterprise, the powers which result in these; principle, beginning, source; birth, family, origin, and in a sense the virility which is behind them; the starting point of enterprises; according to another account, money, fortune, inheritance. REVERSED: Fall, decadence, ruin, perdition, to perish; also a certain clouded joy."
        dscr_2w = "REPRESENTS: A tall man looks from a battlemented roof over sea and shore; he holds a globe in his right hand, while a staff in his left rests on the battlement; another is fixed in a ring. The Rose and Cross and Lily should be noticed on the left side. Divinatory Meanings: Between the alternative readings there is no marriage possible; on the one hand, riches, fortune, magnificence; on the other, physical suffering, disease, chagrin, sadness, mortification. The design gives one suggestion; here is a lord overlooking his dominion and alternately contemplating a globe; it looks like the malady, the mortification, the sadness of Alexander amidst the grandeur of this world's wealth. REVERSED: Surprise, wonder, enchantment, emotion, trouble, fear."
        dscr_3w = "REPRESENTS: A calm, stately personage, with his back turned, looking from a cliff's edge at ships passing over the sea. Three staves are planted in the ground, and he leans slightly on one of them. Divinatory Meanings: He symbolizes established strength, enterprise, effort, trade, commerce, discovery; those are his ships, bearing his merchandise, which are sailing over the sea. The card also signifies able co-operation in business, as if the successful merchant prince were looking from his side towards yours with a view to help you. REVERSED: The end of troubles, suspension or cessation of adversity, toil and disappointment."
        dscr_4w = "REPRESENTS: From the four great staves planted in the foreground there is a great garland suspended; two female figures uplift nosegays; at their side is a bridge over a moat, leading to an old manorial house. Divinatory Meanings: They are for once almost on the surface - country life, haven of refuge, a species of domestic harvest-home, repose, concord, harmony, prosperity, peace, and the perfected work of these. REVERSED: The meaning remains unaltered; it is prosperity, increase, felicity, beauty, embellishment."
        dscr_5w = "REPRESENTS: A posse of youths, who are brandishing staves, as if in sport or strife. It is mimic warfare, and hereto correspond the Divinatory Meanings: Imitation, as, for example, sham fight, but also the strenuous competition and struggle of the search after riches and fortune. In this sense it connects with the battle of life. Hence some attributions say that it is a card of gold, gain, opulence. REVERSED: Litigation, disputes, trickery, contradiction."
        dscr_6w = "REPRESENTS: A laurelled horseman bears one staff adorned with a laurel crown; footmen with staves are at his side. Divinatory Meanings: The card has been so designed that it can cover several significations; on the surface, it is a victor triumphing, but it is also great news, such as might be carried in state by the King's courier; it is expectation crowned with its own desire, the crown of hope, and so forth. REVERSED: Apprehension, fear, as of a victorious enemy at the gate; treachery, disloyalty, as of gates being opened to the enemy; also indefinite delay."
        dscr_7w = "REPRESENTS: A young man on a craggy eminence brandishing a staff; six other staves are raised towards him from below. Divinatory Meanings: It is a card of valour, for, on the surface, six are attacking one, who has, however, the vantage position. On the intellectual plane, it signifies discussion, wordy strife; in business - negotiations, war of trade, barter, competition. It is further a card of success, for the combatant is on the top and his enemies may be unable to reach him. REVERSED: Perplexity, embarrassments, anxiety. It is also a caution against indecision."
        dscr_8w = "REPRESENTS: The card represents motion through the immovable - a flight of wands through an open country; but they draw to the term of their course. That which they signify is at hand; it may be even on the threshold. Divinatory Meanings: Activity in undertakings, the path of such activity, swiftness, as that of an express messenger; great haste, great hope, speed towards an end which promises assured felicity; generally, that which is on the move; also the arrows of love. REVERSED: Arrows of jealousy, internal dispute, stingings of conscience, quarrels; and domestic disputes for persons who are married."
        dscr_9w = "REPRESENTS: The figure leans upon his staff and has an expectant look, as if awaiting an enemy. Behind are eight other staves - erect, in orderly disposition, like a palisade. Divinatory Meanings: The card signifies strength in opposition. If attacked, the person will meet an onslaught boldly; and his build shows, that he may prove a formidable antagonist. With this main significance there are all its possible adjuncts - delay, suspension, adjournment. REVERSED: Obstacles, adversity, calamity."
        dscr_10w = "REPRESENTS: A man oppressed by the weight of the ten staves which he is carrying. Divinatory Meanings: A card of many significances, and some of the readings cannot be harmonized. I set aside that which connects it with honour and good faith. The chief meaning is oppression simply, but it is also fortune, gain, any kind of success, and then it is the oppression of these things. It is also a card of false-seeming, disguise, perfidy. The place which the figure is approaching may suffer from the rods that he carries. Success is stultified if the Nine of Swords follows, and if it is a question of a lawsuit, there will be certain loss. REVERSED: Contrarieties, difficulties, intrigues, and their analogies."
        dscr_Pw = "REPRESENTS: In a scene similar to the former, a young man stands in the act of proclamation. He is unknown but faithful, and his tidings are strange. Divinatory Meanings: Dark young man, faithful, a lover, an envoy, a postman. Beside a man, he will bear favourable testimony concerning him. A dangerous rival, if followed by the Page of Cups; he has the chief qualities of his suit. He may signify family intelligence. REVERSED: Anecdotes, announcements, evil news. Also indecision and the instability which accompanies it."
        dscr_Nw = "REPRESENTS: He is shown as if upon a journey, armed with a short wand, and although mailed is not on a warlike errand. He is passing mounds or pyramids. The motion of the horse is a key to the character of its rider, and suggests the precipitate mood, or things connected therewith. Divinatory Meanings: Departure, absence, flight, emigration. A dark young man, friendly. Change of residence. REVERSED: Rupture, division, interruption, discord."
        dscr_Qw = "REPRESENTS: The Wands throughout this suit are always in leaf, as it is a suit of life and animation. Emotionally and otherwise, the Queen's personality corresponds to that of the King, but is more magnetic. Divinatory Meanings: A dark woman, countrywoman, friendly, chaste, loving, honourable. If the card beside her signifies a man, she is well disposed towards him; if a woman, she is interested in the Querent. Also, love of money, or a certain success in business. REVERSED: Good, economical, obliging, serviceable. Signifies also - but in certain positions and in the neighbourhood of other cards tending in such directions - opposition, jealousy, even deceit and infidelity."
        dscr_Kw = 'REPRESENTS: The physical and emotional nature to which this card is attributed is dark, ardent, lithe, animated, impassioned, noble. The King uplifts a flowering wand, and wears, like his three correspondences in the remaining suits, what is called a cap of maintenance beneath his crown. He connects with the symbol of the lion, which is emblazoned on the back of his throne. Divinatory Meanings: Dark man, friendly, countryman, generally married, honest and conscientious. The card always signifies honesty, and may mean news concerning an unexpected heritage to fall in before very long. REVERSED: Good, but severe; austere, yet tolerant.'
    # Swords Descriptions
    if True:
        dscr_As = "REPRESENTS: A hand issues from a cloud, grasping a sword, the point of which is encircled by a crown. Divinatory Meanings: Triumph, the excessive degree in everything, conquest, triumph of force. It is a card of great force, in love as well as in hatred. The crown may carry a much higher significance than comes usually within the sphere of fortune-telling. REVERSED: The same, but the results are disastrous; another account says: conception, childbirth, augmentation, multiplicity."
        dscr_2s = "REPRESENTS: A hoodwinked female figure balances two swords upon her shoulders. Divinatory Meanings: Conformity and the equipoise which it suggests, courage, friendship, concord in a state of arms; another reading gives tenderness, affection, intimacy. The suggestion of harmony and other favourable readings must be considered in a qualified manner, as Swords generally are not symbolical of beneficent forces in human affairs. REVERSED: Imposture, falsehood, duplicity, disloyalty."
        dscr_3s = "REPRESENTS: Three swords piercing a heart; cloud and rain behind. Divinatory Meanings: Removal, absence, delay, division, rupture, dispersion, and all that the design signifies naturally, being too simple and obvious to call for specific enumeration. REVERSED: Mental alienation, error, loss, distraction, disorder, confusion."
        dscr_4s = "REPRESENTS: The effigy of a knight in the attitude of prayer, at full length upon his tomb. Divinatory Meanings: Vigilance, retreat, solitude, hermit's repose, exile, tomb and coffin. It is these last that have suggested the design. REVERSED: Wise administration, circumspection, economy, avarice, precaution, testament."
        dscr_5s = "REPRESENTS: A disdainful man looks after two retreating and dejected figures. Their swords lie upon the ground. He carries two others on his left shoulder, and a third sword is in his right hand, point to earth. He is the master in possession of the field. Divinatory Meanings: Degradation, destruction, revocation, infamy, dishonour, loss, with the variants and analogues of these. REVERSED: The same; burial and obsequies."
        dscr_6s = "REPRESENTS: A ferryman carrying passengers in his punt to the further shore. The course is smooth, and seeing that the freight is light, it may be noted that the work is not beyond his strength. Divinatory Meanings: Journey by water, route, way, envoy, commissionary, expedient. REVERSED: Declaration, confession, publicity; one account says that it is a proposal of love."
        dscr_7s = "REPRESENTS: A man in the act of carrying away five swords rapidly; the two others of the card remain stuck in the ground. A camp is close at hand. Divinatory Meanings: Design, attempt, wish, hope, confidence; also quarrelling, a plan that may fail, annoyance. The design is uncertain in its import, because the significations are widely at variance with each other. REVERSED: Good advice, counsel, instruction, slander, babbling."
        dscr_8s = "REPRESENTS: A woman, bound and hoodwinked, with the swords of the card about her. Yet it is rather a card of temporary durance than of irretrievable bondage. Divinatory Meanings: Bad news, violent chagrin, crisis, censure, power in trammels, conflict, calumny; also sickness. REVERSED: Disquiet, difficulty, opposition, accident, treachery; what is unforeseen; fatality."
        dscr_9s = "REPRESENTS: One seated on her couch in lamentation, with the swords over her. She is as one who knows no sorrow which is like unto hers. It is a card of utter desolation. Divinatory Meanings: Death, failure, miscarriage, delay, deception, disappointment, despair. REVERSED: Imprisonment, suspicion, doubt, reasonable fear, shame."
        dscr_10s = "REPRESENTS: A prostrate figure, pierced by all the swords belonging to the card. Divinatory Meanings: Whatsoever is intimated by the design; also pain, affliction, tears, sadness, desolation. It is not especially a card of violent death. REVERSED: Advantage, profit, success, favour, but none of these are permanent; also power and authority."
        dscr_Ps = "REPRESENTS: A lithe, active figure holds a sword upright in both hands, while in the act of swift walking. He is passing over rugged land, and about his way the clouds are collocated wildly. He is alert and lithe, looking this way and that, as if an expected enemy might appear at any moment. Divinatory Meanings: Authority, overseeing, secret service, vigilance, spying, examination, and the qualities thereto belonging. REVERSED: More evil side of these qualities; what is unforeseen, unprepared state; sickness is also intimated."
        dscr_Ns = "REPRESENTS: He is riding in full course, as if scattering his enemies. In the design he is really a prototypical hero of romantic chivalry. He might almost be Galahad, whose sword is swift and sure because he is clean of heart. Divinatory Meanings: Skill, bravery, capacity, defence, address, enmity, wrath, war, destruction, opposition, resistance, ruin. There is therefore a sense in which the card signifies death, but it carries this meaning only in its proximity to other cards of fatality. REVERSED: Imprudence, incapacity, extravagance."
        dscr_Qs = "REPRESENTS: Her right hand raises the weapon vertically and the hilt rests on an arm of her royal chair. The left hand is extended, the arm raised her countenance is severe but chastened; it suggests familiarity with sorrow. It does not represent mercy, and, her sword notwithstanding, she is scarcely a symbol of power. Divinatory Meanings: Widowhood, female sadness and embarrassment, absence, sterility, mourning, privation, separation. REVERSED: Malice, bigotry, artifice, prudery, bale, deceit."
        dscr_Ks = "REPRESENTS: He sits in judgment, holding the unsheathed sign of his suit. He recalls, of course, the conventional Symbol of justice in the Trumps Major, and he may represent this virtue, but he is rather the power of life and death, in virtue of his office. Divinatory Meanings: Whatsoever arises out of the idea of judgment and all its connexions-power, command, authority, militant intelligence, law, offices of the crown, and so forth. REVERSED: Cruelty, perversity, barbarity, perfidy, evil intention."
# Card __init__()
if True:
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
    # Cups
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
    # Pentacles
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
    # Wands
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
    # Swords
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

#=======================================================================================================================
# GAME CLASS                                                                                                  GAME CLASS
#=======================================================================================================================
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
        display_significator = False; display_covers = False; display_crosses = False; display_crowns = False
        display_beneath = False; display_behind = False; display_before = False; display_self = False
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
game.reset()

#=======================================================================================================================
# WRAPAROUND FUNCTION                                                                                WRAPAROUND FUNCTION
#=======================================================================================================================
# Makes the description text correctly wrap-around.
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

#=======================================================================================================================
# GAME LOOP                                                                                                    GAME LOOP
#=======================================================================================================================
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
                    else: display_significator = False
                if game.c1 != 0:
                    if game.c1.rect.collidepoint(mouse_pos):
                        display_covers = True
                    else: display_covers = False
                if game.c2 != 0:
                    if game.c2.rect.collidepoint(mouse_pos):
                        display_crosses = True
                    else: display_crosses = False
                if game.c3 != 0:
                    if game.c3.rect.collidepoint(mouse_pos):
                        display_crowns = True
                    else: display_crowns = False
                if game.c4 != 0:
                    if game.c4.rect.collidepoint(mouse_pos):
                        display_beneath = True
                    else: display_beneath = False
                if game.c5 != 0:
                    if game.c5.rect.collidepoint(mouse_pos):
                        display_behind = True
                    else: display_behind = False
                if game.c6 != 0:
                    if game.c6.rect.collidepoint(mouse_pos):
                        display_before = True
                    else: display_before = False
                if game.c7 != 0:
                    if game.c7.rect.collidepoint(mouse_pos):
                        display_self = True
                    else: display_self = False
                if game.c8 != 0:
                    if game.c8.rect.collidepoint(mouse_pos):
                        display_house = True
                    else: display_house = False
                if game.c9 != 0:
                    if game.c9.rect.collidepoint(mouse_pos):
                        display_hopes = True
                    else: display_hopes = False
                if game.c10 != 0:
                    if game.c10.rect.collidepoint(mouse_pos):
                        display_outcome = True
                    else: display_outcome = False

#=======================================================================================================================
# BLITTING SURFACES                                                                                    BLITTING SURFACES
#=======================================================================================================================
    # Background
    screen.fill((69, 145, 19))

    # Buttons
    screen.blit(draw_button_surf,draw_button_rect)
    screen.blit(draw_button_text,(draw_button_rect.x+10, draw_button_rect.y+5))
    screen.blit(all_button_surf,all_button_rect)
    screen.blit(all_button_text,(all_button_rect.x+28, all_button_rect.y+5))
    screen.blit(reset_button_surf,reset_button_rect)
    screen.blit(reset_button_text,(reset_button_rect.x+10, reset_button_rect.y+5))

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
