# OSINT Multi-Tools

> **Un outil OSINT gratuit et open-source, développé en live sur TikTok chaque soir à 21h !**

Ce projet est une suite d'outils OSINT (Open Source Intelligence) destinée aux chercheurs, pentesters et curieux souhaitant apprendre l'OSINT de manière efficace et centralisée. 
**Inspiré de RedTiger-Tools & Clarity-tools**.

:warning: **Projet en construction !** Ce projet est encore en développement et **n'est pas encore prêt pour une utilisation en production**.

---

## Fonctionnalités Actuelles :hammer:
- [x] **Recherche d'informations sur une adresse IP** (geolocalisation, ASN, etc.)

## Fonctionnalités Futures :rocket:
- [ ] **Lookup de noms de domaine** (Whois, DNS records, etc.)
- [ ] **Scraping et OSINT sur les réseaux sociaux** (Twitter, Instagram, etc.)
- [ ] **Analyse d'adresses e-mail** (vérification de leaks, MX lookup...)
- [ ] **Scan de fuites de données** (recherche dans des bases publiques)
- [ ] **Une CLI robuste et interactive** (actuellement en développement)
- [ ] **Un panel web** pour une interface plus intuitive
- [ ] **Une application desktop** pour une utilisation sans dépendances web
- [ ] **Des modules OSINT avancés** (ex. analyse d'images, reconnaissance faciale, etc.)

## Installation :computer:
L'outil est compatible avec **Windows, Linux et macOS**.

```bash
# Clonez le dépôt
git https://github.com/tyki6/TykiTools.git
cd TykiTools

# Installez les dépendances
uv pip install -r pyproject.toml

# Lancez l'outil
python main.py --help
```

## Exemples d'utilisation :wrench:
```bash
python main.py iplookup 127.0.0.1
```

## Contribution :handshake:
Tout le monde peut contribuer ! Voici comment vous pouvez aider :
- **Tester l'outil** et remonter des bugs ou suggestions
- **Proposer de nouvelles fonctionnalités** via des issues GitHub
- **Faire un pull request** si vous codez

## Rejoignez la communauté :speech_balloon:
- **Suivez le développement en live** sur TikTok : [@tyki6](https://www.tiktok.com/@tyki6)
- **Serveur Discord**: [tyki6](https://discord.gg/PC4GF66WEg)
- **Partagez vos idées** et contribuez sur GitHub !

## Versions & Licence
- Licence : [MIT](LICENSE)
- Auteur : @tyki6

---

**:globe_with_meridians: English version available [here](README_EN.md)**


