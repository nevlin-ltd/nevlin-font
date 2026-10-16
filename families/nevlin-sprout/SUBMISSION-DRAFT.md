# DRAFT — not sent

Proposed title: Nevlin Sprout — original family design and onboarding review

Hello Google Fonts team,

We would appreciate a design-eligibility and technical review of **Nevlin
Sprout**, a new upright sans-serif intended for approachable financial-learning
interfaces. The name is provisional and we welcome guidance on naming, including
whether the Nevlin brand reference is acceptable.

This is separate from the Inter-derived Nevlin Font discussed in #11128. The
Sprout family uses newly authored geometric drawing sources; no Inter, SF Pro
or other font outlines/binaries are build inputs. The development process uses
AI-assisted code. We do not present this as independently reviewed professional
type design or assume that original source geometry establishes acceptance.

The candidate has four static weights (400, 500, 600, 700), 389 encoded
characters, full GF Latin Core, tabular numerals and optional slashed zero.
Editable UFO sources and a pinned Fontmake build are included. All files are
licensed under SIL OFL 1.1 with no Reserved Font Names.

Latest Fontspector 1.9.0 results across the four TTFs:
- Universal: 291 PASS, 0 WARN, 0 FAIL/ERROR/FATAL.
- Google Fonts, network enabled: 407 PASS, 8 WARN, 0 FAIL/ERROR/FATAL.
- No check exclusions or severity overrides were used.

The remaining warnings concern `NONE` vendor identification (registration
confirmation is pending) and standard web-serving subsets that omit some
supported marks/auxiliary characters. We retain those characters and have not
claimed unrelated script support merely to satisfy the subset check. Could you
advise how the proposed Latin subset additions should be handled?

We would also welcome feedback on design distinction, spacing/optical quality,
required visual testing, final naming and the current designer-attribution/CLA
onboarding steps. Contributor agreements and independent native-language /
cross-platform review are not yet represented as complete.

Before sending this draft:
- Replace this checklist with links to the published new-family sources,
  exact candidate commit, fonts, QA report and specimen.
- Confirm the copyright-holder/designer identity and agreement status.
- Ensure the proposed name and development-stage disclosures remain accurate.

Intended source host: https://github.com/nevlin-ltd/nevlin-font
Related, different family: https://github.com/google/fonts/issues/11128

Thank you.
