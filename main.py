import random
import datetime
import tkinter as tk

####         settings               ###

date = datetime.datetime.now()

geo = "440x580+800+300"
bg = "#FFEFA4"
fg = "#A38600"
font = ""

#label1
l_width = 27
l_font = 20
#textBOX
t_font = 15
t_width = 39
#button2
b_width = 39
b_font = 15
#entery
e_width = 26
e_font = 17
#button1
b1_font = 14

first = 0
last = 100

cheat_mode = False
cheat_key1 = False
cheat_key2 = False
cheat_scor = False
helped = False
writing = True
pro_jpot = True
pro_jpot_hard = False
auto_bot = False

class start(object): # the class of the modes and the processing

    def __init__(self, fnum, lnum):
        self.fnum = fnum
        self.lnum = lnum

        global list, score, rnum, helped
        ##jpot##
        helped = False
        self.jpot_small_c = first
        self.jpot_great_c = last
        self.jpot_small = first
        self.jpot_great = last

        self.jpot_list = []
        ##jpot##
        list = [" + ", " - "]

        self.rnum = random.randint(self.fnum, self.lnum)
        # print(self.rnum)
        score = 100
        global p100, p95, p90, p85, p80, p75, p70, p65, p60, p55, p50, p45, p40, p35, p30, p25, p20, p15, p10, p05
        p100 = last
        p95 = int((95 / 100) * last)
        p90 = int((90 / 100) * last)
        p85 = int((85 / 100) * last)
        p80 = int((80 / 100) * last)
        p75 = int((75 / 100) * last)
        p70 = int((70 / 100) * last)
        p65 = int((65 / 100) * last)
        p60 = int((60 / 100) * last)
        p55 = int((55 / 100) * last)
        p50 = int((50 / 100) * last)
        p45 = int((45 / 100) * last)
        p40 = int((40 / 100) * last)
        p35 = int((35 / 100) * last)
        p30 = int((30 / 100) * last)
        p25 = int((25 / 100) * last)
        p20 = int((20 / 100) * last)
        p15 = int((15 / 100) * last)
        p10 = int((10 / 100) * last)
        p05 = int( (5 / 100) * last)
        if p20 > 1000:
            p100 = 1000
            p95 = int((95 / 100) * p100)
            p90 = int((90 / 100) * p100)
            p85 = int((85 / 100) * p100)
            p80 = int((80 / 100) * p100)
            p75 = int((75 / 100) * p100)
            p70 = int((70 / 100) * p100)
            p65 = int((65 / 100) * p100)
            p60 = int((60 / 100) * p100)
            p55 = int((55 / 100) * p100)
            p50 = int((50 / 100) * p100)
            p45 = int((45 / 100) * p100)
            p40 = int((40 / 100) * p100)
            p35 = int((35 / 100) * p100)
            p30 = int((30 / 100) * p100)
            p25 = int((25 / 100) * p100)
            p20 = int((20 / 100) * p100)
            p15 = int((15 / 100) * p100)
            p10 = int((10 / 100) * p100)
            p05 = int((5 / 100) * p100)

    def gusee(self): # when the player click the button

        global list, gnum, first, last

        first = self.fnum
        last = self.lnum

        gnum = e1.get()

        global score, cheat_mode, losing_count, win_count
        try:
            int(gnum)
        except:
            insert("THAT IS NOT A NUMBER!")
            e1.delete(0, "end")
            if play(r"sounds/wrong.wav") == False:
                return False
            if score <= 0:
                insert("You LOST!\nYou reached 0 points D:\n\nYou can start guessing " + user_id + "!\nOr enter a user name then select a game mode")
                losing_count += 1
                score_list.append(0)

                global cheat_mode
                if cheat_mode == True:
                    insert(", try " + str(self.rnum) + " [;", False, "end")
                if play(r"sounds/lost.mp3") == False:
                    return False
                e1.delete(0, "end")
                self.__init__(first, last)
            return False
        global diff
        diff = int(gnum) - self.rnum
        # print("diff:", diff)
        if diff < 0:
            diff *= -1
        diff = ((diff * 100) / last) / 5
        if diff <= 0:
            diff += 1
        if score <= 0:
            insert("You LOST!\nYou reached 0 points D:\n\nYou can start guessing " + user_id + "!\nOr enter a user name then select a game mode")
            losing_count += 1
            score_list.append(0)
            if cheat_mode == True:
                insert(", try " + str(self.rnum) + " [;", False, "end")
            if play(r"sounds/lost.mp3") == False:
                return False
            e1.delete(0, "end")
            self.__init__(first, last)
            return False

        elif int(gnum) == self.rnum or int(gnum) == self.rnum + 1 or int(gnum) == self.rnum - 1:
            if play(r"sounds/won.wav") == False:
                return False
            insert("You WON!!!, Your score is: "+ str(score))
            if mode == ez:
                mo = "Easy"
            elif mode == normal:
                mo = "Normal"
            elif mode == hard:
                mo = "Hard"
            else:
                mo = "Error"
            ####      ADDITIONAL     ####
            if auto_bot == True:
                score_list.append(score)
                win_count += 1
            ####      ADDITIONAL     ####

            insert("\n"+mo+" mode " + str(first) + " to " + str(last) + " " + "\nYou can start guessing " + user_id + "!\n\nOr enter a user name then select a game mode", False, "end")
            if cheat_mode == True:
                insert(", try " + str(self.rnum) + " [;", False, "end")
            if score < 100:
                str_score = "0" + str(score)
            else:
                str_score = score
            try:
                secret_key = ""
                if cheat_mode == True:
                    secret_key = " CHEATER!!!"
                if helped == True:
                    secret_key += " Helped by Computer"
                if writing == True:
                    fi1 = open(r"files\results_0.txt", "a")
                    fi1.write(str(user_id) + secret_key + "\n" + str(date.year) + "/" + str(date.month) + "/" + str(date.day) + " " + str(date.hour) + ":"
                              + str(date.minute) + " " + str(mo) + " mode " + str(first) + " to " + str(last) + " " + str(str_score) + " points\n")
                    fi1.close()

            except:
                insert("Missing files, Pls re-install the game!")
                return False

            e1.delete(0, "end")
            self.__init__(first, last)

        elif mode == ez:
            score -= int(diff)
            score -= 1
            if self.lost() == False:
                return False
            ez.pro(p95, p100, p10)
            if tr == False:
                ez.pro(p90, p95, p10)
                if tr == False:
                    ez.pro(p85, p90, p10)
                    if tr == False:
                        ez.pro(p80, p85, p10)
                        if tr == False:
                            ez.pro(p75, p80, p10)
                            if tr == False:
                                ez.pro(p70, p75, p10)
                                if tr == False:
                                    ez.pro(p65, p70, p10)
                                    if tr == False:
                                        ez.pro(p60, p65, p10)
                                        if tr == False:
                                            ez.pro(p55, p60, p10)
                                            if tr == False:
                                                ez.pro(p50, p55, p10)
                                                if tr == False:
                                                    ez.pro(p45, p50, p10)
                                                    if tr == False:
                                                        ez.pro(p40, p45, p10)
                                                        if tr == False:
                                                            ez.pro(p35, p40, p10)
                                                            if tr == False:
                                                                ez.pro(p30, p35, p10)
                                                                if tr == False:
                                                                    ez.pro(p25, p30, p10)
                                                                    if tr == False:
                                                                        ez.pro(p20, p25, p10)
                                                                        if tr == False:
                                                                            ez.pro(p15, p20, p10)
                                                                            if tr == False:
                                                                                ez.pro(p10, p15, p10)
                                                                                if tr == False:
                                                                                    ez.pro(p05, p10, p10)
                                                                                    if tr == False:
                                                                                        ez.pro(0, p05, p100)

                                                                                        if tr == False:
                                                                                            score += int(diff)
                                                                                            score += 1
                                                                                            self.gusee()


        elif mode == normal:
            score -= int(diff)
            score -= 1
            if self.lost() == False:
                return False
            normal.pro()
        elif mode == hard:
            score -= int(diff)
            score -= 1
            if self.lost() == False:
                return False
            hard.pro()

    def pro(self, f_num = first, l_num = last, ran = 999): # processing

        global tr

        self.ran = ran

        if int(gnum) != self.rnum:

            self.jpot_list.append(int(gnum))
            self.jpot_list.append(int(gnum) + 1)
            self.jpot_list.append(int(gnum) - 1)

            temp_list = []

            for j in self.jpot_list:
                if j not in temp_list:
                    temp_list.append(j)

            self.jpot_list = temp_list

            if play(r"sounds/wrong.wav") == False:
                return False
            global i
            i = 0

            for i in range(self.ran):
                global cheat_mode, clue_result
                clue = str(gnum) + str(random.choice(list)) + str(random.randint(f_num, l_num))
                clue_result = eval(clue)
                # print(clue_result)
                # global score
                if self == hard and clue_result < int(self.rnum) and last > clue_result > 0:
                    insert("You guessed " + gnum + "\n\nBut the number is greater than " + str(clue_result) + "\n\nYour Score is: " + str(score))
                    e1.delete(0, "end")
                    tr = True
                    if cheat_mode == True:
                        insert(", try "+str(self.rnum)+" [;", False, "end")
                    self.jpot_small = clue_result
                    break

                elif self == hard and clue_result > int(self.rnum) and last > clue_result > 0:
                    insert("You guessed " + gnum + "\n\nbut the number is smaller than " + str(clue_result) + "\n\nYour Score is: " + str(score))
                    e1.delete(0, "end")
                    tr = True
                    if cheat_mode == True:
                        insert(", try "+str(self.rnum)+" [;", False, "end")
                    self.jpot_great = clue_result
                    break

                elif clue_result < int(self.rnum) and clue_result > int(gnum):
                    insert("You guessed " + gnum + "\n\nBut the number is greater than " + str(clue_result) + "\n\nYour Score is: " + str(score))
                    e1.delete(0, "end")
                    tr = True
                    if cheat_mode == True:
                        insert(", try "+str(self.rnum)+" [;", False, "end")
                    self.jpot_small = clue_result
                    break

                elif clue_result > int(self.rnum) and clue_result < int(gnum):
                    insert("You guessed " + gnum + "\n\nbut the number is smaller than " + str(clue_result) + "\n\nYour Score is: " + str(score))
                    e1.delete(0, "end")
                    tr = True
                    if cheat_mode == True:
                        insert(", try "+str(self.rnum)+" [;", False, "end")
                    self.jpot_great = clue_result
                    break
            else:
                tr = False

    def lost(self): # loosing shortcut
        global score, losing_count
        if score <= 0:
            insert("You LOST!\nYou reached 0 points D:\n\nYou can start guessing " + user_id + "!\nOr enter a user name then select a game mode")
            losing_count += 1
            score_list.append(0)
            global cheat_mode
            if cheat_mode == True:
                insert(", try " + str(self.rnum) + " [;", False, "end")
            if play(r"sounds/lost.mp3") == False:
                return False
            e1.delete(0, "end")
            self.__init__(first, last)
            return False

    def jpot(self): # the computer help thing (it's pretty good tbh :D )
        global helped, auto_bot, pro_jpot

        if self == hard:
            pro_jpot = False
            if pro_jpot_hard == True:
                pro_jpot = True

        if pro_jpot == True:

            try:
                global diff, score, gnum

                r_score = score
                r_score += 1
                r_score += int(diff)
                # print("r_score:", r_score)
                r_diff = score + 1
                r_diff = r_score - r_diff
                # print("diff:", diff)
                # print("r_diff:", r_diff)
                r_diff = ((r_diff * 5) * last) / 100
                r_diff = int(r_diff)

                # print("r_diff:", r_diff)

                if int(gnum) < clue_result:
                    dx = r_diff + int(gnum)
                elif int(gnum) > clue_result:
                    dx = r_diff + -(int(gnum))

                if dx < 0:
                    dx = dx * -1
                # print("dx:", dx)
                self.jpot_great_c = dx + ((last * 5) / 100)
                self.jpot_small_c = dx - ((last * 5) / 100)

            except:
                # print("fail")
                pass

        try:
            if self.jpot_great < self.jpot_great_c:

                self.jpot_great_c = self.jpot_great

            if self.jpot_small > self.jpot_small_c:

                self.jpot_small_c = self.jpot_small
        except:
            pass

        jpot_result = random.randint(int(self.jpot_small_c), int(self.jpot_great_c))
        # print(jpot_result)
        for i in self.jpot_list:
            if i == jpot_result:
                return False
        # print(self.jpot_small_c, self.jpot_great_c)
        self.jpot_list.sort()
        # print(self.jpot_list)

        e1.delete(0, "end")
        if score == 100:
            jpot_result = int(last / 2)
        e1.insert(0, str(jpot_result))
        if auto_bot == True:
            b1.invoke()
        helped = True
        return True

####        funcs                   ###

ez = start(first, last)
normal = start(first, last)
hard = start(first, last)
mode = normal

def ez_mode(): # when easy mode is clicked
    ez.__init__(first, last)
    ez_rnum = ez.rnum
    secret_key = ""
    if play(r"sounds/ez.wav") == False:
        return False
    global mode, user_id, cheat_mode
    mode = ez
    user = e1.get()
    user_id = str(user)

    # things to activate the cheating mode
    if user_id == "ACTIVATE" and cheat_key1 == True and cheat_key2 == True:
        cheat_mode = True
        secret_key = " [;;; "
    if user_id == "DEACTIVATE" and cheat_key1 == True and cheat_key2 == True:
        cheat_mode = False
        secret_key = " ]; "
    ###
    e1.delete(0, "end")
    insert("Easy mode!, start guessing "+user_id+secret_key+"!\n\nFrom " + str(first) + " to " + str(last))
    if cheat_mode == True:
        insert(", try " + str(ez_rnum) + " [;", False, "end")
def nor_mode(): # when normal mode is clicked
    normal.__init__(first, last)
    normal_rnum = normal.rnum
    if play(r"sounds/normal.wav") == False:
        return False
    global mode, user_id
    mode = normal
    user = e1.get()
    user_id = str(user)
    e1.delete(0, "end")
    insert("Normal mode!, start guessing "+user_id+"!\n\nFrom " + str(first) + " to " + str(last))
    global cheat_mode
    if cheat_mode == True:
        insert(", try " + str(normal_rnum) + " [;", False, "end")
def har_mode(): # when normal mode is clicked
    hard.__init__(first, last)
    hard_rnum = hard.rnum
    if play(r"sounds/hard.wav") == False:
        return False
    global mode, user_id
    mode = hard
    user = e1.get()
    user_id = str(user)
    e1.delete(0, "end")
    insert("Hard mode!, start guessing "+user_id+"!\n\nFrom " + str(first) + " to " + str(last))
    global cheat_mode
    if cheat_mode == True:
        insert(", try " + str(hard_rnum) + " [;", False, "end")
def get(): # when leaderboard mode is clicked
    if play(r"sounds/leader.wav") == False:
        return False
    try:

        fi1 = open(r"files\results_0.txt", "r")
        insert(fi1.read())
        fi1.close()
    except:
        insert("Missing files, Pls re-install the game!\n\n(text file)")
        return False
    e1.delete(0, "end")
def hot(): # useless func with sus name just to invoke the button
    b1.config(relief="sunken")
    root.update_idletasks()
    b1.invoke()
    b1.config(relief="raised")
def l100(): # when "Set!" is clicked
    secret_key = ""
    global cheat_key1, cheat_key2, cheat_mode, cheat_scor, pro_jpot, pro_jpot_hard

    # some cheat mode things
    if e2.get() == "#CHEAT%$)!":
        cheat_key1 = True
        secret_key = " [;"
    if e2.get() == "#CHEAT%$)@" and cheat_key1 == True:
        cheat_key2 = True
        secret_key = " [;;"
    if e2.get() == "#SCORE@EDIT" and cheat_mode == True and cheat_scor == False:
        cheat_scor = True
        secret_key = " <___<"
    elif e2.get() == "#SCORE@EDIT" and cheat_mode == True and cheat_scor == True:
        cheat_scor = False
        secret_key = " >___>"
    if e2.get() == "#pro_jpot" and pro_jpot == True:
        pro_jpot = False
        secret_key = "\npro_jpot is off"
    elif e2.get() == "#pro_jpot" and pro_jpot == False:
        pro_jpot = True
        secret_key = "\npro_jpot is on"
    if e2.get() == "#pro_jpot_hard" and pro_jpot_hard == True:
        pro_jpot_hard = False
        secret_key = "\npro_jpot_hard is off"
    elif e2.get() == "#pro_jpot_hard" and pro_jpot_hard == False:
        pro_jpot_hard = True
        secret_key = "\npro_jpot_hard is on"
    ###

    try:
        int(e2.get())
    except:
        insert("THAT IS NOT A NUMBER!" + secret_key)
        e2.delete(0, "end")
        if play(r"sounds/wrong.wav") == False:
            return False
        return False
    if int(e2.get()) <= 0:
        insert("YOU CAN NOT SET IT LOWER THAN 1!" + secret_key)
        e2.delete(0, "end")
        if play(r"sounds/wrong.wav") == False:
            return False
        return False

    # some cheat mode things
    if cheat_mode == True and cheat_scor == True:
        global score
        score = int(e2.get())
        e2.delete(0, "end")
        if play(r"sounds/leader.wav") == False:
            return False
        return score
    ###

    ran = int(e2.get())
    if mode == ez:
        mo = "Easy"
    elif mode == normal:
        mo = "Normal"
    elif mode == hard:
        mo = "Hard"
    else:
        mo = "Error"
    if ran < 101:
        if play(r"sounds/ez.wav") == False:
            return False
    elif ran < 501:
        if play(r"sounds/normal.wav") == False:
            return False
    elif ran >= 501:
        if play(r"sounds/hard.wav") == False:
            return False
    global last
    last = ran
    ez.__init__(0, last)
    normal.__init__(0, last)
    hard.__init__(0, last)
    insert("Range set: from 0 to " + str(last) + "!\n\n" + mo + " mode!, start guessing " + user_id + "!")

    # more cheat mode things
    if cheat_mode == True:
        current_rnum = ""
        if mode == ez:
            current_rnum = str(ez.rnum)
        elif mode == normal:
            current_rnum = str(normal.rnum)
        elif mode == hard:
            current_rnum = str(hard.rnum)

        insert(", try " + current_rnum + " [;", False, "end")
    ###

    e2.delete(0, "end")
def e_delete(event=None): # just to make the gui works
    e1.delete(0, "end")
def e_invoke(event=None): # just to make the gui works
    b1.invoke()
def e2_invoke(event=None): # just to make the gui works
    b6.invoke()

t_mode = 1 # not sure what that is but i'll just keep it

user_id = "Unnamed"

def jpot(): # sometimes the bot can't find a good number and he runs out of attempts, so i had to make hem try more
    while True:
        if mode.jpot() == True:
            break
        else:
            mode.jpot()

####         GUI                    ###


root = tk.Tk()
root.config(bg="lightyellow")
root.title("Guess Game")
root.resizable(0, 0)
root.geometry(geo)

l1 = tk.Label(root, text="Guess game", bg="#F5DB66", width=l_width, fg=fg, font=(font, l_font))
l1.grid(column=1, row=10, columnspan=4, rowspan=1, padx=1, pady=0)

t1 = tk.Text(root, bg=bg, width=t_width, height=5, fg="#615B40", font=(font, t_font), state="disabled", bd=3)
t1.grid(column=1, row=20, columnspan=4, rowspan=1, padx=1, pady=10)

b1 = tk.Button(root, bg=bg, fg=fg, font=(font, b1_font), text="Guess!", bd=2, command= lambda: mode.gusee())
b1.grid(column=4, row=30, columnspan=1, rowspan=1, padx=0, pady=3)

e1 = tk.Entry(root, bg=bg, width=e_width, fg=fg, font=(font, e_font), bd=4)
e1.grid(column=1, row=30, columnspan=3, rowspan=1, padx=1, pady=5)
# keyboard.add_hotkey("Enter", lambda: hot())
e1.insert(0, "Type here")
e1.bind("<Return>", e_invoke)
e1.bind("<Button-1>", e_delete)

l3 = tk.Label(root, text="Select the game mode", bg="#F5DB66", width=b_width, fg=fg, font=(font, b_font))
l3.grid(column=1, row=40, columnspan=4, rowspan=1, padx=1, pady=6)

b2 = tk.Button(root, bg=bg, fg=fg, font=(font, b_font), text="Easy mode", bd=2, width=b_width, command= lambda: ez_mode())
b2.grid(column=1, row=50, columnspan=4, rowspan=1, padx=0, pady=2)

b3 = tk.Button(root, bg=bg, fg="#786200", font=(font, b_font), text="Normal mode", bd=2, width=b_width, command= lambda: nor_mode())
b3.grid(column=1, row=60, columnspan=4, rowspan=1, padx=0, pady=1)

b4 = tk.Button(root, bg=bg, fg="#554500", font=(font, b_font), text="Hard mode", bd=2, width=b_width, command= lambda: har_mode())
b4.grid(column=1, row=70, columnspan=4, rowspan=1, padx=0, pady=1)

b5 = tk.Button(root, bg=bg, fg=fg, font=(font, b_font), text="Leaderboard", bd=2, width=b_width, command= lambda: get())
b5.grid(column=1, row=110, columnspan=4, rowspan=1, padx=0, pady=3)

l2 = tk.Label(root, text="Set the guess range (default is 100)", bg="#F5DB66", width=b_width, fg=fg, font=(font, b_font))
l2.grid(column=1, row=90, columnspan=4, rowspan=1, padx=1, pady=6)

# b6 = tk.Button(root, bg=bg, fg=fg, font=(font, b_font), text="0 - 100", bd=2, width=int((b_width / 3.5) - 1), command= lambda: l100(100))
# b6.grid(column=1, row=10,columnspan=1, rowspan=1, padx=1, pady=1)
#
# b7 = tk.Button(root, bg=bg, fg="#786200", font=(font, b_font), text="0 - 500", bd=2, width=int((b_width / 3.5) - 1), command= lambda: l100(500))
# b7.grid(column=2, row=10, columnspan=1, rowspan=1, padx=1, pady=1)
#
# b8 = tk.Button(root, bg=bg, fg="#554500", font=(font, b_font), text="0 - 1000", bd=2, width=int((b_width / 3.5) - 1.5), command= lambda: l100(1000))
# b8.grid(column=3, row=10, columnspan=1, rowspan=1, padx=1, pady=1)

b6 = tk.Button(root, bg=bg, fg=fg, font=(font, b1_font), text="Set!", bd=2, command= lambda: l100(), width=6)
b6.grid(column=4, row=100, columnspan=1, rowspan=1, padx=0, pady=3)

e2 = tk.Entry(root, bg=bg, width=e_width, fg=fg, font=(font, e_font), bd=4)
e2.grid(column=1, row=100, columnspan=3, rowspan=1, padx=1, pady=5)
e2.bind("<Return>", e2_invoke)

b7 = tk.Button(root, bg=bg, fg=fg, font=(font, b_font), text="Computer Help", bd=2, width=b_width, command= lambda: jpot())
b7.grid(column=1, row=31, columnspan=4, rowspan=1, padx=0, pady=3)

####         some shortcut funcs    ###


def insert(text, dele = True, start_in = "0.0"): # to insert something in the text box easier
    t1.config(state="normal")
    if dele == True:
        t1.delete(0.0, "end")
    t1.insert(start_in, text)
    t1.config(state="disabled")
def play(file): # to play a sound file easier
    try:
        # will do nothing for now
        pass
    except:
        insert("Missing files, Pls re-install the game!\n\n(sound file)")
        return False

insert("Enter a user name then\n\nSelect a game mode") # like this instead of all those lines

def Average(lst): # for the auto jpot bot (it's not even a bot)
    try:
        return sum(lst) / len(lst)
    except:
        pass

####         auto jpot bot          ###


#basically it's make the bot solves the game multiple times (it's fun to see the possibilities of the bot
#it has 99% (100% after some improvements) win rate in a guess between 0 and 1,000,000,000 (1 * 10^9) and u can some other numbers down)
#if u want to activate it just remove the comment "#"
score_list = []  # keep this active (DO NOT COMMENT IT)

# writing = False # this will turn off the leaderboard
# pro_jpot = True # if true the bot will be smarter, false will be normal
# auto_bot = True
# win_count = 0
# losing_count = 0
# mode = normal #select the game mode by typing it in here (ez - normal - hard)
# ### IMPORTANT: DO NOT USE HARD MODE WITH PRO_JPOT
#
# last = 1 * 10**21 #here is the last number in the guess (0 to the last number)
# mode.__init__(first, last)
#
# while (win_count + losing_count) < 100: #edit the "500" to how much times you want the bot to solve the game
#     b7.invoke()
# else:
#     score_list.sort()
#     print(score_list)
#     print("Avrage           : ", Average(score_list))
#     print("Wining count     : ", win_count)
#     print("losing count     : ", losing_count)
#     print("win rate         : ", (win_count * 100) / (losing_count + len(score_list)))
#
# #notes:
# #last             100 | 1m | 10^9    | 10^21  | 10^24   | 10^27      | 10^30       |
# #hard    Avrage = 73  | 57 | 43 98%  | 2  12% | 0.2 2%  | 0.004 0.1% | 0     0.00% |
# #normal  Avrage = 85  | 63 | 50 99%  | 3  21% | 0.8 6%  | 0.042 0.4% | 0     0.00% |
# #easy    Avrage = 88  | 69 | 56 100% | 6  39% | 1.3 10% | 0.102 1.1% | 0.002 0.05% |
#
# #after imporvment  100 |   | 10^9    |        |         |            |             |
# #hard     Avrage = 75  |   | 48 100% |        |         |            |             |
# #normal   Avrage = 88  |   | 56 100% |        |         |            |             |
# #easy     Avrage = 91  |   | 60 100% |        |         |            |             |
#
# #pro jpot          100 |   | 10^9    |        |         |            | 10^30       |
# #hard (not sure Y but it gives a lot of errors when pro_jpot is True so i disabled it)
# #normal   Avrage = 93  |   | 64 100% |        |         |            | 0.016 0.2%  |
# #easy     Avrage = 91  |   | 70 100% |        |         |            | 0.03  0.3%  |
#


root.mainloop()
