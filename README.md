# tennis_career

Fetch a tennis player's career matches from tennisabstract.com and plot
the age gap between the player and their opponents over time.

## Installation

```bash
pip install git+https://github.com/joshuasundjojo/hw03-2-joshuasundjojo.git
```

## Usage

```python
from tennis_career import get_player_matches, plot_player_career

serena = get_player_matches("serena williams")
plot_player_career(serena)
```

`get_player_matches()` accepts names like `"serena williams"`,
`"Serena Williams"` or `"SerenaWilliams"` and returns a DataFrame with
columns `date`, `tournament`, `surface`, `result`, `round`, `opponent`,
`opp_age`, `age` and `age_diff`. An unknown name raises a `ValueError`.

`plot_player_career()` draws the player's age (x) against the age
difference with the opponent (y), colored by win or loss.

## Running the tests

```bash
pip install -e ".[dev]"
pytest
```

## Reflections
