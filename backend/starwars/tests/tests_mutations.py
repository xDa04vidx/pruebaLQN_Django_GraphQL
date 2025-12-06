import json
from django.test import TestCase
from graphene.test import Client
from starwars.schema import schema

from starwars.models import Pelicula, Personaje, Planeta, Director, Productor


class MutationTests(TestCase):

    def setUp(self):
        self.client = Client(schema)

        # Datos base para relaciones
        self.director = Director.objects.create(nombre="George Lucas")
        self.planeta = Planeta.objects.create(nombre="Tatooine")
        self.personaje = Personaje.objects.create(nombre="Luke Skywalker")
        self.productor = Productor.objects.create(nombre="Rick McCallum")

    def test_crear_pelicula(self):
        mutation = """
            mutation CrearPelicula(
                $titulo: String!,
                $texto: String,
                $directores: [Int],
                $planetas: [Int],
                $personajes: [Int],
                $productores: [Int]
            ) {
                crearPelicula(
                    titulo: $titulo,
                    textoApertura: $texto,
                    directorIds: $directores,
                    planetaIds: $planetas,
                    personajeIds: $personajes,
                    productorIds: $productores
                ) {
                    ok
                    pelicula {
                        id
                        titulo
                    }
                }
            }
        """

        variables = {
            "titulo": "Una Nueva Esperanza",
            "texto": "Intro...",
            "directores": [self.director.id],
            "planetas": [self.planeta.id],
            "personajes": [self.personaje.id],
            "productores": [self.productor.id],
        }

        response = self.client.execute(mutation, variables=variables)

        self.assertIsNone(response.get("errors"))
        data = response["data"]["crearPelicula"]

        self.assertTrue(data["ok"])
        self.assertEqual(data["pelicula"]["titulo"], "Una Nueva Esperanza")

        # Validar que se creó en la BD
        pelicula = Pelicula.objects.get(titulo="Una Nueva Esperanza")
        self.assertEqual(pelicula.rel_directores.count(), 1)
        self.assertEqual(pelicula.rel_planetas.count(), 1)
        self.assertEqual(pelicula.rel_personajes.count(), 1)
        self.assertEqual(pelicula.rel_productores.count(), 1)

    def test_crear_personaje(self):
        mutation = """
            mutation CrearPersonaje($nombre: String!, $planetaId: Int) {
                crearPersonaje(nombre: $nombre, planetaId: $planetaId) {
                    ok
                    personaje {
                        nombre
                        planeta {
                            nombre
                        }
                    }
                }
            }
        """

        variables = {
            "nombre": "Han Solo",
            "planetaId": self.planeta.id
        }

        response = self.client.execute(mutation, variables=variables)

        self.assertIsNone(response.get("errors"))
        data = response["data"]["crearPersonaje"]

        self.assertTrue(data["ok"])
        self.assertEqual(data["personaje"]["nombre"], "Han Solo")
        self.assertEqual(data["personaje"]["planeta"]["nombre"], "Tatooine")


    def test_crear_planeta(self):
        mutation = """
            mutation CrearPlaneta($nombre: String!) {
                crearPlaneta(nombre: $nombre) {
                    ok
                    planeta {
                        nombre
                    }
                }
            }
        """

        variables = {"nombre": "Naboo"}

        response = self.client.execute(mutation, variables=variables)

        self.assertIsNone(response.get("errors"))
        data = response["data"]["crearPlaneta"]

        self.assertTrue(data["ok"])
        self.assertEqual(data["planeta"]["nombre"], "Naboo")

        self.assertTrue(Planeta.objects.filter(nombre="Naboo").exists())
