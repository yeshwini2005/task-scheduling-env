# Task Scheduling RL Environment

## 📌 Overview
This project is a Reinforcement Learning (RL) environment that simulates real-world task scheduling. The agent must arrange tasks based on priority and deadlines.

## 🎯 Objective
To train an AI agent to schedule tasks efficiently using reward-based learning.

## 🧠 Tasks
- Easy: 2 tasks scheduling
- Medium: 3 tasks scheduling
- Hard: 4 tasks scheduling

## ⚙️ Observation Space
- List of tasks
- Each task contains:
  - Name
  - Deadline
  - Priority

## 🎮 Action Space
- Ordered list of task indices

## 🏆 Reward Function
- Score between 0 and 1
- Based on correctness of scheduling
- Penalizes incorrect ordering

Team Members:
- Yeshwini Parsi
- Jahnavi Satti

## ▶️ How to Run

```bash
python inference.py