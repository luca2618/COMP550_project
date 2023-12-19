
#used to exclude the cosine similarity
def split_dict(d):
    for i in d:
        list1, list2 = zip(*(d[i]))
        d[i] = list1

#print the common words
def common(d):
    within = {}
    shares = {}

    for i in d:
        for j in d:
            if i == j:
                continue
            if i in d[j]:
                if i in within:
                    within[i].append(j)
                else:
                    within[i] = [j]
                    
        for j in d:
            if i == j:
                continue
            c = list(set(d[i]) & set(d[j]))
            if c != []:
                for w in c:
                    if w in shares and (j, i) not in shares[w]:
                        shares[w].append((i, j))
                    else:
                        shares[w] = [(i,j)]

    print("Words that appear with high cosine similarity in other sets:")
    print(within)
    
    print("Words with words in its cosine similarity set that appear in other sets:")
    print(shares)
    
co_dict = {
    'intelligent': [('smart', 0.860828161239624), ('intellegent', 0.8432874083518982), ('intuitive', 0.8310775756835938), ('resourceful', 0.8184135556221008), ('selfpossessed', 0.808256983757019), ('sharpwitted', 0.8047395944595337), ('observant', 0.801581621170044), ('perceptive', 0.7860488295555115)],
    'sly': [('sneaky', 0.697766125202179), ('wry', 0.6480046510696411), ('mischievous', 0.6323168873786926), ('bth', 0.6320476531982422), ('conniving', 0.6247597336769104), ('cheeky', 0.6173976063728333), ('crafty', 0.6100731492042542), ('shkhsyt', 0.6079998016357422)],
    'charming': [('endearing', 0.8140586018562317), ('charmingly', 0.8095045685768127), ('charismatic', 0.80806964635849), ('charmingand', 0.8064796924591064), ('chivalrous', 0.7975370287895203), ('cheeky', 0.7967521548271179), ('adorably', 0.7957159876823425), ('lovable', 0.7880224585533142)],
    'deceiving': [('deceptive', 0.7761987447738647), ('misleading', 0.7361838221549988), ('decieving', 0.7204534411430359), ('deceitful', 0.647171676158905), ('gorgeousand', 0.6460505723953247), ('misleads', 0.6447351574897766), ('coverwhat', 0.6410283446311951), ('boldfaced', 0.6387922763824463)],
    'confident': [('selfassured', 0.8859027624130249), ('selfconfident', 0.8753819465637207), ('assertive', 0.844588577747345), ('selfconscious', 0.785956084728241), ('independent', 0.7697242498397827), ('selfreliant', 0.764407217502594), ('incontrol', 0.7561300992965698), ('corageous', 0.7555540800094604)],
    'arrogant': [('cocky', 0.8705896139144897), ('egotistical', 0.8654176592826843), ('conceited', 0.8642756938934326), ('pompous', 0.8367554545402527), ('overconfident', 0.81798255443573), ('boastful', 0.7982192635536194), ('egoistical', 0.7918224930763245), ('egotistic', 0.790302038192749)],
    'tough': [('rough', 0.7505917549133301), ('tougher', 0.7176647186279297), ('toughest', 0.7085803151130676), ('resiliant', 0.702938973903656), ('gutsy', 0.7011256217956543), ('smart', 0.6938261389732361), ('resilient', 0.6895763278007507), ('ladyballs', 0.6868810057640076)],
    'stiff': [('stilted', 0.7816661596298218), ('stuffy', 0.7098209261894226), ('choppy', 0.7087615728378296), ('cardboardlike', 0.7052043080329895), ('inconsistent', 0.7045828104019165), ('clunky', 0.7040057182312012), ('overdescriptive', 0.6935878992080688), ('unrefined', 0.691478967666626)],
    'logical': [('reasonable', 0.8535709977149963), ('rational', 0.8131622076034546), ('logically', 0.7521938681602478), ('counterintuitive', 0.7392940521240234), ('plausible', 0.7336328029632568), ('practical', 0.7309069037437439), ('logic', 0.7256289720535278), ('wellreasoned', 0.7161056995391846)],
    'robotic': [('emotionless', 0.7836817502975464), ('mechanical', 0.7822842597961426), ('unemotional', 0.7551903128623962), ('robotlike', 0.752656102180481), ('unfeeling', 0.7246532440185547), ('robot', 0.7009872198104858), ('malfunctioning', 0.6906653046607971), ('proprietary', 0.690534770488739)],
    'fearless': [('courageous', 0.866564154624939), ('brave', 0.8439527153968811), ('strongwilled', 0.8333974480628967), ('fierce', 0.8331995606422424), ('tenacious', 0.8287445902824402), ('headstrong', 0.8102186918258667), ('resourceful', 0.8098711967468262), ('willed', 0.8039389848709106)],
    'reckless': [('impulsive', 0.9046891331672668), ('impetuous', 0.8347610831260681), ('rash', 0.8026986718177795), ('foolish', 0.7996233701705933), ('stubborn', 0.786637544631958), ('pigheaded', 0.7827444076538086), ('foolhardy', 0.7797654271125793), ('selfish', 0.7675729393959045)],
    'aspiring': [('upandcoming', 0.8073954582214355), ('artist', 0.7768445014953613), ('photographer', 0.7583993673324585), ('lyricist', 0.7436136603355408), ('worldrenowned', 0.7408862709999084), ('journalist', 0.7383026480674744), ('singersongwriter', 0.7315822839736938), ('asianaustralian', 0.7303673028945923)],
    'ruthless': [('merciless', 0.8540661334991455), ('coldblooded', 0.8196014761924744), ('cunning', 0.817367672920227), ('unmerciful', 0.8157782554626465), ('powerhungry', 0.8123178482055664), ('calculating', 0.8112161755561829), ('sadistic', 0.8096903562545776), ('remorseless', 0.8064968585968018)],
    'decisive': [('assertive', 0.7799249291419983), ('defiant', 0.7336962819099426), ('selfreliant', 0.7292681336402893), ('courageous', 0.7066306471824646), ('strongminded', 0.7036253213882446), ('resolute', 0.6928088665008545), ('selfsacrificing', 0.6919269561767578), ('selfcritical', 0.690804123878479)],
    'impulsive': [('reckless', 0.9046891927719116), ('impetuous', 0.8781083822250366), ('rash', 0.8479436635971069), ('stubborn', 0.8451371192932129), ('headstrong', 0.8227596282958984), ('hardheaded', 0.818017303943634), ('brash', 0.8064031600952148), ('pigheaded', 0.7970830202102661)],
    'selfless': [('unselfish', 0.9004696607589722), ('brave', 0.8499563932418823), ('courageous', 0.8393770456314087), ('selfsacrificing', 0.8382357358932495), ('dauntlessthe', 0.8215746879577637), ('compassionate', 0.8198468685150146), ('altruistic', 0.8066540360450745), ('fearless', 0.7897011637687683)],
    'submissive': [('subservient', 0.8017132878303528), ('weakwilled', 0.7670981287956238), ('obedient', 0.7532551288604736), ('meek', 0.7459542751312256), ('passive', 0.7282276749610901), ('demure', 0.7280716896057129), ('selfsacrificing', 0.7262827754020691), ('needy', 0.7233805656433105)],
    'flexible': [('adaptable', 0.6807597279548645), ('openminded', 0.6781583428382874), ('conscientious', 0.6584566831588745), ('malleable', 0.6532080173492432), ('analytic', 0.65147864818573), ('durable', 0.6463461518287659), ('intuitive', 0.6452865600585938), ('wearable', 0.6435337066650391)],
    'disorganized': [('unorganized', 0.8232568502426147), ('unstructured', 0.7635501027107239), ('unorganised', 0.7628195285797119), ('haphazard', 0.7626741528511047), ('disorganised', 0.7596861720085144), ('unfocused', 0.748563826084137), ('chaotic', 0.7459595799446106), ('discombobulated', 0.7357112169265747)],
    'optimistic': [('cheerful', 0.8337246775627136), ('hopeful', 0.8295690417289734), ('upbeat', 0.7787349820137024), ('idealistic', 0.7565756440162659), ('pessimistic', 0.7546524405479431), ('cynical', 0.7415680885314941), ('earnest', 0.7253437638282776), ('buoyant', 0.7199153900146484)],
    'idealistic': [('idealized', 0.7742553353309631), ('idealised', 0.7583040595054626), ('optimistic', 0.7565757036209106), ('naiive', 0.7558522820472717), ('dreamyeyed', 0.7546238899230957), ('utopic', 0.7399009466171265), ('unperceptive', 0.7309466004371643), ('idealistically', 0.7305245995521545)],
    'caring': [('compassionate', 0.7992990016937256), ('kindhearted', 0.7717874646186829), ('considerate', 0.7660834789276123), ('forgiving', 0.7600598335266113), ('dependable', 0.7534409165382385), ('loving', 0.7424931526184082), ('hardworking', 0.7385337352752686), ('protective', 0.7326215505599976)],
    'sentimental': [('maudlin', 0.7169241309165955), ('sappy', 0.6982129216194153), ('saccharine', 0.6820350885391235), ('soppy', 0.6618033647537231), ('sensible', 0.658835768699646), ('saccharin', 0.6444067358970642), ('schmaltzy', 0.6394421458244324), ('syrupy', 0.6332496404647827)],
    'reserved': [('quiet', 0.7381575107574463), ('studious', 0.7309197783470154), ('outspoken', 0.7159262299537659), ('withdrawn', 0.7143758535385132), ('observant', 0.7063372135162354), ('opinionated', 0.6914604306221008), ('outgoing', 0.683189332485199), ('softspoken', 0.6830881237983704)],
    'quiet': [('reserved', 0.7381575107574463), ('studious', 0.7323418259620667), ('unassuming', 0.7110466957092285), ('bighearted', 0.7072189450263977), ('quieter', 0.7040658593177795), ('undertheradar', 0.703021764755249), ('bigboned', 0.7018441557884216), ('softspoken', 0.6998587250709534)],
    'organized': [('organised', 0.884977400302887), ('structured', 0.7445008158683777), ('militarylike', 0.7149937748908997), ('coordinated', 0.708903431892395), ('wellorganized', 0.6764585375785828), ('conducted', 0.6764528751373291), ('allcontrolling', 0.674992024898529), ('rulebased', 0.6738951206207275)],
    'perfectionist': [('overachiever', 0.7229192852973938), ('typea', 0.7012236714363098), ('gogetter', 0.6782996654510498), ('straighta', 0.668310284614563), ('supernerd', 0.6452332735061646), ('joiner', 0.6430784463882446), ('fadley', 0.6387692093849182), ('dessy', 0.636910617351532)],
    'supportive': [('dadlike', 0.7595635652542114), ('respectful', 0.7585489749908447), ('protective', 0.7550303339958191), ('trustful', 0.7335478663444519), ('familyorientated', 0.7328094840049744), ('loyal', 0.7324376106262207), ('nonjudgmental', 0.7300341725349426), ('accommodating', 0.7288557291030884)],
    'overbearing': [('overprotective', 0.828288733959198), ('pushy', 0.8177489638328552), ('domineering', 0.8160150051116943), ('overcontrolling', 0.778730571269989), ('unsupportive', 0.7778514623641968), ('neglectful', 0.7737855911254883), ('overbearingly', 0.7619667053222656), ('ineffectual', 0.7603848576545715)],
    'playful': [('cheeky', 0.8495995402336121), ('flirty', 0.8410500884056091), ('flirtatious', 0.8374701142311096), ('witty', 0.8091846704483032), ('banter', 0.786765456199646), ('ribbing', 0.7834697365760803), ('playfulness', 0.7830249071121216), ('humorous', 0.7821800112724304)],
    'immature': [('childish', 0.926044762134552), ('whiny', 0.8505142331123352), ('bratty', 0.8497214317321777), ('whiney', 0.8403732776641846), ('selfcentered', 0.8335916996002197), ('whinny', 0.8255413770675659), ('naive', 0.824855387210846), ('selfabsorbed', 0.8236600756645203)],
}

ant_dict = {
    'intelligent': [('smart', 0.860828161239624), ('intellegent', 0.8432874083518982), ('intuitive', 0.8310775756835938), ('resourceful', 0.8184135556221008), ('selfpossessed', 0.808256983757019), ('sharpwitted', 0.8047395944595337), ('observant', 0.801581621170044), ('perceptive', 0.7860488295555115)],
    'dumb': [('stupid', 0.9482793211936951), ('idiotic', 0.8490210175514221), ('ridiculous', 0.8183220624923706), ('inmature', 0.8093705177307129), ('silly', 0.8085719347000122), ('pathetic', 0.784636378288269), ('dumbass', 0.7830223441123962), ('lame', 0.7821915149688721)],
    'charming': [('endearing', 0.8140586018562317), ('charmingly', 0.8095045685768127), ('charismatic', 0.80806964635849), ('charmingand', 0.8064796924591064), ('chivalrous', 0.7975370287895203), ('cheeky', 0.7967521548271179), ('adorably', 0.7957159876823425), ('lovable', 0.7880224585533142)],
    'repellent': [('humourless', 0.7386808395385742), ('impudent', 0.7289250493049622), ('repulsive', 0.7137743830680847), ('braindead', 0.713760256767273), ('graceless', 0.7076697945594788), ('nincompoop', 0.704801082611084), ('statuesque', 0.6996840238571167), ('soulless', 0.6961754560470581)],
    'confident': [('selfassured', 0.8859027624130249), ('selfconfident', 0.8753819465637207), ('assertive', 0.844588577747345), ('selfconscious', 0.785956084728241), ('independent', 0.7697242498397827), ('selfreliant', 0.764407217502594), ('incontrol', 0.7561300992965698), ('corageous', 0.7555540800094604)],
    'shy': [('timid', 0.6880382299423218), ('introverted', 0.6657356023788452), ('bashful', 0.6520655155181885), ('meek', 0.6446666717529297), ('mousy', 0.6394424438476562), ('selfconscious', 0.6377649307250977), ('unconfident', 0.6371898055076599), ('cripplingly', 0.6305695176124573)],
    'tough': [('rough', 0.7505917549133301), ('tougher', 0.7176647186279297), ('toughest', 0.7085803151130676), ('resiliant', 0.702938973903656), ('gutsy', 0.7011256217956543), ('smart', 0.6938261389732361), ('resilient', 0.6895763278007507), ('ladyballs', 0.6868810057640076)],
    'soft': [('jawline', 0.7003027200698853), ('softy', 0.6771793365478516), ('softest', 0.6721730828285217), ('spot', 0.6711211204528809), ('throaty', 0.6645728349685669), ('softness', 0.6642417907714844), ('chiselled', 0.6606222987174988), ('swoopy', 0.6505212187767029)],
    'logical': [('reasonable', 0.8535709977149963), ('rational', 0.8131622076034546), ('logically', 0.7521938681602478), ('counterintuitive', 0.7392940521240234), ('plausible', 0.7336328029632568), ('practical', 0.7309069037437439), ('logic', 0.7256289720535278), ('wellreasoned', 0.7161056995391846)],
    'emotional': [('rollercoster', 0.785372257232666), ('emtional', 0.7784831523895264), ('rollarcoaster', 0.771230936050415), ('rollar', 0.7596526741981506), ('emotinal', 0.7427282929420471), ('intense', 0.740267276763916), ('rollcoaster', 0.7388925552368164), ('rollercoasters', 0.7366241216659546)],
    'fearless': [('courageous', 0.866564154624939), ('brave', 0.8439527153968811), ('strongwilled', 0.8333974480628967), ('fierce', 0.8331995606422424), ('tenacious', 0.8287445902824402), ('headstrong', 0.8102186918258667), ('resourceful', 0.8098711967468262), ('willed', 0.8039389848709106)],
    'scared': [('terrified', 0.8874903321266174), ('frightened', 0.8514237999916077), ('afraid', 0.8172774314880371), ('shitless', 0.8081414103507996), ('fearful', 0.7979214191436768), ('nervous', 0.7487916946411133), ('embarassed', 0.747816801071167), ('angryand', 0.728304922580719)],
    'aspiring': [('upandcoming', 0.8073954582214355), ('artist', 0.7768445014953613), ('photographer', 0.7583993673324585), ('lyricist', 0.7436136603355408), ('worldrenowned', 0.7408862709999084), ('journalist', 0.7383026480674744), ('singersongwriter', 0.7315822839736938), ('asianaustralian', 0.7303673028945923)],
    'satisfied': [('unsatisfied', 0.844059407711029), ('dissatisfied', 0.8395447134971619), ('contented', 0.770354688167572), ('pleased', 0.7622274160385132), ('satisfying', 0.7619792222976685), ('disappointed', 0.7512137293815613), ('satisified', 0.7504885196685791), ('satisfactory', 0.7391830086708069)],
    'decisive': [('assertive', 0.7799249291419983), ('defiant', 0.7336962819099426), ('selfreliant', 0.7292681336402893), ('courageous', 0.7066306471824646), ('strongminded', 0.7036253213882446), ('resolute', 0.6928088665008545), ('selfsacrificing', 0.6919269561767578), ('selfcritical', 0.690804123878479)],
    'cautious': [('wary', 0.798319399356842), ('untrusting', 0.7578423023223877), ('doubtful', 0.7448326945304871), ('selfcritical', 0.7416219711303711), ('skittish', 0.7316126227378845), ('reticent', 0.7230700254440308), ('distrustful', 0.7212826013565063), ('clearheaded', 0.7200910449028015)],
    'selfless': [('unselfish', 0.9004696607589722), ('brave', 0.8499563932418823), ('courageous', 0.8393770456314087), ('selfsacrificing', 0.8382357358932495), ('dauntlessthe', 0.8215746879577637), ('compassionate', 0.8198468685150146), ('altruistic', 0.8066540360450745), ('fearless', 0.7897011637687683)],
    'selfish': [('selfcentered', 0.940483570098877), ('selfcentred', 0.9037987589836121), ('selfabsorbed', 0.902043342590332), ('inconsiderate', 0.8839948177337646), ('ungrateful', 0.8792480230331421), ('bratty', 0.8629045486450195), ('selfinvolved', 0.8621984124183655), ('whiny', 0.8549797534942627)],
    'flexible': [('adaptable', 0.6807597279548645), ('openminded', 0.6781583428382874), ('conscientious', 0.6584566831588745), ('malleable', 0.6532080173492432), ('analytic', 0.65147864818573), ('durable', 0.6463461518287659), ('intuitive', 0.6452865600585938), ('wearable', 0.6435337066650391)],
    'rigid': [('strict', 0.8717743754386902), ('rigidly', 0.806835412979126), ('restrictive', 0.787655234336853), ('patriarchal', 0.7513852715492249), ('rigidity', 0.7438454031944275), ('constrictive', 0.7305312156677246), ('adherence', 0.7294900417327881), ('stifling', 0.7272341847419739)],
    'optimistic': [('cheerful', 0.8337246775627136), ('hopeful', 0.8295690417289734), ('upbeat', 0.7787349820137024), ('idealistic', 0.7565756440162659), ('pessimistic', 0.7546524405479431), ('cynical', 0.7415680885314941), ('earnest', 0.7253437638282776), ('buoyant', 0.7199153900146484)],
    'pessimistic': [('cynical', 0.8792668581008911), ('defeatist', 0.7829607129096985), ('judgmental', 0.7790351510047913), ('pessimist', 0.7623252868652344), ('mopy', 0.760711133480072), ('judgemental', 0.7550351023674011), ('optimistic', 0.7546525001525879), ('selfcentred', 0.7487937808036804)],
    'caring': [('compassionate', 0.7992990016937256), ('kindhearted', 0.7717874646186829), ('considerate', 0.7660834789276123), ('forgiving', 0.7600598335266113), ('dependable', 0.7534409165382385), ('loving', 0.7424931526184082), ('hardworking', 0.7385337352752686), ('protective', 0.7326215505599976)],
    'stoic': [('gruff', 0.8157429695129395), ('aloof', 0.8141969442367554), ('softspoken', 0.8063249588012695), ('calculating', 0.7937130331993103), ('compassionate', 0.791741132736206), ('calculative', 0.7873081564903259), ('hardass', 0.7867755889892578), ('quicktempered', 0.784755289554596)],
    'reserved': [('quiet', 0.7381575107574463), ('studious', 0.7309197783470154), ('outspoken', 0.7159262299537659), ('withdrawn', 0.7143758535385132), ('observant', 0.7063372135162354), ('opinionated', 0.6914604306221008), ('outgoing', 0.683189332485199), ('softspoken', 0.6830881237983704)],
    'loud': [('laughing', 0.8708649277687073), ('laugh', 0.8384283781051636), ('laughed', 0.8295140862464905), ('outloud', 0.8275067806243896), ('hysterically', 0.8191351294517517), ('chortling', 0.7869711518287659), ('snort', 0.7869116067886353), ('guffawing', 0.785845935344696)],
    'organized': [('organised', 0.884977400302887), ('structured', 0.7445008158683777), ('militarylike', 0.7149937748908997), ('coordinated', 0.708903431892395), ('wellorganized', 0.6764585375785828), ('conducted', 0.6764528751373291), ('allcontrolling', 0.674992024898529), ('rulebased', 0.6738951206207275)],
    'scattered': [('dispersed', 0.8371431827545166), ('strewn', 0.8185615539550781), ('sprinkled', 0.7478182911872864), ('littered', 0.7345632314682007), ('dotted', 0.7211596965789795), ('peppered', 0.7175116539001465), ('spattered', 0.7108328938484192), ('smattered', 0.7102066874504089)],
    'supportive': [('dadlike', 0.7595635652542114), ('respectful', 0.7585489749908447), ('protective', 0.7550303339958191), ('trustful', 0.7335478663444519), ('familyorientated', 0.7328094840049744), ('loyal', 0.7324376106262207), ('nonjudgmental', 0.7300341725349426), ('accommodating', 0.7288557291030884)],
    'independent': [('willed', 0.8784856796264648), ('strongwilled', 0.8619869351387024), ('headstrong', 0.8589646220207214), ('assertive', 0.8414831161499023), ('strongminded', 0.8323834538459778), ('selfreliant', 0.8320457339286804), ('independant', 0.823993444442749), ('resourceful', 0.8211042881011963)],
    'playful': [('cheeky', 0.8495995402336121), ('flirty', 0.8410500884056091), ('flirtatious', 0.8374701142311096), ('witty', 0.8091846704483032), ('banter', 0.786765456199646), ('ribbing', 0.7834697365760803), ('playfulness', 0.7830249071121216), ('humorous', 0.7821800112724304)],
    'serious': [('heavy', 0.7753244042396545), ('constipation', 0.7123400568962097), ('heavyhitting', 0.7108141183853149), ('weightier', 0.7087074518203735), ('weighty', 0.7066584229469299), ('notsofun', 0.7048044204711914), ('heavier', 0.6968924403190613), ('sensitive', 0.6966478228569031)],
}



split_dict(co_dict)
split_dict(ant_dict)

common(co_dict)
common(ant_dict)