# Safertesk Backend task

This task demonstrates basic database management system (DBMS) operations using Python and MySQL. 

It allows users to insert values into tables and search for addresses using both JOIN and non-JOIN methods.

## Functionality

### Insert Values

The project provides functionality to insert values into two tables: `countries` and `locations`. 

- **Insert Countries**: Users can input the country ID, country name, and region ID to insert values into the `countries` table.

- **Insert Locations**: Users can input the location ID, street address, postal code, city, state/province, and country ID to insert values into the `locations` table.

### Search Addresses

The project offers two methods for searching addresses:

1. **With JOIN**: Users can search for addresses using a JOIN operation between the `locations` and `countries` tables. This method allows users to retrieve addresses along with the corresponding country names.

2. **Without JOIN**: Users can search for addresses without using a JOIN operation. Instead, the project uses a correlated subquery to fetch the country name for each address. This method may be less efficient compared to using a JOIN operation.

### For Search Address
![image](https://github.com/Dineshkumaryara/2100031355_Backend/assets/110585667/e5e7c67b-8590-4d35-be24-974f217dcfc3)

### For Insert Values
![image](https://github.com/Dineshkumaryara/2100031355_Backend/assets/110585667/c68dde76-8356-4893-bda8-6053282fdd3f)


