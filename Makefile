all: test

clean:
	@find . -name "*.pyc" | xargs rm -f

test: clean
	app/manage.py collectstatic --noinput
	./runtests

database:
	app/manage.py migrate
	app/manage.py syncdb

run: clean
	app/manage.py runserver 0.0.0.0:7000

install:
	pip install -r requirements.txt
