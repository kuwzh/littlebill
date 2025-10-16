🧾 LittleBill

Petit projet de test technique (FastAPI + React)

-Objectif

Faire une petite appli de gestion de ventes, avec un backend FastAPI et un frontend React qui affichent les données.

-Stack utilisée

Backend : FastAPI (Python)

Frontend : React

Docker : pour lancer les deux services ensemble

-Structure du projet
littlebill-test/
│
├── backend/
│   ├── main.py              # Fichier principal FastAPI
│   ├── api/
│   │   ├── clients.py       # Routes pour les clients
│   │   └── ventes.py        # Routes pour les ventes
│
├── frontend/
│   └── src/App.js           # Page principale React
│
├── docker-compose.yml       # Lancement back + front
└── README.md

-Lancer le projet
Avec Docker
docker-compose up --build


Backend → http://localhost:8000

Frontend → http://localhost:3000

-API
Clients

GET /clients → récupère tous les clients

GET /clients/search?name=... → recherche un client

Ventes

GET /ventes/client/{id} → récupère les ventes d’un client

-Frontend

Le frontend est développé en React.
Il est connecté au backend via des appels fetch() vers http://localhost:8000.

Actuellement, l’affichage des clients et des ventes ne fonctionne pas encore correctement — probablement à cause d’un problème de routes ou de CORS entre le front et le back.

Cependant :

Les appels sont bien configurés dans App.js.

Le backend renvoie correctement les données sur les routes /clients et /ventes/client/{id}.

Le front récupère bien les données quand il est testé indépendamment.

-Détails techniques

Pagination côté backend (5 ventes max par page)

Données “fausses” pour les tests

Routes bien séparées (clients et ventes)

Uvicorn pour lancer le serveur


Projet réalisé par Yanis Lambourg (kuwzh)
Dans le cadre d’un test technique (développement backend + frontend)
