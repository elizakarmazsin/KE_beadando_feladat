# KE_beadando_feladat
Szkript nyelvek beadandó feladat
Karmazsin Eliza
KE Jelszó Erősség Ellenőrző és Generátor

Ez a Python projekt egy egyszerű asztali alkalmazás, amely segít a felhasználóknak ellenőrizni a beírt jelszavak erősségét, valamint biztonságos, véletlenszerű jelszavak generálásában is támogatja őket. A program

A Program Feladata

Cél: Egy felhasználóbarát, grafikus felületű eszköz biztosítása jelszavak biztonságának kiértékelésére és létrehozására.

Fő funkciók:

Jelszóerősség Ellenőrzés: Kiértékeli a beírt jelszót hossza, nagy- és kisbetűk, számok és speciális karakterek megléte alapján.
Jelszó Generálás: Biztonságos, véletlen jelszót hoz létre a 'random' modul segítségével.
Monogramos Függvény Demó: A generált jelszó formázása a saját monogrammal ellátott függvénnyel.

A Program Felépítése és Modulok

A projekt három fő Python fájlból áll:

main.py: Inicializálja az alkalmazást, kezeli a gombnyomásokat.
ke_utils.py: egyedi logikát, amelyet a main.py használ.
demo_module.py: A 'random' modul bemutatása, jelszógenerálásra specializálva.

Osztályok és Függvények

Fő program (main.py)
  App: A fő alkalmazás konténere. Inicializálja a GUI-t és a logikai objektumokat.
  handle_check_password(): Gombnyomásra elindítja a beírt jelszó ellenőrzését.
  handle_generate_password(): Gombnyomásra hívja a demo_module generáló függvényét.
  handle_format_text(): Hívja a ke_utils.ke_format_text saját függvényt.

Saját Modul (ke_utils.py)
  KE_DataHelper: Kezeli és formázza az alkalmazás visszajelzéseit
  ke_format_text(input_text): a bemeneti szöveget (jelszót) nagybetűs, vesszővel elválasztott stringgé alakítja.

Bemutatandó Modul (demo_module.py)
  generate_secure_password(length):  Biztosítja, hogy a jelszó tartalmazzon kis- és nagybetűt, számot és speciális karaktert.
  get_random_int(min_val, max_val): Véletlen egész szám generálása (random.randint).
  get_random_choice(data_list): Véletlen elem kiválasztása listából (random.choice).
  shuffle_list(data_list): Lista elemeinek helyben történő megkeverése (random.shuffle).