# Digital Control Room - Django Test
## RT

## Documentation
The original README file containing the tech specs was moved to [docs/TECH_SPECS_ORIG_README.md](docs/TECH_SPECS_ORIG_README.md) .

## Tech stack
- Python version: 3.11.1
- Virtual environment and package manager: `uv`
- Dev tools:
  - Debugger:`ipdb`
  - Code linter: `ruff`
  - Project tasks manager: `make`
If you have [Make](https://www.gnu.org/software/make/) installed on your system please type `make <enter>` to see commands available.


## Tech response
### Setup
- Repo cloned, remote configured, venv created.
- To setup the environment using `uv`: `uv sync`
- The project have a welcome page on the root url, [localhost:8000](http://localhost:8000) .
### Exercise 1 - Complete Stats View
- Added the query to calculate the stats to the view.
### Exercise 2 - Integrate with API
- Added `requests` package to call the API
- In `manage` command, get data from the API
### Exercise 3 - Store additional Data



-------
