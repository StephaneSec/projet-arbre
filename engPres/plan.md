# 1.Page de présentation OK

* université de Caen (logo)
* Département d'informatique (logo)
* nom du projet
* mon nom
* nom du tuteur



# 2.Plan
* présentation des concepts utiles 
* présentation de la façon dont ces concepts peuvent être utile autour d'un exemple (3-color)
* présentation des autres problèmes
* mon objectif

* TOC


# 3.Décomposition arborescente
## définition d'une décomposition arborescente OK
* Afficher un grapheti
* Afficher la définition de notre décomposition arborescente
* Afficher deux représentation arborescente (dont une trivial car cela montre qu'il en existe toujours au moins une)


## 4.treewidth OK

* Afficher deux représentations et donner la largeur de chacune
* définition de la treewidte


## 5.nice tree OK

### definition
* pour améliorer les manipulations et permettre de simplifier les justifications, on va déformer les decomp pour obtenir un nice tree :
* def : un nice tree est une decomp arb qui ne doit faire apparaître que trois type de noeud
* affichage d'un graphe (très simple) et d'un nice tree associé

### 6 exemple d'obtention de nice tree

#7.Applications :
## k-color
### le problème OK
* un graphe, on veut colorier les noeuds de telle sorte qu'aucun noeuds connectés n'est la même couleur. Le nombre de couleurs nécessaire n'est pas connu.
* problème de décision NP (peut-on le colorier avec 3 couleurs par exemple)
* la treewidth permet de savoir si c'est possible
* le nice tree permet de trouver une coloration
 
### 8 example OK     
* le coloriage : en quoi les propriétés sont utiles


## 9 D'autres problèmes

Décrire brièvement ce que sont ces problèmes
* vertex-color
* problème de la clique maximale
* cycle Hamiltonien

#10 Objectifs du projet : 


### En partant d'une décomposition arborescente
* trouver un moyen de s'en servir pour résoudre les problèmes précédents (comme fait avec le 3-color)
* implémenter cette méthode
### En partant d'un graphe
* trouver une méthode pour obtenir une "bonne décomposition arborescente"
* implémeter cette méthode
### prolongement :
* tester/améliorer ces implémentations sur de grosses structures
* soigner la façon de présenter les résultats pour les rendre le plus compréhensible 

#11 biblio


* Cours de Florent Madeleine : M2 Decim "Complexité des CSP et des requêtes"
* Dániel Marx : Fixed Parameter Algorithms 
* wikipedia : articles divers