# 📊 Enterprise System Monitor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688)
![WebSockets](https://img.shields.io/badge/WebSockets-Live-success)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED)

A lightweight, robust, and real-time hardware and network monitoring platform. This project bridges the gap between low-level system administration and modern backend development by utilizing Python to extract core system metrics and streaming them to a client-facing web dashboard via WebSockets.

---

## ✨ Key Features
* **Real-Time Data Streaming:** Uses WebSockets for instantaneous, zero-latency data transmission.
* **Comprehensive Metrics:** Monitors CPU usage (logical cores), Memory (RAM) utilization, and Network I/O (upload/download traffic).
* **Zero-Dependency Frontend:** The dashboard is built purely with HTML5, Vanilla JavaScript, and CSS3. No heavy JS frameworks required.
* **RESTful API Fallback:** Includes standard HTTP REST endpoints (`/api/v1/status`) alongside the WebSocket stream.

## 🧠 System Data Flow
```mermaid
graph LR
    A[OS Hardware] -->|psutil| B(Python Core)
    B -->|Raw Metrics| C{FastAPI Server}
    C -->|REST HTTP| D[API Endpoint /status]
    C -->|WebSocket| E[Live HTML Dashboard]
    E -->|Renders JSON| F((Client Monitor))
    
    style C fill:#009688,stroke:#fff,stroke-width:2px,color:#fff
    style E fill:#f39c12,stroke:#fff,stroke-width:2px,color:#fff