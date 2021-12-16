TP \_ GildedRowse

Première étape : Filet de tests
Deuxième étape : correction du test déjà présent
Troisième étape : refactorer les choses les plus simples
 - LIGNE 33 : item.quality = item.quality - item.quality  => item.quality = 0
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

