# The Valoo recruitment exam template
## Pre-requisites
You'll need Python 3 and your exam instructions ;)

## Getting started
- Fork this repo
- Setup your virtualenv
- Clone your fork
- Install dependencies and basic data:

```bash
make deps init
```

## Running the test server
```bash
make rs
```

## Running the fabulous test suite!
```bash
make test
```

## Submitting
When you're ready for review, create a PR against the original repo. We'll check it!

## Alexis MANUEL - Work done

### Timeout handling:

To enable user to continue interaction with the front-end on timed out requests, a simple front using asynchronous toggle_playing method call was implemented in vanilla JS. Furthermore, the method is using django-rq as a queue to further process failed remote API call. RQ was chosen in order to build a prototype fast but Celery is also a solid choice. Also, the job worker has to be started manually as no daemon is automatically created on server startup.

### Error storage: 

On error response from remote server, it is stored in the PlayError model which stores playback errors. This way, it is fairly straightforward to get all errors by simply calling one entity (the route api/play_errors is implemented to do so)

### Restart failed operations:

A custom command called mpe (for Manage Play Error) is implemented to allow error listing, syncing and deletion with --list, --sync and --delete arguments respectively. However, the syncing part doesn't work well because of the major verification on create call.
