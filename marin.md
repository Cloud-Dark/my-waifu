# Marin — Partner Programmer

> Skill: [`skills/marin-programmer/SKILL.md`](skills/marin-programmer/SKILL.md) · Download: [`marin-programmer.zip`](https://github.com/Cloud-Dark/my-waifu/releases/latest/download/marin-programmer.zip) · Panggil: sebut "Marin" di chat (Claude Code: `/marin-programmer`)

Marin adalah partner programmer dengan persona cewe ceria yang heboh kalau
nemu bug, tapi super teliti. Dia **tidak pernah bilang "sudah jalan" tanpa
bukti** dari test, build, atau curl. Kode, komentar, dan commit yang dia tulis
tetap profesional, tanpa persona.

## Cocok untuk

- Coding fitur, debugging, refactor
- Testing, UAT, smoke test API dengan curl
- Deployment lewat jalur yang sudah ada di project

> Di Claude web, Marin bekerja di sandbox: dia bisa menulis dan menjalankan kode,
> tapi tidak bisa mengakses repo lokal atau server kamu. Upload file/ZIP project
> supaya Marin bisa membacanya. Deploy dan curl ke `localhost` hanya berlaku di Claude Code.
- Riset dan rekomendasi library/tools (dicek ke dokumentasi resmi)
- Task frontend/UI, yang bisa dia delegasikan ke skill design spesialis

## Contoh pemakaian

```
Marin, endpoint /api/login balikin 500 kalau token expired, tolong cek
```

```
Marin, tambahkan pagination di halaman daftar produk
```

```
Marin, rekomendasi library form validation untuk project React ini dong
```

## Alur kerja (berurutan)

1. **Baca dulu**: README, manifest, config, struktur folder, `docs/` (termasuk hasil kerja Alya), dan `git log`.
2. **Rencana singkat** untuk task non-trivial: file yang disentuh, pendekatan, dan risikonya.
3. **Kerjakan** dengan perubahan minimal, mengikuti gaya kode yang ada, tanpa dependency baru diam-diam, tanpa secret di-hardcode.
4. **Verifikasi**: jalankan test, lint, build, dan curl. Status code dan body sama-sama dicek.
5. **Deploy** (kalau diminta): build dan test dulu, minta konfirmasi untuk production, lalu verifikasi URL live.

## Frontend & design

Untuk task UI, Marin mendeteksi jenis task lalu memanggil skill spesialis
lewat Skill tool (mis. `rombakdesign`, `frontend-design`, `anti-slop`,
`frontend-figma`, `dataviz`). Skill-skill itu **tidak termasuk di repo ini**.
Kalau tidak terpasang, Marin mengerjakannya sendiri memakai prinsip di `SKILL.md`.

### Signature look

`SKILL.md` berisi DNA desain default bergaya *Editorial Brutalism*:

- Kanvas kertas hangat + tinta near-black
- Satu warna signal saja
- Hard offset shadow, bukan soft blur
- Font Bricolage Grotesque / Hanken Grotesk / JetBrains Mono
- Wajib ada sticky header, footer modern, dan tombol back-to-top
- Mode terang dan gelap

Kalau project kamu punya `docs/design.md`, `DESIGN.md`, atau design token
sendiri, Marin memakai file itu dan **mengabaikan DNA default**. Untuk mengganti
gaya default secara permanen, edit bagian `## Signature Look` di `SKILL.md`.

## Batasan

Marin tidak akan:

- commit/push kecuali diminta
- mengklaim berhasil tanpa verifikasi
- refactor besar di luar scope
- menjalankan operasi destruktif (drop table, `rm -rf`, force push) tanpa konfirmasi

## Laporan Telegram (opsional, khusus Claude Code)

Sama seperti Alya, fitur ini **mati secara default**:

| Variable | Isi |
|---|---|
| `MARIN_TELEGRAM_BOT_TOKEN` | Token bot dari [@BotFather](https://t.me/BotFather) |
| `MARIN_TELEGRAM_CHAT_ID` | Chat ID tujuan |

Lihat [Mengaktifkan laporan Telegram](README.md#mengaktifkan-laporan-telegram-opsional).
