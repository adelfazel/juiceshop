init:
	docker pull bkimminich/juice-shop

build:
	docker build -t jstester .

startapp: stopall
	docker run --rm -d --network=host --name juiceshop -p 3000:3000 bkimminich/juice-shop

stopall:
	docker stop juiceshop  || true && docker rm juiceshop || true
	docker stop jstester  || true && docker rm jstester || true

testlocal: build
	docker stop jstester  || true && docker rm jstester || true
	docker run --rm -itd --network=host --name jstester jstester
	docker exec jstester pytest || true
	docker cp jstester:Tests/artefacts .

testweb: build
	docker stop jstester  || true && docker rm jstester || true
	docker run -e host='https://demo.owasp-juice.shop' --rm -itd --network=host --name jstester jstester
	docker exec jstester pytest || true
	docker cp jstester:Tests/artefacts .
	docker stop jstester


startdet:
	docker stop jstester  || true && docker rm tester || true
	docker run --rm -itd --network=host --name jstester jstester bash

goinsideapp:
	docker exec -it juiceshop sh

goinsidetest:
	docker exec -it jstester bash


