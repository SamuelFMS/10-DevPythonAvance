from patisserie.batteur_oeufs import BatteurOeufs
from patisserie.chocolat import Chocolat
from patisserie.fondeur_chocolat import FondeurChocolat
from patisserie.oeuf import Oeuf

if __name__ == "__main__":
    batteur = BatteurOeufs(Oeuf(6))
    fondeur = FondeurChocolat(Chocolat(200))
    batteur.start()
    fondeur.start()
    batteur.join()
    fondeur.join()
    print("\nJe peux à présent incorporer le chocolat aux oeufs")
