from tkinter import *
import random
import version

def v_31():
    global options, prints, i
    # 32 characters
    letters = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    index_to_letter = { i: letters[i] for i in range(32) }
    letter_to_index = { v: k for k, v in index_to_letter.items() }

    def bit_string_to_text(bits):
        # pad the bits array to be multiple of 5
        if len(bits) % 5 > 0:
            bits += [0] * (5 - len(bits) % 5)
        # convert to characters
        result = ""
        for i in range(0, len(bits), 5):
            chunk = bits[i:i + 5]
            value = 0
            for b in range(5):
                value |= chunk[b] << b
            result += index_to_letter[value]
        return result

    def copy():
        entry.selection_range(0, END)
        entry.event_generate("<<Copy>>")

    prints = []
    i = 0;
    options = [0 for i in range(100)]

    def printSeed():
        value.set(bit_string_to_text(options));

    def printNext():
        global i
        if i >= len(prints):
            printSeed()
        else:
            label.config(text=prints[i])
            i+=1

    def generateSeed():
        global options, prints, i

        text_shuffle_max = 0

        if(text_shuffle.get() == "Shuffle excepted Hints and Keys"):
            text_shuffle_max = 1

        elif(text_shuffle.get() == "All text shuffled"):
            text_shuffle_max = 2

        difficulty_max = 0

        if(difficulty.get() == "Hard"):
            difficulty_max = 1

        elif(difficulty.get() == "Very Hard"):
            difficulty_max = 2

        elif(difficulty.get() == "OHKO"):
            difficulty_max = 3

        value.set("");
        prints = []
        options = [0 for i in range(100)]
        i=0
        label.config(text="")

        verbose = False
        if v.get() == 1:
            verbose = True

        #Create spoiler log
        options[5] = 1
        if verbose:
            prints.append("Create spoiler log")


        #Open forest
        options[6] = random.randint(0, 1)
        if verbose:
            if options[1] == 0:
                prints.append("Closed Forest")
            else:
                prints.append("Open Forest")


        #Open kak
        options[7] = random.randint(0, 1)
        if verbose:
            if options[2] == 0:
                prints.append("Closed Kakariko Gate")
            else:
                prints.append("Open Kakariko Gate")


        #Open DoT
        options[8] = random.randint(0, 1)
        if verbose:
            if options[3] == 0:
                prints.append("Closed DoT")
            else:
                prints.append("Open DoT")


        #Option carpenter
        carp = random.randint(0, 2)
        if carp == 0:
            options[9] = 0
            options[10] = 0
            if verbose:
                prints.append("Gerudo : Default")

        elif carp == 1:
            options[9] = 1
            options[10] = 0
            if verbose:
                prints.append("Gerudo : Only One Carpenter")

        else:
            options[9] = 0
            options[10] = 1
            if verbose:
                prints.append("Gerudo : Start with Gerudo Card")


        #Bridge
        bridge = random.randint(0, 3)
        if bridge == 0:
            options[11] = 0
            options[12] = 0
            if verbose:
                prints.append("Bridge : All Dungeons")

        elif bridge == 1:
            options[11] = 1
            options[12] = 0
            if verbose:
                prints.append("Bridge : All Medaillons")

        elif bridge == 2:
            options[11] = 0
            options[12] = 1
            if verbose:
                prints.append("Bridge : Vanilla (Shadow + Spirit Medallions)")

        else:
            options[11] = 1
            options[12] = 1
            if verbose:
                prints.append("Bridge : Open")


        #Trials
        options[16] = random.randint(0, 1)
        if(options[16] == 0):
            trials = random.randint(0, 6)
            if(trials == 0):
                options[17] = 0
                options[18] = 0
                options[19] = 0
                if verbose:
                    prints.append("Trials : 0")

            elif(trials == 1):
                  options[17] = 1
                  options[18] = 0
                  options[19] = 0
                  if verbose:
                      prints.append("Trials : 1")

            elif(trials == 2):
                  options[17] = 0
                  options[18] = 1
                  options[19] = 0
                  if verbose:
                      prints.append("Trials : 2")

            elif(trials == 3):
                  options[17] = 1
                  options[18] = 1
                  options[19] = 0
                  if verbose:
                      prints.append("Trials : 3")

            elif(trials == 4):
                  options[17] = 0
                  options[18] = 0
                  options[19] = 1
                  if verbose:
                      prints.append("Trials : 4")

            elif(trials == 5):
                  options[17] = 1
                  options[18] = 0
                  options[19] = 1
                  if verbose:
                      prints.append("Trials : 5")

            else:
                  options[17] = 0
                  options[18] = 1
                  options[19] = 1
                  if verbose:
                      prints.append("Trials : 6")

        else:
            if verbose:
                prints.append("Trials : Random")

        #Location reachable
        options[13] = random.randint(0, 1)
        if verbose:
            if options[13] == 0:
                prints.append("All locations reachable: OFF")
            else:
                prints.append("All locations reachable: ON")


        #Bombchu logic
        options[14] = random.randint(0, 1)
        if verbose:
            if options[14] == 0:
                prints.append("Bombchu in logic: OFF")
            else:
                prints.append("Bombchu in logic: ON")


        #Major item
        options[15] = random.randint(0, 1)
        if verbose:
            if options[15] == 0:
                prints.append("One Major item per dungeon: OFF")
            else:
                prints.append("One Major item per dungeon: ON")

        #Dungeon quest
        options[51] = random.randint(0, 1)
        if options[51] == 0:
            quest = random.randint(0, 12)
            if quest == 0:
                options[52] = 0
                options[53] = 0
                options[54] = 0
                options[55] = 0
            elif quest == 1:
                options[52] = 1
                options[53] = 0
                options[54] = 0
                options[55] = 0
            elif quest == 2:
                options[52] = 0
                options[53] = 1
                options[54] = 0
                options[55] = 0
            elif quest == 3:
                options[52] = 1
                options[53] = 1
                options[54] = 0
                options[55] = 0
            elif quest == 4:
                options[52] = 0
                options[53] = 0
                options[54] = 1
                options[55] = 0
            elif quest == 5:
                options[52] = 1
                options[53] = 0
                options[54] = 1
                options[55] = 0
            elif quest == 6:
                options[52] = 0
                options[53] = 1
                options[54] = 1
                options[55] = 0
            elif quest == 7:
                options[52] = 1
                options[53] = 1
                options[54] = 1
                options[55] = 0
            elif quest == 8:
                options[52] = 0
                options[53] = 0
                options[54] = 0
                options[55] = 1
            elif quest == 9:
                options[52] = 1
                options[53] = 0
                options[54] = 0
                options[55] = 1
            elif quest == 10:
                options[52] = 0
                options[53] = 1
                options[54] = 0
                options[55] = 1
            elif quest == 11:
                options[52] = 1
                options[53] = 1
                options[54] = 0
                options[55] = 1
            else:
                options[52] = 0
                options[53] = 0
                options[54] = 1
                options[55] = 1

            if verbose:
                prints.append("Dungeons Master Quest Number : " + quest)
        else:
            if verbose:
                prints.append("Dungeons Master Quest Number : Random")

        #Shuffle KS
        options[30] = random.randint(0, 1)
        if verbose:
            if options[30] == 0:
                prints.append("Shuffle Kokiri Sword: OFF")
            else:
                prints.append("Shuffle Kokiri Sword: ON")


        #Shuffle Weird egg
        options[31] = random.randint(0, 1)
        if verbose:
            if options[31] == 0:
                prints.append("Shuffle Weird Egg: OFF")
            else:
                prints.append("Shuffle Weird Egg: ON")


        #Shuffle Ocarinas
        options[32] = random.randint(0, 1)
        if verbose:
            if options[32] == 0:
                prints.append("Shuffle Ocarina: OFF")
            else:
                prints.append("Shuffle Ocarina: ON")


        #Shuffle Songs
        options[33] = random.randint(0, 1)
        if verbose:
            if options[33] == 0:
                prints.append("Songs with items: OFF")
            else:
                prints.append("Songs with items: ON")


        #Shuffle Gerudo card
        options[34] = random.randint(0, 1)
        if verbose:
            if options[34] == 0:
                prints.append("Shuffle Gerudo Card: OFF")
            else:
                prints.append("Shuffle Gerudo Card: ON")


        #Scrub
        scrub = random.randint(0, 3)
        if scrub == 0:
            options[35] = 0
            options[36] = 0
            if verbose:
                prints.append("Scrubsanity: OFF")

        elif scrub == 1:
            options[35] = 1
            options[36] = 0
            if verbose:
                prints.append("Scrubsanity: Affordable")

        elif scrub == 2:
            options[35] = 0
            options[36] = 1
            if verbose:
                prints.append("Scrubsanity: Expensive")

        else:
            options[35] = 1
            options[36] = 1
            if verbose:
                prints.append("Scrubsanity: Random Prize")


        #Shop
        shop = random.randint(0, 6)
        if shop == 0:
            options[38] = 0
            options[39] = 0
            options[40] = 0
            if verbose:
                prints.append("Shopsanity: OFF")

        elif shop == 1:
            options[38] = 1
            options[39] = 0
            options[40] = 0
            if verbose:
                prints.append("Shopsanity: 0 items")

        elif shop == 2:
            options[38] = 0
            options[39] = 1
            options[40] = 0
            if verbose:
                prints.append("Shopsanity: 1 items")

        elif shop == 3:
            options[38] = 1
            options[39] = 1
            options[40] = 0
            if verbose:
                prints.append("Shopsanity: 2 items")

        elif shop == 4:
            options[38] = 0
            options[39] = 0
            options[40] = 1
            if verbose:
                prints.append("Shopsanity: 3 items")

        elif shop == 5:
            options[38] = 1
            options[39] = 0
            options[40] = 1
            if verbose:
                prints.append("Shopsanity: 4 items")

        else:
            options[38] = 0
            options[39] = 1
            options[40] = 1
            if verbose:
                prints.append("Shopsanity: Random items")


        #Maps/Compass
        map = random.randint(0, 3)
        if map == 0:
            options[41] = 0
            options[42] = 0
            if verbose:
                prints.append("Map/Compass: Remove")

        elif map == 1:
            options[41] = 1
            options[42] = 0
            if verbose:
                prints.append("Map/Compass: Start with")

        elif map == 2:
            options[41] = 0
            options[42] = 1
            if verbose:
                prints.append("Map/Compass: Dungeon Only")

        else:
            options[41] = 1
            options[42] = 1
            if verbose:
                prints.append("Map/Compass: Everywhere")


        #Keys
        keys = random.randint(0, 2)
        if keys == 0:
            options[43] = 0
            options[44] = 0
            if verbose:
                prints.append("Keys: Remove")

        elif keys == 1:
            options[43] = 1
            options[44] = 0
            if verbose:
                prints.append("Keys: Dungeon Only")

        else:
            options[43] = 0
            options[44] = 1
            if verbose:
                prints.append("Keys: Everywhere")


        #BK
        bk = random.randint(0, 2)
        if bk == 0:
            options[45] = 0
            options[46] = 0
            if verbose:
                prints.append("Boss Keys: Remove")

        elif bk == 1:
            options[45] = 1
            options[46] = 0
            if verbose:
                prints.append("Boss Keys: Dungeon only")

        else:
            options[45] = 0
            options[46] = 1
            if verbose:
                prints.append("Boss Keys: Everywhere")


        #Information map/compass
        options[47] = random.randint(0, 1)
        if verbose:
            if options[47] == 0:
                prints.append("Informations at Temple of Time")
            else:
                prints.append("Information with Map/Compass")


        #Ganon BK
        if bk > 0:
            options[48] = random.randint(0, 1)
            if verbose:
                if options[48] == 0:
                    prints.append("Ganon Boss Key: Keep")
                else:
                    prints.append("Ganon Boss Key: Remove")


        #token
        token = random.randint(0, 2)
        if token == 0:
            options[49] = 0
            options[49] = 0
            if verbose:
                prints.append("Tokensanity : OFF")

        elif token == 1:
            options[50] = 1
            options[50] = 0
            if verbose:
                prints.append("Tokensanity : Dungeons Only")

        else:
            options[49] = 0
            options[50] = 1
            if verbose:
                prints.append("Tokensanity : Everywhere")


        #MaxSkull
        skull = random.randint(0, 5)
        if(skull == 0):
            options[56] = 0
            options[57] = 0
            options[58] = 0
            if verbose:
                prints.append("Max Skulls : 0")

        elif(skull == 1):
              options[56] = 1
              options[57] = 0
              options[58] = 0
              if verbose:
                  prints.append("Max Skulls : 10")

        elif(skull == 2):
              options[56] = 0
              options[57] = 1
              options[58] = 0
              if verbose:
                  prints.append("Max Skulls : 20")

        elif(skull == 3):
              options[56] = 1
              options[57] = 1
              options[58] = 0
              if verbose:
                  prints.append("Max Skulls : 30")

        elif(skull == 4):
              options[56] = 0
              options[57] = 0
              options[58] = 1
              if verbose:
                  prints.append("Max Skulls : 40")

        else:
              options[56] = 1
              options[57] = 0
              options[58] = 1
              if verbose:
                  prints.append("Max Skulls : 50")


        #Skull SS
        options[59] = random.randint(0, 1)
        if verbose:
            if options[59] == 0:
                prints.append("Skulls without Sun Song")
            else:
                prints.append("Skulls with Sun Song")


        #Big Poes
        options[60] = random.randint(0, 1)
        if verbose:
            if options[60] == 0:
                prints.append("Big Poes: Enable")
            else:
                prints.append("Big Poes: Disable")


        #Child Fishing
        options[61] = random.randint(0, 1)
        if verbose:
            if options[61] == 0:
                prints.append("Child fishing: Enable")
            else:
                prints.append("Child fishing: Disable")


        #Adult Fishing
        options[62] = random.randint(0, 1)
        if verbose:
            if options[62] == 0:
                prints.append("Adult fishing: Enable")
            else:
                prints.append("Adult fishing: Disable")


        #Skull Mask
        options[63] = random.randint(0, 1)
        if verbose:
            if options[63] == 0:
                prints.append("Skull Mask enabled")
            else:
                prints.append("Skull Mask disabled")


        #Mask of Truth
        options[64] = random.randint(0, 1)
        if verbose:
            if options[64] == 0:
                prints.append("Mask of Truth enabled")
            else:
                prints.append("Mask of Truth disabled")


        #1500 archery
        options[65] = random.randint(0, 1)
        if verbose:
            if options[65] == 0:
                prints.append("1500 archery enabled")
            else:
                prints.append("1500 archery disabled")


        #LW Memory
        options[66] = random.randint(0, 1)
        if verbose:
            if options[66] == 0:
                prints.append("LW Memory game enabled")
            else:
                prints.append("LW Memory game disabled")


        #Dampe 2nd time
        options[67] = random.randint(0, 1)
        if verbose:
            if options[67] == 0:
                prints.append("Dampé 2nd time enabled")
            else:
                prints.append("Dampé 2nd time disabled")


        #Biggoron
        options[68] = random.randint(0, 1)
        if verbose:
            if options[68] == 0:
                prints.append("Biggoron enabled")
            else:
                prints.append("Biggoron disabled")



        #Advanced Tricks
        options[77] = random.randint(0, 1)
        if verbose:
            if options[77] == 0:
                prints.append("Advanced tricks disabled")
            else:
                prints.append("Advanced tricks enabled")


        #Man in the roof
        options[78] = random.randint(0, 1)
        if verbose:
            if options[78] == 0:
                prints.append("Man on the roof trick disabled")
            else:
                prints.append("Man on the roof trick enabled")


        #Child deadhand
        options[79] = random.randint(0, 1)
        if verbose:
            if options[79] == 0:
                prints.append("Child deadhand with KS disabled")
            else:
                prints.append("Child deadhand with KS enabled")


        #DC Jump
        options[80] = random.randint(0, 1)
        if verbose:
            if options[80] == 0:
                prints.append("DC jump trick disabled")
            else:
                prints.append("DC jump trick enabled")


        #Windmill HP
        options[81] = random.randint(0, 1)
        if verbose:
            if options[81] == 0:
                prints.append("Windmill HP trick disabled")
            else:
                prints.append("Windmill HP trick enabled")


        #DMC HP with hover
        options[82] = random.randint(0, 1)
        if verbose:
            if options[82] == 0:
                prints.append("DMC HP with hover trick disabled")
            else:
                prints.append("DMC HP with hover trick enabled")


        #Zora with cucco
        options[83] = random.randint(0, 1)
        if verbose:
            if options[83] == 0:
                prints.append("Zora with cucco trick disabled")
            else:
                prints.append("Zora with cucco trick enabled")


        #Zora with hover
        options[84] = random.randint(0, 1)
        if verbose:
            if options[84] == 0:
                prints.append("Zora with hover trick disabled")
            else:
                prints.append("Zora with hover trick enabled")


        #Tunic
        options[85] = random.randint(0, 1)
        if verbose:
            if options[85] == 0:
                prints.append("Tunic requirements trick disabled")
            else:
                prints.append("Tunic requirements trick enabled")


        #Morpha golden scale
        options[86] = random.randint(0, 1)
        if verbose:
            if options[86] == 0:
                prints.append("Morpha with golden scale trick disabled")
            else:
                prints.append("Morpha with golden scale trick enabled")


        #lens
        lens = random.randint(0, 2)
        if lens == 0:
            options[87] = 0
            options[88] = 0
            if verbose:
                prints.append("Lens: required everywhere")

        elif lens == 1:
            options[87] = 1
            options[88] = 0
            if verbose:
                prints.append("Lens: wasteland and chest mini game")

        else:
            options[87] = 0
            options[88] = 1
            if verbose:
                prints.append("Lens: chest mini game only")


        #Skip Collapse
        options[20] = random.randint(0, 1)
        if verbose:
            if options[20] == 0:
                prints.append("Don't skip collapse")
            else:
                prints.append("Skip collapse")


        #Skip Guard
        options[21] = random.randint(0, 1)
        if verbose:
            if options[21] == 0:
                prints.append("Don't skip guard")
            else:
                prints.append("Skip guard")


        #Skip epona
        options[22] = random.randint(0, 1)
        if verbose:
            if options[22] == 0:
                prints.append("Skip epona race: disabled")
            else:
                prints.append("Skip epona race: enabled")


        #Fast Chest
        options[23] = random.randint(0, 1)
        if verbose:
            if options[23] == 0:
                prints.append("Normal chest cutscene")
            else:
                prints.append("Fast chest cutscene")



        #Random big poe
        options[24] = random.randint(0, 1)

        if options[24] == 0:
            poes = random.randint(1, 10)
            if poes == 1:
                options[25] = 0
                options[26] = 0
                options[27] = 0
                options[28] = 0
            elif poes == 2:
                options[25] = 1
                options[26] = 0
                options[27] = 0
                options[28] = 0
            elif poes == 3:
                options[25] = 0
                options[26] = 1
                options[27] = 0
                options[28] = 0
            elif poes == 4:
                options[25] = 1
                options[26] = 1
                options[27] = 0
                options[28] = 0
            elif poes == 5:
                options[25] = 0
                options[26] = 0
                options[27] = 1
                options[28] = 0
            elif poes == 6:
                options[25] = 1
                options[26] = 0
                options[27] = 1
                options[28] = 0
            elif poes == 7:
                options[25] = 0
                options[26] = 1
                options[27] = 1
                options[28] = 0
            elif poes == 8:
                options[25] = 1
                options[26] = 1
                options[27] = 1
                options[28] = 0
            elif poes == 9:
                options[25] = 0
                options[26] = 0
                options[27] = 0
                options[28] = 1
            else:
                options[25] = 1
                options[26] = 0
                options[27] = 0
                options[28] = 1
            if verbose:
                prints.append("Poes : " + str(poes))

        else:
            if verbose:
                prints.append("Poes : Random")

        #Scarecrow
        options[29] = random.randint(0, 1)
        if verbose:
            if options[29] == 0:
                prints.append("Don't start with scarecrow")
            else:
                prints.append("Start with scarecrow")


        #Songs notes random
        options[89] = random.randint(0, 1)
        if verbose:
            if options[89] == 0:
                prints.append("Normal song note")
            else:
                prints.append("Random song note")


        #Chest size
        options[90] = random.randint(0, 1)
        if verbose:
            if options[90] == 0:
                prints.append("Normal chest size")
            else:
                prints.append("Chest size matches with content")


        #Clearer hint
        options[91] = random.randint(0, 1)
        if verbose:
            if options[91] == 0:
                prints.append("Normal Hint")
            else:
                prints.append("Clearer hint")


        #Stones
        stones = random.randint(0, 2)
        if stones == 0:
            options[92] = 0
            options[93] = 0
            if verbose:
                prints.append("No hints")

        elif stones == 1:
            options[92] = 1
            options[93] = 0
            if verbose:
                prints.append("Hints : Mask of Truth")

        elif stones == 2:
            options[92] = 0
            options[93] = 1
            if verbose:
                prints.append("Hints : Stone of agony")

        else:
            options[92] = 1
            options[93] = 1
            if verbose:
                prints.append("Hints : Nothing")


        #Text shuffle
        text = random.randint(0, text_shuffle_max)
        if text == 0:
            options[94] = 0
            options[95] = 0
            if verbose:
                prints.append("No text shuffle")

        elif text == 1:
            options[94] = 1
            options[95] = 0
            if verbose:
                prints.append("Shuffle except key and hint")

        else:
            options[94] = 0
            options[95] = 1
            if verbose:
                prints.append("Text shuffle")


        #Difficulty
        diff = random.randint(0, difficulty_max)
        if diff == 0:
            options[96] = 0
            options[97] = 0
            if verbose:
                prints.append("Difficulty : Normal")

        elif diff == 1:
            options[96] = 1
            options[97] = 0
            if verbose:
                prints.append("Difficulty : Hard")

        elif diff == 2:
            options[96] = 0
            options[97] = 1
            if verbose:
                prints.append("Difficulty : Very hard")

        else:
            options[96] = 1
            options[97] = 1
            if verbose:
                prints.append("Difficulty : OHKO")

        printNext()

    main=Tk()

    main.geometry("700x250+500+300")

    main.title("RawZomizer "+ str(version.VERSION) +" : Setting String Randomizer for OoTR")

    name1 = Label(main, text="RawZomizer for " + version.DEV)
    name1.pack(side=TOP)

    WARNING = "Warning ! The OoTR " + version.DEV + " is developing ! May be incompatible"
    label = Label(main, text=WARNING)
    label.pack(side=TOP)

    name = Label(main, text="Created by RawZ. Thanks to Yanis and Touyet for the texts corrections")
    name.pack(side=BOTTOM)

    l = LabelFrame(main, text="Generate", padx=20, pady=20)
    l.pack(fill="both", expand="yes", side=LEFT)

    difficulty = StringVar(main)
    difficulty.set("OHKO")

    Label(l, text="Maximum Difficulty").grid(row=1, column=1)
    w1 = OptionMenu(l, difficulty, "Normal", "Hard", "Very Hard", "OHKO")
    w1.grid(row=1, column=2)

    text_shuffle = StringVar(main)
    text_shuffle.set("All text shuffled")

    Label(l, text="Maximum Text_shuffle").grid(row=2, column=1)
    w2 = OptionMenu(l, text_shuffle, "No text shuffled", "Shuffle excepted Hints and Keys", "All text shuffled")
    w2.grid(row=2, column=2)

    v = IntVar()
    rbutton = Checkbutton(l, text="Print options step by step", variable=v)
    rbutton.grid(row=4, column=1)

    button=Button(l, text="Generate", command=generateSeed)
    button.grid(row=5, column=1)

    l2 = LabelFrame(main, text="Result", padx=20, pady=20)
    l2.pack(fill="both", expand="yes", side=RIGHT)

    value = StringVar()
    value.set("")
    entry = Entry(l2, textvariable=value, width=30)
    entry.pack()

    label = Label(l2, text="")
    label.pack()

    button2=Button(l2, text="Next", command=printNext)
    button2.pack()

    button3=Button(l2, text="Copy settings", command=copy)
    button3.pack()

    main.mainloop()
