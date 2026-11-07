import tkinter as tk
personnes = {
    "oli":{"masse creuset":32.2469,"masse creuset AgCl":32.8468,"masse inconnu": 0.3002,"inconnu": "A"
    },
    "malik":{"masse creuset":30.5851,"masse creuset AgCl":31.0764,"masse inconnu": 0.3008,"inconnu": "D"
    },
    "lp":{"masse creuset":30.3884,"masse creuset AgCl":31.0931,"masse inconnu": 0.3005,"inconnu": "D"}}
def boucle(frame,inde,y):
    l = 0
    for i in personnes:
        entre(frame, personnes[i][inde], l + 1, y)
        l += 1

def entre(frame:tk.Frame,text:str,x:int,y:int):
    ent = tk.Entry(frame)
    ent.insert(tk.END, text)
    ent.grid(column=x, row=y)

def trouver(p:dict):
    # X + Y = masse mélange inconnu
    # Y(masse nacl) = masse mélange inconnu - X
    mmkcl =  74.551
    mmnacl = 58.44
    mmagcl = 143.321
    p["masse AgCl"] = float(f"{p["masse creuset AgCl"] - p["masse creuset"]:.5g}")
    p["masse NaCl"] = abs(float(f"{((p["masse AgCl"]/mmagcl)-(p["masse inconnu"]/mmkcl))/((1/mmnacl)-(1/mmkcl)):.3g}"))
    p["masse KCl"] = float(f"{p["masse AgCl"] - p["masse NaCl"]:.3g}")
    p["% KCl"] = float(f"{p["masse KCl"]/p["masse AgCl"]*100:.3g}")
    p["% NaCl"] = float(f"{p["masse NaCl"]/p["masse AgCl"]*100:.3g}")
    return p


def main():
    root = tk.Tk()
    root.geometry("700x160")

    frame =  tk.Frame(root)
    frame.pack()
    for personne in personnes:
        personnes[personne] = trouver(personnes[personne])
        print(personnes[personne])

    ent = tk.Entry(frame)
    ent.insert(tk.END, "Tableau #1: Masses et pourcentages de Kcl et Nacl obtenu dans la réaction de chlorure")
    ent.grid(rowspan=1,columnspan=4,column=0,row=0,sticky="ew")
    l = 0
    for i in personnes:

        ent = tk.Entry(frame)
        ent.insert(tk.END, i)
        ent.grid(column=l+1,row=1)
        l += 1
    entre(frame,"Masse AgCl(±0.0001g)",0,2)
    boucle(frame, "masse AgCl", 2)
    entre(frame,"Masse Kcl(±0.001g)",0,3)
    boucle(frame,"masse KCl",3)
    entre(frame, "Masse NaCl(±0.001g)", 0, 4)
    boucle(frame, "masse NaCl", 4)
    entre(frame,"% Kcl dans mélange",0,5)
    boucle(frame,"% KCl",5)
    entre(frame,"% NaCl dans mélange",0,6)
    boucle(frame,"% NaCl",6)
    entre(frame,"inconnu",0,7)
    boucle(frame,"inconnu",7)









    root.mainloop()


main()
