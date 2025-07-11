import google.generativeai as genai
import os

def generateSummary(way, content):
    genai.configure(api_key="AIzaSyCBWZ53C-v6y4LEswaVlIrimuDt2W-FERk")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f'''Summarise this content in just a paragraph and in a {way} way. 
                                    {content} is the content that needs to be summarised.
                                    ''')
    print(response.text)
    return response.text


# generateSummary("funny",''' 
#     Football is a family of team sports that involve, to varying degrees, kicking a ball to score a goal. Unqualified, the word football generally means the form of football that is the most popular where the word is used. Sports commonly called football include association football (known as soccer in Australia, Canada, South Africa, the United States, and sometimes in Ireland and New Zealand); Australian rules football; Gaelic football; gridiron football (specifically American football, arena football, or Canadian football); International rules football; rugby league football; and rugby union football.[1] These various forms of football share, to varying degrees, common origins and are known as "football codes".

# There are a number of references to traditional, ancient, or prehistoric ball games played in many different parts of the world.[2][3][4] Contemporary codes of football can be traced back to the codification of these games at English public schools during the 19th century, itself an outgrowth of medieval football.[5][6] The expansion and cultural power of the British Empire allowed these rules of football to spread to areas of British influence outside the directly controlled empire.[7] By the end of the 19th century, distinct regional codes were already developing: Gaelic football, for example, deliberately incorporated the rules of local traditional football games in order to maintain their heritage.[8] In 1888, the Football League was founded in England, becoming the first of many professional football associations. During the 20th century, several of the various kinds of football grew to become some of the most popular team sports in the world.[9]

# Common elements




# The action of kicking in (clockwise from upper left) association, gridiron, rugby, and Australian football
# The various codes of football share certain common elements and can be grouped into two main classes of football: carrying codes like American football, Canadian football, Australian football, rugby union and rugby league, where the ball is moved about the field while being held in the hands or thrown, and kicking codes such as association football and Gaelic football, where the ball is moved primarily with the feet, and where handling is strictly limited.[10]

# Common rules among the sports include:[11]

# Two teams usually have between 11 and 18 players; some variations that have fewer players (five or more per team) are also popular.[12]
# A clearly defined area in which to play the game.
# Scoring goals or points by moving the ball to an opposing team's end of the field and either into a goal area, or over a line.
# Goals or points resulting from players putting the ball between two goalposts.
# The goal or line being defended by the opposing team.
# Players using only their body to move the ball, i.e. no additional equipment such as bats or sticks.
# In all codes, common skills include passing, tackling, evasion of tackles, catching and kicking.[10] In most codes, there are rules restricting the movement of players offside, and players scoring a goal must put the ball either under or over a crossbar between the goalposts.

# Etymology
# Main article: Football (word)
# There are conflicting explanations of the origin of the word "football". It is widely assumed that the word "football" (or the phrase "foot ball") refers to the action of the foot kicking a ball.[13] There is an alternative explanation, which is that football originally referred to a variety of games in medieval Europe that were played on foot.[14] There is no conclusive evidence for either explanation.

# Early history
# Ancient games
# See also: Episkyros and Cuju
# Ancient China

# Emperor Taizu of Song playing cuju (Chinese football) with his prime minister Zhao Pu (趙普) and other ministers, by Yuan dynasty artist Qian Xuan (1235–1305)
# The Chinese competitive game cuju is an early type of ball game where feet were used, in some aspects resembling modern association football. It was possibly played around the Han dynasty and early Qin dynasty, based on an attestation in a military manual from around the second to third centuries BC.[15][16][17] In one version, gameplay consisted of players passing the ball between teammates without allowing it to touch the ground (much like keepie uppie). In its competitive version, two teams had to pass the ball without it falling, before kicking the ball through a circular hole placed in the middle of the pitch. Unlike association football, the two teams did not interact with each other but instead stayed on opposite sides of the pitch.[18] Cuju has been cited by FIFA as the earliest form of football.[4]
# The Japanese version of cuju is kemari (蹴鞠), and was developed during the Asuka period.[19] This is known to have been played within the Japanese imperial court in Kyoto from about 600 AD. In kemari, several people stand in a circle and kick a ball to each other, trying not to let the ball drop to the ground. The Silk Road facilitated the transmission of cuju, especially the game popular in the Tang dynasty, the period when the inflatable ball was invented and replaced the stuffed ball.[20]


# An ancient Roman tombstone of a boy with a Harpastum ball from Tilurium (modern Sinj, Croatia)
# Ancient Greece and Rome
# The Ancient Greeks and Romans are known to have played many ball games, some of which involved the use of the feet. The Roman game harpastum is believed to have been adapted from a Greek team game known as ἐπίσκυρος (episkyros)[21][22] or φαινίνδα (phaininda),[23] which is mentioned by a Greek playwright, Antiphanes (388–311 BC) and later referred to by the Christian theologian Clement of Alexandria (c. 150 – c. 215 AD). These games appear to have resembled rugby football.[24][25][26][27][28] The Roman politician Cicero (106–43 BC) describes the case of a man who was killed whilst having a shave when a ball was kicked into a barber's shop. Roman ball games already knew the air-filled ball, the follis.[29][30] Episkyros is described as an early form of football by FIFA.[31]

# Native Americans
# There are a number of references to traditional, ancient, or prehistoric ball games, played by indigenous peoples in many different parts of the world. For example, in 1586, men from a ship commanded by an English explorer named John Davis went ashore to play a form of football with Inuit in Greenland.[32] There are later accounts of an Inuit game played on ice, called Aqsaqtuk. Each match began with two teams facing each other in parallel lines, before attempting to kick the ball through each other team's line and then at a goal. In 1610, William Strachey, a colonist at Jamestown, Virginia recorded a game played by Native Americans, called Pahsaheman.[citation needed] Pasuckuakohowog, a game similar to modern-day association football played amongst Amerindians, was also reported as early as the 17th century.

# Games played in Mesoamerica with rubber balls by indigenous peoples are also well-documented as existing since before this time, but these had more similarities to basketball or volleyball, and no links have been found between such games and modern football sports. Northeastern American Indians, especially the Iroquois Confederation, played a game which made use of net racquets to throw and catch a small ball; however, although it is a ball-goal foot game, lacrosse (as its modern descendant is called) is likewise not usually classed as a form of "football".[citation needed]

# Oceania
# On the Australian continent several tribes of indigenous people played kicking and catching games with stuffed balls which have been generalised by historians as Marn Grook (Djab Wurrung for "game ball"). The earliest historical account is an anecdote from the 1878 book by Robert Brough-Smyth, The Aborigines of Victoria, in which a man called Richard Thomas is quoted as saying, in about 1841 in Victoria, Australia, that he had witnessed Aboriginal people playing the game: "Mr Thomas describes how the foremost player will drop kick a ball made from the skin of a possum and how other players leap into the air in order to catch it." Some historians have theorised that Marn Grook was one of the origins of Australian rules football.

# The Māori in New Zealand played a game called Kī-o-rahi consisting of teams of seven players play on a circular field divided into zones, and score points by touching the 'pou' (boundary markers) and hitting a central 'tupu' or target.[citation needed]

# These games and others may well go far back into antiquity. However, the main sources of modern football codes appear to lie in western Europe, especially England.

# Turkic peoples
# Mahmud al-Kashgari in his Dīwān Lughāt al-Turk, described a game called tepuk among Turks in Central Asia. In the game, people try to attack each other's castle by kicking a ball made of sheep leather.[33]

# Ancient Greek athlete balancing a ball on his thigh, Piraeus, 400–375 BC
# Ancient Greek athlete balancing a ball on his thigh, Piraeus, 400–375 BC
 
# A Song dynasty painting by Su Hanchen (c. 1130–1160), depicting Chinese children playing cuju
# A Song dynasty painting by Su Hanchen (c. 1130–1160), depicting Chinese children playing cuju
 
# Paint of a Mesoamerican ballgame player of the Tepantitla murals in Teotihuacan
# Paint of a Mesoamerican ballgame player of the Tepantitla murals in Teotihuacan
 
# A group of indigenous people playing a ball game in French Guiana
# A group of indigenous people playing a ball game in French Guiana
 
# An illustration from the 1850s of indigenous Australians playing marn grook
# An illustration from the 1850s of indigenous Australians playing marn grook
 
# A revived version of kemari being played at the Tanzan Shrine, Japan, 2006
# A revived version of kemari being played at the Tanzan Shrine, Japan, 2006
# Medieval and early modern Europe
# Further information: Medieval football
# The Middle Ages saw a huge rise in popularity of annual Shrovetide football matches throughout Europe, particularly in England. An early reference to a ball game played in Britain comes from the 9th-century Historia Brittonum, attributed to Nennius, which describes "a party of boys ... playing at ball".[34] References to a ball game played in northern France known as La Soule or Choule, in which the ball was propelled by hands, feet, and sticks,[35] date from the 12th century.[36]


# An illustration of so-called "mob football"
# The early forms of football played in England, sometimes referred to as "mob football", would be played in towns or between neighbouring villages, involving an unlimited number of players on opposing teams who would clash en masse,[37] struggling to move an item, such as inflated animal's bladder[38] to particular geographical points, such as their opponents' church, with play taking place in the open space between neighbouring parishes.[39] The game was played primarily during significant religious festivals, such as Shrovetide, Christmas, or Easter,[38] and Shrovetide games have survived into the modern era in a number of English towns (see below).

# The first detailed description of what was almost certainly football in England was given by William FitzStephen in about 1174–1183. He described the activities of London youths during the annual festival of Shrove Tuesday:

# After lunch all the youth of the city go out into the fields to take part in a ball game. The students of each school have their own ball; the workers from each city craft are also carrying their balls. Older citizens, fathers, and wealthy citizens come on horseback to watch their juniors competing, and to relive their own youth vicariously: you can see their inner passions aroused as they watch the action and get caught up in the fun being had by the carefree adolescents.[40]

# Most of the very early references to the game speak simply of "ball play" or "playing at ball". This reinforces the idea that the games played at the time did not necessarily involve a ball being kicked.

# An early reference to a ball game that was probably football comes from 1280 at Ulgham, Northumberland, England: "Henry... while playing at ball.. ran against David".[41] Football was played in Ireland in 1308, with a documented reference to John McCrocan, a spectator at a "football game" at Newcastle, County Down being charged with accidentally stabbing a player named William Bernard.[42] Another reference to a football game comes in 1321 at Shouldham, Norfolk, England: "[d]uring the game at ball as he kicked the ball, a lay friend of his... ran against him and wounded himself".[41]

# In 1314, Nicholas de Farndone, Lord Mayor of the City of London issued a decree banning football in the French used by the English upper classes at the time. A translation reads: "[f]orasmuch as there is great noise in the city caused by hustling over large foot balls [rageries de grosses pelotes de pee][43] in the fields of the public from which many evils might arise which God forbid: we command and forbid on behalf of the king, on pain of imprisonment, such game to be used in the city in the future." This is the earliest reference to football.

# In 1363, King Edward III of England issued a proclamation banning "...handball, football, or hockey; coursing and cock-fighting, or other such idle games",[44] showing that "football" – whatever its exact form in this case – was being differentiated from games involving other parts of the body, such as handball.


# "Football" in France, circa 1750
# A game known as "football" was played in Scotland as early as the 15th century: it was prohibited by the Football Act 1424 and although the law fell into disuse it was not repealed until 1906. There is evidence for schoolboys playing a "football" ball game in Aberdeen in 1633 (some references cite 1636) which is notable as an early allusion to what some have considered to be passing the ball. The word "pass" in the most recent translation is derived from "huc percute" (strike it here) and later "repercute pilam" (strike the ball again) in the original Latin. It is not certain that the ball was being struck between members of the same team. The original word translated as "goal" is "metum", literally meaning the "pillar at each end of the circus course" in a Roman chariot race. There is a reference to "get hold of the ball before [another player] does" (Praeripe illi pilam si possis agere) suggesting that handling of the ball was allowed. One sentence states in the original 1930 translation "Throw yourself against him" (Age, objice te illi).

# King Henry IV of England also presented one of the earliest documented uses of the English word "football", in 1409, when he issued a proclamation forbidding the levying of money for "foteball".[41][45]

# There is also an account in Latin from the end of the 15th century of football being played at Caunton, Nottinghamshire. This is the first description of a "kicking game" and the first description of dribbling: "[t]he game at which they had met for common recreation is called by some the foot-ball game. It is one in which young men, in country sport, propel a huge ball not by throwing it into the air but by striking it and rolling it along the ground, and that not with their hands but with their feet... kicking in opposite directions." The chronicler gives the earliest reference to a football pitch, stating that: "[t]he boundaries have been marked and the game had started.[41]


# Oldest known painting of foot-ball in Scotland, by Alexander Carse, c. 1810

# "Football" in Scotland, c. 1830
# Other firsts in the medieval and early modern eras:

# "A football", in the sense of a ball rather than a game, was first mentioned in 1486.[45] This reference is in Dame Juliana Berners' Book of St Albans. It states: "a certain rounde instrument to play with ...it is an instrument for the foote and then it is calde in Latyn 'pila pedalis', a fotebal".[41]
# A pair of football boots were ordered by King Henry VIII of England in 1526.[46]
# Women playing a form of football was first described in 1580 by Sir Philip Sidney in one of his poems: "[a] tyme there is for all, my mother often sayes, when she, with skirts tuckt very hy, with girles at football playes".[47]
# The first references to goals are in the late 16th and early 17th centuries. In 1584 and 1602 respectively, John Norden and Richard Carew referred to "goals" in Cornish hurling. Carew described how goals were made: "they pitch two bushes in the ground, some eight or ten foote asunder; and directly against them, ten or twelue [twelve] score off, other twayne in like distance, which they terme their Goales".[48] He is also the first to describe goalkeepers and passing of the ball between players.
# The first direct reference to scoring a goal is in John Day's play The Blind Beggar of Bethnal Green (performed circa 1600; published 1659): "I'll play a gole at camp-ball" (an extremely violent variety of football, which was popular in East Anglia). Similarly in a poem in 1613, Michael Drayton refers to "when the Ball to throw, and drive it to the Gole, in squadrons forth they goe".
# Calcio Fiorentino
# Main article: Calcio Fiorentino

# An illustration of the Calcio Fiorentino field and starting positions, from a 1688 book by Pietro di Lorenzo Bini
# In the 16th century, the city of Florence celebrated the period between Epiphany and Lent by playing a game which today is known as "calcio storico" ("historic kickball") in the Piazza Santa Croce.[49] The young aristocrats of the city would dress up in fine silk costumes and embroil themselves in a violent form of football. For example, calcio players could punch, shoulder charge, and kick opponents. Blows below the belt were allowed. The game is said to have originated as a military training exercise. In 1580, Count Giovanni de' Bardi di Vernio wrote Discorso sopra 'l giuoco del Calcio Fiorentino. This is sometimes said to be the earliest code of rules for any football game. The game was not played after January 1739 (until it was revived in May 1930).

# Official disapproval and attempts to ban football
# Main article: Attempts to ban football games
# There have been many attempts to ban football, from the Middle Ages through to the modern day. The first such law was passed in England in 1314; it was followed by more than 30 in England alone between 1314 and 1667.[50]: 6  Women were banned from playing at English and Scottish Football League grounds in 1921, a ban that was only lifted in the 1970s. Female footballers still face similar problems in some parts of the world.

# American football also faced pressures to ban the sport. The game played in the 19th century resembled mob football that developed in medieval Europe, including a version popular on university campuses known as old division football, and several municipalities banned its play in the mid-19th century.[51][52] By the 20th century, the game had evolved to a more rugby style game. In 1905, there were calls to ban American football in the U.S. due to its violence; a meeting that year was hosted by American president Theodore Roosevelt led to sweeping rules changes that caused the sport to diverge significantly from its rugby roots to become more like the sport as it is played today.[53]

# Establishment of modern codes

# Size comparison of modern football codes playing fields
# English public schools
# Main article: English public school football games
# While football continued to be played in various forms throughout Britain, its public schools (equivalent to private schools in other countries) are widely credited with four key achievements in the creation of modern football codes. First of all, the evidence suggests that they were important in taking football away from its "mob" form and turning it into an organised team sport. Second, many early descriptions of football and references to it were recorded by people who had studied at these schools. Third, it was teachers, students, and former students from these schools who first codified football games, to enable matches to be played between schools. Finally, it was at English public schools that the division between "kicking" and "running" (or "carrying") games first became clear.

# The earliest evidence that games resembling football were being played at English public schools – mainly attended by boys from the upper, upper-middle and professional classes – comes from the Vulgaria by William Herman in 1519. Herman had been headmaster at Eton and Winchester colleges and his Latin textbook includes a translation exercise with the phrase "We wyll playe with a ball full of wynde".[54]

# Richard Mulcaster, a student at Eton College in the early 16th century and later headmaster at other English schools, has been described as "the greatest sixteenth Century advocate of football".[55] Among his contributions are the earliest evidence of organised team football. Mulcaster's writings refer to teams ("sides" and "parties"), positions ("standings"), a referee ("judge over the parties") and a coach "(trayning maister)". Mulcaster's "footeball" had evolved from the disordered and violent forms of traditional football:

# [s]ome smaller number with such overlooking, sorted into sides and standings, not meeting with their bodies so boisterously to trie their strength: nor shouldring or shuffing one an other so barbarously ... may use footeball for as much good to the body, by the chiefe use of the legges.[56]

# In 1633, David Wedderburn, a teacher from Aberdeen, mentioned elements of modern football games in a short Latin textbook called Vocabula. Wedderburn refers to what has been translated into modern English as "keeping goal" and makes an allusion to passing the ball ("strike it here"). There is a reference to "get hold of the ball", suggesting that some handling was allowed. It is clear that the tackles allowed included the charging and holding of opposing players ("drive that man back").[57]

# A more detailed description of football is given in Francis Willughby's Book of Games, written in about 1660.[58] Willughby, who had studied at Bishop Vesey's Grammar School, Sutton Coldfield, is the first to describe goals and a distinct playing field: "a close that has a gate at either end. The gates are called Goals." His book includes a diagram illustrating a football field. He also mentions tactics ("leaving some of their best players to guard the goal"); scoring ("they that can strike the ball through their opponents' goal first win") and the way teams were selected ("the players being equally divided according to their strength and nimbleness"). He is the first to describe a "law" of football: "they must not strike [an opponent's leg] higher than the ball".[59][60]

# English public schools were the first to codify football games. In particular, they devised the first offside rules, during the late 18th century.[61] In the earliest manifestations of these rules, players were "off their side" if they simply stood between the ball and the goal which was their objective. Players were not allowed to pass the ball forward, either by foot or by hand. They could only dribble with their feet, or advance the ball in a scrum or similar formation. However, offside laws began to diverge and develop differently at each school, as is shown by the rules of football from Winchester, Rugby, Harrow and Cheltenham, during between 1810 and 1850.[61] The first known codes – in the sense of a set of rules – were those of Eton in 1815[62] and Aldenham in 1825.[62])

# During the early 19th century, most working-class people in Britain had to work six days a week, often for over twelve hours a day. They had neither the time nor the inclination to engage in sport for recreation and, at the time, many children were part of the labour force. Feast day football played on the streets was in decline. Public school boys, who enjoyed some freedom from work, became the inventors of organised football games with formal codes of rules.

# Football was adopted by a number of public schools as a way of encouraging competitiveness and keeping youths fit. Each school drafted its own rules, which varied widely between different schools and were changed over time with each new intake of pupils. Two schools of thought developed regarding rules. Some schools favoured a game in which the ball could be carried (as at Rugby, Marlborough and Cheltenham), while others preferred a game where kicking and dribbling the ball was promoted (as at Eton, Harrow, Westminster and Charterhouse). The division into these two camps was partly the result of circumstances in which the games were played. For example, Charterhouse and Westminster at the time had restricted playing areas; the boys were confined to playing their ball game within the school cloisters, making it difficult for them to adopt rough and tumble running games.[citation needed]


# Although the Rugby School (pictured) became famous due to a version that rugby football was invented there in 1823, most sports historians refuse this version stating it is apocryphal.
# William Webb Ellis, a pupil at Rugby School, is said to have "with a fine disregard for the rules of football, as played in his time [emphasis added], first took the ball in his arms and ran with it, thus creating the distinctive feature of the rugby game." in 1823. This act is usually said to be the beginning of Rugby football, but there is little evidence that it occurred, and most sports historians believe the story to be apocryphal. The act of 'taking the ball in his arms' is often misinterpreted as 'picking the ball up' as it is widely believed that Webb Ellis' 'crime' was handling the ball, as in modern association football, however handling the ball at the time was often permitted and in some cases compulsory,[63] the rule for which Webb Ellis showed disregard was running forward with it as the rules of his time only allowed a player to retreat backwards or kick forwards.

# The boom in rail transport in Britain during the 1840s meant that people were able to travel farther and with less inconvenience than they ever had before. Inter-school sporting competitions became possible. However, it was difficult for schools to play each other at football, as each school played by its own rules. The solution to this problem was usually that the match be divided into two-halves, one half played by the rules of the host "home" school, and the other half by the visiting "away" school.

# The modern rules of many football codes were formulated during the mid- or late- 19th century. This also applies to other sports such as lawn bowls, lawn tennis, etc. The major impetus for this was the patenting of the world's first lawnmower in 1830. This allowed for the preparation of modern ovals, playing fields, pitches, grass courts, etc.[64]

# Apart from Rugby football, the public school codes have barely been played beyond the confines of each school's playing fields. However, many of them are still played at the schools which created them (see § British schools).


# A Football Game (1839) by British painter Thomas Webster
# Public schools' dominance of sports in the UK began to wane after the Factory Act 1850, which significantly increased the recreation time available to working class children. Before 1850, many British children had to work six days a week, for more than twelve hours a day. From 1850, they could not work before 6 a.m. (7 a.m. in winter) or after 6 p.m. on weekdays (7 p.m. in winter); on Saturdays they had to cease work at 2 pm. These changes meant that working class children had more time for games, including various forms of football.

# The earliest known matches between public schools are as follows:


# Football match in the 1846 Shrove Tuesday in Kingston upon Thames, England
# 9 December 1834: Eton School v. Harrow School.[65]
# 1840s: Old Rugbeians v. Old Salopians (played at Cambridge University).[66]
# 1840s: Old Rugbeians v. Old Salopians (played at Cambridge University the following year).[66]
# 1852: Harrow School v. Westminster School.[66]
# 1857: Haileybury School v. Westminster School.[66]
# 24 February 1858: Forest School v. Chigwell School.[67]
# 1858: Westminster School v. Winchester College.[66]
# 1859: Harrow School v. Westminster School.[66]
# 19 November 1859: Radley College v. Old Wykehamists.[66]
# 1 December 1859: Old Marlburians v. Old Rugbeians (played at Christ Church, Oxford).[66]
# 19 December 1859: Old Harrovians v. Old Wykehamists (played at Christ Church, Oxford).[66]
# Firsts
# Clubs
# Main article: Oldest football clubs

# Sheffield F.C. (here pictured in 1857, the year of its foundation) is the oldest surviving association football club in the world.

# Notes about a Sheffield v. Hallam match, dated 29 December 1862
# Sports clubs dedicated to playing football began in the 18th century, for example London's Gymnastic Society which was founded in the mid-18th century and ceased playing matches in 1796.[68][66]

# The first documented club to bear in the title a reference to being a 'football club' were called "The Foot-Ball Club" who were located in Edinburgh, Scotland, during the period 1824–41.[69][70] The club forbade tripping but allowed pushing and holding and the picking up of the ball.[70]

# In 1845, three boys at Rugby school were tasked with codifying the rules then being used at the school. These were the first set of written rules (or code) for any form of football.[71] This further assisted the spread of the Rugby game.

# The earliest known matches involving non-public school clubs or institutions are as follows:

# 13 February 1856: Charterhouse School v. St Bartholemew's Hospital.[72]
# 7 November 1856: Bedford Grammar School v. Bedford Town Gentlemen.[73]
# 13 December 1856: Sunbury Military College v. Littleton Gentlemen.[74]
# December 1857: Edinburgh University v. Edinburgh Academical Club.[75]
# 24 November 1858: Westminster School v. Dingley Dell Club.[76]
# 12 May 1859: Tavistock School v. Princetown School.[77]
# 5 November 1859: Eton School v. Oxford University.[78]
# 22 February 1860: Charterhouse School v. Dingley Dell Club.[79]
# 21 July 1860: Melbourne v. Richmond.[80]
# 17 December 1860: 58th Regiment v. Sheffield.[81]
# 26 December 1860: Sheffield v. Hallam.[82]
# Competitions
# Main article: Oldest football competitions
# One of the longest running football fixture is the Cordner-Eggleston Cup, contested between Melbourne Grammar School and Scotch College, Melbourne every year since 1858. It is believed by many to also be the first match of Australian rules football, although it was played under experimental rules in its first year. The first football trophy tournament was the Caledonian Challenge Cup, donated by the Royal Caledonian Society of Melbourne, played in 1861 under the Melbourne Rules.[83] The oldest football league is a rugby football competition, the United Hospitals Challenge Cup (1874), while the oldest rugby trophy is the Yorkshire Cup, contested since 1878. The South Australian Football Association (30 April 1877) is the oldest surviving Australian rules football competition. The oldest surviving soccer trophy is the Youdan Cup (1867) and the oldest national football competition is the English FA Cup (1871). The Football League (1888) is recognised as the longest running association football league. The first international Rugby football match took place between Scotland and England on 27 March 1871 at Raeburn Place, Edinburgh. The first international Association football match officially took place between sides representing England and Scotland on 30 November 1872 at Hamilton Crescent, the West of Scotland Cricket Club's ground in Partick, Glasgow under the authority of the FA.

# Modern balls
# Main article: Football (ball)

# Richard Lindon (seen in 1880) is believed to have invented the first footballs with rubber bladders.
# In Europe, early footballs were made out of animal bladders, more specifically pig's bladders, which were inflated. Later leather coverings were introduced to allow the balls to keep their shape.[84] However, in 1851, Richard Lindon and William Gilbert, both shoemakers from the town of Rugby (near the school), exhibited both round and oval-shaped balls at the Great Exhibition in London. Richard Lindon's wife is said to have died of lung disease caused by blowing up pig's bladders.[a] Lindon also won medals for the invention of the "Rubber inflatable Bladder" and the "Brass Hand Pump".

# In 1855, the U.S. inventor Charles Goodyear – who had patented vulcanised rubber – exhibited a spherical football, with an exterior of vulcanised rubber panels, at the Paris Exhibition Universelle. The ball was to prove popular in early forms of football in the U.S.[85]

# The iconic ball with a regular pattern of hexagons and pentagons (see truncated icosahedron) did not become popular until the 1960s, and was first used in the World Cup in 1970.

# Modern ball passing tactics
# Main article: Passing (association football)
# The earliest reference to a game of football involving players passing the ball and attempting to score past a goalkeeper was written in 1633 by David Wedderburn, a poet and teacher in Aberdeen, Scotland.[86] Nevertheless, the original text does not state whether the allusion to passing as 'kick the ball back' ('repercute pilam') was in a forward or backward direction or between members of the same opposing teams (as was usual at this time).[87]

# "Scientific" football is first recorded in 1839 from Lancashire[88] and in the modern game in rugby football from 1862[89] and from Sheffield FC as early as 1865.[90][91] The first side to play a passing combination game was the Royal Engineers AFC in 1869/70.[92][93] By 1869 they were "work[ing] well together", "backing up" and benefiting from "cooperation".[94] By 1870 the Engineers were passing the ball: "Lieut. Creswell, who having brought the ball up the side then kicked it into the middle to another of his side, who kicked it through the posts the minute before time was called".[95] Passing was a regular feature of their style.[96] By early 1872 the Engineers were the first football team renowned for "play[ing] beautifully together".[97] A double pass is first reported from Derby school against Nottingham Forest in March 1872, the first of which is irrefutably a short pass: "Mr Absey dribbling the ball half the length of the field delivered it to Wallis, who kicking it cleverly in front of the goal, sent it to the captain who drove it at once between the Nottingham posts".[98] The first side to have perfected the modern formation was Cambridge University AFC;[99][100][101] they also introduced the 2–3–5 "pyramid" formation.[102][103]
# ''')