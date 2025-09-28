COMPOSE=sudo docker compose

DB_RUNNING := $(shell $(COMPOSE) ps -q db)

ifeq ($(DB_RUNNING),)
  POSTGRES_USER :=
  POSTGRES_DB :=
else
  POSTGRES_USER := $(shell $(COMPOSE) exec db printenv POSTGRES_USER)
  POSTGRES_DB := $(shell $(COMPOSE) exec db printenv POSTGRES_DB)
endif

# Docker
up:
	$(COMPOSE) up

stop:
	$(COMPOSE) down

reset:
	$(COMPOSE) down -v --rmi all --remove-orphans

migrate:
	$(COMPOSE) run --rm backend alembic upgrade head

revision:
	@if [ -z "$(m)" ]; then \
		echo "Please provide a message with m='your message'"; \
	else \
		$(COMPOSE) run --rm backend alembic revision --autogenerate -m "$(m)"; \
	fi

load-data:
	$(COMPOSE) exec db psql -U $(POSTGRES_USER) -d $(POSTGRES_DB) -f /db/locations.sql
	

