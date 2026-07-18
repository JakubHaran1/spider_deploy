🕷️ spiders_app (Django REST Framework + React)

Projekt końcowy: aplikacja do zarządzania pająkami z backendem w Django REST Framework oraz frontendem w React.

1. Konfiguracja projektu Django REST Framework
   Utworzenie projektu spiders_app
   Instalacja Django REST Framework
   Konfiguracja CORS (dla React frontend)
   Przygotowanie obsługi plików (MEDIA)

2. Implementacja modeli danych
   User (CustomUser)
   Spider
   Tag
   Spider_img

   Dodatkowo:
   migracje bazy danych
   konfiguracja bazy danych POSTGRESQL

3. Podstawowe CRUD API

- ModelViewSet dla wszystkich modeli
  DefaultRouter
  pełne operacje CRUD:
  Create
  Read
  Update
  Delete

  Dodatkowo:
  Niestandardowe endpointy dla modelu user
  -me
  -login

4.  Uwierzytelnianie JWT
    integracja djangorestframework-simplejwt

        Endpointy:
            /token/
            /token/refresh/

        Funkcje:
        logowanie użytkownika
        autoryzacja API
        automatyczne logowanie przy odświeżeniu strony (refresh token flow)

5.  Filtrowanie, wyszukiwanie i sortowanie
    SearchFilter
    OrderingFilter

    Filtrowanie po:
    -nazwie
    -autorze
    -typie
    -tagach

6.  Relacje między modelami
    Many-to-Many: Spider ↔ Tag
    ForeignKey: Spider_img → Spider
    zagnieżdżone serializery (nested serializers)

7.  System uprawnień
    IsAuthenticated dla tworzenia obiektów
    custom permission: isAuthor
    ograniczenie edycji i usuwania do autora 8.
8.  Testy automatyczne API
    Testy api
    testy CRUD endpointów
    testy JWT
    testy permissions
    framework: pytest

9.  Konteneryzacja aplikacji
    Dockerfile (backend Django)

    docker-compose:
    backend (Django)
    frontend (React)
    PostgreSQL

10. Integracja backendu z frontendem (React)
    utworzenie aplikacji React
    komunikacja z API Django ( axios)

    Obsługiwane funkcje:
    - logowanie (JWT)
    - automatyczne logowanie przy odświeżeniu strony (sprawdzenie refresh tokena i pobranie nowego access tokena)
    - lista pająków (GET /spiders)
    - tworzenie, edycja i usuwanie (POST /PUT/DELETE)

Szybki start (Docker)
Wymagania:
Docker
Docker Compose

    Uruchomienie:
        docker compose up --build

    Domyslne adresy:
        Frontend: http://localhost:5173
        Backend API: http://localhost:8000/api/
        Django admin: http://localhost:8000/admin/

    Aktywne uslugi:
        backend
        frontend
        postgres

    Domyslna baza danych:
        PostgreSQL (kontener postgres)

    Uruchomienie lokalne
        Backend
        cd backend
        python -m venv .env
        .env\Scripts\activate
        pip install -r requirements.txt
        copy .env.example .env
        python manage.py migrate
        python manage.py runserver

    Frontend
        cd frontend
        npm install
        copy .env.example .env
        npm run dev

    Konfiguracja srodowiska
    Backend (backend/.env)
        Podstawowe zmienne:
            SECRET_KEY
        Zmienne PostgreSQL:
            POSTGRES_DB
            POSTGRES_USER
            POSTGRES_PASSWORD
            POSTGRES_HOST
            POSTGRES_PORT
