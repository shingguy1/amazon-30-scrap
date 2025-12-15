# Product Recommendation Platform Backend

This is a Python FastAPI backend for serving product recommendations to your website frontend.

## Features
- REST API endpoint for product recommendations
- Easily extendable recommendation logic

## Getting Started

1. **Install dependencies:**
   ```powershell
   pip install fastapi uvicorn
   ```
2. **Run the server:**
   ```powershell
   uvicorn main:app --reload
   ```
3. **API Endpoint:**
   - `GET /recommendations?user_id=123`

## Project Structure
- `main.py` — FastAPI app and endpoints
- `.github/copilot-instructions.md` — Copilot custom instructions

---

Replace the sample recommendation logic with your own as needed.
