# POKENO Game

This project is a Python implementation of the POKENO card game. The game involves players marking their card grids based on random card draws, and the first player to achieve a winning configuration wins.

## Features

- **Card Drawing**: Utilizes the `Carte` class to draw random cards.
- **Player Cards**: Each player is assigned a unique card grid using the `Carton` class.
- **Winning Rules**: Determines the winner based on the rules defined in the `winRules` module.

## Modules

- **`cartes`**: Contains the `Carte` class, which manages card drawing.
- **`carton`**: Contains the `Carton` class, which generates players' card grids.
- **`winRules`**: Contains the `isWinner` class, which includes methods to mark the grid and check for winning configurations.

## Usage

- **Setup**: Enter player names and initialize their card grids.
- **Gameplay**: Players take turns drawing cards and marking their grids based on the drawn cards.
- **Winning**: The game checks after each draw if any player has achieved the winning configuration.


## Contributing

Contributions are welcome! If you'd like to contribute to the project, please fork the repository, make your changes, and submit a pull request.


## Acknowledgments

- Inspired by the original POKENO card game.
- Built using Python and standard libraries.

## Installation

To run the POKENO Game locally, ensure you have Python 3.x installed. Clone the repository and navigate to the project directory:

```sh
git clone https://github.com/Ednie25/Jeu_Pokeno.git
cd pokeno-game


