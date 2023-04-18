import sqlite3
import random as rd
import prenoms as pr

con = sqlite3.connect("BDD_joueurs.db")

cur = con.cursor()

cur.execute("CREATE TABLE joueurs(id, prénom, nom, poste, note)")
cur.execute("CREATE TABLE reserve_joueurs(id, prénom, nom, poste, note)")

data = []
for i in range(1, 25):
    data.append((i, pr.get_prenom(), pr.get_nom(), "Attaquant", rd.randint(20, 100)))
for i in range(25, 49):
    data.append((i, pr.get_prenom(), pr.get_nom(), "Défenseur", rd.randint(20, 100)))
for i in range(49, 81):
    data.append((i, pr.get_prenom(), pr.get_nom(), "Milieu", rd.randint(20, 100)))
for i in range(81, 89):
    data.append((i, pr.get_prenom(), pr.get_nom(), "Gardien", rd.randint(20, 100)))

cur.executemany("INSERT INTO joueurs VALUES(?, ?, ?, ?, ?)", data)
con.commit()
cur.executemany("INSERT INTO reserve_joueurs VALUES(?, ?, ?, ?, ?)", data)
con.commit()

# for ligne in cur.execute("SELECT * FROM joueurs"):
#     print(type(ligne[0]))

# n = [1]
# a = cur.execute("SELECT * FROM reserve_joueurs WHERE poste == 'Défenseur'")
# j = a.fetchall()
# print(j)
# j1 = j[23][4]
# print(j1)

# attaquant = cur.execute("SELECT * FROM reserve_joueurs WHERE poste == 'Attaquant' ORDER BY random() LIMIT 3")
# at = attaquant.fetchall()
# print(at)
# for j in at:
#     cur.execute("DELETE FROM reserve_joueurs WHERE id == (?)", [j[0]])
# a = cur.execute("SELECT * FROM reserve_joueurs WHERE poste == 'Attaquant'")
# print(a.fetchall())


