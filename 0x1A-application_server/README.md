### Application_server


## Project Requirements

- A README.md file, at the root of the folder of the project, is mandatory
- Everything Python-related must be done using `python3`
- All config files must have comments
- All your files will be interpreted on `Ubuntu 16.04 LTS`
- All your files should end with a new line
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck` (`version 0.3.7-5~ubuntu16.04.1` via `apt-get`) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing.

### Project task
- 0. Set up development with Python
	Let’s serve what you built for AirBnB clone v2 - Web framework on web-01. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.

	__Requirements:__

	- Make sure that task #3 of your SSH project is completed for web-01. The checker will connect to your servers.
	- Git clone your AirBnB_clone_v2 on your web-01 server.
	- Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000.
	- Your Flask application object must be named app (This will allow us to run and check your code).

