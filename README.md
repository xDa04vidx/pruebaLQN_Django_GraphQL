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
query{
  allPersonajes{
    id
    nombre
  }
}
------
query{
  allPersonajes(nombre:"Darth Vader"){
    id
    nombre
  }
}
```

### 📸 *Captura del Query funcionando*  
<img width="1677" height="894" alt="image" src="https://github.com/user-attachments/assets/98fed810-93d6-4a22-9505-4f67d813b4b2" />
<img width="1852" height="696" alt="image" src="https://github.com/user-attachments/assets/03972e4a-277e-4c9b-80c0-ccd5b418035a" />

### **2. Para cada personaje, consultar las películas en las que aparece.**
```graphql
query{
  allPersonajes{
    id
    nombre
    peliculas{
      id
      titulo
      textoApertura
    }
  }
}
```

### 📸 *Captura del Query funcionando*  
<img width="1727" height="873" alt="image" src="https://github.com/user-attachments/assets/2f662d86-ff25-4c60-9a55-bcc995a083d9" />

### **3. Pelicula con campos relacionados.**
```graphql
query{
  allPeliculas{
    titulo
    textoApertura
    personajes{
      nombre
    }
    planetas{
      nombre
    }
    directores{
      nombre
    }
    productores{
      nombre
    }
    }
}

```

### 📸 *Captura del Query funcionando*  
<img width="1777" height="870" alt="image" src="https://github.com/user-attachments/assets/88eaaa16-c121-473d-86f1-55c5e916ab1d" />

---

### **4. Mutaciones para crear películas**

```graphql
mutation {
  crearPelicula(
    titulo: "Una Nueva Esperanza"
    textoApertura: "Hace mucho tiempo en una galaxia muy, muy lejana..."
    directorIds: [1, 2]
    planetaIds: [1, 3]
    personajeIds: [5, 7, 9]
    productorIds: [1]
  ) {
    ok
    pelicula {
      id
      titulo
      textoApertura
      relDirectores {
        director {
          id
          nombre
        }
      }
      relPlanetas {
        planeta {
          id
          nombre
        }
      }
      relPersonajes {
        personaje {
          id
          nombre
        }
      }
      relProductores {
        productor {
          id
          nombre
        }
      }
    }
  }
}
```

### 📸 *Captura de la mutation funcionando*  
<img width="1746" height="874" alt="image" src="https://github.com/user-attachments/assets/708fe021-6631-4cda-819b-5f5d5d240f6d" />

### **5. Mutaciones para crear personaje**

```graphql
mutation {
  crearPersonaje(
    nombre: "Obi-Wan Kenobi"
    planetaId: 1
  ) {
    ok
    personaje {
      id
      nombre
      planeta {
        id
        nombre
      }
    }
  }
}
```

### 📸 *Captura de la mutation funcionando*  
<img width="1399" height="403" alt="image" src="https://github.com/user-attachments/assets/2c59fd4e-7308-453a-9360-34300eb42768" />

### **6. Mutaciones para crear planeta**

```graphql
mutation {
  crearPlaneta(nombre: "Mustafar") {
    ok
    planeta {
      id
      nombre
    }
  }
}
```

### 📸 *Captura de la mutation funcionando*  
<img width="1733" height="299" alt="image" src="https://github.com/user-attachments/assets/40a3ce2d-f776-4cb2-9deb-355b13adc702" />

---

### **7. Pruebas unitarias e integración**
- Se implementaron pruebas de:
  - Modelos
  - Queries
  - Mutaciones

---

## **8. 🧩 Tecnologías principales**

| Tecnología | Uso |
|-----------|-----|
| Django | Framework principal |
| Graphene | Motor GraphQL moderno |
| PostgreSQL | Base de datos |

---

## **9. 📂 Estructura del Proyecto**

```
backend/
│
├─ core/
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
│
├─ starwars/
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations/
│  ├─ models.py
│  ├─ queries.py
│  ├─ schema.py
│  ├─ types.py
│  ├─ views.py
│  ├─ tests/
│  │   ├─ __init__.py
│  │   ├─ tests_queries.py
│  │   ├─ tests_mutations.py
│  │   └─ tests_resolvers.py
│  └─ mutations/
│      ├─ __init__.py
│      ├─ index.py
│      ├─ mutations_peliculas.py
│      ├─ mutations_personajes.py
│      └─ mutations_planetas.py
│
├─ manage.py
│
├─ database/
│  ├─ Diagrama entidad relacion.png
│  ├─ Diagrama entidad relacion.png.Zone.Identifier
│  ├─ inserts_basicos.sql
│  ├─ script_creacion.sql
│  └─ script_dbdigramam.sql
│
├─ .env
├─ .gitignore
├─ README.md
└─ requirements.txt
```

---


Crear archivo `.env`:

```
DJANGO_BD_URL=postgres://postgres:1234@127.0.0.1:5432/pruebalqnstarwars
```
### 10. Ejecutar servidor

```bash
python manage.py runserver
```

### 11. Abrir GraphiQL

```
http://127.0.0.1:8000/graphql
```

---

## 📜 Licencia

Proyecto desarrollado como parte del **Challenge Back-End – LQN**.

---

## ⭐ Autor

**David Arias**  
[GitHub: https://github.com/tu_usuario](https://github.com/xDa04vidx)

