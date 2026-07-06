from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from pydantic import BaseModel
import logging
from datetime import datetime

logger = logging.getLogger("gsagency")


class ContactForm(BaseModel):
    name: str
    email: str
    company: str = ""
    budget: str = ""
    message: str


app = FastAPI(title="GS Creative Agency")

# Static files
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

# Templates — Starlette 1.3+ signature: TemplateResponse(request, name, context)
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


def _context(active: str = "") -> dict:
    return {
        "active": active,
        "year": datetime.now().year,
    }


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html", _context("home"))


@app.get("/services", response_class=HTMLResponse)
async def services(request: Request):
    return templates.TemplateResponse(request, "services.html", _context("services"))


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(request, "about.html", _context("about"))


@app.get("/portfolio", response_class=HTMLResponse)
async def portfolio(request: Request):
    return templates.TemplateResponse(request, "portfolio.html", _context("portfolio"))


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse(request, "contact.html", _context("contact"))


@app.get("/health")
async def health():
    return JSONResponse({"status": "ok"})


@app.post("/contact")
async def contact_submit(form: ContactForm):
    logger.info(
        "Contact form submission: name=%s, email=%s, company=%s, budget=%s",
        form.name, form.email, form.company, form.budget,
    )
    # In production: send email notification to hello@gscreativeagency.com
    return JSONResponse({"ok": True})


@app.exception_handler(404)
async def not_found(request: Request, exc):
    return templates.TemplateResponse(request, "404.html", _context(), status_code=404)
