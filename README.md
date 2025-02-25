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
- Admin access: `admin / SuperUser`
- 
### Exercise 1 - Complete Stats View
- Added the query to calculate the stats to the view.
### Exercise 2 - Integrate with API
- Added `requests` package to call the API
- In `manage` command, get data from the API
### Exercise 3 - Store additional Data
- Note about the `top_level_domain` field:
  - In the API to ingest the data, the Top leve; domain is return as a list, that may contain more than one value.    
    So, we need a way to store one or more values in the same field.
  - The standard approach would be to use the models.JSONField(), that exists in Django since version 3.1. 
  - However, this project is using Django 2.2, that does not support this feature. 
  - The proper handle this task would be to upgrade Django to a newer version. 
  - However, I'm assuming that this is part of the challenge - finding an alternative solution. 
  - So, we went with the present solution:
    - a TextField that stores serialized JSON, with the required helper functions. 
  - Another alternative would be to create an additional table for TLDs with a relation to the Countries table. 
  However, this would be more time consuming - and inefficient from the perspective of data management, once the TLDs are unique.
 

 - Note 2: Once we don't have an "update" method, I erased the SqLite DB and recreated it with a new ingest.
   - Admin access: `admin / SuperUser`
  
- Added a new endpoint to list the countries: [http://localhost:8000/countries/countries/](http://localhost:8000/countries/countries/)
  - This is an extra feature, not required by the exercise.
 
## Final note:
We could have used Django Rest Framework to handle the API.   
However, once it was not required, nor have a reference to freedom of technology adoption, we went with the approach already present in the Project.

Thank you for reading and evaluating!

-------

