# equip_monitoring_system

1. The homepage will display all the API endpoints.
http://127.0.0.1:8000/

2. This is a POST request to generate sample data for the following:
Cannot be used multiple times (Will only update the data), 
Company, Department and Users
http://127.0.0.1:8000/core/populate_db/

3. This is another POST request to generate sample data for Equipments.
Can be used multiple times. 
The data generated will have unique serial numbers.
http://127.0.0.1:8000/core/populate_devices/

