# Keep in touch | my personal CRM
This is a personal CRM I built for myself.
It reminds me to get in touch with my contacts from time to time.
It's a super-small project built in Django, fully dockerized, running locally.

## How it works
Keep in touch lets you store contacts with a frequency to get in touch with them, e.g. 7 days to get in touch once a week. 
If you haven't contacted the person for this timespan, 
they will be marked as due to remind you to get in touch. 
After you've gotten in touch, 
mark the it as done and get reminded once the interval is over again.

It's that easy to keep in touch once in a while! 

## Development
### Set up PyCharm
To set up a remote interpreter for PyCharm, choose docker-compose, the `web` service.
As a python path, use the return of the following command:
```
docker-compose exec web pipenv --py
```
which should be
```
/root/.local/share/virtualenvs/code-_Py8Si6I/bin/python
```

## ToDo
* Improve import by editing afterwards
* Improve import by extracting and using emails
* Merging contacts
* add type of touchpoint and note functionality