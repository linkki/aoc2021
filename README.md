# Linkin Advent of Code 2021

## Ratkaisut

Pohja on Pythonille (jotta kansiot tarttuvat mukaan), mutta toteutus voi olla millä kielellä ja tekniikalla tahansa.

Jos ratkaisupohjia tarvitsee muuttaa bulkkina, onnistuu esim bashilla (muokkaa lukuarvoja sen mukaan minkä päivän kohdalla on sopiva pohja ja mistä eteenpäin kopioit sen, olettaen että jätät päivän numeron kyseisestä mallipohjasta pois):

```bash
for i in {5..25}; do cd $i; rm solution.py; cp ../4/solution.py .; sed -i "s/Day/Day $i/g" solution.py ; cd ..; done
```

Ratkaisut striimataan tai postataan videoina Linkin YouTube-kanavalla: https://www.youtube.com/channel/UCB4Eh-p8h7Qzyigs5QWzWFA

## Striimaus

Thumbnail-kuva on asetettu striimiin valmiiksi, ja löytyy myös täältä: https://github.com/linkki/aoc2021/blob/main/images/thumbnail.png

### YouTube
- kirjaudu Linkin YouTube-tilille
- yläpalkista Create > Go live
- säädä tarvittaessa näkymän tiedot, kuten **Titleen päivän numero** ja kuvauksen linkit
- kopioi Stream key

### OBS
- ensi kertaa käynnistäessä kysynee asetuksia; automaatin antamat ovat todennäköisesti OK
    - voit ajaa automaatin milloin vain uudestaan: Tools > Auto-Configuration Wizard
- luo uusi profiili: Profile > New
- oikeasta alakulmasta Settings (jos et asetus-automaatin yhteydessä säätänyt): 
    - Stream > Service: YouTube/YouTube Gaming 
    - Stream > Server: Primary 
    - Stream > Stream Key: liitä kopioimasi YouTuben stream key
    - voit myös ottaa varalle nauhoituksen automaattisesti: General > Output > Automatically record when streaming
    - muita asetuksia ei välttämättä tarvitse säätää ollenkaan
- luo 2 sceneä: vscode ja chrome
    - vscode: Window Capture (Xcomposite) vscode-ikkunasta ja Video Capture Device kamerasta
    - chrome: Window Capture (Xcomposite) chrome-ikkunasta ja olemassaoleva Video Capture Device, kun loit sen jo edelliseen sceneen
    - mahdollisesti täppää ruutukaappaus-ikkunoiden asetuksista Swap red and blue
- jos sinulle sopii vaihdella eri ikkunoiden välillä (eli auki ei ole mitään "turhaa"), voit luoda vain yhden skenen, johon lisäät **Screen** Capturen ja Video Capturen
    - tämä saattaa olla joka tapauksessa parempi vaihtoehto; jos ikkunoita on auki runsaasti, OBS tuppaa unohtamaan minkä olit valinnut, ja valitsee sceneä vaihtaessa jonkin satunnaisen ikkunan näkyviin...
- kokeile nauhoittaa, katso että ääni tarttuu jne. 
- klikkaa Start Streaming oikeasta alakulmasta 
    - tsekkaa toisella laitteella että toimiihan oikein, äänet kuuluu jne, tai pyydä jotakuta muuta tsekkaamaan
    - voit myös asettaa pikanäppäimet striimauksen aloitukseen (ja lopetukseen; voi hyvin käyttää samaa näppäinyhdistelmää molempiin, esim. ääkkösiä käyttävät tuppaavat olemaan vapaina): Settings > Hotkeys
    - ennen striimin lopetusta kannattaa jättää hetki tyhjää, YouTube/OBS välillä leikkaa striimin lopusta pätkän

### Striimin jälkeen
- avaa Youtubessa Video Manager ja sieltä kyseinen video (Linkki-kanavan etusivulta kirjautuneena "Manage videos" > Content > Live > Live replay > kynä-symboli eli Details ko. videon kohdalta)
- lisää kuvaukseen jos videossa on jotain huomautettavaa, esim. äänenlaadusta tai linkkejä lisämateriaaleihin tms. HUOM: saattaa vaikuttaa koko striimin kuvaustekstiin myös, joten tarkista se tallennettuasi!
- lisää video Advent of Code -soittolistaan jos se ei ole siellä jo
- **muista tallentaa!**
- YouTubella kestää aika kauan prosessoida video editoitavaksi 
    - kun näkymässä oikealla "Subtitles" -linkki ei ole enää harmaa, on video editoitavissa
    - klikkaa vasemmalta "Editor"
    - leikkaa alusta ja lopusta turhat pois (jos jaksat)
    - leikkaa ainakin mahdolliset kirosanat pois XD
    - muista tallentaa! YouTube taas prosessoi videota jonkin aikaa
- muokkaa striimin nimi ja kuvaus seuraavaa päivää varten (yläpalkista Create > Go live > Edit > Title ja Description -kentät ainakin)
