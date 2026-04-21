*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://www.amazon.in/

*** Test Cases ***
Handling alerts(simple)
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2

    Click Element    xpath=//a[contains(text(),'Electronics')]
    Sleep    3

    Scroll Element Into View    xpath=//span[text()='boAt']
    Click Element    xpath=(//span[text()='boAt'])[2]
    Sleep    3

    ${product_name}=    Get Text    xpath=(//a[@class = 'a-link-normal s-line-clamp-4 s-link-style a-text-normal'])[8]

    Click Element    xpath=(//div[@class = 'a-section a-spacing-base desktop-grid-content-view'])[8]

    Switch Window    NEW
    Sleep    3

    ${new_title}=    Get Text    xpath=//span[@id='productTitle']
    Should Contain    ${new_title}    ${product_name}
    Sleep    2
    ${actual_price}=    Get Text    xpath=(//span[@class="a-price a-text-price apex-basisprice-value"]/span)[2]
    ${discount_price}=    Get Text    xpath=//span[@class='a-price-whole']
    ${discount_percent}=    Get Text    xpath=//span[@class="apex-savings-container"]/span

    Log To Console    Actual Price: ${actual_price}
    Log To Console    Discounted Price: ${discount_price}
    Log To Console    Discount: ${discount_percent}

    Sleep    5
    Scroll Element Into View    id=add-to-cart-button
    Click Button    id=add-to-cart-button
    Sleep    3s
    Sleep    3

    Click Element    xpath=//span[@id='nav-cart-count']
    Sleep    3

    ${cart_product}=    Get Text    xpath=//span[@class='a-truncate-cut']
    Should Contain    ${cart_product}    ${product_name}

    Close Browser