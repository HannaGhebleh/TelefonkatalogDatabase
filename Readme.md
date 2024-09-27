# 🐧 Oppsett av Ubuntu på Raspberry Pi

## 🧰 Utstyr som trengs

1. **Raspberry Pi**
2. **MicroSD-kort**
3. **En datamaskin** for å laste ned og skrive OS-bildet
4. **Strømforsyning** til Raspberry Pi
5. **HDMI-kabel og skjerm** (for oppsett)
6. **Tastatur og mus** (for oppsett)

---

## 📝 Steg 1: Last ned Ubuntu for Raspberry Pi

1. Gå til **[Ubuntu sin nedlastingsside for Raspberry Pi](https://ubuntu.com/download/raspberry-pi)**.
2. Velg ønsket versjon:
   - **Ubuntu Desktop** for grafisk grensesnitt
   - **Ubuntu Server** for kommandolinje
3. Last ned filen.

---

## 💾 Steg 2: Installer Ubuntu på SD-kortet

1. Last ned **[Raspberry Pi Imager](https://www.raspberrypi.org/software/)** fra Raspberry Pi sin nettside.
2. Åpne **Raspberry Pi Imager**.
3. Velg **Ubuntu** under operativsystemer.
4. Velg **SD-kortet** ditt.
5. Klikk **Write** for å skrive Ubuntu til SD-kortet.

---

## 🚀 Steg 3: Start Raspberry Pi

1. Sett inn **SD-kortet** i Raspberry Pi-en.
2. Koble til **skjerm, tastatur og mus**.
3. Koble til **strømforsyningen** – Raspberry Pi vil starte opp.

---

## 🔧 Steg 4: Oppsett

1. På første oppstart vil **Ubuntu** bli konfigurert automatisk.
2. Hvis du bruker **Ubuntu Server**, logg inn med:
   - **Brukernavn**: `ubuntu`
   - **Passord**: `ubuntu`
3. Du blir bedt om å **endre passordet** etter første pålogging.
4. **Ubuntu Desktop** vil vise et grafisk brukergrensesnitt hvor du kan sette opp språk, tidssone og WiFi.

---

## 🔄 Steg 5: Oppdater systemet

Åpne terminalen (eller bruk `Ctrl + Alt + T` i Ubuntu Desktop) og kjør:

```bash
sudo apt update
sudo apt upgrade -y


