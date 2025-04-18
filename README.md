# chatboat
local path

/Users/kartik/llm

# Mini LLM Chatbot (GPT2-based)

This is a lightweight, containerized project designed to showcase how to run a basic Large Language Model (LLM) system using HuggingFace's GPT-2 model. It includes both a backend (FastAPI) and a user-friendly UI (Gradio), wrapped in Docker for portability.

---

## What This Project Does
- Uses HuggingFace Transformers to load a GPT-2 model
- Exposes a FastAPI endpoint (`/generate`) to serve responses
- Provides a Gradio web UI (optional enhancement)
- Entire setup is automated with a bash script and `Makefile`

---

## Components
| File/Folder        | Purpose                                  |
|--------------------|-------------------------------------------|
| `app/model.py`     | Loads GPT-2 and defines text generator   |
| `app/main.py`      | FastAPI backend exposing `/generate` API |
| `ui/interface.py`  | Gradio UI to interact with the chatbot   |
| `Dockerfile`       | Docker setup to containerize the app     |
| `run.sh`           | Auto-generates all files and structure    |
| `Makefile`         | Build and run commands                    |

---

## Setup Instructions

### 1. Clone and run the setup script
```bash
git clone https://github.com/etlguru/chatboat.git
cd chatboat
```

### 2. Build the Docker image
```bash
make build
```

### 3. Run the chatbot container (FastAPI)
```bash
make run
```

### 4. Test the endpoint (via curl or browser)
```bash
curl "http://localhost:7860/generate?prompt=Hello"
```

Expected response:
```json
{"response":"Hello, how are you doing today?..."}
```

### Optional: Enable Gradio UI
If you want to use the Gradio chat interface instead of FastAPI:
- Change the Dockerfile `CMD` to run `ui/interface.py`
- Update the launch command in Gradio:
```python
grad_interface.launch(server_name="0.0.0.0", server_port=7860)
```

---

## Requirements
- Docker
- Python (3.10+ if running without Docker)

### Python packages used
```
fastapi
gradio
transformers
uvicorn
torch
```

---

## Performance Notes
- Based on GPT-2 (124M parameters)
- Runs entirely on CPU (can be upgraded to GPU)
- Ideal for demos, experimentation, and prototyping
- No API limits (runs locally)

---

## License and Use
- GPT-2 is open-source under [OpenAI License](https://github.com/openai/gpt-2/blob/master/LICENSE)
- This repo is for educational and non-commercial use
- Replace with larger models (e.g., GPT-Neo, LLaMA) for production use

---

## Contributions
PRs welcome! Open issues or suggest features for improvement.

---

## Resources
- [GPT-2 on HuggingFace](https://huggingface.co/gpt2)
- [Gradio Docs](https://gradio.app)
- [FastAPI Docs](https://fastapi.tiangolo.com)
- [Docker Docs](https://docs.docker.com)

---
Made with care by Kartikey Mishra
