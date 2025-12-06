# 🚀 API GraphQL de Star Wars — Django + Strawberry

Este proyecto fue desarrollado como parte del **Challenge Back-End – LQN**, cuyo objetivo es construir una API GraphQL en Django que permita consultar y administrar información del universo Star Wars.

---

## 🌌 Objetivo del Challenge

La API debe permitir:

- Listar todos los personajes del universo Star Wars.
- Consultar las películas en las que aparece cada personaje.
- Mostrar por cada película:
  - Opening crawl
  - Planetas relacionados
  - Director
  - Productores
  - Otros datos relevantes

---

## ✅ Requisitos Funcionales Implementados

### **1. Query para listar personajes (con filtro por nombre)**

```graphql
query {
  personajes(nombre: "luke") {
    id
    nombre
    planeta {
      nombre
    }
    peliculas {
      id
      titulo
    }
  }
}
```

### 📸 *Captura del Query funcionando*  
(Insertar aquí la imagen)  
![query-personajes](./docs/img/query-personajes.png)

---

### **2. Mutaciones para crear personajes, planetas y películas**

#### Ejemplo: Crear personaje

```graphql
mutation {
  crearPersonaje(input: {
    nombre: "Mace Windu",
    planetaId: 3
  }) {
    id
    nombre
    planeta {
      nombre
    }
  }
}
```

### 📸 *Captura de la mutation funcionando*  
(Insertar aquí la imagen)  
![mutation-personaje](./docs/img/mutation-personaje.png)

---

### **3. Pruebas unitarias e integración**

- Se usó Pytest
- Se implementaron pruebas de:
  - Modelos
  - Queries
  - Mutaciones
  - Relaciones
- Se utilizaron factories para generar datos consistentes

Ejecutar pruebas:

```bash
pytest -v
```

### 📸 *Captura de pruebas ejecutándose*  
(Insertar aquí la imagen)  
![tests](./docs/img/tests.png)

---

## 🧩 Tecnologías principales

| Tecnología | Uso |
|-----------|-----|
| Django | Framework principal |
| Strawberry GraphQL | Motor GraphQL moderno |
| PostgreSQL | Base de datos |
| Pytest | Testing |
| Docker (opcional) | Entorno reproducible |

---

## 📂 Estructura del Proyecto

```
project/
├─ app_core/
│  ├─ models.py
│  ├─ schema/
│  │  ├─ types.py
│  │  ├─ queries.py
│  │  ├─ mutations.py
│  └─ services.py
├─ starwars/
│  ├─ settings.py
│  ├─ urls.py
│  └─ asgi.py
├─ tests/
│  ├─ test_queries.py
│  ├─ test_mutations.py
│  └─ factories.py
├─ docs/
│  └─ img/
│      ├─ query-personajes.png
│      ├─ mutation-personaje.png
│      ├─ tests.png
│      └─ architecture.png
└─ README.txt
```

---

## ▶️ Instalación y ejecución

### 1. Clonar repositorio

```bash
git clone https://github.com/tu_usuario/tu_repo.git
cd tu_repo
```

### 2. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos PostgreSQL

```sql
CREATE DATABASE starwars;
```

Crear archivo `.env`:

```
DATABASE_NAME=starwars
DATABASE_USER=postgres
DATABASE_PASSWORD=1234
DATABASE_HOST=127.0.0.1
DATABASE_PORT=5432
```

### 5. Migrar

```bash
python manage.py migrate
```

### 6. Ejecutar servidor

```bash
python manage.py runserver
```

### 7. Abrir GraphiQL

```
http://127.0.0.1:8000/graphql
```

---

## 🔍 Más queries y mutaciones

### Query: Obtener películas de un personaje
(Insertar imagen)
![query-peliculas](./docs/img/query-peliculas.png)

### Mutación: Crear planeta
(Insertar imagen)
![mutation-planeta](./docs/img/mutation-planeta.png)

### Mutación: Crear película
(Insertar imagen)
![mutation-pelicula](./docs/img/mutation-pelicula.png)

---

## 📜 Licencia

Proyecto desarrollado como parte del **Challenge Back-End – LQN**.

---

## ⭐ Autor

**David Arias**  
GitHub: https://github.com/tu_usuario

