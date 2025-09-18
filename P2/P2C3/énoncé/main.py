def salaire_mensuel(salaire_annuel):
  resultat = round(salaire_annuel/12)
  return resultat

def salaire_hebdomadaire(salaire_mensuel):
  resultat = round(salaire_mensuel / 4)
  return resultat

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
  rfesultat = round(salaire_hebdomadaire / heures_travaillees )
  return resultat

montant_annuel = float(input("Entrez votre salaire annuel : "))
heure_hebdo = float(input("Entrez nbre heures travaillees semaine : "))
try
  salaire_mois = salaire_annuel(montant_annuel)
  mt_hebdo = salaire_hebdomadaire(salaire_mois)
  mt_horaire = salaire_horaire(mt_mois,heure_hebdo)
  print("Votre salaire horaire est de ",mt_horaire," euros")
except ValueError:
  print("Oops!  That was no valid number.  Try again...")
