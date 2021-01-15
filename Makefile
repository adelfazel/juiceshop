init:
	docker pull bkimminich/juice-shop

build:
	docker build -t jstester .

start: stop
	docker run --rm -d --network=host --name juiceshop -p 3000:3000 bkimminich/juice-shop

stop:
	docker stop juiceshop  || true && docker rm juiceshop || true
	docker stop jstester  || true && docker rm jstester || true

test: build
	docker stop jstester  || true && docker rm jstester || true
	docker run --rm -itd --network=host --name jstester jstester bash
	docker exec jstester pytest || true
	docker cp jstester:Tests/artefacts .

startdet:
	docker stop jstester  || true && docker rm tester || true
	docker run --rm -itd --network=host --name jstester jstester bash

goinside:
	docker exec -it jstester bash