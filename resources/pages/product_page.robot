*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/prod_page_loc.robot
Resource  ../../locators/home_pg_loc.robot

*** Keywords ***
click_prod
    Wait Until Element Is Visible    ${product}
    Click Element    ${product}

Size
    Wait Until Element Is Visible    ${size_bar}
    Select From List By Value    ${size_bar}  UK9

Gender
    Wait Until Element Is Visible    ${gender}
    Click Element    ${gender}

Quantity
    Wait Until Element Is Visible    ${quantity}
    Clear Element Text    ${quantity}
    Input Text    ${quantity}    2
    Press Keys    ${quantity}    ENTER

Cart
    Scroll Element Into View    xpath=//p[text()='Pairs well with']
    Wait Until Element Is Visible    ${add_to_cart}
    Sleep    5
    Click Element    ${add_to_cart}
    Sleep    2
    Wait Until Element Is Visible    ${quantity}
    
 