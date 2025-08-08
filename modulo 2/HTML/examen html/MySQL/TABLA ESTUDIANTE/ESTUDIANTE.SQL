CREATE DATABASE IF NOT EXISTS Estudiantes;

CREATE TABLE Estudiantes (
    Cedula INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Apellido VARCHAR(100)
)

INSERT INTO Estudiantes(Cedula,Nombre,Apellido) VALUES 
    (16186354,'Robert','Borges'),
    (29767741,'Jimmy','Chacin'),
    (30604870,'Maria','Urdaneta'),
    (30820000,'Daniel','Sandoval'),
    (31279773,'Daviannys','Villalobos'),
    (31913070,'Humberto','Alvarez'),
    (32056687,'German','Suarez'),
    (32410084,'Julio','Pacheco'),
    (32636138,'Juan','Polania'),
    (33319114,'Gabriel','Suarez'),
    (33607751,'Roberti','Boscan'),
    (33893333,'Carlos','Moreno'),
    (33966984,'Jimn','Chacin'),
    (34544638,'Juan','Arrieta');
