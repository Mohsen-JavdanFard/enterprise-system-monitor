from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import psutil
import asyncio
import uvicorn

# مقداردهی اولیه برنامه با توضیحات استاندارد
app = FastAPI(
    title="Enterprise System Monitor API",
    description="Real-time hardware and network monitoring service",
    version="1.0.0"
)

# همان هسته پردازشی فاز اول
def fetch_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=None) # برای سرعت در API اینتروال را حذف کردیم
    cpu_cores = psutil.cpu_count(logical=True)
    
    ram = psutil.virtual_memory()
    net_io = psutil.net_io_counters()

    return {
        "CPU": {
            "Cores": cpu_cores,
            "Usage_Percent": cpu_usage
        },
        "RAM": {
            "Total_GB": round(ram.total / (1024**3), 2),
            "Usage_Percent": ram.percent
        },
        "Network": {
            "Sent_MB": round(net_io.bytes_sent / (1024**2), 2),
            "Received_MB": round(net_io.bytes_recv / (1024**2), 2)
        }
    }

# ---------------------------------------------------------
# مسیر اول (REST API): برای دریافت وضعیت لحظه‌ای با درخواست HTTP
# ---------------------------------------------------------
@app.get("/api/v1/status")
async def get_current_status():
    return fetch_system_metrics()

# ---------------------------------------------------------
# مسیر دوم (WebSocket): برای استریم زنده و مداوم داده‌ها به سمت مانیتور کلاینت
# ---------------------------------------------------------
@app.websocket("/ws/stream")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # دریافت داده‌ها و ارسال مستقیم به صورت فرمت JSON
            data = fetch_system_metrics()
            await websocket.send_json(data)
            
            # تاخیر ۱ ثانیه‌ای برای جلوگیری از فشار به پردازنده سرور
            await asyncio.sleep(1)
            
    except WebSocketDisconnect:
        print("Client disconnected from the dashboard.")

# اجرای سرور
if __name__ == "__main__":
    print("Starting Enterprise API Server on port 8000...")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)