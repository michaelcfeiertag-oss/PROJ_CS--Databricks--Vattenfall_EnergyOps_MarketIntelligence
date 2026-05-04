# PROJ_CS--Databricks--Vattenfall_EnergyOps_MarketIntelligence
StartSteps // Databricks // Vattenfall : Market Intelligence Lakehouse (raw files, 3 layers, SQL, Spark, Permissions mgmt)

## DISCLAIMER:
This project is built from scratch and refers to => [https://github.com/cloud-data-engineering/vattenfall-week9-day1-github-tutorial.git]

Overall, it is built in the training "Week 9" taught by StartSteps organization. 
The development goes over 4 working days.

## SCOPE: 
### Themes: 
This capstone simulates a Databricks implementation that combines:
- reference data (assets master data => raw-data file "/reference/asset_reference.csv").
- energy market price data (=> raw-data file "/market_prices/market_prices_north_01.csv")
- weather observations (=> raw-data file "/weather/weather_north_01.csv")
- grid telemetry and incident events (=> raw-data file "/grid_events/grid_events_north_01.csv")

All these raw-data files are being uploaded into Databricks Repository into dedicated Folder: "sample_data".

### Targets of the Project from content perspective: 
- Load raw data files from a project folder into according Databricks UNITY CATALOG objects (namely: Volumes).
- Build in UNITY CATALOG a LAYERED ARCHITECTURE for the database tables (namely: Bronze / Silver / Gold).
- Use Databricks Notebooks with SQL-Cells to create the UNITY CATALOG objects, and SPARK-SQL for creating the UNITY CATALOG tables.
- Use a layered Notebook approach to be able to create and load respectively everything PROGRAMMATICALLY.
- Use re-usable PYTHON script files for data management (cleaning and filtering).
- Use re-usable PYTHON script files for data enrichment (Business Rules as PYTHON functions, eventually UDF based Business Rules).
- Permission Management on the UNITY CATALOG objects.

### Targets of the Project from additional learning perspective: 
- Start a Databricks development project directyl and firstly from GIT-HUB (!).
- Implement a good Governance Structure on both: Git-Hub repository and Best-Practise folder structure.




