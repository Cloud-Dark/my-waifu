# Alya — Dokumenter Proyek

> Skill: [`skills/alya-dokumenter/SKILL.md`](skills/alya-dokumenter/SKILL.md) · Download: [`alya-dokumenter.zip`](https://github.com/Cloud-Dark/my-waifu/releases/latest/download/alya-dokumenter.zip) · Panggil: sebut "Alya" di chat (Claude Code: `/alya-dokumenter`)

Alya adalah asisten dokumentasi proyek dengan persona cewe manja yang agak
posesif soal kerapian docs. Dia ngobrol dengan manja, tapi **isi dokumen yang
dia tulis tetap formal dan profesional**. Persona tidak pernah masuk ke file.

## Cocok untuk

- Membuat set dokumentasi awal proyek (charter, PRD, arsitektur, checklist, changelog)
- PRD, BRD, FRD, TRD, roadmap, risk register, ADR, glossary
- Rencana implementasi dan spec per fitur
- Dokumen hasil UAT
- Merapikan `docs/` yang berantakan tanpa merusak penomoran lama

## Contoh pemakaian

```
Alya, buatkan dokumentasi awal untuk project ini
```

```
Alya, tambahkan TRD untuk fitur autentikasi
```

```
Alya, update changelog dan master checklist, fitur export PDF sudah selesai
```

## Struktur yang dihasilkan

```
docs/
  standards/        NN_TOPIK_STANDARD.md + 00_STANDARD_INDEX.md
  plans/            YYYY-MM-DD-slug-fitur.md
  specs/            YYYY-MM-DD-slug-design.md / -checklist.md / -implementation-plan.md
  uat/              YYYY-MM-DD_deskripsi-uat.md
  00_PROJECT_CHARTER.md
  01_PRD.md
  02_BRD.md
  ...
  31_CHANGELOG.md
```

Aturan penting:

- Dokumen inti bernama `NN_NAMA_UPPERCASE.md` (dua digit, zero-padded).
- Nomor yang sudah terbit **tidak pernah** diubah. Dokumen baru mengambil nomor kosong berikutnya.
- Setiap dokumen diawali header Status, Terakhir diperbarui, dan Pemilik.
- Fakta yang tidak ditemukan di kode ditandai `_TBD_`, tidak dikarang.
- Tanggal selalu absolut (`YYYY-MM-DD`).

## Alur kerja

1. **Audit** `docs/` yang sudah ada, lalu ikuti nomor dan bahasanya.
2. **Gali konteks** dari README, manifest, dan struktur kode.
3. **Tulis**: satu dokumen untuk satu tujuan.
4. **Update turunan**: index, checklist, roadmap, changelog, decisions.
5. **Lapor**: daftar file yang dibuat/diubah plus saran dokumen berikutnya.

Alya tidak commit ke git kecuali diminta.

## Laporan Telegram (opsional, khusus Claude Code)

Alya bisa kirim laporan ke Telegram setiap task selesai. Fitur ini **mati
secara default** dan hanya aktif kalau kedua environment variable di-set:

| Variable | Isi |
|---|---|
| `ALYA_TELEGRAM_BOT_TOKEN` | Token bot dari [@BotFather](https://t.me/BotFather) |
| `ALYA_TELEGRAM_CHAT_ID` | Chat ID tujuan |

Lihat [Mengaktifkan laporan Telegram](README.md#mengaktifkan-laporan-telegram-opsional) untuk cara set-nya.
Jangan pernah menulis token langsung di `SKILL.md`.
