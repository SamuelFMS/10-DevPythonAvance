from patisserie.batteur_oeufs import BatteurOeufs
from patisserie.chocolat import Chocolat
from patisserie.fondeur_chocolat import FondeurChocolat
from patisserie.oeuf import Oeuf
from patisserie.recipient import Recipient

if __name__ == "__main__":
    recipientOeuf = Recipient("Recipient a oeuf", Oeuf(6))
    batteur = BatteurOeufs(recipientOeuf)
    recipientChocolat = Recipient("Recipient a chocolat", Chocolat(200))
    fondeur = FondeurChocolat(recipientChocolat)
    secondfondeur = FondeurChocolat()
    batteur.start()
    fondeur.start()
    batteur.join()
    fondeur.join()
    print("\nJe peux à présent incorporer le chocolat aux oeufs")
