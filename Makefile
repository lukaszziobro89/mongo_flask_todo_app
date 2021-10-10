up:
	docker-compose up
up-detached:
	docker-compose up -d
up-recreate:
	docker-compose up --build --force-recreate
up-detached-recreate:
	docker-compose up -d --build --force-recreate
down:
	docker-compose down
