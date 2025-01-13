# Binance API Menadžer

Ovaj projekat je Python aplikacija za interakciju sa Binance API-jem, omogućavajući upravljanje kriptovalutama, praćenje cena i izvršavanje raznih zadataka poput trgovanja i beleženja aktivnosti.

## **Funkcionalnosti**

- Sigurna integracija API ključeva korišćenjem `.env` fajla.
- Praćenje cena BTC/USDT u realnom vremenu.
- Modularna struktura projekta za laku održivost i proširenje.
- Sistem za beleženje aktivnosti i debagovanje.

## **Postavljanje i Instalacija**

1. Klonirajte repozitorijum:
   ```bash
   git clone <repository-url>
   cd binance-api-manager
   ```

2. Kreirajte Python virtuelno okruženje:
   ```bash
   python -m venv venv
   ```

3. Aktivirajte virtuelno okruženje:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. Instalirajte zavisnosti:
   ```bash
   pip install -r requirements.txt
   ```

5. Konfigurišite API ključeve:
   - Dodajte vaš Binance API ključ i tajni ključ u `config/.env` fajl:
     ```env
     BINANCE_API_KEY=vaš_api_ključ
     BINANCE_SECRET_KEY=vaš_tajni_ključ
     ```

6. Testirajte postavku:
   ```bash
   python src/test_api.py
   ```

## **Napredak Projekta**

### **Završeni Zadaci**
- ✅ Inicijalizovana struktura projekta.
- ✅ Kreirano virtuelno okruženje i instalirane zavisnosti.
- ✅ API ključevi sigurno konfigurisani.
- ✅ Uspešno testirana veza sa Binance API-jem.

### **Sledeći Koraci**
- [ ] Implementirati praćenje cena BTC/USDT u realnom vremenu.
- [ ] Dodati strategije trgovanja (npr. kupovina ispod $40,000, prodaja iznad $45,000).
- [ ] Poboljšati beleženje sa JSON i tekst formatima.
- [ ] Dodati testove za API pozive i logiku trgovanja.

## **Struktura Projekta**
```
📁 binance-api-manager/
├── 📁 config/         # Konfiguracioni fajlovi
│   └── .env          # Promenljive okruženja
├── 📁 logs/           # Izlaz beleženja
├── 📁 src/            # Izvorni kod
│   ├── test_api.py    # Skripta za testiranje API konekcije
├── 📁 tests/          # Jedinični i integracioni testovi
├── 📄 requirements.txt # Python zavisnosti
├── 📄 README.md        # Dokumentacija projekta
```

## **Doprinos**
Slobodno forkujte repozitorijum i pošaljite pull zahteve sa unapređenjima ili novim funkcionalnostima.

---

**Licenca:** MIT