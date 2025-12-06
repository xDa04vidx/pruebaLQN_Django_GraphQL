from django.test import TestCase
from graphene.test import Client
from starwars.schema import schema
from starwars.models import *

class GraphQLTestCase(TestCase):

    def setUp(self):
        self.client = Client(schema)

        # Datos iniciales
        self.planeta = Planeta.objects.create(nombre="Tatooine")
        self.director = Director.objects.create(nombre="George Lucas")
        self.personaje = Personaje.objects.create(nombre="Luke Skywalker", planeta=self.planeta)
        self.productor = Productor.objects.create(nombre="Gary Kurtz")

    def test_crear_planeta(self):
        query = '''
        mutation {
            crearPlaneta(nombre: "Alderaan") {
                ok
                planeta {
                    id
                    nombre
                }
            }
        }
        '''

        response = self.client.execute(query)
        data = response["data"]["crearPlaneta"]

        self.assertTrue(data["ok"])
        self.assertEqual(data["planeta"]["nombre"], "Alderaan")
        self.assertEqual(Planeta.objects.count(), 2)

    def test_crear_personaje(self):
        query = f'''
        mutation {{
            crearPersonaje(nombre: "Leia Organa", planetaId: {self.planeta.id}) {{
                ok
                personaje {{
                    id
                    nombre
                    planeta {{
                        id
                        nombre
                    }}
                }}
            }}
        }}
        '''

        response = self.client.execute(query)
        data = response["data"]["crearPersonaje"]

        self.assertTrue(data["ok"])
        self.assertEqual(data["personaje"]["nombre"], "Leia Organa")
        self.assertEqual(data["personaje"]["planeta"]["nombre"], "Tatooine")

    def test_crear_pelicula_con_relaciones(self):
        query = f'''
        mutation {{
            crearPelicula(
                titulo: "Una Nueva Esperanza",
                textoApertura: "Hace mucho tiempo...",
                directorIds: [{self.director.id}],
                planetaIds: [{self.planeta.id}],
                personajeIds: [{self.personaje.id}],
                productorIds: [{self.productor.id}]
            ) {{
                ok
                pelicula {{
                    id
                    titulo
                }}
            }}
        }}
        '''

        response = self.client.execute(query)
        data = response["data"]["crearPelicula"]

        self.assertTrue(data["ok"])
        self.assertEqual(data["pelicula"]["titulo"], "Una Nueva Esperanza")
        self.assertEqual(Pelicula.objects.count(), 1)
        pelicula = Pelicula.objects.first()

        self.assertEqual(pelicula.rel_directores.count(), 1)
        self.assertEqual(pelicula.rel_planetas.count(), 1)
        self.assertEqual(pelicula.rel_personajes.count(), 1)
        self.assertEqual(pelicula.rel_productores.count(), 1)


    def test_query_all_planetas(self):
        query = '''
        {
            allPlanetas {
                nombre
            }
        }
        '''
        response = self.client.execute(query)
        data = response["data"]["allPlanetas"]

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["nombre"], "Tatooine")

    def test_query_personaje_by_name(self):
        query = '''
        {
            personajeByName(nombre: "Luke Skywalker") {
                nombre
                planeta {
                    nombre
                }
            }
        }
        '''
        response = self.client.execute(query)
        data = response["data"]["personajeByName"]

        self.assertEqual(data["nombre"], "Luke Skywalker")
        self.assertEqual(data["planeta"]["nombre"], "Tatooine")

    def test_query_all_peliculas(self):
        Pelicula.objects.create(titulo="El Imperio Contraataca")

        query = '''
        {
            allPeliculas {
                titulo
            }
        }
        '''
        resp = self.client.execute(query)
        data = resp["data"]["allPeliculas"]

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["titulo"], "El Imperio Contraataca")

    def test_query_all_personajes(self):
        """Debe retornar TODOS los personajes, sin filtro."""
        query = '''
        {
            allPersonajes {
                nombre
            }
        }
        '''

        resp = self.client.execute(query)
        data = resp["data"]["allPersonajes"]

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["nombre"], "Luke Skywalker")

    def test_query_all_personajes_filtrado(self):
        """Debe retornar solo coincidencias por icontains."""
        # Agregamos otros personajes
        Personaje.objects.create(nombre="Leia Organa", planeta=self.planeta)
        Personaje.objects.create(nombre="Han Solo", planeta=self.planeta)

        query = '''
        {
            allPersonajes(nombre: "Luke") {
                nombre
            }
        }
        '''

        resp = self.client.execute(query)
        data = resp["data"]["allPersonajes"]

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["nombre"], "Luke Skywalker")

    def test_query_personaje_by_name_exact(self):
        """Prueba adicional: búsqueda exacta con personajeByName"""
        query = '''
        {
            personajeByName(nombre: "Luke Skywalker") {
                nombre
                planeta {
                    nombre
                }
            }
        }
        '''

        resp = self.client.execute(query)
        data = resp["data"]["personajeByName"]

        self.assertEqual(data["nombre"], "Luke Skywalker")
        self.assertEqual(data["planeta"]["nombre"], "Tatooine")
