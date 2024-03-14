SHELL := /bin/bash
.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	
reinstall_package: ## Reinstall the package
	@pip uninstall -y musicbrain || :
	@pip install -e .

run_backend: ## Run the API
	uvicorn musicbrain.api.fast:app --reload

run_frontend: ## Run the API
	streamlit run ./musicbrain-front/userinterface.py

docker_build:
	docker build -f ./musicbrain/Dockerfile . -t musicbrain

docker_run:
	docker run --env-file="./.env" -p 8000:8000 musicbrain 