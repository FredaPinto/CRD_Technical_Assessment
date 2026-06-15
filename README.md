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

### Sample_Output

`C:\Users\freda\AppData\Local\Python\bin\python.exe "C:/Program Files/JetBrains/PyCharm 2026.1.2/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py" --path C:\Users\freda\PycharmProjects\CRD_Technical_Assessment\test_RebalancinAppTest.py 
Testing started at 21:25 ...
Launching pytest with arguments C:\Users\freda\PycharmProjects\CRD_Technical_Assessment\test_RebalancinAppTest.py --no-header --no-summary -q in C:\Users\freda\PycharmProjects\CRD_Technical_Assessment

============================= test session starts =============================
collecting ... collected 8 items

test_RebalancinAppTest.py::test_login I have logged in as user abc
PASSED                             [ 12%]Rebalancing App Test

test_RebalancinAppTest.py::test_ibm_buy PASSED                           [ 25%]
test_RebalancinAppTest.py::test_orcl_sell PASSED                         [ 37%]
test_RebalancinAppTest.py::test_hold_positions PASSED                    [ 50%]
test_RebalancinAppTest.py::test_total_buy_equals_total_sell PASSED       [ 62%]
test_RebalancinAppTest.py::test_negative_variance_means_buy PASSED       [ 75%]
test_RebalancinAppTest.py::test_positive_variance_means_sell PASSED      [ 87%]
test_RebalancinAppTest.py::test_invalid_input PASSED                     [100%]

============================== 8 passed in 0.02s ==============================

Process finished with exit code 0`
