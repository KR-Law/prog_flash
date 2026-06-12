# High-Level Architecture and Structure

Prog-Flash is a command-line flashcard application built with Python, designed for efficient spaced repetition and knowledge review directly in the terminal. The architecture separates core data logic from the user interface (CLI).

**Core Components:**
*   **Data Layer:** Manages the creation, loading, and saving of structured card decks (flashcards) typically persisted as JSON files. This layer handles the serialization/deserialization of content for subjects and individual cards.
*   **State Management (`StudySessionController`):** This component is responsible for managing the current state of a learning session—tracking which deck is active, the progression through cards, and controlling the flow (e.g., deciding if the user should see the front or back).
*   **Presentation Layer (`Card`):** Encapsulates the view logic for a single flashcard, handling how the question and answer are displayed to the CLI user.
*   **Application Entry Point:** The main executable point that initializes dependencies and routes commands (e.g., `prog-flash review`, `prog-flash create`).

## Class Diagram

```mermaid
---
title: Flashcard Application Class Diagram (Optimized)
---
classDiagram
    class App {
      +list~Deck~ decks
      +Deck current_deck
      +int session_correct_count
      +_load_from_json(file_path: str) None
      +_serialize_to_json(file_path: str) None
      +review_deck() None
      +_select_deck() Deck
      +manage_deck() None
      +list_decks() None
    }

    class Deck {
        +str title
        +list~Card~ cards
        +int num_cards
        +get_review_queue() list~Card~
        +reset_deck() None
        +add_card(card: Card) None
        +remove_card(card: Card) None
        -_count_deck() int
    }

    class Card {
        +str front
        +str back
        +int number_correct
        +mark_correct() None
        +mark_incorrect() None
    }

    App *-- Deck : contains
    Deck *-- Card : contains
```

## App Startup

```mermaid
flowchart TD
    %% 1. LOAD PHASE
    Start([Launch CLI App]) --> ReadJSON[Read Raw JSON File]
    ReadJSON --> ParseDict[Parse JSON into Dictionary]
    subgraph Load Phase
        ReadJSON
        ParseDict
    end

    %% 2. HYDRATE PHASE
    ParseDict --> HydrateClasses[Pass Dict Data to Class Constructors\ne.g., Card**card_data]
    HydrateClasses --> PopState[Populate Active App State Memory]
    subgraph Hydrate Phase
        HydrateClasses
        PopState
    end

    %% 3. PROCESS PHASE
    PopState --> MainMenu{Main Menu\nChoose an Option}

    subgraph Process Phase
        MainMenu
        LinkReview[Launch Review Subsystem\n*Separate Flow*]
        LinkManage[Launch Manage Subsystem\n*Separate Flow*]
        LinkList[Launch List Subsystem\n*Separate Flow*]
    end

    MainMenu -- "1. Review" --> LinkReview --> MainMenu
    MainMenu -- "2. Manage Deck" --> LinkManage --> MainMenu
    MainMenu -- "3. List" --> LinkList --> MainMenu

    %% 4. SERIALIZE PHASE
    MainMenu -- "4. Exit App" --> ClassesToDict[Convert Live Objects back to Dict]
    ClassesToDict --> WriteJSON[Write JSON String to File]
    WriteJSON --> End([Terminate CLI App])

    subgraph Serialize Phase
        ClassesToDict
        WriteJSON
    end
```

## Review Flow

```mermaid
flowchart TD
    %% Setup Phase
    Start([Start Session]) --> ShowDecks[Display List of Decks]
    ShowDecks --> SelectDeck[User Selects a Deck]

    %% Main Review & Filtering Entry
    FilterCards[Filter Cards Needing Review] --> CheckQueue{Are there cards\nin the queue?}
    SelectDeck --> FilterCards

    %% Empty Queue Branch (Your New Requirement)
    CheckQueue -- No --> ShowCount[Show Total Card Count for Deck]
    ShowCount --> AskReset{Do you want to\nreset the deck?}

    AskReset -- Yes --> ResetDeck[Reset Card Review States]
    ResetDeck --> FilterCards
    AskReset -- No --> EndSession([Show Summary & Exit\nDisplay Correct Count])

    %% Active Card Loop
    CheckQueue -- Yes --> FetchCard[Fetch Next Card]
    FetchCard --> ShowFront[Display Card Front]
    ShowFront --> WaitReveal[User Clicks 'Reveal Answer']

    WaitReveal --> ShowBack[Display Card Back]
    ShowBack --> ChooseGrade{User Chooses Grade}

    %% Grading Actions
    ChooseGrade -- Correct --> IncCorrect[Add to Correct Count]
    ChooseGrade -- Incorrect --> Requeue[Add Card Back to\nCurrent Session Queue]
    ChooseGrade -- Re-review --> Requeue

    %% Routing back to check the queue
    IncCorrect --> CheckQueue
    Requeue --> CheckQueue
```

## Manage Deck Flow

```mermaid
flowchart TD
    %% Entry from Main Menu
    Start([Launch Manage Subsystem]) --> DisplayDecks[Display List of Decks]
    DisplayDecks --> ManageMenu{Choose an Option}

    %% Option 1: Add a Deck
    ManageMenu -- "1. Add a New Deck" --> PromptDeckName[Prompt for New Deck Title]
    PromptDeckName --> CreateDeckObj[Instantiate New Deck Class]
    CreateDeckObj --> AppendApp[Append New Deck to App.decks List]
    AppendApp --> SaveJSON1[Save Changes to JSON] --> LoopOrExit

    %% Option 2: Manage Existing Deck
    ManageMenu -- "2. Manage Existing Deck" --> SelectDeck[User Selects Deck to Modify]
    SelectDeck --> SetCurrent[Set App.current_deck]

    SetCurrent --> DeckActionsMenu{Deck Actions Menu\nWhat do you want to do?}

    %% Card Sub-operations (Add & Remove)
    DeckActionsMenu -- "A. Add Card" --> PromptCard[Prompt for Card Front & Back]
    PromptCard --> CreateCardObj[Instantiate New Card Class]
    CreateCardObj --> CallAddCard[Call current_deck.add_card]
    CallAddCard --> SaveJSON2[Save Changes to JSON] --> DeckActionsMenu

    DeckActionsMenu -- "B. Remove Card" --> DisplayCardsR[Display List of Cards]
    DisplayCardsR --> SelectCardR[User Selects Card to Remove]
    SelectCardR --> CallRemoveCard[Call current_deck.remove_card]
    CallRemoveCard --> SaveJSON2

    %% UPDATED: Sequential Card Update Operation
    DeckActionsMenu -- "C. Update Card" --> DisplayCardsU[Display List of Cards]
    DisplayCardsU --> SelectCardU[User Selects Card to Update]

    SelectCardU --> EditFront[Prompt New Front Text\nLeave blank to keep current]
    EditFront --> ApplyFront[Update card.front if changed]

    ApplyFront --> EditBack[Prompt New Back Text\nLeave blank to keep current]
    EditBack --> ApplyBack[Update card.back if changed]

    ApplyBack --> SaveJSON2

    %% Delete Deck Operation
    DeckActionsMenu -- "D. Delete This Deck" --> ConfirmDelete{Are you sure?}
    ConfirmDelete -- Yes --> RemoveDeck[Remove Deck from App.decks List]
    RemoveDeck --> SaveJSON1
    ConfirmDelete -- No --> DeckActionsMenu

    %% Back/Exit Triggers
    DeckActionsMenu -- "E. Back to Manage Menu" --> DisplayDecks
    ManageMenu -- "3. Back to Main Menu" --> ReturnMain([Return Control to Main Menu])

    %% Post-Save Logic
    LoopOrExit{Do you want to\ncontinue managing?}
    LoopOrExit -- Yes --> DisplayDecks
    LoopOrExit -- No --> ReturnMain
```

## List Flow

```mermaid
flowchart TD
    %% Entry from Main Menu
    Start([Launch List Subsystem]) --> PrintDecks[Print All Decks, Descriptions & Card Counts]

    %% Post-List Action Router
    PrintDecks --> ListMenu{What would you like\nto do next?}

    %% Route 1: Go straight to Review
    ListMenu -- "1. Review a Deck" --> SelectReview[Select Deck to Review]
    SelectReview --> SetCurrentReview[Set App.current_deck]
    SetCurrentReview --> LinkReview[Launch Review Subsystem\n*Separate Flow*]
    LinkReview --> ReturnPoint[Return to List Menu] --> PrintDecks

    %% Route 2: Go straight to Manage
    ListMenu -- "2. Manage a Deck" --> SelectManage[Select Deck to Manage]
    SelectManage --> SetCurrentManage[Set App.current_deck]
    SetCurrentManage --> LinkManage[Launch Manage Subsystem\n*Separate Flow*]
    LinkManage --> ReturnPoint

    %% Route 3: Go back
    ListMenu -- "3. Back to Main Menu" --> ReturnMain([Return Control to Main Menu])
```
