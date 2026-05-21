# 🩺 Real-Time Multilingual Voice AI Agent – Clinical Appointment Booking

## Overview
This project implements a **real-time voice AI agent** for digital healthcare platforms.  
The agent manages the full appointment lifecycle — booking, rescheduling, cancellation, and conflict resolution — entirely through natural voice conversations in **English, Hindi, and Tamil**.

Target latency: **< 450 ms** from speech end to first audio response.

---

## 🚀 Tech Stack
- **Backend:** Python (FastAPI, WebSockets, Redis, PostgreSQL)
- **Frontend:** React + TypeScript
- **Speech:** Whisper/Vosk (ASR), Coqui TTS (voice responses)
- **Memory:** Redis (TTL for session + persistent patient history)
- **Scheduling:** PostgreSQL (doctors, slots, appointments)

---

## 📂 Project Structure

---

## 🧠 Architecture Decisions
- **FastAPI + WebSockets** → low-latency streaming pipeline.
- **Redis** → hybrid memory (session TTL + persistent patient history).
- **PostgreSQL** → structured scheduling with conflict resolution.
- **React Hooks** → lightweight demo UI for voice input and appointment display.

---

## 🗂️ Memory Design
- **Session memory:** Current intent, pending confirmations.
- **Persistent memory:** Patient history, preferred doctor, last appointment.
- Redis schema:

---

This README is **recruiter-ready**: it shows clear architecture, latency awareness, tradeoffs, and limitations.  

👉 Do you want me to also generate the **architecture diagram (PNG)** layout so you can drop it into your repo, or should we expand the **frontend with microphone streaming** first?
