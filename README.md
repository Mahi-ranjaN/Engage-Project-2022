# PROJECT FOR THE INTERN ENGAGE MENTORSHIP 2022

## PROBLEM STATEMENT: 

* Develop an application to demonstrate how the Automotive Industry could harness data to take informed decisions.
* You could choose to use the data set provided, or use any open-source data set available you might have access to, or create your own.
* Demonstrate the use of data analytics in identifying: Customer segments, Most popular car specification combination (engine type, fuel, mileage, etc), Right time to launch a new car, etc.


### LANGUAGE USED
* Python

### HOW TO RUN THIS PROJECT IN YOUR LOCAL SYSTEM?

* Step 1: Install Python from [here](https://www.python.org/downloads/)

![Python](/Screen_Shots/Python_Download.png)

* Step 2: Install any IDE of your choice. I have used [Visual Studio Code](https://code.visualstudio.com/)

![Visual Studio Code](/Screen_Shots/VS_Code.png)

* Step 3: Create a folder in your local system and open it inside Visual Studio Code.

* Step 4: Install an extension named 'GitHub Pull Requests and Issues' inside the Visual Studio Code. A source control tab will get appear in the side bar of the VS Code window once you install this extension.  

![Github Extension](/Screen_Shots/Github_Extension.png)

* Step 5: Inside VS Code, go to Settings --> Command Palette --> Git:Clone.

* Step 6: A box will open up and will ask you to provide the repository URL. Paste the below URL into it. The repository will get cloned into your local system.

 ``` 
 https://github.com/Mahi-ranjaN/Engage-Project-2022.git
 ```

![Cloning](/Screen_Shots/Clone.png)

* Step 7: Install the following Python Libraries from the terminal.

  1. ### dash
 
  ```
  pip install dash
  ```
  2. ### dash-labs
  ```
  pip install dash-labs
  ```
  3. ### dash_bootstrap_components
  ```
  pip install dash-bootstrap-components
  ```
  4. ### plotly
  ```
  pip install plotly
  ```
  5. ### plotly-express
  ```
  pip install plotly-express
  ```
  6. ### pandas
  ```
  pip install pandas
  ```
  7. ### dash-table
  ```
  pip install dash-table
  ```
  8. ### numpy
  ```
  pip install numpy
  ```
  9. ### dash-auth
  ```
  pip install dash-auth
  ```
  -----------------------

* Step 8: In the main content section you will see **"Main_App.py"** file. Run that file.

![Cars Specifications by company](/Screen_Shots/10.png)

* Step 9: In the output section you will see a developer link like this. click on that link (*ctrl+click*)

![Cars Specifications by company](/Screen_Shots/11.png)


## OVERVIEW OF THE PROJECT

  First of all you need to **SIGN IN** using :- 
  
   *username* (**EngageProject**)
  
   *password* (**MahiRanjan**)
  
  ![Cars Specifications by company](/Screen_Shots/7.png)
  
  
  The Project layout is divided into multiple pages named as:-
   * Audi  => (Company wise data of cars and specifications)
   * State wise Data => (State wise sales of cars per financial year)
   * Customer's Behaviour => (Car purchaser's status while purchashing the cars (i.e, marital status , educational status , age group etc.))
   * Top Values => Top sellers of each brand.
   
  ![Home page layout](/Screen_Shots/1.png)
  
 ### Let's see further pages in depth:
 
  * ### AUDI:-
  
   *This page shows the details of cars, model, and other relative data offered by the company to the customers.*
   
  __Specifications of the page__
   
   *Here, you can select the company of car and see the related data table and bar charts.*
    
   1. Data table :- 
     In the data table you can see the different information regarding the cars such as engine type, model , showroom price, engine cc, height, length, milege etc.You can also sort the data table based on your selection in the filter section of data table (please note that the data is case sensitive do please enter full name/value )
    
   2. Bar chart of Showroom price as per Engine displacement :- 
      The bar graph shows the price of cars of that particular brand you selected as per engine cc.
      You can also hover over the bar graph for getting the accurate information.

   ![Cars Specifications by company](/Screen_Shots/2.png)
   
   3. Bar chart of power/fuel capacity :- 
      This bar chart shows the fuel capacity vs power generation ratio by the engines.
     
   4. Bar chart of car length as per model of the cars:- 
      Accurate representation of the information of length of car models in millimeters scale.

   ![Cars Specifications by company](/Screen_Shots/3.png)
   
 * ### STATE WISE DATA:-
 
  *This page shows the sales of cars as per state.*
  
  __Specifications of the page__
  
  *Here, you can select the financial year from the drop down and as per the data available and you will see a map of india and a bar chart.* 
  
  1. Geographical Representation(map) :- 
     The map is showing the sales of cars in the particular financial year and when you hover over it, it will show the data of quarterly sales in all the year and the state name. You can easily download , zoom in , zoom out and select the particular section in the map.
  2. Bar chart :- it is the graphical representation of the data avalible in the map. You can easily  download , zoom in , zoom out and select the particular section in the graph.

![Cars Specifications by company](/Screen_Shots/4.png)

 * ### CUSTOMER'S BEHAVIOUR":-
  
  *This page shows you the details of the customers.*
  
   __Specifications of the page__
   
   1. Car Purchaser's Income Status :- Pie chart representing the percentage of the income(salaried/business) mode.
   2. Car Purchaser's Marital Status :- Pie chart representing the percentage of the marital status(married/single).
   3. Car Purchaser's Education Status :- Pie chart representing the percentage of the education status(graduate/postgraduate) mode.
   4. Salary vs Age Ratio Of The Customers :- Bar chart of age group vs income per age group. This bar chart could be beneficial for the companies for designing the models as per the age group who can afford the cars.
   5. Car Choice As Per Age Group :- Bar chart representing the choice of cars per age group.

![Cars Specifications by company](/Screen_Shots/5a.png)

![Cars Specifications by company](/Screen_Shots/5b.png)

 * ### TOP VALUES:-
  
  *This page basically shows you the top selleing car model of each brands with their sales in the year 2020.*
  
  __Specifications of the page__
  
  There is an alert on the top of page showing -
  You must be seeing two blank graph right now!! First, You need to select the company from the drop- down menu.
  
![Cars Specifications by company](/Screen_Shots/6a.png)
  
  When you select the brand name from the company you will see a bar chart and pie chart of the sales and top selling models like this:

![Cars Specifications by company](/Screen_Shots/6b.png)

--------------------
## THANKS A LOT FOR VIEWING MY PROJECT!!


## For more information, view this ==> [Vedio demo](https://drive.google.com/drive/folders/1W4erfKaumFvhFeCb7-EcOoq9VpdZ830t?usp=sharing).
