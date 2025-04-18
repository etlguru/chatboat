build:
	docker build -t llm-chatbot .

run:
	docker run -p 7860:7860 llm-chatbot
