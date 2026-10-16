# Draft — Google Fonts eligibility and onboarding review

Not submitted. Proposed issue title: **Nevlin Font — Inter-derived family eligibility and onboarding review**

Repository: https://github.com/nevlin-ltd/nevlin-font
Website: https://nevlin.com
Contact: zhanat.salimova@nevlin.com
License: SIL Open Font License 1.1 (upstream notices preserved)

We would like an initial eligibility review for Nevlin Font. It is substantially derived from Inter 4.001, with selected letterform changes (a, e, g, r, t, 1, 4, 7, dots, Q tail and tenge bars), adjusted weight and font-engineering repairs. Most inherited letterforms, spacing and layout functionality remain attributable to the Inter Project Authors. We do not claim an independently drawn family. Please advise whether this degree of differentiation qualifies for the collection before we proceed further with onboarding. Please also review the proposed family name for compliance with naming requirements.

The core candidate has four upright weights (400/500/600/700), 374 encoded characters, editable Glyphs/UFO sources, pinned Fontmake dependencies, build scripts and TTF binaries. The earlier broad-language beta remains separately preserved under the OFL. No Apple font software is included.

Validation with the full Google Fonts profile and network access:
- Fontspector 1.9.0: 417 PASS, 0 FAIL, 0 ERROR, 8 WARN.
- FontBakery 1.1.0: 613 PASS, 0 FAIL, 0 ERROR, 12 WARN.
- No checks or severities were overridden.
- Tight-join outline warnings are repaired; coverage, dot-removal, tabular digits and unchanged advance widths pass.

Remaining warnings need external review:
1. Vendor registration: requested NVLN from Microsoft on 16 October 2026; confirmation pending. Fonts still use NONE and do not claim a registered ID.
2. Designer catalog: credit is Nevlin, Rasmus Andersson. The older FontBakery cannot resolve profiles for either name; current Fontspector does not report this warning. Please advise on the current catalog process. Suggested Nevlin biography: Nevlin maintains an open-source interface typeface derived from Inter, contributing selected letterform redraws and font engineering.
3. Serving subsets: the candidate includes GF Latin Core combining marks and financial symbols that the checker says are outside latin/latin-ext/menu serving definitions. We preserved required coverage and did not declare unsupported scripts. Please review the subset coverage during onboarding.

Reports: https://github.com/nevlin-ltd/nevlin-font/blob/main/CORE-VALIDATION.md
Full source package: https://github.com/nevlin-ltd/nevlin-font/blob/main/NevlinFont-core-latin-candidate.zip

No Google acceptance, exception or completed copyright-holder CLA is claimed. Any required agreement would be completed by an authorized human signatory. We welcome guidance on design eligibility and outstanding onboarding requirements.
