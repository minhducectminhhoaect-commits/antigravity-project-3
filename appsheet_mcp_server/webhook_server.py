"""
AppSheet Webhook Receiver Hub
Receives HTTP POST webhooks dispatched by Google AppSheet Automation Bots.
Logs incoming events to 'webhook_events.jsonl' for the Antigravity Agent to inspect and act on.
"""

import os
import json
import uvicorn
from datetime import datetime
from pathlib import Path
from fastapi import FastAPI, Request, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

# Load env
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

PORT = int(os.getenv("APPSHEET_WEBHOOK_PORT", "8000"))
WEBHOOK_SECRET = os.getenv("APPSHEET_WEBHOOK_SECRET", "")
EVENTS_LOG_FILE = Path(__file__).parent / "webhook_events.jsonl"

app = FastAPI(
    title="AppSheet Webhook Gateway for Antigravity",
    description="Bridge connecting AppSheet Automation Bots with Antigravity Agent"
)


def append_event_log(event_data: dict):
    """Ghi nhận sự kiện vào file webhook_events.jsonl"""
    try:
        with open(EVENTS_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(event_data, ensure_ascii=False) + "\n")
    except Exception as e:
        print(f"[-] Lỗi ghi nhận event: {e}")


@app.get("/")
def health_check():
    return {
        "status": "online",
        "service": "AppSheet Webhook Gateway",
        "timestamp": datetime.now().isoformat(),
        "events_logged": EVENTS_LOG_FILE.exists()
    }


@app.post("/webhook/appsheet")
async def receive_appsheet_webhook(request: Request, background_tasks: BackgroundTasks):
    """
    Endpoint nhận dữ liệu từ AppSheet Bot
    AppSheet Automation -> Task: Call a Webhook -> Url: http://your-tunnel-or-ip:8000/webhook/appsheet
    """
    # 1. Kiểm tra Secret nếu cấu hình
    if WEBHOOK_SECRET:
        token = request.headers.get("X-AppSheet-Secret") or request.query_params.get("secret")
        if token != WEBHOOK_SECRET:
            raise HTTPException(status_code=401, detail="Invalid Webhook Secret")

    # 2. Đọc payload
    try:
        payload = await request.json()
    except Exception:
        body_text = await request.body()
        payload = {"raw_text": body_text.decode("utf-8", errors="ignore")}

    event = {
        "id": f"evt_{int(datetime.now().timestamp() * 1000)}",
        "received_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "headers": dict(request.headers),
        "payload": payload
    }

    # 3. Ghi vào file bất đồng bộ
    background_tasks.add_task(append_event_log, event)

    print(f"\n[+] [APPSHEET TRIGGER NHẬN ĐƯỢC lúc {event['received_at']}]")
    print(json.dumps(payload, ensure_ascii=False, indent=2))

    return JSONResponse(
        status_code=200,
        content={"status": "received", "event_id": event["id"]}
    )


if __name__ == "__main__":
    print(f"[*] Khởi động AppSheet Webhook Server trên cổng {PORT}...")
    print(f"[*] Endpoint nhận sự kiện: http://localhost:{PORT}/webhook/appsheet")
    print(f"[*] File lưu sự kiện: {EVENTS_LOG_FILE}")
    uvicorn.run("webhook_server:app", host="0.0.0.0", port=PORT, reload=False)
