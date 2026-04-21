*** Settings ***
Resource  ../../resources/common_resources.robot
Resource  ../../resources/pages/home_pg.robot
Resource  ../../resources/pages/login_page.robot
Resource  ../../resources/pages/logout_page.robot


Suite Setup  Load Environment
Test Setup  open app
Test Teardown  close app

*** Test Cases ***
TC001 Successful Login
    [Documentation]  Login
    [Tags]  Functional

    account_tab
    Sleep    1
    login  ${USER_EMAIL}  ${USER_PWD}
    Sleep    1


TC007 Login with invalid credentials
    [Documentation]  credentials
    [Tags]  Negative
    account_tab
    Sleep    1
    login   ${USER_EMAIL}  123
    Sleep    2
    Wait Until Element Is Visible    xpath=//div[@class='alert alert--error flex items-start gap-3 text-sm md:text-base leading-tight']
    Page Should Contain    Incorrect email or password.
    Sleep    2
