# Luukku 6: Valokalat

# Toimintaperiaate

Kaikki samanikäiset kalat ovat tämän tehtävän kannalta identtisiä. Siksi
yksittäisten kalojen sijaan seuraammekin ainoastaan, moniko kala on 
lisääntymässä tietyn ajan jälkeen. Tässä ratkaisussa kalojen tilat onkin
tallennettu 9-alkioiseen taulukkoon, jonka `i`. alkio kertoo, moniko kala on
lisääntymässä seuraavan kerran `i` päivän jälkeen.

Kun päivä vaihtuu, tämän päivän aikana lisääntyvien kalojen määrä laitetaan
talteen, ja kaikki muut kalat siirretään taulukossa indeksiin `i-1`. Tämän
jälkeen lisääntyvät kalat siirretään tehtävänannon mukaisesti indeksiin 6 ja
niiden jälkeläiset indeksiin 8.

Kun haluttu määrä päiviä on kulunut, saadaan kalojen kokonaismäärä laskemalla
taulukon kaikkien alkioiden summa.

# Ohjelman suorittaminen

Tämän päivän luukku on toteutettu C-kielellä. Voit suorittaa ohjelman seuraavalla komennolla:
```
make run
```

Makefilestä löytyy targetit myös esimerkkidatan käyttöön sekä muistivuotojen diagnosointiin `valgrind`-komentoa käyttäen.
