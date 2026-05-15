<h1 align="center">🐌 FiveM Resolver 🐌</h1>

<p align="center">
  <a href="https://www.python.org" target="_blank"><img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python" /></a>
  <a href="https://t.me/swezy" target="_blank"><img src="https://img.shields.io/badge/Telegram-@Swezy-blue?style=for-the-badge&logo=telegram" /></a>
  <br>
  <code>Leave a ⭐ if you like this Repository</code>
</p>

---

# 🚀 Project overview

**CFX Resolver** is a sleek and interactive Python utility that lets you **inspect FiveM servers** using a `cfx.re/join` invite code, enabling fast retrieval of detailed server information directly from the official FiveM backend.

The program provides a **clean CLI interface** with a **beautiful animated logo**, *fast server lookup*, and *structured data extraction* for analysis and informational use.

> [!CAUTION]
> This tool is intended for **personal and educational use only**.
> Do **not** use it to exploit, abuse, or automate unauthorized actions against any server or service.
> The author and contributors are **not responsible for any misuse of this code**.

---

## ✨ Features
- 🔎 **Server Lookup** — Quickly retrieve any FiveM server using its invite code.
- 📊 **Full Server Details** — Includes hostname, player count, max players, gamemode, and map.
- 🧠 **Advanced Data Extraction** — Pulls additional server metadata such as:
  - Project name & description
  - Tags & locale
  - Server flags (private, premium, script hook settings, etc.)
  - Owner information (name, ID, avatar, profile)
  - Voting statistics (upvotes, burst power)
- 👥 **Live Player List** — Displays player ID, name, ping, and identifiers.
- 💾 **Auto Save Output** — Automatically exports results into a structured `.txt` file.
- 🌈 **Aesthetic CLI** — Gradient animated startup logo and colored terminal output.

---

## 🧭 How It Works

1. Run the tool (`python main.py`).
2. Enter the server invite code:
   ```
   https://cfx.re/join/XXXXXX
   ```
3. The tool will:
   - Query the FiveM API
   - Parse server JSON data
   - Extract additional metadata using regex
   - Display results in the terminal
   - Save output to a file
> ✅ Fully automatic — no setup required.

---

## 🧰 Requirements

- 🐍 Python **3.9+**
- 📦 Dependencies:
```bash
pip install requests colorama pystyle
```
- 🌐 Internet connection

---

## 📝 Repository structure

```
├─ assets/ ➔ Screenshots of the Program in action
│ └─ preview.png ➔ A screenshot of the Program running
├─ LICENSE ➔ License file
├─ README.md ➔ Read me file
└── main.py ➔ Main program logic and CLI
```

---

## 🖼️ Preview

<p align="center">
  <img src="https://img.shields.io/badge/UI-Gradient%20CLI-orange?style=for-the-badge"/>
  <br><br>
  <img src="https://github.com/SwezyDev/CFX-Resolver/blob/main/assets/preview.png?raw=true" alt="Program preview">
</p>

---

## ⚙️ Technical Details

- Uses the **FiveM server API**:
  ```
  https://servers-frontend.fivem.net/api/servers/single/<id>
  ```
- Parses:
  - JSON response (`Data` object)
  - Raw response text (regex extraction for extended metadata)
- Combines structured + unstructured parsing for maximum coverage.

---

## ⚖️ License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 🙌 Credits & contact

- Maintainer: [@SwezyDev](https://github.com/SwezyDev) — reach out via Telegram: [@Swezy](https://t.me/swezy)  

---

## 🚨 Disclaimer

This project is **unofficial and not affiliated with Cfx.re, FiveM, or Rockstar Games**. It only interacts with **publicly available server data**.

---

## 📣 Final note

This project is made for **learning, analysis, and informational purposes only**.
Use responsibly — avoid abuse or excessive automated requests.

> "Make Public Information Visible"