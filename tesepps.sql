-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 20, 2022 at 07:25 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tesepps`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('1d0a182d1343');

-- --------------------------------------------------------

--
-- Table structure for table `hasil_tes`
--

CREATE TABLE `hasil_tes` (
  `id_hasil` bigint(20) NOT NULL,
  `nilai_ach` int(11) NOT NULL,
  `nilai_def` int(11) NOT NULL,
  `nilai_ord` int(11) NOT NULL,
  `nilai_exh` int(11) NOT NULL,
  `nilai_aut` int(11) NOT NULL,
  `nilai_aff` int(11) NOT NULL,
  `nilai_int` int(11) NOT NULL,
  `nilai_suc` int(11) NOT NULL,
  `nilai_dom` int(11) NOT NULL,
  `nilai_aba` int(11) NOT NULL,
  `nilai_nur` int(11) NOT NULL,
  `nilai_chg` int(11) NOT NULL,
  `nilai_end` int(11) NOT NULL,
  `nilai_het` int(11) NOT NULL,
  `nilai_agg` int(11) NOT NULL,
  `hasil_pekerjaan_ach` varchar(250) NOT NULL,
  `hasil_pekerjaan_def` varchar(250) NOT NULL,
  `hasil_pekerjaan_ord` varchar(250) NOT NULL,
  `hasil_pekerjaan_exh` varchar(250) NOT NULL,
  `hasil_pekerjaan_aut` varchar(250) NOT NULL,
  `hasil_pekerjaan_aff` varchar(250) NOT NULL,
  `hasil_pekerjaan_int` varchar(250) NOT NULL,
  `hasil_pekerjaan_suc` varchar(250) NOT NULL,
  `hasil_pekerjaan_dom` varchar(250) NOT NULL,
  `hasil_pekerjaan_aba` varchar(250) NOT NULL,
  `hasil_pekerjaan_nur` varchar(250) NOT NULL,
  `hasil_pekerjaan_chg` varchar(250) NOT NULL,
  `hasil_pekerjaan_end` varchar(250) NOT NULL,
  `hasil_pekerjaan_het` varchar(250) NOT NULL,
  `hasil_pekerjaan_agg` varchar(250) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hasil_tes`
--

INSERT INTO `hasil_tes` (`id_hasil`, `nilai_ach`, `nilai_def`, `nilai_ord`, `nilai_exh`, `nilai_aut`, `nilai_aff`, `nilai_int`, `nilai_suc`, `nilai_dom`, `nilai_aba`, `nilai_nur`, `nilai_chg`, `nilai_end`, `nilai_het`, `nilai_agg`, `hasil_pekerjaan_ach`, `hasil_pekerjaan_def`, `hasil_pekerjaan_ord`, `hasil_pekerjaan_exh`, `hasil_pekerjaan_aut`, `hasil_pekerjaan_aff`, `hasil_pekerjaan_int`, `hasil_pekerjaan_suc`, `hasil_pekerjaan_dom`, `hasil_pekerjaan_aba`, `hasil_pekerjaan_nur`, `hasil_pekerjaan_chg`, `hasil_pekerjaan_end`, `hasil_pekerjaan_het`, `hasil_pekerjaan_agg`, `user_id`) VALUES
(1, 94, 42, 40, 57, 46, 39, 44, 71, 50, 49, 40, 54, 29, 66, 62, 'Manager', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 1),
(2, 37, 97, 40, 95, 46, 39, 44, 71, 50, 49, 40, 54, 29, 66, 62, '-', 'Personal Staff', '-', 'Sales Management', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 5),
(5, 46, 52, 47, 66, 54, 48, 53, 77, 50, 49, 40, 54, 29, 66, 62, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 1),
(6, 46, 52, 47, 66, 54, 48, 53, 77, 50, 49, 40, 54, 29, 66, 62, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 1),
(7, 81, 86, 63, 92, 21, 12, 28, 50, 50, 41, 55, 70, 23, 66, 62, '-', 'Personal Staff', '-', 'Sales Management', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 4),
(8, 81, 86, 63, 92, 21, 12, 28, 50, 50, 41, 55, 70, 23, 66, 62, '-', 'Personal Staff', '-', 'Sales Management', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 5),
(9, 37, 0, 83, 29, 54, 81, 53, 77, 75, 81, 55, 46, 13, 66, 62, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 1),
(10, 29, 1, 83, 29, 54, 81, 53, 77, 75, 81, 55, 46, 13, 66, 62, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 3),
(11, 21, 52, 40, 87, 46, 39, 44, 65, 50, 56, 40, 46, 67, 66, 62, '-', '-', '-', 'Sales Management', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 6),
(12, 21, 18, 77, 29, 54, 81, 61, 96, 57, 69, 55, 24, 18, 66, 62, '-', '-', '-', '-', '-', '-', '-', 'Management Personalia', '-', '-', '-', '-', '-', '-', '-', 7),
(13, 56, 42, 33, 57, 70, 48, 92, 71, 57, 33, 26, 62, 52, 66, 62, '-', '-', '-', '-', '-', '-', 'Team Leader', '-', '-', '-', '-', '-', '-', '-', '-', 8),
(14, 4, 25, 47, 47, 70, 58, 53, 65, 37, 69, 40, 82, 23, 66, 62, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 10),
(16, 21, 0, 15, 29, 70, 81, 53, 50, 80, 9, 55, 87, 23, 66, 62, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 'Personal Staff / Customer Service', '-', '-', '-', 9),
(20, 46, 52, 47, 66, 54, 48, 53, 77, 50, 49, 40, 54, 29, 66, 62, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 11),
(21, 46, 52, 47, 66, 54, 48, 53, 77, 50, 49, 40, 54, 29, 66, 62, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 11),
(22, 46, 52, 47, 66, 54, 48, 53, 77, 50, 49, 40, 54, 29, 66, 62, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 11),
(29, 94, 42, 40, 57, 46, 39, 44, 71, 50, 49, 40, 54, 29, 66, 62, 'Manager', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 12),
(30, 91, 42, 33, 47, 37, 31, 44, 71, 50, 86, 40, 54, 29, 66, 62, 'Manager', '-', '-', '-', '-', '-', '-', '-', '-', 'Regional Staff', '-', '-', '-', '-', '-', 12);

-- --------------------------------------------------------

--
-- Table structure for table `percentile`
--

CREATE TABLE `percentile` (
  `id_percentile` bigint(20) NOT NULL,
  `score` int(11) DEFAULT NULL,
  `ach` int(11) DEFAULT NULL,
  `DEF` int(11) DEFAULT NULL,
  `ord` int(11) DEFAULT NULL,
  `exh` int(11) DEFAULT NULL,
  `aut` int(11) DEFAULT NULL,
  `aff` int(11) DEFAULT NULL,
  `int` int(11) DEFAULT NULL,
  `suc` int(11) DEFAULT NULL,
  `dom` int(11) DEFAULT NULL,
  `aba` int(11) DEFAULT NULL,
  `nur` int(11) DEFAULT NULL,
  `chg` int(11) DEFAULT NULL,
  `end` int(11) DEFAULT NULL,
  `het` int(11) DEFAULT NULL,
  `agg` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `percentile`
--

INSERT INTO `percentile` (`id_percentile`, `score`, `ach`, `DEF`, `ord`, `exh`, `aut`, `aff`, `int`, `suc`, `dom`, `aba`, `nur`, `chg`, `end`, `het`, `agg`) VALUES
(1, 28, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 99, 0),
(2, 27, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 99, 98, 0),
(3, 26, 0, 0, 0, 0, 0, 0, 0, 0, 99, 0, 99, 0, 98, 97, 0),
(4, 25, 0, 0, 99, 0, 0, 0, 0, 0, 98, 99, 98, 99, 97, 95, 0),
(5, 24, 99, 0, 98, 0, 99, 99, 99, 0, 97, 98, 96, 98, 94, 93, 99),
(6, 23, 98, 99, 96, 0, 98, 98, 98, 99, 95, 96, 93, 97, 90, 91, 98),
(7, 22, 97, 98, 94, 99, 97, 97, 97, 98, 93, 94, 90, 96, 86, 89, 97),
(8, 21, 94, 97, 91, 98, 95, 94, 95, 98, 89, 91, 86, 94, 81, 87, 96),
(9, 20, 91, 95, 88, 97, 92, 91, 92, 96, 85, 86, 81, 91, 74, 85, 94),
(10, 19, 86, 91, 83, 95, 88, 87, 87, 95, 80, 81, 76, 87, 67, 82, 91),
(11, 18, 81, 86, 77, 92, 84, 81, 82, 93, 75, 75, 70, 82, 59, 80, 87),
(12, 17, 74, 79, 71, 87, 77, 75, 77, 91, 69, 69, 63, 76, 52, 76, 82),
(13, 16, 65, 71, 63, 82, 70, 67, 69, 87, 63, 62, 55, 70, 44, 73, 76),
(14, 15, 56, 62, 55, 75, 62, 58, 61, 83, 57, 56, 47, 62, 37, 69, 69),
(15, 14, 46, 52, 47, 66, 54, 48, 53, 77, 50, 49, 40, 54, 29, 66, 62),
(16, 13, 37, 42, 40, 57, 46, 39, 44, 71, 44, 41, 33, 46, 23, 62, 54),
(17, 12, 29, 32, 33, 47, 37, 31, 36, 65, 37, 33, 26, 38, 18, 58, 46),
(18, 11, 21, 25, 26, 37, 29, 24, 28, 58, 31, 27, 20, 31, 13, 54, 37),
(19, 10, 15, 18, 20, 29, 21, 18, 21, 50, 25, 21, 15, 24, 10, 50, 29),
(20, 9, 10, 12, 15, 22, 15, 12, 15, 42, 19, 17, 11, 18, 7, 45, 22),
(21, 8, 6, 8, 11, 14, 10, 8, 10, 33, 14, 12, 7, 14, 5, 42, 16),
(22, 7, 4, 4, 8, 9, 7, 5, 6, 26, 9, 9, 5, 10, 3, 37, 11),
(23, 6, 2, 2, 5, 5, 3, 3, 4, 19, 6, 6, 2, 6, 2, 33, 8),
(24, 5, 1, 1, 3, 3, 2, 1, 2, 13, 3, 4, 1, 4, 1, 29, 5),
(25, 4, 0, 0, 1, 1, 1, 0, 1, 8, 2, 2, 0, 2, 0, 24, 2),
(26, 3, 0, 0, 0, 0, 0, 0, 0, 4, 1, 1, 0, 1, 0, 20, 1),
(27, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 15, 0),
(28, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 10, 0),
(29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0);

-- --------------------------------------------------------

--
-- Table structure for table `soal`
--

CREATE TABLE `soal` (
  `id_soal` bigint(20) NOT NULL,
  `pernyataan_a` varchar(1000) DEFAULT NULL,
  `pernyataan_b` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `soal`
--

INSERT INTO `soal` (`id_soal`, `pernyataan_a`, `pernyataan_b`) VALUES
(1, 'Saya suka menolong teman-teman saya, bila mereka dalam kesulitan.', 'Saya ingin melakukan pekerjaan apa asaja sebaik mungkin.'),
(2, 'Saya ingin mengetahui bagaimana pandangan orang - prang besar mengenai berbagai masalah yang menarik perhatian saya', 'Saya ingin menjnadi seorang ahli yang diakui dalam salah satu pekerjaan, jabatan atau bidang khusus.'),
(3, 'Saya ingin agar setiap pekeraan tulisan saya teliti, rapi dan tersusun dengan baik.', 'Saya ingin menjnadi seorang ahli yang diakui dalam salah satu pekerjaan, jabatan atau bidang khusus.'),
(4, 'Saya suka menceritakan cerita-cerita yang lucu dan lelucon-lelucon waktu pesta.', 'Saya ingin menulis roman atau sandiwara yang hebat.'),
(5, 'Saya ingin dapat berbuat sekehendak hati saya.', 'Saya ingin bisa mengatakan bahwa saya telah melakukan dengan baik suatu pekerjaan yang sulit.'),
(6, 'Saya ingin dapat memecahkan teka-teki dan persoalan - persoalan yang sukar bagi orang lain.', 'Saya suka mengikuti petunjuk - petunjuk dan melakukan apa yang diharapkan prang dari diri saya.'),
(7, 'Saya ingin mengalami hal - hal yang baru dan perubahan - perubahan dala kehidupan saya sehari - hari.', 'Saya suka menyatakan pada atasan - atasan saya, bahwa mereka telag melakukan sesuatu pekerjaan dengan baik, bila memang demikian menurut pikiran saya.'),
(8, 'Saya suka merencanakan dan mengatur detail - detail dari setiap pekerjaan yang harus saya lakukan.', 'Saya suka mengikuti petunjuk - petunjuk dan melakukan apa yang diharapkan orang dari diri saya.'),
(9, 'Saya ingin orang - orang memperhatikan dan memberikan komentar mengenai penampilan saya di depan umum.', 'Saya suka membaca riwayat hidup orang - orang besar.'),
(10, 'Saya suka mengelakkan keadaan - keadaan dimana saya diharapkan akan berlaku secara konvensional (kebiasaan umum).', 'Saya suka membaca riwayat hidup orang - orang besar.'),
(11, 'Saya ingin menjnadi seorang ahli yang diakui dalam salah satu pekerjaan, jabatan atau bidang khusus.', 'Saya ingin agar pekerjaan saya diatur dan direncanakan sebelum dimulai.'),
(12, 'Saya ingin mengetahui bagaimana pandangan orang - orang besar / ahli mengenai berbagai masalah yang menarik perhatian saya.', 'Seandainya saya harus bepergian, maka saya ingin segala sesuatunya telah direncanakan terlebih dahulu.'),
(13, 'Saya ingin mengerjakan sampai selesai setiap pekerjaan ataupun tugas yang telah saya mulai.', 'Saya ingin barang - barang saya tersusun rapi dan teratur di atas meja atau di dalam ruang kerja saya.'),
(14, 'Saya suka bercerita kepada orang - orang lain tentang petualangan - petualangan saya dan hal - hal aneh yang pernah saya alami.', 'Saya suka makan saya teratur dan ada waktu - waktu tertentu untuk makan.'),
(15, 'Saya ingin tidak tergantung dari orang lain dalam menentukan apa yang akan saya lakukan.', 'Saya ingin barang - barang saya tersusun rapi dan teratur di atas meja atau di dalam ruang kerja saya'),
(16, 'Saya ingin mengerjakan segala sesuatu lebih baik daripada orang - orang lain.', 'Saya suka menceritakan cerita - cerita lucu dan lelucon - lelucon waktu pesta.'),
(17, 'Saya suka mengikuti adat - istiadat dan menghindarkan melakukan hal - hal yang mungkin dianggap tidak wajar oleh orang - orang yang saya hormati.', 'Saya suka berbicara tentang hal - hal yang telah saya capai.'),
(18, 'Saya ingin agar hidup saya teratur sedemikian rupa sehingga berjalan lancar dan tanpa banyak perubahan - perubahan dalam rencana saya.', 'Saya suka bercerita kepada orang - orang lain tentang petualangan - petualangan saya dan hal - hal aneh yang pernah saya alami.'),
(19, 'Saya suka membaca buku - buku atau sandiwara - sandiwara yang terutama berkisar sekitar soal - soal sex.', 'Saya suka menjadi pusat perhatian dalam suatu kelompok.'),
(20, 'Saya suka mengecam orang - orang yang mempunyai kedudukan sebagai yang berwenang.', 'Saya suka menggunakan kata - kata yang maknanya seringkali tidak diketahui oleh orang lain.'),
(21, 'Saya ingin menyelesaikan tugas - tugas yang dianggap orang membutuhkan keterampilan serta usaha.', 'Saya ingin dapat berbuat sekehendak hati saya.'),
(22, 'Saya suka memuji seseorang yang saya kagumi.', 'Saya ingin merasa bebas untuk melakukan apa yang saya kehendaki.'),
(23, 'Saya suka menyimpan surat - surat, bon - bon dan kertas - kertas lain secara tersusun rapi dan menurut sistem tertenu.', 'Saya ingin tidak tergantung dari orang lain dalam menentukan apa yang akan saya lakukan.'),
(24, 'Saya suka mengajukan pertanyaan - pertanyaan yang setahu saya tak seorang pun akan bisa menjawabnya.', 'Saya suka mengecam orang - orang yang mempunyai kedudukan sebagai yang berwenang.'),
(25, 'Saya menjadi sedemikian marahny a sehingga rasanya ingin melemparkan dan\r\nmerusak barang - barang.', 'Saya suka mengelakan tanggung jawab dan kewajiban- kewajiban.'),
(26, 'Sayaingin berhasil dalam apa yang saya lakukan.', 'Saya suka membuat teman - teman baru.'),
(27, 'Saya suka mengikuti petunjuk - petunjuk dan melakukan apa yang diharapkan\r\norang lain dari diri saya.', 'Saya ingin mempunyai ikatan perasaan yang kuat dengan teman - teman saya.'),
(28, 'Saya ingin agar setiap pekerjaan tulisan saya teliti, rapi dan tersusun dengan baik.', 'Saya ingin membuat teman sebanyak mungkin.'),
(29, 'Sayasuka menceritakan cerita - cerita lucu dan lelucon - lelucon waktu pesta.', 'Saya suka berkirim surat pada teman - teman saya.'),
(30, 'Saya ingin dpat berbuat sekehendak hati saya.', 'Saya suka bersama - sama dengan teman - teman saya melakukan atau melayani\r\nsesuatu.'),
(31, 'Saya ingin dapat memecahkan teka - teki dan persoalan - persoalan yang suhar\r\nbagi orang lain.', 'Saya suka menilai orang - orang berdasarkan sebab - sebab mereka melakuhan\r\nsesuatu dan bukan atas dasar yang sesungguhnya mereka lakukan.'),
(32, 'Saya suka menerima pimpinan orang - orang yang saya kagumi.', 'Saya inglin menahami bagaimana porsalt trelman= reman saya dalem\r\nmenghadapi berbagai masalah.'),
(33, 'Saya suka makan saya teratur dan ada wakty- waktu tertentu untuk makan.', 'Saya suka mem pelajari dan menganalisa tingka laku orang-orang lain.'),
(34, 'Saya ingin mengatakan hal - hal yang diangeap lucu dan cerdas oleh orang-orang\r\nlain.', 'Sava suka menempatkan diri saya dalam kedudukan orang lain, dan\r\nmembayangkan bagaimana perasaan saya bila berada dalam keadaan yang sama.'),
(35, 'Saya ingin merasa bebas untuk melakukan apa yang saya kehendaki', 'Saya suka mengamati - amati bagaimana perasaan orang lain dalam keadaan\r\ntertentu.'),
(36, 'Saya ingin menyelesaikan tugas - tugas yang dianggap orang membutuhkan\r\nketerampilan serta usaha.', 'Saya ingin teman - teman meberikan dorongan - dorongan kepada saya bila saya\r\nmenghadapikegagalan.'),
(37, 'Dalam merencanakan sesuatu, saya ingin mendapat saran - saran dari orang\r\norang yang pendapatny a saya hormati.', 'Saya ingin diperlakukan dengan ramah oleh teman - teman saya.'),
(38, 'Saya ingin agar hidup saya teratur sedemikian rupa sehingga berjalan lancar dan\r\ntapa banyak perubahan - perubahan dalam rencana saya.', 'Saya ingin teman - teman saya merasa kasihan pada saya apabila saya sakit.'),
(39, 'Saya suka menjadi pusat perhatian dalam suatu kelompok.', 'Saya ingin agar teman - teman saya meributkan tentang diri saya apabila saya\r\nmendapatkan cedera atau sakit.'),
(40, 'Saya suka mengelakan keadaan - keadaan dimana saya diharapkan akan berlaku\r\nsecara konvensional (kebiasaan umum).', 'Saya ingin agar teman - teman saya bersimpati terhadap saya dan menghibur saya\r\nbila saya bersusah hati.'),
(43, 'Saya ingin menulis roman atau sandiwara yang hebat.', 'Bila saya termasuk dalam suatu kepanitian, saya ingin ditunjuk atau dipilih\r\nsebagaiketuanya.'),
(44, 'Bila saya berada dalam suatu kelompok, saya suka menerima pimpinan orang\r\nlain dalam memutuskan apa yang akan dilakukan oleh kelompok itu.', 'Saya ingin mengawasi dan mengarahkan tindakan - tindakan orang lain bilamana\r\nsaya mungkin.'),
(45, 'Saya suka menyimpan surat - surat, bon - bon dan kertas - kertas lainnya secara\r\ntersusun rapi dan menurut sistem tertentu.', 'Saya ingin menjadi salah seorang pemimpin dalam organisasi - organisasi atau\r\nkelompok -kelompok dimana saya menjadi anggotanya.'),
(46, 'Saya suka mengajukan pertanyaan - pertanyaan yang setahu saya tak seorang pun\r\nakan bisa menjawabnya.', 'Saya suka mengatakan pada orang - orang lain bagaimana mereka harus\r\nmelakukan pekerjaan mereka.'),
(47, 'Saya suka mengelakan tanggung jawab dan kewajiban - kewajiban.', 'Saya ingin diminta untuk menyelesaikan perdebatan - perdebatan atau\r\nperselisihan - perselisihan antara orang - orang lain.'),
(48, 'Saya ingin menjadi seorang ahli yang diakui dalam suatu pekerjaan, jabatan atau\r\nbidang yang khusus.', 'Saya merasa bersalah apabila saya telah melakukan sesuatu yang saya ketahui\r\nadalah tidak baik.'),
(49, 'Saya suka membaca riwayat hidup orang - orang besar.', 'Saya merasa bahwa saya harus mengakui hal - hal yang telah saya lakukan dan\r\nsaya anggap tidak baik'),
(50, 'Saya suka merencakan dan mengatur detail - detail setiap pekerjaan yang harus\r\nsaya lakukan.', 'Bila keadaan kurang menguntungkan bagi saya, maka saya merasa bahwa saya\r\nharus lebih disalahkan daripada orang lain.'),
(51, 'Saya suka menggunakan kata - kata yang maknanya sering tidak diketahui oleh\r\norang lain.', 'Saya merasa dalam banyak hal, saya kalah bila dibandingkan dengan orang\r\norang lain.'),
(52, 'Saya suka mengecam orang - orang yang mempunyai kedudukan sebagai yang\r\nberwenang.', 'Saya merasa canggung di tengah - tengah orang - orang lain yang saya anggap\r\nsebagai atasan saya.'),
(53, 'Saya ingin melakukan pekerjaan apa saja sebaik mungkin.', 'Saya suka menolong orang - orang yang tidak begitu beruntun g seperti saya.'),
(54, 'Saya ingin mengetahui bagaimana pandangan orang - orang besar mengenai\r\nberbagai masalah yang menarik perhatian saya.', 'Saya suka bermurah hati terhadap teman - teman saya.'),
(55, 'Saya suka membuat rencana sebelum memulai pekerjaan yang sulit.', 'Saya suka memberi pertolongan - pertolongan kecil kepada teman - teman saya.'),
(56, 'Saya suka bercerita kepada orang - orang lain tentang petualangan - petualangan\r\nsaya dan hal - hal aneh yang saya alami.', 'Saya ingin teman - teman saya mempercayai saya dan menceritakan kesulitan -\r\nkesulitan mereka kepada saya.'),
(57, 'Saya suka menyatakan pendapat saya tentang berbagai hal.', 'Saya suka memaafkan teman - teman saya yang kadang - kadang mungkin\r\nmenyakiti hati saya.'),
(58, 'Saya ingin mengerjakan segala sesuatu lebih baik daripada orang - orang lain.', 'Saya suka makan di restoran - restoran yang baru atau asing.'),
(59, 'Saya suka mengikuti adat istiadat dan menghindarkan untuk melakukan hal - hal\r\nyang mungkin dianggap tidak wajar oleh orang- orang yang saya hormati.', 'Saya suka mengikuti mode - mode baru.'),
(60, 'Saya in in pekerjaan saya diatur dan direncanakan sebelum dimulai.', 'Saya suka bepergian melihat - lihat daerah pedalaman.'),
(61, 'Saya ingin orang- orang memperhatikan dan memberikan komentar mengenai\r\npenampilan saya di depan umum.', 'Saya suka berkeliling di pedalaman dan tinggal di berbagai tempat.'),
(62, 'Saya ingin tidak tergantung dari orang lain dalam menentukan apa yang akan\r\nsaya lakukan.', 'Saya suka mengerjakan hal - hal yang baru dan lain.'),
(63, 'Saya ingin bisa mengatakan bahwa saya telah melakukan dengan baik sesuatu\r\npekerjaan yang sulit.', 'Saya suka bekerja keras pada tiap pekerjaan yang saya hadapi.'),
(64, 'Saya suka mengatakan pada atasan - atasan saya bahwa mereka telah melakukan\r\nsesuatu pekerjaan dengan baik, bila memang demikian halnya, menurut pikiran\r\nsaya.', 'Saya ingin menyelesaikan pekerjaan satu per satu sebelum memulai yang\r\nlainnya.'),
(65, 'Seandainya saya harus bepergian, maka say ingin agar segala sesuatunya telah\r\ndirencanakan terlebih dahulu.', 'Saya suka mengerjakan teka - teki atau memecahkan persoalan - persoalan\r\nsampai selesai.'),
(66, 'Saya kadang - kadang suka melakukan hal - hal hanya untuk melihat bagaimana\r\neffeknya terhadap orang lain.', 'Saya suka bertahan menghadapi suatu pekerjaan atau masalah, sekalipun\r\ntampaknya seolah -olah saya tidak akan berhasil.'),
(67, 'Saya suka melakukan hal - hal yang dianggap orang lain tidak sesuai dengan adat\r\nkebiasaan.', 'Saya ingin bekerja berjam - jam tanpa diganggu.'),
(68, 'Saya ingin mengerjakan sesuatu yang berarti.', 'Saya suka mencium orang yang menarik dari lawan jenis saya.'),
(69, 'Saya suka memuji seseorang yang saya kagumi.', 'Saya ingin dianggap punya daya tarik fisik oleh orang-orang dari lawn jenis\r\nsaya.'),
(70, 'Saya ingin barang-barang saya tersusun rapi dan teratur di atas meja atau di\r\ndalam ruang kerja saya.', 'Saya suka jatuh cinta pada seseorang dari lawan jenis saya.'),
(71, 'Saya suka berbicara tentang hal-hal yang telah saya capai.', 'Saya suka mendengarkan atau menceritakan lelucon-lelucon yang terutama\r\nberkisar soal sex.'),
(72, 'Saya ingin melakukan hal-hal dengan cara saya sendiri tapa menghiraukan apapun.', 'Saya suka membaca buku-buku dan sandiwara yang terutama berkisar sekitar\r\nsoal sex.'),
(73, 'Saya ingin menulis roman atau sandiwara yang hebat.', 'Saya suka menyerang pendirian-pendirian yang bertentangan dengan pendirian\r\nsaya.'),
(74, 'Bila saya berada dalam suatu kelompok, saya suka menerima pimpinan orang\r\nlain dalam memutuskan apa yang akan dilakukan oleh kelompok.', 'Saya rasanya ingin mengecam seseorang di muka umum bila orang itu memang\r\npatutmenerimanya.'),
(75, 'Saya ingin agar hidup saya teratur sedemikian rupa sehingga berjalan lancar dan\r\ntapa banyak perubahan dalam rencana-rencana saya.', 'Saya menjadi sedemikian marahnya sehingga rasanya ingin melemparkan dan\r\nmerusak barang-barang.'),
(76, 'Saya suka mengajukan pertanyaan-pertanyaan yang setahu saya, tak seorangpun\r\nakan bisa menjawabnya.', 'Saya suka mengatakan kepada orang-orang lain bagaimana pendapat saya\r\nmengenai mereka.'),
(77, 'Saya suka mengelakkan tanggung jawab dan kewajiban-kewajiban.', 'Saya rasanya ingin memperolok-olok orang-orang yang melakukan hal-hal yang saya anggap bodoh.'),
(78, 'Saya ingin loyal terhadap terhadap teman-teman saya.', 'Saya ingin melakukan pekerjaan apa saja sebaik mungkin.'),
(79, 'Saya suka mengamat-amati bagaimana perasaan orang lain dalam suatu keadaan.', 'Saya ingin bisa mengatakan bahwa saya telah melakukan dengan baik sesuatu pekerjaan yang sulit.'),
(80, 'Saya ingin teman-teman saya memberi dorongan kepada saya bila saya\r\nmenghadapikegagalan.', 'Saya ingin bisa mengerjakan segala sesuatu lebih baik dari pada orang-orang\r\nlain.'),
(81, 'Saya ingin menjadi salah seorang pemimpin dalam organisasi-organisasi atau kelompok-kelompok di mana saya menjadi \r\nanggota.', 'Saya ingin bisa mengerjakan segala sesuatu lebih baik dari pada orang-orang\r\nlain.'),
(82, 'Bila keadaan kurang menguntungkan bagi saya, maka saya merasa bahwa saya harus lebih disalahkan dari pada orang lain.', 'Saya ingin dapat memecahkan teka-teki dan persoalan-persoalan yang sukar bagi orang lain.'),
(83, 'Saya suka melakukan sesuatu untuk teman-teman saya.', 'Dalam merencanakan sesuatu saya ingin mendapat saran-saran dari orang-orang yang pendapatnya saya hormati.'),
(84, 'Saya suka menempatkan diri saya ke dalam kedudukan orang lain dan membayangkan bagaimana perasaan saya bila berada dalam keadaan yang sama.', 'Saya suka mengatakan kepada atasan-atasan saya bahwa mereka telah\r\nmelakukan sesuatu pekerjaan dengan baik, bila menurut pikiran saya memang demikian halnya.'),
(85, 'Saya ingin agar teman-teman saya menunjukan simpati dan pengertian bila saya mengalamikesukaran kesukaran', 'Saya ingin menyelesaikan tugas - tugas yang dianggap orang memburuhkan\r\nketerampilan serta usaha.'),
(86, 'Bila saya termasuk dalam suatu kepanitiaan, saya ingin ditunjukan atau dipilin sebagai ketuanya.', 'Bila saya berada dalam suatu kelompok, saya suka menerima pimpinan orang\r\nlain dalam memutuskan apa yang akan dilakukan oleh sekelompok itu.'),
(87, 'Apabila saya melakukan sesuatu hal yang salah, saya merasa bahwa untuk itu saya harus dihukum.', 'Saya suka mengikuti adat istiadat dan menghindarkan untuk melakukan hal-hal yang mungkin dianggap tidak wajar oleh orang-orang yang saya hormati.'),
(88, 'Saya suka bersama-sama dengan teman-teman saya melakukan atau menjalani sesuatu.', 'Saya suka membuat perencanaan sebelum memulai pekerjaan yang sulit.'),
(89, 'Saya ingin memahami bagaimana perasaan teman-teman saya dalam menghadapi berbagai masalah.', 'Seandainya saya harus berpergian, maka saya ingin agar segala sesuatunya telah direncanakan terlebih dahulu.'),
(90, 'Saya ingin diperlakukan ramah oleh teman-teman saya.', 'Saya ingin pekerjaan saya diatur dan direncanakan sebelum dimulai.'),
(91, 'Saya ingin dianggap sebagai pemimpin oleh orang - orang lain.', 'Saya suka menyimpan surat - surat, bon - bon dan kertas - kertas lain secara\r\ntersusun rapi dan menurut sistem tertentu.'),
(92, 'Saya merasa bahwa pilu hati dan kesusahan yang telah saya alami lebih banyak membawa kebaikan daripada kerugian bagi saya.', 'Saya ingin agar hidup saya teratur sedemikian rupa sehingga berjalan lancar dan\r\ntapa banyak perubahan dalam rencana - rencana saya.'),
(93, 'Saya ingin mempunyai ikatan perasaan yang kuat dengan teman -teman saya.', 'Saya ingin mengatakan hal -hal yang dianggap lucu dan cerdas oleh orang - orang lain.'),
(94, 'Saya suka merenungkan kepribadian teman - teman saya dan mencoba mengerti\r\nsebab- sebab yang menjadikan mereka sebagaimana terlihat.', 'Saya kadang - kadang suka melakukan hal - hal hanya untuk melihat bagaimana\r\neffeknya terhadap orang - orang.'),
(95, 'Saya ingin agar teman - teman saya meributkan tentang diri saya bila saya mendapat cedera atau sakit.', 'Saya suka berbicara tentang hal - hal yang telah saya capai.'),
(96, 'Saya suka mengatakan kepada orang - orang bagaimana mereka harus\r\nmelakukan pekerjaan mereka.', 'Saya suka menjadi pusat perhatian dalam suatu kelompok.'),
(97, 'Saya merasa canggung di tengah orang - orang yang say a anggap sebagai atasan\r\nsaya.', 'Saya suka menggunakan kata - kata yang maknanya sering tidak diketahui oleh\r\norang lain.'),
(98, 'Saya lebih suka mengerjakan sesuatu bersama - sama dengan teman - teman saya\r\ndaripada sendirian.', 'Saya suka menyatakan pendapat saya tentang berbagai hal.'),
(99, 'Saya suka mempelajari dan menganalisa tingkah laku orang - orang lain.', 'Saya suka melakukan hal - hal yang dianggap orang lain tidak sesuai dengan adat kebiasaan.'),
(100, 'Saya ingin agar teman - teman saya merasa kasihan pada saya bila saya sakit.', 'Saya suka mengelakkan keadaan diman saya diharapkan akan berlaku secara\r\nkonvensional (kebiasaan umum).'),
(101, 'Saya ingin mengawasi dan mengarahkan tindakan - tindakan orang lain bilamana saja mungkin.', 'Saya suka melakukan hal - hal dengan cara saya sendiri tanpa menghiraukan apa\r\nyang mungkin dipikirkan orang lain.'),
(102, 'Saya merasa bahwa dalam banyak hal saya kalah bila dibandingkan dengan\r\norang lain.', 'Saya suka mengelakkan tanggung jawab dan kewajiban - kewajiban.'),
(103, 'Saya ingin berhasil dalam apa yang saya lakukan.', 'Saya suka membuat teman - teman baru.'),
(104, 'Saya suka menganalisa perasaan - perasaan saya dan sebab - sebab mengapa saya melakukan sesuatu.', 'Saya ingin membuat teman saya sebanyak mungkin.'),
(105, 'Saya ingin agar teman -teman saya membantu apabila saya mengalami kesulitan.', 'Saya suka melakukan sesuatu untuk teman - teman saya.'),
(106, 'Saya suka memperdebatkan pendirian saya bila diserang oleh orang- orang lain.', 'Saya suka berkirim surat kepada teman - teman saya.'),
(107, 'Saya merasa bersalah apabila saya telah melakukan sesuatu hal yang saya\r\nketahui adalah tidak baik.', 'Saya ingin mempunyai ikatan perasaan yang kuat dengan teman - teman saya.'),
(108, 'Saya suka bersama - sama dengan teman - teman saya melakukan atau menjalani\r\nsesuatu.', 'Saya suka menganalisa perasaan - perasaan saya dan sebab - sebab mengapa saya\r\nmelakukan sesuatu.'),
(109, 'Saya suka menerima pimpinan orang - orang yang saya kagumi.', 'Saya ingin memahami perasaan teman - teman saya dalam menghadapi berbagai\r\nmasalah.'),
(110, 'Saya ingin agar teman - teman saya dengan gembira memberikan pertolongan -\r\npertolongan kecil kepada saya.', 'Saya suka menilai orang - orang berdasarkan sebab - sebab mereka melakukan sesuatu dan bukannya atas dasar apa yang sesungguhnya mereka lakukan.'),
(111, 'Bila saya berada dalam suatu kelompok, saya ingin menentukan apa yang akan kami kerjakan.', 'Saya suka meramalkan bagaimana teman - teman saya akan bertindak dalam\r\nberbagai situasi.'),
(112, 'Saya lebih suka bila saya mengalah dan menghindarkan perkelahian daripada bila saya mencoba memaksakan kemauan saya.', 'Saya suka menganalisa perasaan - perasaan saya dan sebab - sebab mengapa saya melakukan sesuatu.'),
(113, 'Saya suka membuat teman - teman baru.', 'Saya ingin agar teman - teman saya membantu saya bila saya mengalami\r\nkesulitan.'),
(114, 'Saya suka menilai orang-orang berdasarkan sebab-sebab mereka melakukan sesuatu dan bukan atas dasar apa yang sesungguhnya mereka lakukan.', 'Saya ingin teman-teman saya banyak menunjukan rasa sayang mereka terhadap\r\nsaya.'),
(115, 'Saya ingin agar hidup saya teratur sedemikian rupa sehingga berjalan lancar dan tanpa banyak perubahan-perubahan dalam rencana-rencana saya.', 'Saya ingin agar teman-teman saya merasa kasihan pada saya apabila saya sakit.'),
(116, 'Saya ingin diminta untuk menyelesaikan perdebatan-perdebatan atau perselisihan-perselisihan antara orang-orang lain.', 'Saya ingin agar teman-teman saya dengan gembira memberikan pertolongan-\r\npertolongan kecil pada saya.'),
(117, 'Saya merasa saya harus mengakui hal-hal yang telah saya lakukan dan saya anggap tidak baik.', 'Saya ingin teman-teman saya bersimpati terhadap saya dan menghibur saya bila saya bersusah hati.'),
(118, 'Saya lebih suka melakukan sesuatu dengan teman saya dari pada sendirian.', 'Saya suka memperdebatkan pendirian saya bila diserang orang lain.'),
(119, 'Saya suka merenungkan kepribadian teman-teman saya dan mencoba mengerti\r\nsebab-sebab yang menjadikan mereka sebagaimanan terlihat.', 'Saya ingin mampu membujuk dan mempengaruhi orang lain untuk melakukan\r\napa yang saya kehendaki.'),
(120, 'Saya ingin teman-teman saya bersimpati terhadap saya dan menghibur saya bila saya bersusah hati.', 'Bila saya berada dalam suatu kelompok, saya ingin menentukan apa yang akan kami lakukan'),
(121, 'Saya suka mengajukan pertanyaan yang setahu saya tak seorang pun akan bisa menjawabnya.', 'Saya suka menyatakan kepada orang lain bagaimana mereka harus melakukan pekerjaan mereka.'),
(122, 'Saya merasa canggung di tengah orang-orang yang saya anggap sebagai atasan saya.', 'Saya ingin mengawasi dan mengarahkan tindakan-tindakan orang lain bilamana saja mungkin.'),
(123, 'Saya suka bergaul dalam lingkungan di mana para anggotanya mempunyai\r\nperasaan-perasaan yang akrab satu sama lainnya.', 'Saya merasa bersalah apabila saya telah melakukan sesuatu hal yang saya ketahui\r\nadalah tidak baik.'),
(124, 'Saya suka menganalisa perasaan orang lain dan sebab-sebab mereka melakukan sesuatu.', 'Saya merasa sedih oleh ketidakmampuan saya sendiri untuk menghadapi\r\nperbagai macam keadaan.'),
(125, 'Saya ingin agar teman-teman saya merasa kasihan pada saya bila saya sakit.', 'Saya lebih suka bila saya mengalah dan menghindarkan perkelahian dari pada\r\nbila saya mencoba memaksakan kemauan saya.'),
(126, 'Saya ingin mampu membujuk dan mempengaruhi orang lain untuk melakukan\r\napa yang saya kehendaki.', 'Saya merasa sedih oleh ketidakmampuan saya sendiri untuk menghadapi\r\nberbagai macam keadaan.'),
(127, 'Saya suka mengecam orang-orang yang mempunyai kedudukan sebagai yang\r\nberwenang.', 'Saya merasa canggung di tengah orang-orang yang saya anggap sebagai atasan saya.'),
(128, 'Saya suka bergaul dalam lingkungan dimana para anggotanya mempunyai\r\nperasaan yang akrab satu sama lainnya.', 'Saya suka menolong teman-teman saya bila mereka berada dalam kesulitan.'),
(129, 'Saya suka menganalisa perasaan-perasaan saya dan sebab-sebab mengapa saya melakukan sesuatu.', 'Saya suka menunjukan simpati saya kepada teman-teman saya bila mereka mendapat cedera atau sakit.'),
(130, 'Saya ingin agar teman - teman saya membantu saya bila saya mengalami\r\nkesulitan.', 'Saya suka memperlakukan orang lain dengan ramah dan simpatik.'),
(131, 'Saya ingin menjadi salah seorang pemimpin dalam organisasi atau kelompok\r\nkelompok yang saya masuki.', 'Saya suka menunjukan sumpati saya kepada teman - teman saya bila mereka\r\nmendapat cedera atau sakit.'),
(132, 'Saya merasa bahwa pilu hati dan penderitaan yang telah saya alami lebih banyak membawa kebaikan daripada kerugian bagi diri saya.', 'Saya suka berlaku sangat ramah terhadap teman - teman saya.'),
(133, 'Saya ingin agar teman - teman saya menunjukan simpati dan pengertian bila saya mengalamikesukaran-kesukaran.', 'Saya suka bertemu dengan orang - orang baru.'),
(134, 'Saya suka memperdebatkan pendirian say bila diserang orang lain.', 'Saya ingin mengalami hal - hal yang baru dan perubahan - perubahan dalam bentuk kehidupan saya sehari-hari.'),
(135, 'Saya lebih suka bila saya mengalah dan menghindarkan perkelahian daripada bila saya mencoba memaksakan kemauan saya.', 'Saya suka berkeliling di pedalaman dan tinggal di berbagai tempat.'),
(136, 'Saya suka melakukan sesuatu untuk teman - teman saya.', 'Bila saya harus melakukan suatu tugas, saya ingin mengerjakannya sampai\r\nselesai.'),
(137, 'Saya suka menganalisa perasaan orang lain dan sebab - sebab mengapa mereka melakukan sesuatu.', 'Saya ingin menghindarkan gangguan bila saya sedang bekerja.'),
(138, 'Saya ingin agar teman - teman saya dengan gembira memberikan pertolongan\r\nkecil kepada saya.', 'Saya suka bekerja sampai jauh malam untuk menyelesaikan suatu pekerjaan.'),
(139, 'Saya ingin dianggap sebagai seorang pemimpin oleh orang - orang lain.', 'Saya ingin bekerja berjam - jam tanpa diganggu.'),
(140, 'Bila saya melakukan sesuatu yang salah, saya merasa bahwa untuk itu saya harus dihukum.', 'Saya suka bertahan menghadapi suatu pekerjaan atau masalah sekalipun tampaknya seolah - olah saya tak akan berhasil.'),
(141, 'Saya ingin loyal terhadap teman - teman saya.', 'Saya suka bepergian dengan (untuk laki -laki) wanita - wanita yang menarik\r\n(untuk wanita) laki - laki yang menarik.'),
(142, 'Saya suka meramalkan bagaimana teman - teman saya akan bertindak dalam\r\nberbagai situasi.', 'Saya suka ikut serta dalam diskusi - diskusi tentang sex dan aktivitas sexual'),
(143, 'Saya ingin teman - teman saya banyak menunjukan rasa sayang mereka terhadap saya.', 'Saya suka nafsu saya terangsang.'),
(144, 'Bila saya berada dalam suatu kelompok, saya ingin menentukan apa yang akan kami kerjakan.', 'Saya suka bersibuk diri dengan aktivitas - aktivitas sosial bersama - sama dengan orang - orang dari lawan jenis saya.'),
(145, 'Saya merasa sedih olch ketidakmampuan saya sendiri untuk menghadapi\r\nberbagai macam keadaan.', 'Saya suka membaca buku - buku dan sandiwara - sandiwara yang terutama\r\nberkisar sekitar soal-soal sex.'),
(146, 'Sayasuka berkirim surat Kepada teman - teman saya.', 'Saya suka membaca berita - berita surat kabar tentang pembunuhan\r\npembunuhan dan lain - lain perbuatan kekerasan.'),
(147, 'Saya suka meramalkan bagaimana teman - teman saya akan bertindak dalam\r\nberbagai situasi.', 'Saya suka menyerang pendirian yang bertentangan dengan pendirian saya.'),
(148, 'Saya ingin teman - teman saya meributkan tentang diri saya, bila saya mendapat cedera atau sakit.', 'Saya rasanya ingin menyalahkan orang lain bila keadaannya kurang\r\nmenguntungkan bagi saya.'),
(149, 'Saya suka menyatakan Kepada orang - orang lain bagaimana mereka harus\r\nmelakukan pekerjaan mereka.', 'Saya rasanya ingin membalas dendam bila seseorang menghina saya.'),
(150, 'Saya merasa bahwa dalam banyak hal saya kalah bila dibandingkan dengan\r\norang lain.', 'Saya rasanya ingin menhardik orang lain bila saya berbeda pendapat dengan mereka.'),
(151, 'Saya suka menolong teman - teman saya bila mereka berada dalam kesulitan.', 'Saya ingin melakukan pekerjaan apa saja sebaik mungkin.'),
(152, 'Saya suka bepergian melihat - lihat daerah pedalaman.', 'Saya ingin menyelesaikan tugas - tugas yang dianggap orang membutuhkan keterampilan serta usaha.'),
(153, 'Saya suka bekerja keras pada tiap pekerjaan yang saya hadapi.', 'Saya ingin mengerjakan sesuatu yang berarti.'),
(154, 'Saya suka bepergian dengan (untuk laki- laki) wanita - wanita yang menarik (untuk wanita) laki - laki yang menarik.', 'Saya ingin berhasil dalam apa yang saya lakukan.'),
(155, 'Saya suka membaca berita\r\n- berita surat kabar tentang pembunuhan\r\npembunuhan dan lain - lain perbuatan kekerasan.', 'Saya ingin menulis roman atau sandiwara yang hebat.'),
(156, 'Saya suka memberikan pertolongan - pertolongan kecil kepada teman - teman saya.', 'Dalam merencanakan sesuatu, saya ingin mendapat saran - saran dari orang orang yang pendapatnya saya hormati.'),
(157, 'Saya ingin mengalami hal - hal yang baru dan perubahan - perubahan dalam kehidupan saya sehari-hari.', 'Saya suka menyatakan pada atasan saya bahwa mereka telah melakukan suatu pekerjaan dengan baik, bila memang demikian halnya menurut pikiran saya.'),
(158, 'Saya suka bekerja sampai jauh malam untuk menyelesaikan suatu pekerjaan.', 'Saya suka memuji seseorang yang saya kagumi.'),
(159, 'Saya suka nafsu saya terangsang.', 'Saya suka menerima pimpinan dari orang - orang yang saya kagumi.'),
(160, 'Saya rasanya ingin membalas dendam bila seseorang menghina saya.', 'Bila saya berada dalam suatu kelompok, saya suka menerima pimpinan orang\r\nlain dalam memutuskan apa yang akan dilakukan oleh kelompok itu.'),
(161, 'Saya suka bermurah hati terhadap teman - teman saya.', 'Saya suka membuat rencana sebelum memula pekerjaan yang sulit.'),
(162, 'Saya suka bertemu dengan orang - orang baru.', 'Saya ingin agar setiap pekerjaan tulisan say a teliti, rapidan tersusun dengan baik'),
(163, 'Saya ingin mengerjakan sampai selesai setiap pekerjaan ataupun tugas yang telah saya mulai.', 'Saya ingin barang - barang saya tersusun rapi dan teratur di atas meja atau di dalam rang kerja saya.'),
(164, 'Saya ingin dianggap mempunyai data tarik fisik oleh orang - orang dari lawan jenis saya.', 'Saya suka merencanakan dan mengatur detail - detail dari setiap pekerjaan yang\r\nharus saya lakukan.'),
(165, 'Saya suka mengatakan kepada orang - orang lain bagaimana pendapat saya\r\nmengenai mereka', 'Saya suka makan saya teratur dan ada waktu tertentu untuk makan.'),
(166, 'Saya suka berlaku sangat ramah terhadap teman - teman saya.', 'Saya ingin mengatakan hal - hal yang dianggap lucu dan cerdas oleh orang - orang lain.'),
(167, 'Saya lebih suka mencoba pekerjaan yang baru dan lain daripada terus menerus melakukan pekerjaan yang saman.', 'Saya kadang - kadang suka melakukan hal - hal hanya untuk melihat bagaimana\r\nefeknya terhadap orang lain.'),
(168, 'Saya suka bertahan menghadapi satu pekerjaan atau masalah, sekalipun\r\ntampaknya seolah -olah saya tak akan berhasil.', 'Saya ingin orang - orang memperhatikan dan memberikan komentar mangenal penampilan saya di depan umum.'),
(169, 'Saya suka membaca buku - buku dan sandiwara - sandiwara yang terutama\r\nberkisar sekitar soal-soal sex.', 'Saya suka menjadi pusat perhatian dalam suatu kelompok.'),
(170, 'Saya rasanya ingin menyalahkan orang - orang lain bila keadaan kurang\r\nmenguntungkan bagi saya.', 'Saya suka mengajukan pertanyaan - pertanyaan yang setahu saya tak seorang pun akan bisa menjawabnya.'),
(171, 'Saya suka menunjukan simpati saya kepada teman - teman saya bila mereka\r\nmendapat cedera atau sakit.', 'Saya suka mengatakan pendapat saya tentang berbagai hal.'),
(172, 'Saya suka makan di restotan - restoran yang baru atau asing.', 'Saya suka melakukan hal - hal yang dianggap orang lain tidak sesuai dengan adat kebiasaan.'),
(173, 'Saya ingin menyelesaikan pekerjaan satu per satu sebelum memulai yang baru.', 'Saya ingin merasa bebas untuk melakukan apa yang sayakehendaki.'),
(174, 'Saya suka ikut serta dalam diskusi - diskusi tentang sex dan aktivitas sexual.', 'Saya ingin melakukan hal - hal dengan cara saya sendiri tanpa menghiraukan apa\r\nyang mungkin dipikirkan orang lain.'),
(175, 'Saya menjadi sedemikian marahnya sehingga rasanya ingin melemparkan dan\r\nmerusak barang - barang.', 'Saya suka mengelakan tanggung jawab dan kewajiban-kewajiban.'),
(176, 'Saya suka menolong teman - teman saya bila mereka berada dalam kesulitan.', 'Saya ingin loyal terhadap teman - teman saya.'),
(177, 'Saya suka melakukan hal - hal yang baru.', 'Saya suka membuat teman - teman baru.'),
(178, 'Bila saya harus melakukan suatu tugas, saya ingin mengerjakannya sampai\r\nselesai.', 'Saya suka bergaul dalam lingkungan dimana para anggotanya mempunyai\r\nperasaan yang akrab satu sama lainnya.'),
(179, 'Saya suka bepergian dengan (untuk laki- laki) wanita - wanita yang menarik (untuk wanita) laki - laki yang menarik.', 'Saya ingin membuat teman sebanyak mungkin.'),
(180, 'Saya suka menyerang pendirian - pendirian yang bertentangan dengan pendirian\r\nsaya', 'Saya suka berkirim surat kepada teman - teman saya.'),
(181, 'Saya suka bermurah hati kepada teman -teman saya.', 'Saya suka mengamati - amati bagaimana perasaan orang lain dalam suatu\r\nkeadaan tertentu.'),
(182, 'Saya suka makan di restoran - restoran baru atau asing.', 'Saya suka menempatkan diri saya dalam kedudukan orang lain, dan\r\nmembayangkan bagaimana perasaan saya bila berada dalam keadaan yang sama.'),
(183, 'Saya suka bekerja sampai jauh malam untuk menyelesaikan suatu pekerjaan.', 'Saya ingin memahami bagaimana perasaan teman\r\n- teman saya dalam\r\nmenghadapi berbagai masalah.'),
(184, 'Saya suka natsu saya terangsang.', 'Saya suka mempelajari dan menganalisa tingkah laku orang - orang lain.'),
(185, 'Saya rasanya ingin memperolok - olok orang - orang yang melakukan hal - hal yang saya anggap bodoh.', 'Saya suka meramalkan bagaimana teman - teman saya akan bertindak dalam\r\nberbagai situasi.'),
(186, 'Saya suka memaafkan teman - teman saya yang kadang - kadang mungkin\r\nmenyakiti hati saya.', 'Saya ingin teman - teman saya memberi dorongan kepada saya bila saya\r\nmengalamikegagalan.'),
(187, 'Saya suka bereksperimen dan mencoba hal - hal yang baru.', 'Saya ingin agar teman - teman saya menunjukan simpati dan pengertian bila saya mengalami kesukaran-kesukaran.'),
(188, 'Saya suka mengerjakan teka - teki atau memecahkan persoalan - persoalan\r\nsampai selesai.', 'Saya ingin diperlakukan dengan ramah oleh teman - teman saya.'),
(189, 'Saya ingin dianggap mempunyai daya tarik fisik oleh orang - orang dari lawan jenis saya.', 'Saya ingin teman - teman saya banyak menunjukan rasa sayang mereka terhadap saya.'),
(190, 'Saya rasanya ingin mengecam seseorang di muka umum bila orang itu memang patut menerimanya.', 'Saya ingin agar teman - teman saya meributkan diri saya apabila saya mendapat cedera atau sakit.'),
(191, 'Saya suka berlaku sangat ramah terhadap teman - teman saya.', 'Saya ingin dianggap sebagai pemimpin oleh orang - orang lain.'),
(192, 'Saya lebih suka mencoba pekerjaan - pekerjaan yang baru dan lain daripada terus\r\nmenerus melakukan pekerjaan yang sama.', 'Bila saya termasuk dalam suatu kepanitian, saya ingin ditunjuk atau dipilih sebagai ketua.'),
(193, 'Saya ingin mengerjakan sampai selesai setiap pekerjaan ataupun tugas yang telah saya mulai.', 'Saya ingin mampu membujuk dan mempengaruhi orang lain untuk melakukan\r\napa yang saya kehendaki.'),
(194, 'Saya suka ikutu serta dalam diskusi - diskusi tentang sex dan aktivitas sexual.', 'Saya ingin diminta untuk menyelesaikan perdebatan - perdebatan atau\r\nperselisihan - perselisihan antara orang - orang lain.'),
(195, 'Saya menjadi sedemikian marahnya sehingga rasanya ingin melemparkan dan\r\nmerusak barang - barang.', 'Saya suka mengatakan kepada orang lain bagaimana mereka harus melakukan\r\npekerjaan mereka.'),
(196, 'Saya suka berlaku sangat ramah terhadap teman - teman saya.', 'Bila keadaan kurang menguntungkan bagi saya, maka saya merasa bahwa saya harus lebih disalahkan dari pada orang - orang lain.'),
(197, 'Saya suka berkeliling di pedalaman dan tinggal di berbagai tempat.', 'Apabila saya melakukan sesuatu yang salah, saya merasa bahwa untuk itu saya harus dihukum.'),
(198, 'Saya suka bertahan menghadapi suatu pekerjaan atau masalah, sekalipun tampaknya seolah - olah saya tak akan berhasil.', 'Saya merasa bahwa pilu hati dan penderitaan yang telah saya alami lebih banyak membawa kebaikan daripada kerugian bagi saya.'),
(199, 'Saya suka membaca buku - buku dan sandiwara yang terutama berkisar sekitar\r\nsoal-soal sex.', 'Saya merasa bahwa saya harus mengakui hal - hal yang telah saya lakukan dan saya anggap tidak baik.'),
(200, 'Saya rasanya ingin menyalahkan orang lain bila keadaan kurang menguntungkan bagi saya', 'Saya merasa bahwa saya dalam banyak hal kalah bila dibandingkan dengan orang lain.'),
(201, 'Saya ingin melakukan setiap pekerjaan sebaik mungkin.', 'Saya suka menolong orang - orang lain yang tidak begitu beruntung seperti saya.'),
(202, 'Saya suka melakukan hal - hal yang baru dan lain.', 'Saya suka memperlakukan oran - orang lain dengan ramah dan simpatik.'),
(203, 'Bila saya harus melakukan suatu tugas, saya ingin mengerjakannya sampai\r\nselesai.', 'Saya suka menolong orang - orang lain yang tidak begitu beruntung seperti saya.'),
(204, 'Saya suka bersibuk diri dengan aktivitas - aktivitas sosial bersama - sama dengan orang - orang dari lawan jenis saya.', 'Saya suka memaalkan teman - teman saya yang kadang - kadang mungkin\r\nmenyakiti hati saya.'),
(205, 'Saya suka menyerang pendirian - pendirian yang bertentangan dengan pendirian saya.', 'Saya ingin teman - teman saya mempercayai saya dan menceritakan kesulitan -\r\nkesulitan mereka kepada saya.'),
(206, 'Saya suka memperlakukan orang lain dengan ramah dan simpatik.', 'Saya suka bepergian melihat - lihat ke daerah pedalaman.'),
(207, 'Saya suka mengikuti adat - istiadat dan menghindarkan melakukan hal - hal yang\r\nmungkin dianggap tidak wajaroleh orang - orang yang saya hormati.', 'Saya suka mengikuti mode baru.'),
(208, 'Saya suka bekerja keras pada tiap pekerjaan yang saya hadapi.', 'Saya ingin mengalami hal - hal yang baru dan perubahan - perubahan dalam kehidupan saya sehari - hari.'),
(209, 'Saya suka mencium orang - orang yang menarik dari lawan jenis saya.', 'Saya suka bereksperimen dan mencoba hal - hal yang baru.'),
(210, 'Saya rasanya ingin menghardik orang - orang lain bila saya berbeda pendapat dengan mereka', 'Saya suka mengikuti mode baru.'),
(211, 'Saya suka menolong orang - orang lain yang tidak begitu beruntung seperti\r\nsaya.', 'Saya ingin mengerjakan sampai selesai setiap pekerjaan atau tugas yang telah saya mulai.'),
(212, 'Saya suka berkeliling di pedalaman dan tinggal di berbagai tempat.', 'Saya ingin bekerja berjam -berjam tapa diganggu.'),
(213, 'Jika saya berpergian, saya ingin segala sesuatunya telah direncanakan terlebih,\r\ndahulu.', 'Saya suka mengerjakan teka - teki dan memecahkan persoalan - persoalan sampai selesai.'),
(214, 'Saya suka jatuh cinta pada seseorang dari lawan jenis saya.', 'Saya ingin mengerjakan pekerjaan satu per satu, sebelum memulai yang baru.'),
(215, 'Saya suka mengatakan kepada orang - orang lain bagaimana pendapat saya\r\nmengenai mereka.', 'Saya ingin menghindarkan diganggu bila saya sedang bekerja.'),
(216, 'Saya suka memberi pertolongan - pertolongan kecil kepada teman- teman saya.', 'Saya suka bersibuk diri dengan aktivitas - aktivitas sosial bersama - sama dengan\r\norang- orang dari lawan jenis saya.'),
(217, 'Saya suka bertemu dengan orang - orang yang baru.', 'Saya suka mencium orang- orang yang menarik dari lawan jenis saya.'),
(218, 'Saya ingin mengerjakan teka - teki atau memecahkan persoalan - persoalan sampai selesai.', 'Saya suka jatuh cinta kepada seseorang dari lawan jenis saya.'),
(219, 'Saya suka berbicara tentang hal - hal yang telah saya capai.', 'Saya suka mendengarkan atau menceritakan lelucon - lelucon yang terutama\r\nberkisar soal-soal sex.'),
(220, 'Saya rasanya ingin memperolok - olok orang - orang yang melakukan hal - hal yang saya anggap bodoh.', 'Saya suka mendengarkan atau menceritakan lelucon - lelucon yang terutamà\r\nberkisar soal-soal sex.'),
(221, 'Saya ingin teman - teman saya mempercayai saya dan menceritakan kesulitan-\r\nkesulitan mereka kepada saya.', 'Saya suka membaca berita - berita surat kabar tentang pembunuhan\r\npembunuhan dan lain - lain perbuatan kekerasan.'),
(222, 'Saya suka mengikuti mode baru.', 'Saya rasanya ingin mengecam seseorang di muka umum bila orang itu memang patut menerimanya.'),
(223, 'Saya ingin menghindarkan diganggu bila saya sedang bekerja.', 'Saya rasanya ingin menghardik orang - orang lain bila saya berbeda pendapat dengan mereka.'),
(224, 'Saya suka mendengarkan atau menceritakan lelucon - lelucon yang terutama\r\nberkisar sekitar soal - soal sex.', 'Saya rasanya ingin membalas dendam bila seseorang menghina saya.'),
(225, 'Saya suka mengelakkan tanggung jawab dan kewajiban - kewajiban.', 'Saya rasanya ingin memperolok - olok orang - orang yang melakukan hal - hal yang saya anggap bodoh.'),
(230, 'Saya lebih suka melakukan sesuatu bersama-sama teman saya daripada sendirian.', 'Saya suka bereksperimen dan melakukan hal-hal yang baru.'),
(231, 'Saya suka merenungkan kepribadian teman - teman saya dan mencoba memahami apa yang menjadikan mereka sebagaimana terlihat.', 'Saya lebih suka mencoba pekerjaan - pekerjaan yang baru dan lain daripada terus - menerus melakukan pekerjaan yang sama.');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` bigint(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(250) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `fullname` varchar(250) NOT NULL,
  `umur` int(11) NOT NULL,
  `jeniskelamin` varchar(50) NOT NULL,
  `image_file` varchar(100) NOT NULL,
  `roles` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `email`, `username`, `password`, `created_at`, `fullname`, `umur`, `jeniskelamin`, `image_file`, `roles`) VALUES
(1, 'attallaharelian5@gmail.com', 'areliannaufhal', 'arelian12', '2021-12-10 06:12:01', 'Attallah Arelian Naufhal', 21, 'Laki-Laki', '', ''),
(3, 'akubisamembuatmu@gmail.com', 'meskikautakcinta', '$2b$12$rxooWzaVhffGhPUgw434aehyPcv0z/m6n2XPtVMpVuhQEspItVaJi', '2022-01-16 08:08:02', 'Meski Kau Tak Cinta', 23, 'Laki-Laki', 'undraw_profile.svg', 'User'),
(4, 'alaarrantuka@gmail.com', 'Adzanlr', '$2b$12$mUxB9ZiYVPHhAJppKYtnY.RbkxXYrbT1IwhqrYVVDoVhjdGA3L7Zm', '2022-01-16 09:39:30', 'Adzan Larrantuka', 22, 'Laki-Laki', 'undraw_profile.svg', 'User'),
(5, 'ffadhell@gmail.com', 'farhanfadhell', '$2b$12$ralORY5EsuK8uzUOvpdeZeJ2e30f2iUg0iVx1WPWc2NdkfWiPjlum', '2022-01-16 10:08:12', 'Farhan Fadhell', 22, 'Laki-Laki', 'undraw_profile.svg', 'User'),
(6, 'irghiansyah12@gmail.com', 'irghian', '$2b$12$cbWTFibyuWE/4LYJLHoZjOb5uslOKx/84rtO5LrCbRvDtY8jnBZd2', '2022-01-16 11:04:52', 'Irghiansyah Haque', 22, 'Laki-Laki', 'undraw_profile.svg', 'User'),
(7, 'rahardi0805@gmail.com', 'rahardi', '$2b$12$JaRk0Jk3E/wqHULoEaWOfOYZ2ZBLX7hIVcf7WS0WW94gUDQIX12Ge', '2022-01-16 11:19:39', 'rahardi masmur', 22, 'Laki-Laki', 'undraw_profile.svg', 'User'),
(8, 'bennykhalid29@gmail.com', 'bennykhalid', '$2b$12$/ccC0hGrxjNhk0RHTWzbRuc/LiVfyN9/kvf878A.pZzSNCXd6ws7C', '2022-01-16 11:35:33', 'benny khalid', 22, 'Laki-Laki', 'undraw_profile.svg', 'User'),
(9, 'irvanguari9@gmail.com', 'Guarix', '$2b$12$NBLxoYF5FgiDZWnckULYv.kpQUzeGA2ZqQz.1NZKQ3RZu0YTT1Amy', '2022-01-16 12:36:35', 'Irvan Guari', 22, 'Laki-Laki', 'undraw_profile.svg', 'User'),
(10, 'areliannaufhal@gmail.com', 'arelian', '$2b$12$JYzGrtzCT/SLxK2Zu0O2legFI.qtzjRh3KbjzcMBDR/9Nlyr3XdTC', '2022-01-16 20:41:11', 'Arelian Naufhal', 21, 'Laki-Laki', 'undraw_profile.svg', 'User'),
(11, 'test@gmail.com', 'testing', '$2b$12$yO4Q76K9AdYtqqZf7KeBDOICt31NfWiBXQWespVfnoaaluyIsfS2u', '2022-01-18 10:50:18', 'testing terus', 21, 'Laki-Laki', 'undraw_profile.svg', 'User'),
(12, 'cobain@gmail.com', 'cobain', '$2b$12$r0gODOHb2XmrPh67754BWeSvb8z1Tx4Zp9KmNzjPyl5dPrVnkekpq', '2022-01-20 07:28:45', 'cobain dulu', 21, 'Laki-Laki', 'undraw_profile.svg', 'User');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `hasil_tes`
--
ALTER TABLE `hasil_tes`
  ADD PRIMARY KEY (`id_hasil`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `percentile`
--
ALTER TABLE `percentile`
  ADD PRIMARY KEY (`id_percentile`);

--
-- Indexes for table `soal`
--
ALTER TABLE `soal`
  ADD PRIMARY KEY (`id_soal`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_user_email` (`email`),
  ADD UNIQUE KEY `ix_user_username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `hasil_tes`
--
ALTER TABLE `hasil_tes`
  MODIFY `id_hasil` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `percentile`
--
ALTER TABLE `percentile`
  MODIFY `id_percentile` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `soal`
--
ALTER TABLE `soal`
  MODIFY `id_soal` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=232;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `hasil_tes`
--
ALTER TABLE `hasil_tes`
  ADD CONSTRAINT `hasil_tes_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
