# Data Integrations Systems Engineer Final Evaluation

## How to run

```
docker build -t evaluation .
docker run -v ~/output:/output evaluation
```

The script will output several files into `~/output` on host. The `summary.txt` files includes the results of the analysis.

## Problem Statement

The Philly311 contact center services non-emergency requests from residents, such as potholes, illegal dumping, and other public issues. These requests/complaints are available for the public to see here.  311 routes certain service requests to the department of Licenses and Inspections (service requests for which L&I is the “agency_responsible”), and then L&I sends out inspectors to determine if there is a code violation that needs to be issued. 

### Results of analysis

My analysis is summarized below:

Current year L&I requests count: 128324
Current year L&I requests percent with violation issued: 100.0
Current year L&I requests percent not closed: 54.68891244038527

While 100% violations issued seems odd to me, and I therefore wonder if I should have derived this differently, if I take the results at face value they would suggest that 311 requests are leading to violations being issued consistently, and that approximately one in two of those requests are closed for the year. Not knowing much of the context for what it takes to close a request that leads to an L&I code violation, this seems reasonable to me, which suggests the process is working well, though there is perhaps room for improvement. We could investigate further by looking into mean time to resolution.

## Plan

- [x] Initialize git repo

- [x] Write up initial README

- [x] Set up initial Dockerfile

- [x] Set up initial Python script and dependencies

- [x] Grab 311 tickets for 2025 assigned to L&I

  - [x] Download https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20FROM%20public_cases_fc%20WHERE%20requested_datetime%20%3E=%20%272025-01-01%27%20AND%20requested_datetime%20%3C%20%272026-01-01%27

  - [x] Select tickets assigned to L&I

- [x] Use AIS API to search  by address to get the "opa_account_num" for each service request

  - https://api.phila.gov/ais/v2/search/1400%20john%20f%20kennedy%20blvd

- [x]  Use "opa_account_num" to join your service requests subset to the Violations dataset

  - [x] Download https://phl.carto.com/api/v2/sql?&filename=violations&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20violations%20WHERE%20violationdate%20%3E=%20%272019-01-01%27

  - [x] JOIN to service requests on opa_account_num

- [x]  Perform analysis

  - [x] How many service requests since the beginning of the year has 311 associated with “License & Inspections” as the agency_responsible? 
    
  - [x] What percentage of these service requests have resulted in the issuance of a code violation? 

  - [x] What percentage of these service requests have not been closed? (i.e. L&I has not finished inspecting them)

- [x] Dump results into home

- [x] Test Dockerfile

- [x] Clean up README


### Next Steps

A few things I would like to do given more time:

- Improve error handling

- Parallelize calls to AIS API so they don't take so long

- Specify dtypes on CSVs during import

- Break up the setup file into several files to improve Docker's caching during builds

- Add an ENV for skipping cached files

