## Käyttötapauksia

Opiskelija voi rekisteröityä (nimi, käyttäjätunnus ja salasana) ja kirjautua (käyttäjätunnus ja salasana) sovellukseen.  
Tämän jälkeen opiskelja voi tarkastella työtuntejaan, lisätä merkinnän, katsoa kurssivalikoimaa tai lisätä kurssin.

### Kurssin lisäys ja niiden tarkastelu
Kurssi voidaan lisätä kohdasta "Lisää kurssi". Tämän jälkeen voi tarkastella kurssilistaa ("Kurssit"), jossa lista saatavilla olevista kursseista. Kurssin voi poistaa tai sen nimeä voi muokata. Kurssilista haetaan SQL-kyselyllä Courses.query.all().

### Työtuntikirjaukset
Yksittäisen tuntikirjauksen voi tehdä kohdassa "Uusi kirjaus", jolloin valitaan valikosta haluttu kurssi ja merkitää sitten siihen käytetyt tunnit.  

"Työtunnit" kohdasta pääsee tarkastelemaan listaa kaikista (kirjautuneen opiskelijan) kirjauksista (SQL: SELECT Courses.name, Hours.timehours, Hours.id FROM Courses, Hours WHERE Courses.id = Hours.courses_id;")).  

Yksittäistä merkintää voi katsoa klikkaamalla sen nimeä. Näkymässä luetellaan kurssin nimi, merkinnän id ja merkityt tunnit. (SQL: Hours.query.get(hours_id) ja (SELECT Courses.name, Hours.timehours, Hours.id FROM Hours LEFT JOIN Courses ON Courses.id = Hours.courses_id WHERE Hours.id = :id").params(id=id))  

Yksittäisen merkinnän voi poistaa tai sen tuntimäärää muokata.  

Statistiikka-osiossa kerrotaan muutamia tilastoja.  
Ensin on kaikki opiskelijan työtunnit yhteensä (SQL: "SELECT SUM(hours.timehours) FROM hours WHERE account_id = :id").params(id=current_user.id)).  

Tämän jäkeen lueteltu kurssien yhteenlasketut tunnit (SQL: SELECT Courses.name, SUM(Hours.timehours) FROM Courses, Hours WHERE Courses.id=Hours.courses_id GROUP BY Courses.id).  

Viimeisänä lista kursseista joihin käytetty aika yhteensä on alle 27 tuntia (SQL: SELECT Courses.name, SUM(Hours.timehours) as summa FROM Courses LEFT JOIN Hours ON Courses.id=Hours.courses_id  GROUP BY Courses.id HAVING SUM(Hours.timehours)<27).


