# Deployment Guide — AICTE AI-Powered Scrutiny & EVC Review Platform

This project is configured for cloud deployment across platforms including **Render**, **Vercel**, **Netlify**, and **Docker**.

---

## 🚀 Option 1: 1-Click Blueprint on Render (Recommended & Fastest)

The repository includes a ready-to-use [`render.yaml`](../render.yaml) blueprint that deploys **both the FastAPI backend and React frontend** simultaneously.

### Step-by-Step:
1. **Push your code to GitHub**:
   ```bash
   git add .
   git commit -m "Add production deployment configurations"
   git push origin main
   ```
2. Log in to [Render Dashboard](https://dashboard.render.com).
3. Click **New +** and select **Blueprint**.
4. Connect your GitHub repository (`SIH_PramanAI`).
5. Render will detect [`render.yaml`](../render.yaml) and automatically configure:
   - **`aicte-scrutiny-backend`** (Python/FastAPI web service)
   - **`aicte-scrutiny-frontend`** (React/Vite static site with SPA routing)
   - Automatic environment binding (`VITE_API_BASE_URL` mapped to backend URL)
6. Click **Apply**. Both services will build and deploy!

---

## 🌐 Option 2: Render (Backend) + Vercel (Frontend)

If you prefer using Vercel for frontend edge CDN performance:

### Step 1: Deploy Backend on Render
1. Go to [Render Dashboard](https://dashboard.render.com) > **New +** > **Web Service**.
2. Connect your GitHub repository.
3. Configure the settings:
   - **Name**: `aicte-scrutiny-backend`
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Health Check Path**: `/health`
4. Click **Deploy Web Service**.
5. Once deployed, copy your backend URL (e.g., `https://aicte-scrutiny-backend.onrender.com`).

### Step 2: Deploy Frontend on Vercel
1. Go to [Vercel Dashboard](https://vercel.com) > **Add New Project**.
2. Import your GitHub repository.
3. In project settings:
   - **Root Directory**: Click edit and choose `frontend`.
   - **Framework Preset**: `Vite`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
4. Expand **Environment Variables** and add:
   - `VITE_API_BASE_URL` = `https://aicte-scrutiny-backend.onrender.com` *(your Render backend URL)*
5. Click **Deploy**. Vercel will use [`vercel.json`](../frontend/vercel.json) to handle SPA client routes.

---

## ⚡ Option 3: Netlify (Frontend)

If deploying the frontend on Netlify:
1. Go to [Netlify Dashboard](https://app.netlify.com) > **Add new site** > **Import an existing project**.
2. Select your repository.
3. Settings:
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `frontend/dist`
4. Add Environment Variable:
   - `VITE_API_BASE_URL` = `https://your-backend-url.onrender.com`
5. Netlify will use [`netlify.toml`](../frontend/netlify.toml) to route all paths to `index.html`.

---

## 🐳 Option 4: Docker & Docker Compose (Any VPS / Cloud Server)

To deploy both frontend and backend on any VPS (AWS EC2, DigitalOcean, Hetzner, etc.):

```bash
# Clone and enter the repository
git clone https://github.com/syntaxaeror/SIH_PramanAI.git
cd SIH_PramanAI

# Build and start all containers in the background
docker compose up -d --build
```

- Frontend will be live on: `http://<your-server-ip>:3000`
- Backend API will be live on: `http://<your-server-ip>:8000`
- API documentation: `http://<your-server-ip>:8000/docs`

---

## ⚙️ Environment Variables Summary

| Service | Variable | Description | Default |
|---|---|---|---|
| **Backend** | `PORT` | Listening port for Uvicorn | `8000` |
| **Backend** | `DATABASE_URL` | SQLAlchemy database connection string (SQLite, PostgreSQL, etc.) | `sqlite:///aicte_scrutiny.db` |
| **Frontend** | `VITE_API_BASE_URL` | Full URL of the deployed FastAPI backend | `""` (uses local Vite proxy) |

---

## 🛡️ Database & Auto-Seeding
- When the backend starts up, it automatically verifies the database.
- If the database is empty, it runs [`seed_data.py`](../backend/seed_data.py) to seed **20 realistic AICTE applications across 5 categories** with documents, OCR findings, and EVC room assets.
