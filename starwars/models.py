from django.db import models

class AuditModel(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_creacion = models.CharField(max_length=150, default="system")
    fecha_modificacion = models.DateTimeField(null=True, blank=True)
    usuario_modificacion = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        abstract = True

class Planeta(AuditModel):
    nombre = models.CharField(max_length=150)

    class Meta:
        db_table = "planetas"
        managed = False 

    def __str__(self):
        return self.nombre

class Director(AuditModel):
    nombre = models.CharField(max_length=150)

    class Meta:
        db_table = "directores"
        managed = False 

    def __str__(self):
        return self.nombre

class Pelicula(AuditModel):
    titulo = models.CharField(max_length=150)
    texto_apertura = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "peliculas"
        managed = False 

    def __str__(self):
        return self.titulo

class Personaje(AuditModel):
    nombre = models.CharField(max_length=100)
    planeta = models.ForeignKey(
        Planeta,
        on_delete=models.CASCADE,
        db_column="planeta_id",
        related_name="personajes"
    )

    class Meta:
        db_table = "personajes"
        managed = False 

    def __str__(self):
        return self.nombre

class Productor(AuditModel):
    nombre = models.CharField(max_length=150)

    class Meta:
        db_table = "productores"
        managed = False 

    def __str__(self):
        return self.nombre

class PeliculaPlaneta(AuditModel):
    pelicula = models.ForeignKey(
        Pelicula,
        on_delete=models.CASCADE,
        db_column="pelicula_id",
        related_name="rel_planetas"
    )
    planeta = models.ForeignKey(
        Planeta,
        on_delete=models.CASCADE,
        db_column="planeta_id",
        related_name="rel_peliculas"
    )

    class Meta:
        db_table = "pelicula_planeta"
        managed = False 


class PeliculaProductor(AuditModel):
    pelicula = models.ForeignKey(
        Pelicula,
        on_delete=models.CASCADE,
        db_column="pelicula_id",
        related_name="rel_productores"
    )
    productor = models.ForeignKey(
        Productor,
        on_delete=models.CASCADE,
        db_column="productor_id",
        related_name="rel_peliculas"
    )

    class Meta:
        db_table = "pelicula_productor"
        managed = False 


class PeliculaDirector(AuditModel):
    pelicula = models.ForeignKey(
        Pelicula,
        on_delete=models.CASCADE,
        db_column="pelicula_id",
        related_name="rel_directores"
    )
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        db_column="director_id",
        related_name="rel_peliculas"
    )

    class Meta:
        db_table = "pelicula_director"
        managed = False 


class PeliculaPersonaje(AuditModel):
    pelicula = models.ForeignKey(
        Pelicula,
        on_delete=models.CASCADE,
        db_column="pelicula_id",
        related_name="rel_personajes"
    )
    personaje = models.ForeignKey(
        Personaje,
        on_delete=models.CASCADE,
        db_column="personaje_id",
        related_name="rel_peliculas"
    )

    class Meta:
        db_table = "pelicula_personaje"
        managed = False 
