*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/home_pg_loc.robot
Resource  ../../locators/cart_pg_loc.robot

*** Keywords ***
Verify_cart
    Click Element    ${cart}
    Sleep    2
    Wait Until Page Contains    GULLY NUMBER 001 - Baaz Laakh Red
    Sleep    1

Open_cart
    Click Element    ${cart}
    Sleep    2

Close_cart
    Click Element    ${close_cart}