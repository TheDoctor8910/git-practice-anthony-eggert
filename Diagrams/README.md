# Diagrams

## Entity Relationship Diagram

```mermaid
erDiagram
    ADMIN {
        string name
    }
    USER {
        string name
        int userID
    }
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
    ADMIN ||--|{ USER : manages
    ADMIN ||--o{ CARD : approves
    USER ||--o{ DECK : owns
    DECK ||--|{ CARD : contains
```

## User Flow Diagram

View Cards
```mermaid
flowchart LR

    id1[Login] --> id2[Deck viewer]
```

Add Card
```mermaid
flowchart LR

    id1[Login] --> id2[Add card dialog] --> id3[Card information entry] --> id4[Submit for approval]
```

Create Deck
```mermaid
flowchart LR

    id1[Login] --> id2[Deck builder] --> id3[Card selection] --> id4[Name deck]
```

Approve Card
```mermaid
flowchart LR

    id1[Admin login] --> id2[Card approval queue] --> id3[Card review]
```

## Architecture Diagram

```mermaid
architecture-beta

    group api(cloud)[API]

    service frontend(internet)[Frontend] in api
    service server(server)[Server] in api
    service db(database)[Database] in api

    frontend:T --> B:server
    server:R --> L:db
```

## API Endpoints Diagram

```mermaid
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
```

## Database Schema

```mermaid
erDiagram
    USER {
        uuid id
        varchar name
        datetime2 join_date
        bit is_admin
        varchar email
        varchar password_hash
    }
    DECK {
        uuid id
        uuid userId
        varchar name
    }
    DECKCARD {
        uuid deckId
        uuid cardId
    }
    CARD {
        uuid id
        varchar name
        varchar type
        int rarity
        bit is_approved
        int attack
        int defense
    }

    USER ||--o{ DECK : has
    DECK ||--|{ DECKCARD : has
    CARD ||--o{ DECKCARD : has
```
    
