import tkinter as tk
import random


window = tk.Tk()
window.title("Python Speed Typing Test")
window.geometry("900x800")
window.config(background="#d3d3d3")


play_button = tk.PhotoImage(file="play-button.png")

options = ["this is a simple paragraph that is meant to be nice and easy to type which is why there will be mommas no "
           "periods or any capital letters so i guess this means that it cannot really be considered a paragraph but "
           "just a series of run on sentences this should help you get faster at typing as im trying not to use too "
           "many difficult words in it although i think that i might start making it hard by including some more "
           "difficult letters I'm typing pretty quickly so forgive me for any mistakes i think that i will not just "
           "tell you a story about the time i went to the zoo and found a monkey and a fox playing together they were "
           "so cute and i think that they were not supposed to be in the same cage but they somehow were and i loved "
           "watching them horse around forgive the pun well i hope that it has been highly enjoyable typing this "
           "paragraph and i wish you the best of luck getting the best score that you possibly can",
           "Discipline is the first thing which all citizens of a country must imbibe and inculate in their day to day life. In the modern era youths are generally inclined to be swayed by the sentiments and passions of a luxurious life so that they could have all the amenities and facilities of a rich person. They would like to have a spacious bungalow, a new modern looking car; lot of currency notes and no check or hindrance upon their day to day activities. In other words, they want to have all the rights but no duties. If there were no checks upon the member of a society, entire fabric or structure of society is likely to crumble down like a pack of cards. It is only the laws and the rules which bind the citizens of a country or other persons residing in it remain within certain specified limits and no to exceed beyond these boundaries in which they are expected to confine themselves. Discipline is the other name of self-imposition of certain limitations laid down by the social principles, precedents, financial curbs, ethical and religious limits and environmental checks, for example, a student in a college must obey his teachers & Principle from time to time. A student is expected to behave upto others as he would expect others to behave with him. Similarly, a student has to bear in mind that his parents have got him admitted to the college with the object of getting him properly educated in a specified line. If he maintains discipline in the college and attends his classes regularly and does not disobey the set rules and guide-lines, then he would definitely achieve the desired goal. But if he fails to catch up with the set principles, he would no reach the destination.",
           "Some frogs were traveling through woods and two of them accidentally fell into a pit. The other frogs which were safe upside understood how deep the pit was and saw no hope for the frogs to escape out of it. Both of these frogs started trying to get out of the pit but failed many times. The frogs on the safe side shouted at them to give up the pain of trying as it was not possible. Eventually, one frog heard the other frogs and decided to stop trying and fell down to death. However, the other frog went on trying and at last managed to reach the top. The other frogs asked him, Did you not hear us? He explained that he was deaf and thought other frogs were encouraging him to get out.",
           "Once upon a time, a merchant named Sam owed a huge sum of money to Tom, a money lender. The time came when the merchant ran out of the last chance given to him to give the money back. Sam had a beautiful daughter who was very affectionate with her father. Tom asked the merchant to give all the money back failing which he will marry his beautiful daughter. Tom was not at all good looking and ill minded and so the merchant was in dilemma. Tom proposed a new condition. There was a mix of black and white pebbles on the ground where they were standing. He will take two pebbles on both hands, one will be white and the other will be black. If the daughter correctly chooses the white pebble, then Tom will write off all the debt and leave the marriage proposal too. But if she chooses the black pebble, he will write off the debt but will marry the daughter."]


# Creates a screen to display the game and make sure the user is ready to begin.
def start_screen():
    global start_button, start_text
    start_button = tk.Label(window, image=play_button, border=0, background="#d3d3d3", activebackground="#d3d3d3")
    start_button.place(height=316, width=316, x=450, y=400, anchor="center")
    start_text = tk.Label(text="Welcome to my first ever Python Speed Typing Tester.\n\n"
                               "To begin, merely get yourself ready and "
                               "press the enter key.\n"
                               "Good luck, and lets see how fast you can type!", background="#d3d3d3",
                          font=("Arial", 14))
    start_text.place(x=450, y=150, anchor="center")
    window.bind('<Return>', game_start)


# This selects the paragraph to type and automatically selects the text box.
def game_start(event):
    global typing_box, text_window, speed_paragraph, selection
    start_button.destroy()
    start_text.destroy()
    window.unbind('<Return>')
    text_window = tk.Frame(window, cursor="target")
    text_window.place(height=450, width=850, x=450, y=250, anchor="center")
    selection = random.choice(options)
    speed_paragraph = tk.Label(window, text=selection, wraplength=800, font=("Arial", 14))
    speed_paragraph.place(x=450, y=250, anchor="center")
    typing_box = tk.Text(window, height=10, width=100)
    typing_box.place(x=450, y=600, anchor="center")
    typing_box.focus()
    typing_box.after(60000, figure_wpm)


#This takes in the typed information, compares it to the selection, and tells you how many words were successfully typed.
def figure_wpm():
    global start_again
    typed = typing_box.get("1.0","end")
    total_words = typed.split()
    selection_split = selection.split()
    correct_words = []
    for x in total_words:
        if x in selection_split:
            correct_words.append(x)
    wpm = len(correct_words)
    start_again = tk.Button(text=f"Congratulations! You typed at a speed of {wpm} words per minute! "
                                f"\nPress this button if you'd like to start again!", background="#d3d3d3",
                           font=("Arial", 14), command=reset)
    start_again.place(x=400, y=750, anchor="center")


# This will reset the board and take up back to the beginning.
def reset():
    start_again.destroy()
    typing_box.destroy()
    text_window.destroy()
    speed_paragraph.destroy()
    start_screen()


start_screen()

window.mainloop()