from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from slowapi import Limiter # type: ignore
from slowapi.util import get_remote_address # type: ignore
from slowapi.errors import RateLimitExceeded # type: ignore
from slowapi.middleware import SlowAPIMiddleware # type: ignore
from dotenv import load_dotenv
load_dotenv()

from database import SessionLocal
from models.request_log import RequestLog

# Routers
from routers import city, crop, upload, health, weather, analytics, analysis

# ================== Rate Limiter ==================
limiter = Limiter(key_func=get_remote_address)

# ================== Lifespan (تحميل الموديل مرة واحدة) ==================
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Server starting... loading AI models once")
    # load_model()  ← هيتحط هنا لاحقًا
    yield
    print("🛑 Server shutting down")

app = FastAPI(lifespan=lifespan, title="Smart Crop API")
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# ================== CORS ==================
app.add_middleware(
    CORSMiddleware,
    allow_origins=
    ["*"],  
    
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================== Request Logging ==================
@app.middleware("http")
async def log_requests(request: Request, call_next):
    db = SessionLocal()
    response = await call_next(request)

    log = RequestLog(
        endpoint=request.url.path,
        method=request.method
    )

    db.add(log)
    db.commit()
    db.close()
    return response

# ================== Global Validation Error ==================
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "message": "البيانات المدخلة غير صحيحة",
            "details": exc.errors()
        },
    )

# ================== Rate Limit Error ==================
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"message": "عدد الطلبات كبير جدًا، حاول مرة أخرى بعد دقيقة"}
    )

# ================== Include Routers ==================
app.include_router(city.router)
app.include_router(crop.router)
app.include_router(upload.router)
app.include_router(health.router)
app.include_router(weather.router)
app.include_router(analytics.router)
app.include_router(analysis.router)

# ================== Home ==================
@app.get("/")
def home():
    return {"message": "Smart Crop API working"}
    