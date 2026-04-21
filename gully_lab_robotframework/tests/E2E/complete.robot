*** Settings ***
Resource  ../../resources/common_resources.robot
Resource  ../../resources/pages/home_pg.robot
Resource  ../../resources/pages/login_page.robot
Resource  ../../resources/pages/logout_page.robot
Resource  ../../resources/pages/search_page.robot
Resource  ../../resources/pages/product_page.robot
Resource    ../../resources/pages/cart_page.robot

Suite Setup  Load Environment
Test Setup  open app
Test Teardown  close app

*** Test Cases ***
TC006 Complete user journey (Login to Logout)
    [Documentation]  end to end
    [Tags]  Functional

    account_tab
    Sleep    2
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

    Close_cart

    verify_cart
    Sleep    1

    Close_cart
    Sleep    1

    logout