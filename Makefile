PWD=$(shell pwd)

setup:
	docker pull butomo1989/docker-android-x86-7.1.1

start:
	docker run --privileged -d -p 6080:6080 -p 4723:4723 -p 5554:5554 -p 5555:5555 -v $(PWD)/apps:/root/tmp -e DEVICE="Nexus 5" -e APPIUM=True -e APPIUM_HOST="127.0.0.1" -e APPIUM_PORT=4723 -e SELENIUM_HOST="172.17.0.1" -e SELENIUM_PORT=4444 --name android-container butomo1989/docker-android-x86-7.1.1

start-with-vpn:
	docker run --privileged -d -p 6080:6080 -p 4723:4723 -p 5554:5554 -p 5555:5555 -p 443:443 -v $(PWD)/apps:/root/tmp -e DEVICE="Nexus 5" -e APPIUM=True -e APPIUM_HOST="127.0.0.1" -e APPIUM_PORT=4723 -e SELENIUM_HOST="172.17.0.1" -e SELENIUM_PORT=4444 --name android-container butomo1989/docker-android-x86-7.1.1

stop:
	sudo docker stop android-container && sudo docker rm android-container
