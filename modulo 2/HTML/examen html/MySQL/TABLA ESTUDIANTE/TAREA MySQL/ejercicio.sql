CREATE TABLE musica (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    cantantes VARCHAR(100),
    genero VARCHAR(100),
    fecha_salida VARCHAR(100),
    colaboradores VARCHAR(100),
    album VARCHAR(100)
);
INSERT INTO musica (id,nombre,cantantes,genero,fecha_salida,colaboradores,album) 
values
(1,'0217','EduardoRz','RYB','2025','solista','borealis'),
(2,'JPN','Alvaro Diaz','pop','2024','solista','SAYONARA'),
(3,'BROKEBOI','frozouda','trap argentino','2021','solista','otra vision'),
(4,'Fly','frozouda','trap argentino','2021','solista','otra vision'),
(5,'La doble f con visa','frozouda','trap argentino','2025','solista','FRO!2'),
(6,'PIEL','NSQK','trap argentino','2025','solista','piel / krav magá'),
(7,'SIN PODERES','Alvaro Diaz','pop / argentina trap','2024','young cister','SAYONARA'),
(8,'aGaRRo La PLaTa','Duki','trap argentino','2025','Cluster','5202'),
(9,'Apretar+','mvrk','trap argentino','2025','solista','portate bien'),
(10,'BAD INTENCIONES','NSQK','electropop','2024','solista','atp'),
(11,'blamegame','nsqk','reggaeton','2024','paopao','atp'),
(12,'mami reza por mi','frozouda','trap argentino','2025','solista','FRO!'),
(13,'sugarrush','frozouda','trap argentino','2025','solista','FRO!'),
(14,'la cruz como a sampaoli','frozouda','trap argentino','2025','solista','FRO!'),
(15,'con los duros','frozouda','trap argentino','2025','pabloxo','FRO!');

UPDATE musica
SET genero = 'R&B'
WHERE id = 1;

UPDATE musica
SET colaboradores = 'con ella'
WHERE id = 2;

UPDATE musica
SET nombre = 'brokeboi'
WHERE id = 3;

UPDATE musica
SET fecha_salida = '2021/2022'
WHERE id = 4;

UPDATE musica 
SET nombre = 'ff con visa'
WHERE id = 5;

UPDATE musica
SET cantantes = 'nsqk'
WHERE id = 6;

UPDATE musica
SET nombre = 'sin poderes'
WHERE id = 7;

UPDATE musica
SET colaboradores = 'ClUsTeR'
WHERE id = 8;

UPDATE musica
SET nombre = 'ApRetAr +'
WHERE id = 9;

UPDATE musica
SET nombre = 'bad intenciones'
WHERE id = 10;

UPDATE musica
SET genero = 'ReggaetOon'
WHERE id = 11;

UPDATE musica
SET nombre = 'mami_reza_por_mi'
WHERE id = 12;

UPDATE musica
SET nombre = 'SUGARRUSH'
WHERE id = 13;

UPDATE musica
SET colaboradores = 'LA HIZO SOLO'
WHERE id = 14;

UPDATE musica
SET nombre = 'con_los_duros'
WHERE id = 15;

ALTER TABLE musica
DROP COLUMN genero

ALTER TABLE musica
DROP COLUMN nombre

ALTER TABLE musica
DROP COLUMN cantantes

ALTER TABLE musica
DROP COLUMN fecha_salida

ALTER TABLE musica
DROP COLUMN colaboradores

ALTER TABLE musica
ADD nombre_de_la_musica

ALTER TABLE musica
ADD nombre_del_cantante

ALTER TABLE musica
ADD genero_musical

SELECT COUNT(*) FROM musica;

SELECT SUM(id) FROM musica;

SELECT AVG(id) FROM musica;

SELECT MAX(id), MIN(id) FROM musica;

SELECT fecha_salida, COUNT(*) AS cuantos_son
FROM musica
GROUP BY fecha_salida;


