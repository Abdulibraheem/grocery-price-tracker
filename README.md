# Grocery Price Tracker

## Setup Instructions

### 1. Clone Repo
```bash
git clone https://github.com/YOUR_USERNAME/grocery-price-tracker.git
cd grocery-price-tracker

### 2. Run Backend
cd backend
uvicorn app.main:app --reload

### 3. Start Database
cd infra
docker-compose up -d


