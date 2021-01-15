build:
	docker build -t anztester .

startjs:
	docker pull bkimminich/juice-shop
	docker run --rm -d --name juiceshop -p 3000:3000 bkimminich/juice-shop

init: build startjs

stop:
	docker stop js


test:
	docker run --rm anztester

startdet:
	docker run --rm -itd --name tester anztester bash

goinside:
	docker exec -it tester bash