# repliq_monitoring_system

This is my Django Practical Challenge app for assigning/returning company equipments

Usage:
This is a POST request to generate sample data for the following:
Cannot be used multiple times (Will only update the data), 
Company, Department and Users

http://127.0.0.1:8000/core/populate_db/

This is another POST request to generate sample data for Equipments.
Can be used multiple times. 
The data generated will have unique serial numbers.
http://127.0.0.1:8000/core/populate_devices/

