# Linkin Advent of Code 2021

## Ratkaisut

Pohja on Pythonille (jotta kansiot tarttuvat mukaan), mutta toteutus voi olla millä kielellä ja tekniikalla tahansa.

Ratkaisut striimataan tai postataan videoina Linkin YouTube-kanavalla: https://www.youtube.com/channel/UCB4Eh-p8h7Qzyigs5QWzWFA

## Striimaus

### YouTube
- kirjaudu haluamallesi YouTube-tilille
- yläpalkista Create > Go live
- säädä näkymän tiedot, kuten Title ja kuvauksen linkit
- kopioi Stream key

### OBS
- ensi kertaa käynnistäessä kysynee asetuksia; automaatin antamat ovat todennäköisesti OK
    - voit ajaa automaatin milloin vain uudestaan: Tools > Auto-Configuration Wizard
- luo uusi profiili: Profile > New
- oikeasta alakulmasta Settings: 
    - Stream > Service: YouTube/YouTube Gaming 
    - Stream > Server: Primary 
    - Stream > Stream Key: liitä kopioimasi YouTuben stream key
    - voit myös ottaa varalle nauhoituksen automaattisesti: General > Output > Automatically record when streaming
    - muita asetuksia ei välttämättä tarvitse säätää ollenkaan
- luo 2 sceneä: vscode ja chrome
    - vscode: Window Capture (Xcomposite) vscode-ikkunasta ja Video Capture Device kamerasta
    - chrome: Window Capture (Xcomposite) chrome-ikkunasta ja olemassaoleva Video Capture Device, kun loit sen jo edelliseen sceneen
    - mahdollisesti täppää ruutukaappaus-ikkunoiden asetuksista Swap red and blue
- Kokeile nauhoittaa, katso että ääni tarttuu jne. 
- Klikkaa Start Streaming oikeasta alakulmasta 
    - tsekkaa toisella laitteella että toimiihan oikein, äänet kuuluu jne, tai pyydä jotakuta muuta tsekkaamaan
