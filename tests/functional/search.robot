*** Settings ***
Resource  ../../resources/common_resources.robot
Resource  ../../resources/pages/search_page.robot


Suite Setup  Load Environment
Test Setup  open app
Test Teardown  close app

*** Test Cases ***
TC003 Search product
    [Documentation]  product search
    [Tags]  Functional

    Search

TC008 Search non-existing product
    [Documentation]  product search
    [Tags]  Negative

    Search