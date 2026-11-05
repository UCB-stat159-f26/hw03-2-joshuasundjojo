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
## Reflections

I learned how to turn the work from HW1 and HW2 into a reusable Python
package. This was very helpful in showing me the difference between code
that works once in a notebook and code that someone else can install and
run. In HW2 we were given Serena's birthday, but a package has to work for
any player from just a name, so I had to figure out where that data lives
and fetch it myself. Splitting the work into small private helpers
(parsing, cleaning, fetching) made each piece easy to test, and the two
public functions stayed short and readable.

The most useful lesson was testing against mockup files instead of the
live site. My tests passed on the fixtures, but my first live run failed
because the real file was laid out differently from the sample. That
showed me both why tests matter and what they can't catch, so I still
checked the real output by hand. Using small, descriptive commits also
helped: when I forgot to ignore cache files, it was easy to see what to
fix.

Next time I would plan the data sources first, since I only discovered
where the player's birthday lived halfway through. I would also add
tests that simulate website errors, such as an unknown player name,
without contacting the server.