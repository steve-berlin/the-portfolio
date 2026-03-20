# Portfolio

Personal portfolio site for Steve. Terminal/hacker aesthetic, dark theme, monospace font.

## Stack

- `index.html` — Single-page static site. All CSS is inline (no build step, no external deps).
- `index.py` — Python 3 stdlib HTTP server (port 80). Displays public IP on startup via ipify API.

## Architecture

Zero dependencies. No JS frameworks, no CSS preprocessors, no package manager. The site is one HTML file served by one Python file.

## Design system

CSS vars in `:root` — dark background (`#0a0a0a`), green accent (`#4af626`). Terminal motifs: `$` prompts, `>` prefixes, `[tag]` brackets, blinking cursor. Responsive at 600px and 480px breakpoints.

## Running

```
sudo python3 index.py
```

Requires root (port 80). Prints public IP then serves CWD.

## Status

Early stage — projects section and contact links are placeholder ("coming soon").
