from unittest.mock import patch, MagicMock
from django.test import SimpleTestCase
from starwars.schema import Query


class TestResolvers(SimpleTestCase):

    @patch("starwars.schema.Pelicula")
    def test_resolve_all_peliculas(self, mock_model):
        mock_qs = MagicMock()
        mock_model.objects.prefetch_related.return_value = mock_qs
        mock_qs.all.return_value = ["OK"]

        result = Query.resolve_all_peliculas(None, None)

        mock_model.objects.prefetch_related.assert_called_once()
        mock_qs.all.assert_called_once()
        self.assertEqual(result, ["OK"])


    @patch("starwars.schema.Director")
    def test_resolve_all_directores(self, mock_model):
        mock_qs = MagicMock()
        mock_model.objects.prefetch_related.return_value = mock_qs
        mock_qs.all.return_value = ["OK"]

        result = Query.resolve_all_directores(None, None)

        mock_model.objects.prefetch_related.assert_called_once()
        mock_qs.all.assert_called_once()
        self.assertEqual(result, ["OK"])


    @patch("starwars.schema.Planeta")
    def test_resolve_all_planetas(self, mock_model):
        mock_qs = MagicMock()
        mock_model.objects.prefetch_related.return_value = mock_qs
        mock_qs.all.return_value = ["OK"]

        result = Query.resolve_all_planetas(None, None)

        mock_model.objects.prefetch_related.assert_called_once()
        mock_qs.all.assert_called_once()
        self.assertEqual(result, ["OK"])


    @patch("starwars.schema.Personaje")
    def test_resolve_all_personajes_sin_filtro(self, mock_model):

        mock_select = MagicMock()
        mock_prefetch = MagicMock()

        mock_model.objects.select_related.return_value = mock_select
        mock_select.prefetch_related.return_value = mock_prefetch

        result = Query.resolve_all_personajes(None, None, nombre=None)

        mock_model.objects.select_related.assert_called_once_with("planeta")
        mock_select.prefetch_related.assert_called_once_with("rel_peliculas__pelicula")

        self.assertEqual(result, mock_prefetch)


    @patch("starwars.schema.Personaje")
    def test_resolve_all_personajes_con_filtro(self, mock_model):

        mock_select = MagicMock()
        mock_prefetch = MagicMock()

        mock_model.objects.select_related.return_value = mock_select
        mock_select.prefetch_related.return_value = mock_prefetch

        mock_prefetch.filter.return_value = "filtered_result"

        result = Query.resolve_all_personajes(None, None, nombre="Luke")

        mock_prefetch.filter.assert_called_once_with(nombre__icontains="Luke")
        self.assertEqual(result, "filtered_result")


    @patch("starwars.schema.Productor")
    def test_resolve_all_productores(self, mock_model):
        mock_qs = MagicMock()
        mock_model.objects.prefetch_related.return_value = mock_qs
        mock_qs.all.return_value = ["OK"]

        result = Query.resolve_all_productores(None, None)

        mock_model.objects.prefetch_related.assert_called_once()
        mock_qs.all.assert_called_once()
        self.assertEqual(result, ["OK"])


    @patch("starwars.schema.Pelicula")
    def test_resolve_pelicula_by_title_encontrado(self, mock_model):
        mock_model.objects.get.return_value = "Pelicula Mock"

        result = Query.resolve_pelicula_by_title(None, None, titulo="A")

        mock_model.objects.get.assert_called_once_with(titulo="A")
        self.assertEqual(result, "Pelicula Mock")


    @patch("starwars.schema.Pelicula")
    def test_resolve_pelicula_by_title_no_encontrado(self, mock_model):
        mock_model.DoesNotExist = Exception
        mock_model.objects.get.side_effect = mock_model.DoesNotExist

        result = Query.resolve_pelicula_by_title(None, None, titulo="A")

        self.assertIsNone(result)


    @patch("starwars.schema.Director")
    def test_resolve_director_by_name_encontrado(self, mock_model):
        mock_model.objects.get.return_value = "Director Mock"

        result = Query.resolve_director_by_name(None, None, nombre="Lucas")

        mock_model.objects.get.assert_called_once_with(nombre="Lucas")
        self.assertEqual(result, "Director Mock")


    @patch("starwars.schema.Director")
    def test_resolve_director_by_name_no_encontrado(self, mock_model):
        mock_model.DoesNotExist = Exception
        mock_model.objects.get.side_effect = mock_model.DoesNotExist

        result = Query.resolve_director_by_name(None, None, nombre="Lucas")

        self.assertIsNone(result)


    @patch("starwars.schema.Planeta")
    def test_resolve_planeta_by_name_encontrado(self, mock_model):
        mock_model.objects.get.return_value = "Planeta Mock"

        result = Query.resolve_planeta_by_name(None, None, nombre="Tatooine")

        mock_model.objects.get.assert_called_once_with(nombre="Tatooine")
        self.assertEqual(result, "Planeta Mock")


    @patch("starwars.schema.Planeta")
    def test_resolve_planeta_by_name_no_encontrado(self, mock_model):
        mock_model.DoesNotExist = Exception
        mock_model.objects.get.side_effect = mock_model.DoesNotExist

        result = Query.resolve_planeta_by_name(None, None, nombre="Tatooine")

        self.assertIsNone(result)


    @patch("starwars.schema.Personaje")
    def test_resolve_personaje_by_name_encontrado(self, mock_model):
        mock_model.objects.get.return_value = "Luke"

        result = Query.resolve_personaje_by_name(None, None, nombre="Luke")

        mock_model.objects.get.assert_called_once_with(nombre="Luke")
        self.assertEqual(result, "Luke")


    @patch("starwars.schema.Personaje")
    def test_resolve_personaje_by_name_no_encontrado(self, mock_model):
        mock_model.DoesNotExist = Exception
        mock_model.objects.get.side_effect = mock_model.DoesNotExist

        result = Query.resolve_personaje_by_name(None, None, nombre="Luke")

        self.assertIsNone(result)


    @patch("starwars.schema.Productor")
    def test_resolve_productor_by_name_encontrado(self, mock_model):
        mock_model.objects.get.return_value = "Prod Mock"

        result = Query.resolve_productor_by_name(None, None, nombre="Gary")

        mock_model.objects.get.assert_called_once_with(nombre="Gary")
        self.assertEqual(result, "Prod Mock")


    @patch("starwars.schema.Productor")
    def test_resolve_productor_by_name_no_encontrado(self, mock_model):
        mock_model.DoesNotExist = Exception
        mock_model.objects.get.side_effect = mock_model.DoesNotExist

        result = Query.resolve_productor_by_name(None, None, nombre="Gary")

        self.assertIsNone(result)
