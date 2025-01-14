# Binance API Manager

Ovaj projekat omogućava pregled stanja na vašem Binance nalogu, uključujući balans, alokaciju sredstava i statistike tržišta.

## Trenutno implementirano ✅
- Pregled stanja na računu
- Prikupljanje podataka o tržištu
- Beleženje aktivnosti u log fajlovima
- Implementacija testne trgovine sa USDT

## Sledeći koraci ⬜
- Implementacija strategije trgovanja na osnovu top 100 trgovina u poslednja 24 sata
- Prikaz 100 trgovina sa pozitivnim procentom profita
- Dodavanje grafičkog korisničkog interfejsa (GUI)

## Kratko uputstvo za instalaciju

### Klonirajte repozitorijum:
```bash
git clone https://github.com/nidzation/binance-api-manager.git
cd binance-api-manager
```

### Kreirajte i aktivirajte virtuelno okruženje:
```bash
python3 -m venv venv
source venv/bin/activate  # Na Windows-u: .\venv\Scripts\activate
```

### Instalirajte potrebne biblioteke:
```bash
pip install -r requirements.txt
```

### Konfigurišite API ključeve:
Kreirajte fajl `config/.env` sa sledećim sadržajem:
```
BINANCE_API_KEY=VAŠ_API_KLJUČ
BINANCE_SECRET_KEY=VAŠ_SECRET_KLJUČ
```

### Pokrenite testove:
Proverite validnost podešavanja:
```bash
python src/test_env_variables.py
python src/test_binance_connection.py
```

### Pokrenite skripte:
Pregled stanja na računu:
```bash
python src/account_summary.py
```

Testirajte strategiju trgovanja:
```bash
python src/trading_strategy.py
```

