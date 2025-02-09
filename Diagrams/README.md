# Diagrams

## Entity Relationship Diagram

'''
erDiagram
    ADMIN ||--o(USER : manages
    ADMIN ||--o(CARD : approves
    ADMIN {
        name
    }
    USER ||--o(DECK : owns
    USER {
        string name
        int userID
    }
    DECK ||--|(CARD : contains
    DECK {
        int cardCount
        int deckID
        string name
    }
    CARD {
        string name
        string type
        int rarity
        int attack
        int defense
    }
'''

## User Flow Diagram

'''
title: View Cards
'''
flowchart LR
    Login
    Deck viewer

'''
title: Add Card
'''
flowchart LR
    Login
    Add card dialog
    Card information entry
    Submit for approval

'''
title: Create Deck
'''
flowchart LR
    Login
    Deck builder
    Card selection
    Name deck

'''
title: Approve Card
'''
flowchart LR
    Admin login
    Card approval queue
    Card review

## Architecture Diagram

'''
architecture-beta
    group api(cloud)API

    service frontend(internet)[Frontend] in api
    service server(server)[Server] in api
    service db(database)[Database] in api

    frontend:b -- t:server
    server:l -- r:db
'''

## API Endpoints Diagram

'''
requirementDiagram

    requirement auth_req {
        id: 1
        text: User authenticated
        risk: medium
        verifymethod: inspection
    }

    requirement admin_req {
        id: 2
        text: Admin authorization granted
        risk: high
        verifymethod: inspection
    }

    requirement owner_req {
        id: 3
        text: Owner authenticated
        risk: high
        verifymethod: inspection
    }

    element fetch_cards {
        type: GET
    }

    element submit_card {
        type: PUT
    }

    element approve_card {
        type: POST
    }

    element delete_card {
        type: DELETE
    }

    element create_deck {
        type: PUT
    }

    element update_deck {
        type: POST
    }

    element delete_deck {
        type: DELETE
    }

    fetch_cards - satisfies -> auth_req
    submit_card - satisfies -> auth_req
    create_deck - satisfies -> auth_req
    approve_card - satisfies -> admin_req
    delete_card - satisfies -> admin_req
    update_deck - satisfies -> owner_req
    delete_deck - satisfies -> owner_req
'''
