# Flask Multi-Containter Application using Redis database

---

 # Visitor Analytics Dashboard

<img width="1912" height="873" alt="Visitor analytics" src="https://github.com/user-attachments/assets/9a79e89e-73a8-4bef-a1d9-85251c2fa8d4" />


A full-stack, real-time visitor analytics dashboard built with a React frontend and a Python/Flask backend, all containerized with Docker.

---

  # Features

*   **Real-time Visitor Tracking:** Captures visitor location data (Country, City, Lat/Lon) on page load.
*   **Interactive Map:** Visualizes all visitor locations on a world map using Leaflet.
*   **Dynamic Stats Cards:** Displays key metrics like total visitors, daily visits, weekly visits, and unique countries.
*   **Data-driven Components:** Shows lists of top locations and recent visitors.
*   **Persistent Data:** Uses a Redis database to store all visitor information.
*   **Containerized Environment:** Fully containerized with Docker and Docker Compose for easy setup and deployment.

---

  # Tech Stack

# Frontend
*   **React** (with Vite)
*   **Framer Motion** (for animations)
*   **React Leaflet** (for the interactive map)
*   **Lucide React** (for icons)
*   **Tailwind CSS** (for styling)
 
 # Backend & Infrastructure
*   **Python** with **Flask**
*   **Redis** (as the primary database)
*   **Gunicorn** (as the WSGI server)
*   **Nginx** (as the reverse proxy)
*   **Docker** & **Docker Compose**

---

 🏁 Getting Started

To get a local copy up and running, follow these simple steps.

 Prerequisites

*   Docker and Docker Compose must be installed on your machine.
*   Node.js and npm (for potential frontend modifications).

 Installation & Launch

1.  **Clone the repo:**
    ```sh
    git clone https://github.com/ElsaDevOps/docker-learning.git 
2.  **Navigate to the project directory:**
    ```sh
    cd flask_redis_projects
    ```
3.  **Build and launch the Docker containers:**
    This single command will build the Flask/Nginx image, pull the Redis image, and start all services.
    ```sh
    docker-compose up  -d --scale web=3 --build
    ```
4.  **Run the frontend development server:**
    In a **new terminal**, navigate to the React frontend directory and start the dev server.
    ```sh
    cd my-react-frontend
    npm install
    npm run dev
    ```

5.  **View the application:**
    *   The backend API is available at `http://localhost:5002`
    *   The frontend application is running at `http://localhost:5173`

---
 Acknowledgements
*   The initial dashboard component design was inspired by a template from **Base44**.

# What I've learned and practiced
* **Docker** : Using Docker fundamentals in order to build custom images and use offical ones.
* **Persistance** : Using volumes to ensure that data can survive container restarts
* **Full Stack Debugging** : Network debugging, Console Debugging, Log Analysis and Root Cause Analysis
* **Containerization (Docker)**: wrote a Dockerfile to create a reproducible image of the Python application.
* **Multi-Container Orchestration (Docker Compose)**: Defined and managed a complex, multi-service application (web, nginx, redis), making them all work together on a single network.
* **Networking in Docker**: Debugged and solved critical networking issues, understanding port mapping ("5002:5002") and inter-container communication (binding to 0.0.0.0).
* **Reverse Proxy Configuration (Nginx)**: Used Nginx as a gateway to the application, a standard practice for production environments.
* **Data Persistence (Docker Volumes)**: Learned the crucial difference between ephemeral container storage and persistent data by implementing a Docker Volume for the Redis database.
* **Build Optimization**: Created a .dockerignore file to ensure fast, efficient, and secure Docker image builds.
