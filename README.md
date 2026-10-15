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

## Instalasi di Claude web (claude.ai)

Bisa dipakai di paket Free, Pro, Max, Team, dan Enterprise.

1. Download ZIP skill yang kamu mau dari halaman
   [**Releases**](https://github.com/Cloud-Dark/my-waifu/releases/latest):
   - [`waguri.zip`](https://github.com/Cloud-Dark/my-waifu/releases/latest/download/waguri.zip)
   - [`alya-dokumenter.zip`](https://github.com/Cloud-Dark/my-waifu/releases/latest/download/alya-dokumenter.zip)
   - [`marin-programmer.zip`](https://github.com/Cloud-Dark/my-waifu/releases/latest/download/marin-programmer.zip)
2. Buka **Settings → Capabilities**, lalu pastikan **Code execution and file creation** aktif.
3. Buka **Customize → Skills**, klik **+**, pilih **Create skill → Upload a skill**, lalu pilih file ZIP-nya.
   ZIP tidak perlu diekstrak.
4. Pastikan toggle skill-nya menyala.

### Cara memanggil

Di Claude web, skill dipanggil **otomatis** sesuai isi chat. Tidak ada slash command.
Cukup sebut namanya:

```
Marin, endpoint login-ku balikin 500 kalau token expired, tolong cek
Alya, buatkan PRD untuk aplikasi kasir ini
Waguri, rapikan email ini biar lebih sopan ke klien
```

Kalau skill belum terpanggil, tegaskan saja: "pakai skill Marin ya".

## Instalasi di Claude Code (opsional)

Copy folder skill ke `~/.claude/skills/`, lalu panggil langsung dengan
`/marin-programmer`, `/alya-dokumenter`, atau `/waguri`:

```bash
git clone https://github.com/Cloud-Dark/my-waifu.git
mkdir -p ~/.claude/skills
cp -r my-waifu/skills/* ~/.claude/skills/
```

Atau lewat plugin. Dengan cara ini, nama skill diberi prefix, mis. `/my-waifu:marin-programmer`:

```
/plugin marketplace add Cloud-Dark/my-waifu
/plugin install my-waifu@my-waifu
```

## Mengaktifkan laporan Telegram (opsional, khusus Claude Code)

Alya dan Marin bisa kirim laporan ke Telegram setiap task selesai. Fitur ini
**mati secara default** dan aktif hanya kalau environment variable di-set.
Di Claude web tidak ada environment variable, jadi fitur ini otomatis dilewati.
Semua fitur lain tetap jalan.

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
scripts/
  build-zips.py        bikin dist/<skill>.zip untuk upload ke claude.ai
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
