mulutiprocess_test:
	docker build . -t python37
	- docker run --rm -it -v `pwd`:/usr/src python37 concurrent_test.py
	- docker run --rm -it -v `pwd`:/usr/src python37 multiprocess_starmap_test.py
	- docker run --rm -it -v `pwd`:/usr/src python37 multiprocess_starmap_async_test.py
