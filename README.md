# Space-Maps

## Description

A full-stack project built with **Next.js (frontend)**, **FastAPI (backend)**, and **Tailwind CSS**.  
This repo contains both the frontend and backend code to run the Space-Maps app for the **NASA Space Apps Challenge 2025**.

---

## How to Run

Open **CMD** from the project directory and run the following commands:

```cmd
:: Git clone
git clone https://github.com/YOUR_USERNAME/Space-Maps/
cd Space-Maps

:: Create and activate virtual environment (only for first run) and install backend dependencies
py -m venv venv
venv\Scripts\activate
pip install -r backend/requirements.txt
deactivate

:: Install frontend dependencies
cd frontend
npm install
cd ..
