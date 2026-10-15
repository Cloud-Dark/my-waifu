# my-waifu

Tiga asisten berpersona untuk [Claude Code](https://claude.com/claude-code), dalam Bahasa Indonesia.

| Skill | Persona | Untuk apa | Docs |
|---|---|---|---|
| `waguri` | Office lady ramah & jujur | Email, dokumen, CS, riset, merangkum, jadwal | [waguri.md](waguri.md) |
| `alya-dokumenter` | Cewe manja yang rapi | Dokumentasi proyek: PRD, TRD, arsitektur, changelog, UAT | [alya.md](alya.md) |
| `marin-programmer` | Cewe ceria yang teliti | Coding, debugging, testing, deploy, frontend | [marin.md](marin.md) |

Persona hanya dipakai saat ngobrol. File, kode, dan dokumen yang dihasilkan tetap profesional.

Ketiganya saling melengkapi: Alya menulis `docs/`, Marin membaca `docs/` itu sebelum coding,
dan Waguri menangani urusan kantor di sekitarnya.

## Instalasi

### Opsi 1 — sebagai plugin (paling mudah)

Di Claude Code:

```
/plugin marketplace add Cloud-Dark/my-waifu
/plugin install my-waifu@my-waifu
```

Skill akan muncul dengan prefix plugin, mis. `/my-waifu:marin-programmer`.

### Opsi 2 — copy skill satu per satu

Ambil hanya skill yang kamu mau:

```bash
git clone https://github.com/Cloud-Dark/my-waifu.git
mkdir -p ~/.claude/skills
cp -r my-waifu/skills/marin-programmer ~/.claude/skills/
# atau: cp -r my-waifu/skills/* ~/.claude/skills/
```

PowerShell (Windows):

```powershell
git clone https://github.com/Cloud-Dark/my-waifu.git
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
Copy-Item -Recurse my-waifu\skills\marin-programmer "$HOME\.claude\skills\"
```

Untuk satu project saja, copy ke `.claude/skills/` di root project.
Restart Claude Code, lalu panggil `/marin-programmer`, `/alya-dokumenter`, atau `/waguri`.

## Mengaktifkan laporan Telegram (opsional)

Alya dan Marin bisa kirim laporan ke Telegram setiap task selesai. Fitur ini
**mati secara default** dan aktif hanya kalau environment variable di-set.

1. Buat bot lewat [@BotFather](https://t.me/BotFather) untuk mendapatkan token.
2. Kirim pesan ke bot, lalu buka `https://api.telegram.org/bot<TOKEN>/getUpdates` untuk melihat `chat.id`.
3. Set environment variable. Simpan di profile shell, **jangan** di repo ini:

```bash
# ~/.bashrc / ~/.zshrc
export MARIN_TELEGRAM_BOT_TOKEN="..."
export MARIN_TELEGRAM_CHAT_ID="..."
export ALYA_TELEGRAM_BOT_TOKEN="..."
export ALYA_TELEGRAM_CHAT_ID="..."
```

```powershell
# Windows (persisten per user)
[Environment]::SetEnvironmentVariable("MARIN_TELEGRAM_BOT_TOKEN", "...", "User")
[Environment]::SetEnvironmentVariable("MARIN_TELEGRAM_CHAT_ID", "...", "User")
```

Atau taruh di blok `env` pada `~/.claude/settings.json` (file lokal, bukan bagian dari repo).

## Struktur repo

```
.claude-plugin/
  plugin.json          manifest plugin
  marketplace.json     supaya bisa di-install via /plugin
skills/
  waguri/SKILL.md
  alya-dokumenter/SKILL.md
  marin-programmer/SKILL.md
waguri.md  alya.md  marin.md   dokumentasi per skill
CONTRIBUTING.md
```

## Kontribusi

Silakan fork, pecah, remix, atau tambah persona baru. Lihat [CONTRIBUTING.md](CONTRIBUTING.md).

## Lisensi

[MIT](LICENSE)
