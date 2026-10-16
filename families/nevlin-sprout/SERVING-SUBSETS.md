# Google Fonts serving-subset review

These 18 encoded characters trigger the serving-range warning in all four weights.
They remain in the font. Current metadata declares only Latin, Latin-ext and menu.

- U+02D8 — BREVE
- U+02D9 — DOT ABOVE
- U+02DB — OGONEK
- U+0302 — COMBINING CIRCUMFLEX ACCENT
- U+0306 — COMBINING BREVE
- U+0307 — COMBINING DOT ABOVE
- U+030A — COMBINING RING ABOVE
- U+030B — COMBINING DOUBLE ACUTE ACCENT
- U+030C — COMBINING CARON
- U+0326 — COMBINING COMMA BELOW
- U+0327 — COMBINING CEDILLA
- U+1EBC — LATIN CAPITAL LETTER E WITH TILDE
- U+1EBD — LATIN SMALL LETTER E WITH TILDE
- U+2190 — LEFTWARDS ARROW
- U+2192 — RIGHTWARDS ARROW
- U+2264 — LESS-THAN OR EQUAL TO
- U+2265 — GREATER-THAN OR EQUAL TO
- U+25CC — DOTTED CIRCLE

Proposed reviewer action: include the required Latin combining/spacing marks and
auxiliary Latin letters in the appropriate Latin serving range, and advise whether
the arrows/math/dotted-circle symbols need a separate symbols range. This is a
proposal, not an applied Google configuration change. Do not advertise unrelated
scripts or remove required marks just to clear this check.
