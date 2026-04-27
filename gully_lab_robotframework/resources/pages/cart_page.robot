*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/home_pg_loc.robot
Resource  ../../locators/cart_pg_loc.robot
Resource  ../../locators/prod_page_loc.robot

*** Keywords ***
Verify_cart
    Click Element    ${cart}
    Sleep    2
    Wait Until Page Contains  ${name}
    Sleep    1

Open_cart
    Click Element    ${cart}
    Wait Until Page Contains    ${name}
    Sleep    2

Close_cart
    Click Element    ${close_cart}