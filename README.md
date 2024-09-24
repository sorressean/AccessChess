# AccessChess
Accessible Chess game
## Code Architecture
The code is split into multiple core components.
  * core
  * UI
  * broker

### Core
Core contains all game logic including all game types, the sound manager, and the interfaces to the engines. With some exceptions that Idon't know where to put (sound manager, for example), core is basically decoupled and fully able to wrap around engines and games to be played however you want. For example you should presumably be able to bolt a console onto the game objects.
### UI
The UI logic includes all dialogs and game panels for specialized games. Also the component factory, which requires a bit of explaining.

#### Component Factory
The Component Factory class handles a mapping between the board type on the UI side to the game type on the core side. This allows multiple games to match a single board, or each game to have it's own board. This is important because it creates a definition of what board maps to the game objects. This is all that we care about; we don't ever pass messages between the two objects from either the core or UI layer. For that, see the Broker heading below.

### Broker
The broker object is the proxy between our Core and UI component. When either type of object needs to receive events, it will set those callbacks by calling the Broker object, which will handle setting them on their specific UI or Game object. These callbacks can receive status updates and data, and the callbacks will be represented in their abstract classes. Further, all logic such as events triggered by the game or the UI will call the Broker object, as well. While this might get confusing, I hope that this will enable the individual components to remain decoupled.
