# Population

## Overview
This shows an example of extracting clinical resources from a FHIR Server and pushing it to Medidata Rave

Notes:
* You will need a Username/Password on the Rave URL (with RWS role on the Study)
* Much of the translation from FHIR Resources to Clinical Data Elements has been hard coded.  
  * In the future we expect to be able to make this more dynamic using registries of element mappings (eg CDISC E2C, Mapping on the Resources themselves)
