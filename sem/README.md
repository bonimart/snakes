# Semestrální práce do předmětu BI-ZUM: Had

Cílem této semestrální práce je naimplementovat umělou inteligenci pro klasickou hru Had. V této hře hráč ovládá hada, který se snaží sníst co nejvíc ovoce, aniž by hlavou narazil sám do sebe. To komplikuje fakt, že s každým snězeným ovocem je had delší.

Hlavní část kódu se nachází v adresáři `src`. Tento adresář je rozdělen na:

- `game` - zde se nachází samostatná herní logika a vykreslování
- `solver` - zde se nachází implementace umělé inteligence

V adresáři `conf` naleznete nastavení pro samotnou hru a vykreslování. V adresáři `test` pak testy funkcionality.

Program lze spustit z kořenového adresáře tohoto repozitáře pomocí `python3 sem`.

