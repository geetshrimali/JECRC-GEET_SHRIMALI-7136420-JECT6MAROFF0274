*** Settings ***
Resource  ../../resources/common_resources.robot
Resource  ../../resources/pages/home_pg.robot
Resource  ../../resources/pages/login_page.robot
Resource  ../../resources/pages/search_page.robot
Resource  ../../resources/pages/product_page.robot

Suite Setup  Load Environment
Test Setup  open app
Test Teardown  close app

*** Test Cases ***
TC004 Add product to cart
    [Documentation]  add to cart
    [Tags]  Functional

    account_tab
    Sleep    6
    login  ${USER_EMAIL}  ${USER_PWD}
    Sleep    1

    Search

    click_prod
    Sleep    1

    Gender
    Sleep    2
    Gender
    Sleep    2

    Size

    Cart
    Sleep    4

    Quantity
    Sleep    1
