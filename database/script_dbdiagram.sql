-- El diagrama se realizo con la plataforma https:--dbdiagram.io, para replicarlo se suministra el código de creación
-- Use DBML to define your database structure
-- Docs: https:--dbml.dbdiagram.io/docs

Table planetas {
  id integer [primary key]
  nombre varchar(150) 
  -- auditoria
  fecha_creacion timestamp
  usuario_creacion varchar(150)
  fecha_modificacion timestamp
  usuario_modificacion varchar(150) 
}

Table personajes {
  id integer [primary key]
  nombre varchar(100)
  planeta_id integer 
  -- auditoria
  fecha_creacion timestamp
  usuario_creacion varchar(150)
  fecha_modificacion timestamp
  usuario_modificacion varchar(150) 
}

Table peliculas {
  id integer [primary key]
  titulo varchar(150)
  texto_apertura varchar(255)
  -- auditoria
  fecha_creacion timestamp
  usuario_creacion varchar(150)
  fecha_modificacion timestamp
  usuario_modificacion varchar(150) 
}

Table pelicula_planeta {
  id integer [primary key]
  pelicula_id integer
  planeta_id integer
  -- auditoria
  fecha_creacion timestamp
  usuario_creacion varchar(150)
  fecha_modificacion timestamp
  usuario_modificacion varchar(150) 
}

Table productores{
  id integer [primary key]
  nombre varchar(150) 
  -- auditoria
  fecha_creacion timestamp
  usuario_creacion varchar(150)
  fecha_modificacion timestamp
  usuario_modificacion varchar(150) 
}

Table directores{
  id integer [primary key]
  nombre varchar(150) 
  -- auditoria
  fecha_creacion timestamp
  usuario_creacion varchar(150)
  fecha_modificacion timestamp
  usuario_modificacion varchar(150) 
}

Table pelicula_productor {
  id integer [primary key]
  pelicula_id integer
  productor_id integer
  -- auditoria
  fecha_creacion timestamp
  usuario_creacion varchar(150)
  fecha_modificacion timestamp
  usuario_modificacion varchar(150) 
}

Table pelicula_director {
  id integer [primary key]
  pelicula_id integer
  director_id integer
  -- auditoria
  fecha_creacion timestamp
  usuario_creacion varchar(150)
  fecha_modificacion timestamp
  usuario_modificacion varchar(150) 
}

Table pelicula_personaje {
  id integer [primary key]
  pelicula_id integer
  personaje_id integer
  -- auditoria
  fecha_creacion timestamp
  usuario_creacion varchar(150)
  fecha_modificacion timestamp 
  usuario_modificacion varchar(150)
}


Ref pelicula_planetas_1: pelicula_planeta.planeta_id > planetas.id -- many-to-one

Ref pelicula_planetas_2: pelicula_planeta.pelicula_id > peliculas.id -- many-to-one

Ref pelicula_director_1: pelicula_director.director_id > directores.id -- many-to-one

Ref pelicula_director_2: pelicula_director.pelicula_id > peliculas.id -- many-to-one

Ref pelicula_productor_1: pelicula_productor.productor_id > productores.id -- many-to-one

Ref pelicula_productor_2: pelicula_productor.pelicula_id > peliculas.id -- many-to-one

Ref pelicula_personaje_1: pelicula_personaje.personaje_id > personajes.id -- many-to-one

Ref pelicula_personaje_2: pelicula_personaje.pelicula_id > peliculas.id -- many-to-one

Ref planeta_personaje: personajes.planeta_id > planetas.id -- many-to-one


-- Con este resultado se exporta a Postgres y se realizan las mejoras correspondientes al script de creación.