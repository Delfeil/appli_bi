Pour lancer le script, il faut au préalable avoir python version 3.6
il faut avoir les librairies:
- pandas 0.23.3
- NumPy >= 1.11.0
- Matplotlib >= 2.0.0
- Scikit-learn >= 0.18.0
- fanalysis >= 0.0.1
- scipy >= 1.4.1


Pour que les scripts  fonctionnent correctement, il faut obligatoiremment mettre en place l'architecture des fichiers suivante:
./src/ -> Contenant l'ensemble des scripts python
./fig/ -> contiendras l'ensemble des graphes et figures générés lors des traitements des scripts
./donnees/source/data_mining_DB_clients_tbl.csv
./donnees/source/data_mining_DB_clients_tbl_bis.csv -> les deux fichiers csv initiaux.

Pour lancer le programmel suffit de lancer la commande:
cd ./src
python3 ./bi.py