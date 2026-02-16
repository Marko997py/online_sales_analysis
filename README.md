# Online Sales Analysis

Python projekat za upravljanje inventarom proizvoda i korpom kupca, uz korišćenje OOP principa i GitHub verzionisanja (grane, merge, konflikti).

## Funkcionalnosti

### Product (product.py)
- Atributi: `name`, `price`, `quantity`
- Metode:
  - prikaz informacija o proizvodu
  - ažuriranje količine proizvoda

### ProductManager (product_manager.py)
- Čuva listu dostupnih proizvoda
- Metode:
  - dodavanje proizvoda
  - prikaz svih proizvoda
  - izračunavanje ukupne vrednosti inventara
  - uklanjanje proizvoda po imenu

### Cart (cart.py)
- Atribut: `cart_items` (lista proizvoda u korpi)
- Metode:
  - dodavanje proizvoda u korpu
  - prikaz sadržaja korpe
  - izračunavanje ukupne vrednosti za naplatu

## Pokretanje
1. Kloniraj repo
2. Pokreni:
```bash
python main.py
