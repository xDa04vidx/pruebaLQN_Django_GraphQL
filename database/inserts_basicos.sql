-- ==========================
-- PLANETAS
-- ==========================
INSERT INTO planetas (nombre) VALUES
('Tatooine'),
('Alderaan'),
('Coruscant'),
('Naboo'),
('Dagobah'),
('Hoth'),
('Endor'),
('Mustafar');

-- ==========================
-- PERSONAJES
-- ==========================
INSERT INTO personajes (nombre, planeta_id) VALUES
('Luke Skywalker', 1),
('Leia Organa', 2),
('Han Solo', 1),
('Darth Vader', 1),
('Obi-Wan Kenobi', 3),
('Yoda', 5),
('Chewbacca', 1),
('Padmé Amidala', 4),
('Emperor Palpatine', 3),
('Boba Fett', 1);

-- ==========================
-- PELICULAS
-- ==========================
INSERT INTO peliculas (titulo, texto_apertura) VALUES
('A New Hope', 'It is a period of civil war...'),
('The Empire Strikes Back', 'It is a dark time for the Rebellion...'),
('Return of the Jedi', 'Luke Skywalker has returned to his home planet...'),
('The Phantom Menace', 'Turmoil has engulfed the Galactic Republic...'),
('Attack of the Clones', 'There is unrest in the Galactic Senate...'),
('Revenge of the Sith', 'War! The Republic is crumbling...');

-- ==========================
-- DIRECTORES
-- ==========================
INSERT INTO directores (nombre) VALUES
('George Lucas'),
('Irvin Kershner'),
('Richard Marquand');

-- ==========================
-- PRODUCTORES
-- ==========================
INSERT INTO productores (nombre) VALUES
('Gary Kurtz'),
('Rick McCallum');

-- ==========================
-- PELICULA_PLANETA (relación películas – planetas)
-- ==========================
-- A New Hope
INSERT INTO pelicula_planeta (pelicula_id, planeta_id) VALUES
(1,1),(1,2),(1,3);
-- The Empire Strikes Back
INSERT INTO pelicula_planeta (pelicula_id, planeta_id) VALUES
(2,5),(2,6),(2,3);
-- Return of the Jedi
INSERT INTO pelicula_planeta (pelicula_id, planeta_id) VALUES
(3,7),(3,1),(3,3);
-- The Phantom Menace
INSERT INTO pelicula_planeta (pelicula_id, planeta_id) VALUES
(4,4),(4,3);
-- Attack of the Clones
INSERT INTO pelicula_planeta (pelicula_id, planeta_id) VALUES
(5,4),(5,3);
-- Revenge of the Sith
INSERT INTO pelicula_planeta (pelicula_id, planeta_id) VALUES
(6,4),(6,8),(6,3);

-- ==========================
-- PELICULA_DIRECTOR
-- ==========================
INSERT INTO pelicula_director (pelicula_id, director_id) VALUES
(1,1),(2,2),(3,3),(4,1),(5,1),(6,1);

-- ==========================
-- PELICULA_PRODUCTOR
-- ==========================
INSERT INTO pelicula_productor (pelicula_id, productor_id) VALUES
(1,1),(2,1),(3,1),(4,2),(5,2),(6,2);

-- ==========================
-- PELICULA_PERSONAJE
-- ==========================
-- A New Hope
INSERT INTO pelicula_personaje (pelicula_id, personaje_id) VALUES
(1,1),(1,2),(1,3),(1,4),(1,5),(1,9);
-- The Empire Strikes Back
INSERT INTO pelicula_personaje (pelicula_id, personaje_id) VALUES
(2,1),(2,2),(2,3),(2,4),(2,6),(2,7);
-- Return of the Jedi
INSERT INTO pelicula_personaje (pelicula_id, personaje_id) VALUES
(3,1),(3,2),(3,3),(3,4),(3,6),(3,7),(3,8);
-- The Phantom Menace
INSERT INTO pelicula_personaje (pelicula_id, personaje_id) VALUES
(4,5),(4,8),(4,9);
-- Attack of the Clones
INSERT INTO pelicula_personaje (pelicula_id, personaje_id) VALUES
(5,1),(5,5),(5,8),(5,9);
-- Revenge of the Sith
INSERT INTO pelicula_personaje (pelicula_id, personaje_id) VALUES
(6,1),(6,4),(6,5),(6,8),(6,9);
