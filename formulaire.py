import tkinter as tk
import ttkbootstrap as ttk
from tkinter import *
from datetime import datetime
import sqlite3


root = Tk()
root.title('Fiche d\'inscription')
root.geometry('800x800')

# Connexion à la base de données
connexion = sqlite3.connect("utilisateurs.db")
curseur = connexion.cursor()

# Création de la table 'utilisateurs' s'il n'existe pas
curseur.execute("""
    CREATE TABLE IF NOT EXISTS utilisateurs (
        nom TEXT,
        prenom TEXT,
        email TEXT,
        nationalite TEXT,
        date_naissance DATE,
        filiere TEXT,
        sexe TEXT
    )
""")
connexion.commit()

# Fonction appelée lors de la soumission du formulaire
def soumettre_formulaire():
    # Récupération des valeurs saisies dans les champs
    nom = e_nom.get()
    prenom = e_prenom.get()
    email = e_mail.get()
    nationalite = e_nationalite.get()
    date_naissance = datetime.strptime(champ_date_naissance.get(), "%m/%d/%Y").date()
    filiere = efiliere.get()
    sexe = valeur_sexe.get()

    # Insertion des données dans la base de données
    curseur.execute("INSERT INTO utilisateurs VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (nom, prenom, email, nationalite, date_naissance, filiere, sexe))
    connexion.commit()

    # Réinitialisation des champs de saisie
    e_nom.delete(0, tk.END)
    e_prenom.delete(0, tk.END)
    e_mail.delete(0, tk.END)
    e_nationalite.delete(0, tk.END)
    champ_date_naissance.delete(0, tk.END)
    menu_filiere.set("")
    valeur_sexe.set("")

    # Affichage d'un message de confirmation
    message_confirmation = tk.Label(root, text="Formulaire soumis avec succès !", fg="green")
    message_confirmation.pack()

    # Fonction appelée lors du clic sur le bouton "Quitter"
def quitter():
    root.quit()

# Création des étiquettes et des champs de saisie

titre = Label(root, text='FORMULAIRE D\'INSCRIPTION',font=('times new roman',20,'bold'), bg="grey", fg="black")
nom = Label(root, text='Nom ',font=('times new roman',15,'bold'), fg="black")
prenom = Label(root, text='Prénom ',font=('times new roman',15,'bold'), fg="black")
email = Label(root, text='Email',font=('times new roman',15,'bold'), fg="black")
# age = Label(root, text='Age',font=('times new roman',15,'bold'), fg="black")
nationalite = Label(root, text='Nationalité',font=('times new roman',15,'bold'), fg="black")
filiere = Label(root, text='Filière ',font=('times new roman',15,'bold'), fg="black")
sexe = Label(root, text='Sexe ',font=('times new roman',15,'bold'), fg="black")

e_nom = Entry(root, width=40)
e_prenom = Entry(root, width=40)
e_mail = Entry(root, width=40)
# e_age = Entry(root, width=40)
e_nationalite = Entry(root, width=40)
efiliere = ttk.Combobox(root, width=40 ,values=["Gestion de projet","Algèbre","Statistiques","Developpement web","Developpement mobile","Réseaux informatiques","Télécoms"])
homme = ttk.Radiobutton( text='Homme', value=0)
femme = ttk.Radiobutton( text='Femme', value=1)

titre.grid(row=0, column=1, padx=20, pady=25)
nom.grid(row=1, column=0 ,padx=15 , pady=20)
e_nom.grid(row=1, column=1, padx=15, pady=20)

prenom.grid(row=2, column=0, padx=15, pady=20)
e_prenom.grid(row=2, column=1, padx=15, pady=20)

email.grid(row=3, column=0, padx=15, pady=20)
e_mail.grid(row=3, column=1, padx=15, pady=20)

nationalite.grid(row=4, column=0, padx=15, pady=20)
e_nationalite.grid(row=4, column=1, padx=15, pady=20)

menu_filiere = tk.StringVar(root)
menu_filiere.set("")
filiere.grid(row=5, column=0, padx=15, pady=20)
efiliere.current(0)
efiliere.grid(row=5, column=1 ,padx=15, pady=20)

etiquette_date_naissance = tk.Label(root, text="Date de naissance",font=('times new roman',15,'bold'), bg="grey", fg="black")
etiquette_date_naissance.grid(row=6, column=0)
champ_date_naissance = tk.Entry(root, width=40)
champ_date_naissance.grid(row=6, column=1)


valeur_sexe = tk.StringVar()
sexe.grid(row=7, column=0, padx=15, pady=20)
homme.grid(row=7, column=1 ,pady=10)
femme.grid(row=7, column=2)

bouton_enregistrer = tk.Button(text='Enregistrer',width=10, command=soumettre_formulaire)
bouton_enregistrer.grid(row=8, column=0,pady=20,padx=10)

bouton_quitter = tk.Button(text='Quitter',width=10, command= quitter)
bouton_quitter.grid(row=8, column=1,pady=20,padx=10)


connexion.commit()

root.mainloop()

# Fermeture de la connexion à la base de données à la sortie de l'application
connexion.close()

