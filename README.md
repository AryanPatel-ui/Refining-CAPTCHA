# Passive CAPTCHA Replacement System 🤖

An ML-based passive CAPTCHA alternative that detects bots and distinguishes them from legitimate human users without requiring users to solve traditional CAPTCHA challenges.

## 🎯 Objective

Develop an intelligent security system that improves user experience while protecting web applications from automated bot traffic.

## ⚙️ Proposed Approach

The system uses a hybrid detection mechanism:

- **Rule-Based Detection:** Identifies suspicious request patterns and abnormal activity.
- **Logistic Regression:** Provides baseline bot classification.
- **Random Forest:** Detects complex behavioral patterns.
- **Adaptive Verification:** Assigns risk levels and determines appropriate security actions.

## 🛠️ Tech Stack

- Python
- FastAPI
- Scikit-learn
- Pandas & NumPy
- PostgreSQL
- Redis (Optional)

## 🏗️ System Workflow

1. Collect user behavioral and request-level signals.
2. Extract relevant features.
3. Analyze activity using rules and ML models.
4. Calculate the risk level.
5. Allow, verify, or restrict the request.

## 🚀 Project Status

<badge color="warning">In Development</badge>

- [x] System architecture and database design
- [x] Technology stack selection
- [ ] FastAPI backend
- [ ] Feature extraction
- [ ] ML model training
- [ ] Risk assessment engine
- [ ] System integration and testing

## 🎯 Goal

Build a scalable, explainable, and efficient bot detection system that minimizes friction for legitimate users while identifying automated threats.

---

*An independent academic project inspired by UIDAI's passive CAPTCHA replacement problem statement.*
