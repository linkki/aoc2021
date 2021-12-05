# Luukku 5: Kuumat lähteet

Tämän päivän luukun komentorivikäyttöliittymä on tehty click-kirjastoa
käyttäen. Kirjaston pitääkin olla asennettuna, jotta koodin voi suorittaa.
Lisäksi koodi on kirjoitettu python 3 -yhteensopivaksi, eikä sen
suorittaminen esimerkiksi python 2.6:lla todennäköisesti onnistu. Helpoimmin
ja turvallisimmin oikeat versiot ja kirjastot saa käyttöön virtuaaliympäristöä
käyttämällä seuraavasti:

```
# luodaan uusi virtuaaliympäristö
virtualenv .venv -p python3

# otetaan se käyttöön
source .venv/bin/activate

# asennetaan vaaditut kirjastot
pip install -r requirements.txt
```

Mikäli sinulla eiole virtualenv-pakettia ennestään asennettuna, voit asentaa
sen komennolla `pip install virtualenv`.

Kun olet virtuaaliympäristössä ja sinulla on vaaditut kirjastot asennettuna,
voi ohjelman suorittaa antamalla sille polun tiedostoon, jossa päivän syöte
on, sekä syötteen kuvaaman merenpohjan sivun pituuden. Esimerkiksi
```
python main.py data/input.txt 10000
```
tai
```
python main.py data/example.txt 10
```
