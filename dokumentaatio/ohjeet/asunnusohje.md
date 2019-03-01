## Lataaminen omalle koneelle (linux/macOs)
- lataa repositoria haluamaasi kansioon ja siirry kansioon sisälle  
    git clone https://github.com/Hilma-H/Opiskeluaika  
    cd kansionnimi
- luo virtuaaliympäristö, ota se käyttöön, asenna riippuvuudet  
    python3 -m venv venv  
    source venv/bin/activate  
    pip install -r requirements.txt
- Avaa sovellus  
    python3 hello.py
- Syöte kertoo sinulle osoitteen ja miten pääset pois.  
  Esimerkiksi  
    Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
- tietokantaa voit tarkastella SQLitella  
    sqlite3 application/tasks.db

## Heroku
(minulle jäi epäselväksi millä tavalla heroku pitäisi liittää)


