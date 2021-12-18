TP \_ GildedRowse

Première étape : Filet de tests

Deuxième étape : correction du test déjà présent

Troisième étape : refactorer les choses les plus simples

- LIGNE 33 : item.quality = item.quality - item.quality => item.quality = 0
- EXECUTION DES TESTS : OK
- LIGNES 21/22/23 : redondance de code des lignes 18 à 20 => suppression des lignes 21 à 23
- EXECUTION DES TESTS : OK
- LIGNES 18/19 : remplacement des if imbriqués par une condition => if ... and ...
- EXECUTION DES TESTS : OK
- LIGNE 13 : remplacement des if imbriqués (ligne 10 et 13) par une condition => if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name != "Sulfuras, Hand of Ragnaros"
- EXECUTION DES TESTS : OK

Quatrieme etape : decomposer les choses simples en petites méthodes

- Dans Item ajout des méthodes : decrease_quality, increase_quality, decrease_sell_in, increase_sell_in
- Remplacement des augmentations et diminution dans la méthode update_quality par les méthodes créées précédements
- EXECUTION DES TESTS : OK

Cinquième étape : division de l'update de qualité en deux fonction (vision plus clair du code)

Sixième étape : ajout du test "if quality < 50" dans la méthode increase_quality afin de enlever tous les "if quality < 50"
  
Septième étape : ajout du test "if quality > 0" dans la méthode decrease_quality afin de enlever tous les "if quality > 0"

NOTA : Après avoir relu le but, nous nous somme rendu compte que notre filet de test n'est pas assez important. Il faut qu'on ajoute des tests pour 10 jours

Huitième étape : ajout de plusieurs tests à notre filet.

Neuvième étape : ajout d'autre tests à notre filet.

Dixième étape : ajout de tests unitaires pour nos méthodes de modifications de sell_in et quality

Onzième étape : heritage d'item en différents objets et partage de l'update dans chacune de ces sous-classes. Modification des tests filets en conséquence (sauf tests basés sur texttest_fixture.py) - Test OK

Douxieme étape : nous nous sommes rendu que nous avions modifié la class Item. Pour cela nous afin refactorisé les classes en consequence.

Treizieme étape : ajout d'une factory et débugage de nos modifications à l'aide des tests filets

Quatorzieme étape : ajout de tests unitaires. 

Quinzieme étape : ajout du produit Conjured pour cela on implémente la classe, on ajoute un test permettant de verifier le bon comportement de la méthode update_quality. Puis on modifie le test filet pour y intégrer ce nouvel élément.

Seizieme : dernière analyse de refactorisation du code et passage de tous les tests.