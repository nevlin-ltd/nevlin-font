# Technical audit — 22 October 2026

Proposed name: Nevlin Font. Binary name: Study A pending naming clearance.
This is the separately drawn Sprout revision, not the historical Inter-derived family.
Submission: https://github.com/google/fonts/issues/11158

## Repository and reproducibility

Run `PYTHON=/path/to/venv/bin/python bash sources/build.sh` from the package root.
The script also works from another working directory. Python drawings are authoritative;
UFOs are regenerated, then compiled with fontmake. `make qa` retains the historical
FontBakery checks. `make qa-fontspector FONTSPECTOR=/path/to/fontspector` runs the newer
Google-recommended checker without suppressing checks.

## Warnings requiring external decisions

- Vendor ID: retain NONE until the requested NVLN registration is confirmed. Do not
  impersonate another vendor or assume that a request equals registration.
- Serving subsets: the full fonts contain Latin accents that the service's subset
  definitions do not serve. Retain the accents and correct Latin coverage. Do not
  declare unrelated scripts or remove necessary marks just to silence this warning.
  Google needs to confirm serving coverage during onboarding.
- The older FontBakery report additionally flags designer-profile onboarding. A
  Google catalog profile must be arranged with the onboarding team; no profile is
  invented in this repository.

## Design and platform review

HarfBuzz-shaped Regular specimens were visually inspected, including accents,
localized forms, numeral pairs and text at 12, 14, 16 and 20 px. This is a rendered
outline proof, not a browser or OS rasterization test. At small sizes Regular is
light; I/l/1, O/0 and rn/m still deserve independent readability assessment.
No new outline defect was established by this inspection, so no speculative
letterform changes were made. Independent expert review is still pending.
Browser automation previously rejected the local-file preview. No alternate route
was used to bypass that restriction; actual browser/OS testing remains unverified.

## Governance left to the user

Copyright-owner/author listing, CLA, final naming clearance and a committed maintainer
cannot be filled in from technical evidence. AUTHORS.txt must not be fabricated.
A complete Google upstream-compliance claim therefore remains unchecked.

## Verified current checker result

Fontspector 1.9.0, Google Fonts profile, network enabled: 415 PASS, 8 WARN,
236 SKIP, 30 INFO, zero FAIL/ERROR/FATAL. The eight warnings are four vendor
ID and four serving-subset findings. This is not a claim that the older
FontBakery warnings were fixed; both reports remain visible.
The new build entry point was executed from /tmp and reproduced the tracked
binaries without changes. Latin Core and shaping checks passed again.
