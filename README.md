# Folder ApiMsNoWeb obsahuje Python program ktory spracuvava udaje z API a pracuje s fake datami a fake serverom.
# Folder ApiMsWeb opsadhuje Python program s vlastnou database.
# Na spustenie oboch programov je potreba nainstalovat vsetky naimportovane moduly.
# Errors:
Program bez webu vyhadzuje ValueError pri zadani blank alebo str hodnoty do int(input()).
Program s webom a database vyhadzuje ties errors pri zadani zlej type alebo blank hodnoty.
# ApiMsWeb localhost sa spusta cez terminal v IDE. Najprv zaktivujeme virtual environment commandom: python -m venv .venv (pre windows). Nasledne ak by sa venv nezaktivoval pouzijeme command: .venv\Scripts\activate. Ked uz nas terminal bezi vo virtual enviromnent pouzijeme tieto tri commands: 
> $env:FLASK_APP = "app" ; 
> $env:FLASK_ENV = "development" ; 
> flask run ;
# Tieto commands nam zhotovili localhost.
