# Sunglasses Hub

## Overview

This project showcases the application of Data Engineering tools and concepts. 
The ETL pipeline extracts data from the Sunglasseshut website and visualizes it in a Power BI dashboard.

## Tools and Technologies

The following tools were utilized in this project:

- **Azure**: Hosting the infrastructure.
- **Terraform**: Infrastructure as Code (IaaC) for resource provisioning.
- **Airflow**: Workflow orchestration.
- **Docker**: Containerization of the pipeline.
- **Insomnia**: Generating code to send requests to the web page API.
- **Power BI**: Data visualization.
- **Python**: Primary programming language.

## Architecture

1. **Data Scraping**: Use Insomnia and Python to scrape data from the Sunglasseshut website.
2. **Data Storage**: Convert the extracted data into a DataFrame and upload it to an Azure Storage account using Azure Identity and Azure Blob Storage client libraries.
3. **Data Cleaning**: Clean and validate data types using Pydantic's data classes.
4. **Data Delivery**: Store the processed data in Azure Synapse (Data Warehouse) and Azure Database for PostgreSQL - Flexible Server.
5. **Data Visualization**: Analyze and visualize the data using Power BI or other preferred tools.

## Dashboard

The final dashboard provides insights into the extracted data. 

## Project Requirements

To ensure the pipeline functions correctly, the following tools need to be installed and configured:

- **Azure CLI**: For account configuration and Terraform provisioning.
- **Terraform**: For infrastructure provisioning.
- **Docker**: For running Airflow and containerizing the pipeline.
