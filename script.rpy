label start:

scene bg opening

play sound "<from 1 to 15.5>writing.mp3"


x "Be wary of who you invest your energy into."

"You have the potential to be consumed, corrupted, and by the demons of others..."

stop sound fadeout 1.0

scene bg black

play music [ "theme.mp3" ] fadein 1.0

"My name is Risha."

define r = Character ("Risha", color="#ffcccc")
define m = Character("Sylvie", color="#c8ffc8")
define x = Character(_(""), color="#c8c8ff")

    risha animated:
        "risha normal.png"
        0.1
        "risha amazed.png"
        0.1
        "risha door.png"
        0.1
        repeat


r "I live with my mother, alone by the edge of Dark Forest."

scene bg forest
with fade

r "I don't know how long she's lived here, but I've lived here for the entirety of my fourteen years of living."

scene bg house
with fade

r "She keeps me inside, I rarely leave the house, except I'm allowed out once a week."

show mom normal at right

r "When my mother leaves to go get supplies, whether she knows it or not, I leave to go water my gift."

hide mom normal

show risha normal

image bg atl transitions:
    "bg house"
    "bg dads_room" with dissolve
    pause 1.0

r "Before I was born, my father left me and my mother. He had a room in the house he never allowed my mother to access."

scene bg dads_room
with fade

show mom normal:
    xalign .3 yalign .7
    linear 1.0 xalign .7 yalign .3
    linear 1.0 xalign .3 yalign .7
    repeat

r "Whenever she tried to open the door, it would never budge. She said it must've been rusted shut and it became a metaphor for his role in her life."

hide mom normal

show risha normal

r "But four years ago, I was able to open it. It was pure curiousity. But I turned the handle and entered my father's private room."

scene bg garden
with fade

r "It was an indoor garden. Most of the flora was dead already, but there were a few surviors."

show risha amazed at left

r "In particular, there was a tree sitting on a desk, sitting by a crack in the wall, surviving off the little sunlight and rain that squeezed through the gap."

show tree small at right

r "It was weak, small, but it was strong and it'd outlived all the other plants. It was a plain little tree with roots too big for it's pot."

r "Ugly, ugly roots."

r "I felt a connection..."

show risha amazed

scene bg feet

r "I was born with horrible feet. They're covered in blisters and are horribly swollen. I'm missing a toe on my left foot, and two on my right."
r "When I was younger, it never bothered me."

show risha youngsmiling

r "When I got older, they started to get worse and hurt more. Kids started torturing me, calling me Monster Toes..."

show risha young crying

r "It was harder and harder to live a normal child's life."

scene bg house

show mom talking
show risha youngcrying2 at right

m "I don't want you going outside anymore when I'm not around."
m "And you always have to ask first."
m "This world is cruel, and you're a target..."
m "Someone could snatch you away"

hide risha youngcrying
show risha youngsniffling

m "Promise me, you'll stay safe and stay inside..."
r "I promise, mama..."




    # This ends the game.

stop music fadeout 1.0
return
