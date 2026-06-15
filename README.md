## Rebalancing App

### 📂 Project Structure

* ├── Manual_Test_Cases.pdf         # Manual Test Suite
* ├── RebalancingApp.py          # calculation logic
* ├── test_RebalancingAppTest.py # Automated PyTest test cases
* ├── README.md             # Documentation
* └── conftest.py          # A dummy login step

### Contents

I have included the manual test case pdf in the project.
This project contains the rebalancing app function that calculates the shares and maintains the portfolio value to zero variance.
There is an automated test case for the function that uses pytest to test the functionality.
The assumptions are included in this file for reference used in this project.

### Assumptions

* Total portfolio value is always provided and valid

* Percentages are based on total portfolio value

* Shares can be fractional

* Prices are always positive

* Rounding to 2 decimals is acceptable

* No transaction fees or taxes

* Only one buy and one sell required to rebalance

### Run the test suite

To run and validate the test cases are passing ,you need to have PyCharm and python installed  
Run command :-pytest  
OR  
Run from the Pycharm Menu Bar - Run - Run 'test_RebalancingAppTest.py'