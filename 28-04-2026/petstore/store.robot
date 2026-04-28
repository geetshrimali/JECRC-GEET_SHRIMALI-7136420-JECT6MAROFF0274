*** Settings ***
Library           RequestsLibrary
Library           Collections

*** Variables ***
${base_url}    https://petstore.swagger.io/v2

*** Test Cases ***
Pet inventories
    [Documentation]    Get pet inventories by status
    Create Session    petapi    ${base_url}  verify=True

    ${response}=    GET On Session    petapi    /store/inventory
    Should Be Equal As Integers    ${response.status_code}    200

    ${body}=    Set Variable    ${response.json()}

    Log To Console    ${body}
    Log To Console    ${response.status_code}

Place Order
    [Documentation]     Place an order for a pet
    Create Session    petapi    ${base_url}  verify=True

    ${payload}=    Create Dictionary    id=12345    petId=54321    quantity=1    shipDate=2024-06-01T12:00:00.000Z    status=placed    complete=true

    ${response}=    Post On Session    petapi    /store/order  json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200


    ${body}=    Set Variable    ${response.json()}
    Should Be Equal As Integers    ${body}[id]    12345
    Should Be Equal As Strings    ${body}[status]    placed

    Log To Console    ${body}
    Log To Console    ${response.status_code}


    Set Suite Variable    ${order_id}    ${body}[id]

Find Purchase by ID
    [Documentation]     Find purchase order by ID
    Create Session    petapi    ${base_url}  verify=True

    ${response}=    GET On Session    petapi    /store/order/${order_id}
    Should Be Equal As Integers    ${response.status_code}    200

    ${body}=    Set Variable    ${response.json()}
    Should Be Equal As Integers    ${body}[id]    12345
    Should Be Equal As Strings    ${body}[status]    placed

    Log To Console    ${body}
    Log To Console    ${response.status_code}

Delete Purchase by ID
    [Documentation]     Delete purchase order by ID
    Create Session    petapi    ${base_url}  verify=True
    ${response}=    DELETE On Session    petapi    /store/order/${order_id}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    order deleted

E2E
    Create Session    e2eapi    ${base_url}  verify=True
    ${payload}=    Create Dictionary    id=12345    petId=54321    quantity=1    shipDate=2024-06-01T12:00:00.000Z    status=placed    complete=true

    ${res1}=  Post On Session  e2eapi  /store/order  json=${payload}

    Should Be Equal As Integers    ${res1.status_code}    200
    ${body}=  Set Variable    ${res1.json()}
    Set Suite Variable    ${order_id}  ${body}[id]

    Log To Console    Created an order

    ${res2}=  GET On Session  e2eapi    /store/order/${order_id}

    Should Be Equal As Integers    ${res2.status_code}    200
    Log To Console    got order by ID

    ${res3}=  DELETE On Session    e2eapi    /store/order/${order_id}
    Should Be Equal As Integers    ${res3.status_code}    200
    Log To Console    Deleted
    Log To Console    e2e complete
