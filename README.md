# KALENDER JAWA

> Implementasi Kalender Jawa versi Walisongo

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Fitur

-	**Memperoleh tanggal jawa dari tanggal masehi sejak penanggalan Gregorian dimulai,** bahkan sejak tahun 1355 Masehi (Jauh sebelum diresmikan oleh Sultan Agung pada 1633)\*.
-	**Hampir abadi,** terus berlaku sampai dengan 2983 Masehi\*.
-	**Memperoleh Tanggal Pranata Mangsa** atas suatu tanggal (Masehi/Jawa).
-	**Memperoleh Hari, Pasaran, Wuku, dan Angka Neptu** atas suatu tanggal (Masehi/Jawa).
-	**Penghitungan *Pendhak* (hari setelah kejadian)**, misal untuk peringatan kelahiran/kematian.
-	Menyertakan _interface_ sederhana menggunakan Tkinter.

\* berdasarkan penelitian (baca:browsing) yang dilakukan, selengkapnya dalam catatan.

## Requirement

-	Python 3
-	Library : datetime, Tkinter

## Dokumentasi

Modul ini terdiri atas dua jenis class (masehi, jawa) yang masing-masing memiliki method:

-	**.neptu()** mengebalikan nilai (urip) hari dalam siklus 35 hari.
-	**.pawukon()** mengembalikan nama pawukon (hari, pasaran, wuku) atas suatu tanggal.
-	**.tgljawa()** mengembalikan nilai tanggal jawa atas suatu tanggal.
-	**.pendhak()** mengembalikan tanggal peringatan setelah kejadian (dalam masehi maupun jawa).
-	**.mangsa()** mengembalikan hari dan mangsa pada suatu tanggal masehi maupun jawa.

Dokumentasi lebih lanjut sedang dikerjakan. Dokumentasi juga dapat dilihat lebih lanjut dalam kode yang disediakan.

## Catatan dan Tautan Penting

-	Kalender dibuat berdasarkan artikel [Yudi Rohmad](https://www.caknun.com/author/yudi-rohmad/) dalam [caknun.com](https://www.caknun.com/2019/kalender-jowo-digowo-kalender-arab-digarap-kalender-barat-diruwat/)
-	Penghitungan kalender diadaptasi dari perhitungan kalender islam dan kalender bali oleh Reingold dan Dershowitz dalam [Calendrical Calculations](https://doi.org/10.1017/9781107415058) dengan penyesuaian terhadap perbedaan penghitungan tahun kabisat pada kalender Islam Timur Tengah dan Kalender Jawa, termasuk penentuan tanggal epoch untuk memulai perhitungan sebagaimana artikel sebelumnya.
-	Penghitungan Pranata Mangsa mengikuti Artikel Wikipedia \[[Citation needed](https://xkcd.com/285/)\]
- 	Karena keterbatasan Library Datetime, penanggalan sebelum dimulainya era gregorian akan mengalami pergeseran. [*selengkapnya*](https://docs.python.org/3/library/datetime.html#date-objects)
-	Penanggalan yang dihasilkan oleh paket ini mungkin akan berbeda dengan penanggalan lain seperti kalender hijriah atau kalender jawa Sultan Agungan (Asapon/Aboge).

## Lisensi

**[MIT license](http://opensource.org/licenses/mit-license.php)**