# Kontribusi

Terima kasih sudah mau ikut bantu.

## Menambah skill/persona baru

1. Buat folder `skills/<nama-skill>/` berisi `SKILL.md` dengan frontmatter:

   ```markdown
   ---
   name: nama-skill
   description: Satu kalimat jelas — kapan skill ini dipakai dan trigger-nya.
   ---
   ```

   `name` harus sama dengan nama folder (kebab-case, maks 64 karakter).
   `description` **maksimal 200 karakter**. Kalau lebih, upload di claude.ai akan ditolak.
2. Tambahkan dokumentasi `<nama>.md` di root, mengikuti format `waguri.md`, `alya.md`, dan `marin.md`.
3. Tambahkan baris di tabel README.

## Aturan wajib

- **Tidak ada credential di repo.** Token, API key, chat ID, password, dan URL
  privat dibaca dari environment variable, bukan ditulis di file.
  Fitur yang butuh credential harus mati secara default kalau env var kosong.
- **Tidak ada data pribadi**: nama asli, nama kantor, atau path lokal (`C:\Users\...`, `D:\project\...`).
- **Persona tidak bocor ke hasil kerja.** Kode, commit, dan dokumen yang dihasilkan skill harus profesional.
- **Persona tetap jujur**: tidak mengarang, mengaku AI kalau ditanya, berani menyampaikan keberatan.

## Cek sebelum PR

Build ZIP untuk memastikan skill bisa di-upload ke claude.ai:

```bash
python scripts/build-zips.py
```

Scan credential:

```bash
grep -rnE "bot[0-9]{8,}:|AAE|AAF|api[_-]?key|secret|password|[A-Z]:\\(Users|project)" skills *.md
```

Hasilnya harus kosong, atau hanya berisi nama variabel dan contoh placeholder.

## Mengubah skill yang ada

- Jaga perubahan tetap fokus. Satu PR untuk satu perubahan perilaku.
- Jelaskan di PR: perilaku sebelum vs sesudah, dan kenapa.
- Update file dokumentasi `.md` yang terkait.
