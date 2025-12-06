CREATE OR REPLACE FUNCTION set_modified_fields()
RETURNS TRIGGER AS $$
BEGIN
    NEW.fecha_modificacion = CURRENT_TIMESTAMP;
    NEW.usuario_modificacion = CURRENT_USER;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TABLE IF NOT EXISTS planetas (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario_creacion VARCHAR(150) NOT NULL DEFAULT CURRENT_USER,
    fecha_modificacion TIMESTAMP,
    usuario_modificacion VARCHAR(150)
);


CREATE TABLE IF NOT EXISTS personajes (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    planeta_id INTEGER NOT NULL,
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario_creacion VARCHAR(150) NOT NULL DEFAULT CURRENT_USER,
    fecha_modificacion TIMESTAMP,
    usuario_modificacion VARCHAR(150),
    CONSTRAINT fk_personaje_planeta FOREIGN KEY (planeta_id)
        REFERENCES planetas(id)
);


CREATE TABLE IF NOT EXISTS peliculas (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    texto_apertura VARCHAR(255),
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario_creacion VARCHAR(150) NOT NULL DEFAULT CURRENT_USER,
    fecha_modificacion TIMESTAMP,
    usuario_modificacion VARCHAR(150)
);


CREATE TABLE IF NOT EXISTS pelicula_planeta (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    pelicula_id INTEGER NOT NULL,
    planeta_id INTEGER NOT NULL,
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario_creacion VARCHAR(150) NOT NULL DEFAULT CURRENT_USER,
    fecha_modificacion TIMESTAMP,
    usuario_modificacion VARCHAR(150),
    CONSTRAINT fk_pp_pelicula FOREIGN KEY (pelicula_id) REFERENCES peliculas(id),
    CONSTRAINT fk_pp_planeta  FOREIGN KEY (planeta_id) REFERENCES planetas(id)
);

CREATE TABLE IF NOT EXISTS productores (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario_creacion VARCHAR(150) NOT NULL DEFAULT CURRENT_USER,
    fecha_modificacion TIMESTAMP,
    usuario_modificacion VARCHAR(150)
);

CREATE TABLE IF NOT EXISTS directores (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario_creacion VARCHAR(150) NOT NULL DEFAULT CURRENT_USER,
    fecha_modificacion TIMESTAMP,
    usuario_modificacion VARCHAR(150)
);


CREATE TABLE IF NOT EXISTS pelicula_productor (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    pelicula_id INTEGER NOT NULL,
    productor_id INTEGER NOT NULL,
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario_creacion VARCHAR(150) NOT NULL DEFAULT CURRENT_USER,
    fecha_modificacion TIMESTAMP,
    usuario_modificacion VARCHAR(150),
    CONSTRAINT fk_ppr_pelicula FOREIGN KEY (pelicula_id) REFERENCES peliculas(id),
    CONSTRAINT fk_ppr_productor FOREIGN KEY (productor_id) REFERENCES productores(id)
);


CREATE TABLE IF NOT EXISTS pelicula_director (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    pelicula_id INTEGER NOT NULL,
    director_id INTEGER NOT NULL,
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario_creacion VARCHAR(150) NOT NULL DEFAULT CURRENT_USER,
    fecha_modificacion TIMESTAMP,
    usuario_modificacion VARCHAR(150),
    CONSTRAINT fk_pd_pelicula FOREIGN KEY (pelicula_id) REFERENCES peliculas(id),
    CONSTRAINT fk_pd_director FOREIGN KEY (director_id) REFERENCES directores(id)
);


CREATE TABLE IF NOT EXISTS pelicula_personaje (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    pelicula_id INTEGER NOT NULL,
    personaje_id INTEGER NOT NULL,
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    usuario_creacion VARCHAR(150) NOT NULL DEFAULT CURRENT_USER,
    fecha_modificacion TIMESTAMP,
    usuario_modificacion VARCHAR(150),
    CONSTRAINT fk_ppj_pelicula FOREIGN KEY (pelicula_id) REFERENCES peliculas(id),
    CONSTRAINT fk_ppj_personaje FOREIGN KEY (personaje_id) REFERENCES personajes(id)
);

-- planetas
CREATE TRIGGER trg_planetas_mod
BEFORE UPDATE ON planetas
FOR EACH ROW EXECUTE FUNCTION set_modified_fields();

-- personajes
CREATE TRIGGER trg_personajes_mod
BEFORE UPDATE ON personajes
FOR EACH ROW EXECUTE FUNCTION set_modified_fields();

-- peliculas
CREATE TRIGGER trg_peliculas_mod
BEFORE UPDATE ON peliculas
FOR EACH ROW EXECUTE FUNCTION set_modified_fields();

-- directores
CREATE TRIGGER trg_directores_mod
BEFORE UPDATE ON directores
FOR EACH ROW EXECUTE FUNCTION set_modified_fields();

-- productores
CREATE TRIGGER trg_productores_mod
BEFORE UPDATE ON productores
FOR EACH ROW EXECUTE FUNCTION set_modified_fields();

-- pelicula_planeta
CREATE TRIGGER trg_pelicula_planeta_mod
BEFORE UPDATE ON pelicula_planeta
FOR EACH ROW EXECUTE FUNCTION set_modified_fields();

-- pelicula_productor
CREATE TRIGGER trg_pelicula_productor_mod
BEFORE UPDATE ON pelicula_productor
FOR EACH ROW EXECUTE FUNCTION set_modified_fields();

-- pelicula_director
CREATE TRIGGER trg_pelicula_director_mod
BEFORE UPDATE ON pelicula_director
FOR EACH ROW EXECUTE FUNCTION set_modified_fields();

-- pelicula_personaje
CREATE TRIGGER trg_pelicula_personaje_mod
BEFORE UPDATE ON pelicula_personaje
FOR EACH ROW EXECUTE FUNCTION set_modified_fields();


