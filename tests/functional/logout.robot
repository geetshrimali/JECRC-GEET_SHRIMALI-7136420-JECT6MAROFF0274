*** Settings ***
Resource  ../../resources/common_resources.robot
Resource  ../../resources/pages/home_pg.robot
Resource  ../../resources/pages/login_page.robot
Resource  ../../resources/pages/logout_page.robot


Suite Setup  Load Environment
Test Setup  open app
Test Teardown  close app

*** Test Cases ***
TC002 Logout functionality
    [Documentation]  Logout
    [Tags]  Functional

    account_tab
    Sleep    1
    login  ${USER_EMAIL}  ${USER_PWD}
    Sleep    1

    logout