# LLM Security Helper

A professional security auditing tool designed to identify vulnerabilities in source code and perform threat modeling for GenAI/Agentic application specifications. This tool maps findings to the **OWASP Top 10 for LLM Applications (2025)** and the **MITRE ATLAS** framework.

## 🛠 Features

### Part 1: Source Code Security Analysis
* **Vulnerability Detection:** Identifies critical flaws such as SQL Injection, Command Injection, and Insecure Deserialization.
* **Security Remediation:** Provides actionable, secure-by-default code snippets to fix identified risks.
* **Technical Focus:** Concentrates specifically on security invariants rather than general code style.

### Part 2: GenAI Architecture Threat Modeling
* **Spec Analysis:** Evaluates system architectures, agent permissions, and data flow.
* **Framework Mapping:** * **OWASP LLM Top 10:** Identifies risks like Excessive Agency (LLM06) and System Prompt Leakage (LLM07).
    * **MITRE ATLAS:** Maps adversarial tactics such as LLM Prompt Injection (AML.T0051) and AI Service API exploitation (AML.T0096).

---

##  Start Guide

Follow these commands in your terminal to set up and run the application on macOS.

### 1. Repository Setup
```bash
# Clone the repository
git clone
[https://github.com/YOUR_USERNAME/llm-security-helper.git](https://github.com/YOUR_USERNAME/llm-security-helper.git)](https://github.com/ahlahaider/LLM-security-helper.git)
cd llm-security-helper

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate
