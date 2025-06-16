# Data Integrations Systems Engineer Final Evaluation


### Problem Statement

The Philly311 contact center services non-emergency requests from residents, such as potholes, illegal dumping, and other public issues. These requests/complaints are available for the public to see here.  311 routes certain service requests to the department of Licenses and Inspections (service requests for which L&I is the “agency_responsible”), and then L&I sends out inspectors to determine if there is a code violation that needs to be issued. 

### Plan

- [x] Initialize git repo

- [x] Write up initial README

- [x] Set up initial Dockerfile

- [r] Set up initial Python script and dependencies

- [x] Grab 311 tickets for 2025 assigned to L&I

  - [x] Download https://phl.carto.com/api/v2/sql?filename=public_cases_fc&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*%20FROM%20public_cases_fc%20WHERE%20requested_datetime%20%3E=%20%272025-01-01%27%20AND%20requested_datetime%20%3C%20%272026-01-01%27

  - [x] Select tickets assigned to L&I

- [x] Use AIS API to search  by address to get the "opa_account_num" for each service request

  - https://api.phila.gov/ais/v2/search/1400%20john%20f%20kennedy%20blvd

- [ ]  Use "opa_account_num" to join your service requests subset to the Violations dataset

  - [ ] Download https://phl.carto.com/api/v2/sql?&filename=violations&format=csv&skipfields=cartodb_id,the_geom,the_geom_webmercator&q=SELECT%20*,%20ST_Y(the_geom)%20AS%20lat,%20ST_X(the_geom)%20AS%20lng%20FROM%20violations%20WHERE%20violationdate%20%3E=%20%272019-01-01%27

  - [ ] JOIN to service requests on opa_account_num

- [ ]  Perform analysis

  - [ ] How many service requests since the beginning of the year has 311 associated with “License & Inspections” as the agency_responsible? 
    
  - [ ] What percentage of these service requests have resulted in the issuance of a code violation? 

  - [ ] What percentage of these service requests have not been closed? (i.e. L&I has not finished inspecting them)

- [ ] Dump results into home

- [ ] Test Dockerfile

- [ ] Clean up README


