## FontBakery report

fontbakery version: 1.1.0







## Check results



<details><summary>[1] Family checks</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Fonts have consistent underline thickness? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-family-underline-thickness">opentype/family/underline_thickness</a></summary>
    <div>


> 
> Dave C Lemon (Adobe Type Team) recommends setting the underline thickness to be
> consistent across the family.
> 
> If thicknesses are not family consistent, words set on the same line which have
> different styles look strange.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>Thickness of the underline is not the same across this family. In order to fix this, please make sure that the underlineThickness value is the same in the 'post' table of all of this family font files.
Detected underlineThickness values are:
output/nevlin-google-fonts/repository/NevlinUIPlus-Bold.ttf: 210
output/nevlin-google-fonts/repository/NevlinUIPlus-Medium.ttf: 168
output/nevlin-google-fonts/repository/NevlinUIPlus-Regular.ttf: 147
output/nevlin-google-fonts/repository/NevlinUIPlus-Semibold.ttf: 188</p>
 [code: inconsistent-underline-thickness]



</div>
</details>
</div>
</details>

<details><summary>[12] NevlinUIPlus-Bold.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 fsSelection value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-fsselection">opentype/fsselection</a></summary>
    <div>


> 
> The OS/2.fsSelection field is a bit field used to specify the stylistic
> qualities of the font - in particular, it specifies to some operating
> systems whether the font is italic (bit 0), bold (bit 5) or regular
> (bit 6).
> 
> This check verifies that the fsSelection field is set correctly for the
> font style. For a family of static fonts created in GlyphsApp, this is
> set by using the style linking checkboxes in the exports settings.
> 
> Additionally, the bold and italic bits in OS/2.fsSelection must match the
> bold and italic bits in head.macStyle per the OpenType spec.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829
> See also: https://github.com/fonttools/fontbakery/pull/2382





* 🔥 **FAIL** <p>fsSelection Bold flag False does not match font style Bold</p>
 [code: bad-BOLD]



* 🔥 **FAIL** <p>fsSelection Regular flag True does not match font style Bold</p>
 [code: bad-REGULAR]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking head.macStyle value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-mac-style">opentype/mac_style</a></summary>
    <div>


> 
> The values of the flags on the macStyle entry on the 'head' OpenType table
> that describe whether a font is bold and/or italic must be coherent with the
> actual style of the font as inferred by its filename.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>head macStyle BOLD bit should be set.</p>
 [code: bad-BOLD]





</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check base characters have non-zero advance width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#base-has-width">base_has_width</a></summary>
    <div>


> 
> Base characters should have non-zero advance width.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4906





* 🔥 **FAIL** <p>The following glyphs had zero advance width:
- uni0488 (U+0488)</p>
<pre><code>- uni0489 (U+0489)
</code></pre>
 [code: zero-width-bases]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>


> 
> Ensure that no glyph lacks its corresponding upper or lower counterpart
> (but only when unicode supports case-mapping).
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/3230





* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+01C6: LATIN SMALL LETTER DZ WITH CARON</td>
<td align="left">U+01C4: LATIN CAPITAL LETTER DZ WITH CARON</td>
</tr>
<tr>
<td align="left">U+023A: LATIN CAPITAL LETTER A WITH STROKE</td>
<td align="left">U+2C65: LATIN SMALL LETTER A WITH STROKE</td>
</tr>
<tr>
<td align="left">U+023E: LATIN CAPITAL LETTER T WITH DIAGONAL STROKE</td>
<td align="left">U+2C66: LATIN SMALL LETTER T WITH DIAGONAL STROKE</td>
</tr>
<tr>
<td align="left">U+0265: LATIN SMALL LETTER TURNED H</td>
<td align="left">U+A78D: LATIN CAPITAL LETTER TURNED H</td>
</tr>
<tr>
<td align="left">U+0266: LATIN SMALL LETTER H WITH HOOK</td>
<td align="left">U+A7AA: LATIN CAPITAL LETTER H WITH HOOK</td>
</tr>
<tr>
<td align="left">U+026A: LATIN LETTER SMALL CAPITAL I</td>
<td align="left">U+A7AE: LATIN CAPITAL LETTER SMALL CAPITAL I</td>
</tr>
<tr>
<td align="left">U+026C: LATIN SMALL LETTER L WITH BELT</td>
<td align="left">U+A7AD: LATIN CAPITAL LETTER L WITH BELT</td>
</tr>
<tr>
<td align="left">U+029D: LATIN SMALL LETTER J WITH CROSSED-TAIL</td>
<td align="left">U+A7B2: LATIN CAPITAL LETTER J WITH CROSSED-TAIL</td>
</tr>
<tr>
<td align="left">U+0376: GREEK CAPITAL LETTER PAMPHYLIAN DIGAMMA</td>
<td align="left">U+0377: GREEK SMALL LETTER PAMPHYLIAN DIGAMMA</td>
</tr>
<tr>
<td align="left">U+03FA: GREEK CAPITAL LETTER SAN</td>
<td align="left">U+03FB: GREEK SMALL LETTER SAN</td>
</tr>
<tr>
<td align="left">U+052F: CYRILLIC SMALL LETTER EL WITH DESCENDER</td>
<td align="left">U+052E: CYRILLIC CAPITAL LETTER EL WITH DESCENDER</td>
</tr>
<tr>
<td align="left">U+2132: TURNED CAPITAL F</td>
<td align="left">U+214E: TURNED SMALL F</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#family-win-ascent-and-descent">family/win_ascent_and_descent</a></summary>
    <div>


> 
> A font's winAscent and winDescent values should be greater than or equal to
> the head table's yMax, abs(yMin) values. If they are less than these values,
> clipping can occur on Windows platforms
> (https://github.com/RedHatBrand/Overpass/issues/33).
> 
> If the font includes tall/deep writing systems such as Arabic or Devanagari,
> the winAscent and winDescent can be greater than the yMax and absolute yMin
> values to accommodate vowel marks.
> 
> When the 'win' Metrics are significantly greater than the UPM, the linespacing
> can appear too loose. To counteract this, enabling the OS/2 fsSelection
> bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values
> instead. This means the font developer can control the linespacing with
> the 'typo' values, whilst avoiding clipping by setting the 'win' values to
> values greater than the yMax and absolute yMin.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 2297, but got 1984 instead</p>
 [code: ascent]



* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 689, but got 494 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure font doesn't have Mac name table entries (platform=1). <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#no-mac-entries">no_mac_entries</a></summary>
    <div>


> 
> Mac name table entries are not needed anymore. Even Apple stopped producing
> name tables with platform 1. Please see for example the following system font:
> 
> /System/Library/Fonts/SFCompact.ttf
> 
> Also, Dave Opstad, who developed Apple's TrueType specifications, told
> Olli Meier a couple years ago (as of January/2022) that these entries are
> outdated and should not be produced anymore.
> 




> Original proposal: https://github.com/googlefonts/gftools/issues/469





* 🔥 **FAIL** <p>Please remove name ID 1</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 2</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 3</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 4</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 5</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 6</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 10</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 16</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 17</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 18</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 25</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 257</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 298</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 301</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 302</p>
 [code: mac-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure smart dropout control is enabled in "prep" table instructions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#smart-dropout">smart_dropout</a></summary>
    <div>


> 
> This setup is meant to ensure consistent rendering quality for fonts across
> all devices (with different rendering/hinting capabilities).
> 
> Below is the snippet of instructions we expect to see in the fonts:
> B8 01 FF    PUSHW 0x01FF
> 85          SCANCTRL (unconditinally turn on
> dropout control mode)
> B0 04       PUSHB 0x04
> 8D          SCANTYPE (enable smart dropout control)
> 
> "Smart dropout control" means activating rules 1, 2 and 5:
> Rule 1: If a pixel's center falls within the glyph outline,
> that pixel is turned on.
> Rule 2: If a contour falls exactly on a pixel's center,
> that pixel is turned on.
> Rule 5: If a scan line between two adjacent pixel centers
> (either vertical or horizontal) is intersected
> by both an on-Transition contour and an off-Transition
> contour and neither of the pixels was already turned on
> by rules 1 and 2, turn on the pixel which is closer to
> the midpoint between the on-Transition contour and
> off-Transition contour. This is "Smart" dropout control.
> 
> For more detailed info (such as other rules not enabled in this snippet),
> please refer to the TrueType Instruction Set documentation.
> 
> Generally this occurs with unhinted fonts; if you are not using autohinting,
> use gftools-fix-nonhinting (or just gftools-fix-font) to fix this issue.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>The 'prep' table does not contain TrueType instructions enabling smart dropout control. To fix, export the font with autohinting enabled, or run ttfautohint on the font, or run the <code>gftools fix-nonhinting</code> script.</p>
 [code: lacks-smart-dropout]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-mark-chars">opentype/gdef_mark_chars</a></summary>
    <div>


> 
> Mark characters should be in the GDEF mark glyph class.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2877





* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
uni0488 (U+0488), uni0489 (U+0489), uni20DD (U+20DD) and uni20DE (U+20DE)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check glyphs in mark glyph class are non-spacing. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-spacing-marks">opentype/gdef_spacing_marks</a></summary>
    <div>


> 
> Glyphs in the GDEF mark glyph class should be non-spacing.
> 
> Spacing glyphs in the GDEF mark glyph class may have incorrect anchor
> positioning that was only intended for building composite glyphs during design.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2877





* ⚠️ **WARN** <p>The following glyphs seem to be spacing (because they have width &gt; 0 on the hmtx table) so they may be in the GDEF mark glyph class by mistake, or they should have zero width instead:
dotbelow (U+0323)</p>
 [code: spacing-mark-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: numbersign	Contours detected: 4	Expected: 2

- Glyph name: dollar	Contours detected: 2	Expected: 1, 3 or 5

- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: K	Contours detected: 3	Expected: 1 or 2

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: asciicircum	Contours detected: 2	Expected: 1

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: k	Contours detected: 3	Expected: 1 or 2

- Glyph name: braceleft	Contours detected: 3	Expected: 1

- Glyph name: braceright	Contours detected: 3	Expected: 1

- 596 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* Q_rthook (U+024A): L&lt;&lt;1128.0,0.0&gt;--&lt;1441.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* feng.1 (U+EE11): L&lt;&lt;1644.0,0.0&gt;--&lt;1331.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* feng (U+02A9): L&lt;&lt;1746.0,0.0&gt;--&lt;1433.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0452 (U+0452): L&lt;&lt;1120.0,0.0&gt;--&lt;807.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0267 (U+0267): L&lt;&lt;1120.0,0.0&gt;--&lt;807.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* lrthook (U+026D): L&lt;&lt;419.0,0.0&gt;--&lt;106.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0271 (U+0271): L&lt;&lt;1729.0,0.0&gt;--&lt;1416.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* nrthook (U+0273): L&lt;&lt;1120.0,0.0&gt;--&lt;807.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* eng (U+014B): L&lt;&lt;1120.0,0.0&gt;--&lt;807.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* nlfthook (U+0272): L&lt;&lt;419.0,0.0&gt;--&lt;106.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* 10 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>


> 
> Glyphs are either accessible directly through Unicode codepoints or through
> substitution rules.
> 
> In Color Fonts, glyphs are also referenced by the COLR table. And mathematical
> fonts also reference glyphs via the MATH table.
> 
> Any glyphs not accessible by these means are redundant and serve only
> to increase the font's file size.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3160





* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- _part.t_base

- _part.tcurl_base

- koronisaccentleft.cn

- macrondieresiscomb.cn

- tildemacroncomb.cn

- uni1DC4.cn

- uni1DC6.cn
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>
</div>
</details>

<details><summary>[10] NevlinUIPlus-Medium.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Check base characters have non-zero advance width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#base-has-width">base_has_width</a></summary>
    <div>


> 
> Base characters should have non-zero advance width.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4906





* 🔥 **FAIL** <p>The following glyphs had zero advance width:
- uni0488 (U+0488)</p>
<pre><code>- uni0489 (U+0489)
</code></pre>
 [code: zero-width-bases]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>


> 
> Ensure that no glyph lacks its corresponding upper or lower counterpart
> (but only when unicode supports case-mapping).
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/3230





* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+01C6: LATIN SMALL LETTER DZ WITH CARON</td>
<td align="left">U+01C4: LATIN CAPITAL LETTER DZ WITH CARON</td>
</tr>
<tr>
<td align="left">U+023A: LATIN CAPITAL LETTER A WITH STROKE</td>
<td align="left">U+2C65: LATIN SMALL LETTER A WITH STROKE</td>
</tr>
<tr>
<td align="left">U+023E: LATIN CAPITAL LETTER T WITH DIAGONAL STROKE</td>
<td align="left">U+2C66: LATIN SMALL LETTER T WITH DIAGONAL STROKE</td>
</tr>
<tr>
<td align="left">U+0265: LATIN SMALL LETTER TURNED H</td>
<td align="left">U+A78D: LATIN CAPITAL LETTER TURNED H</td>
</tr>
<tr>
<td align="left">U+0266: LATIN SMALL LETTER H WITH HOOK</td>
<td align="left">U+A7AA: LATIN CAPITAL LETTER H WITH HOOK</td>
</tr>
<tr>
<td align="left">U+026A: LATIN LETTER SMALL CAPITAL I</td>
<td align="left">U+A7AE: LATIN CAPITAL LETTER SMALL CAPITAL I</td>
</tr>
<tr>
<td align="left">U+026C: LATIN SMALL LETTER L WITH BELT</td>
<td align="left">U+A7AD: LATIN CAPITAL LETTER L WITH BELT</td>
</tr>
<tr>
<td align="left">U+029D: LATIN SMALL LETTER J WITH CROSSED-TAIL</td>
<td align="left">U+A7B2: LATIN CAPITAL LETTER J WITH CROSSED-TAIL</td>
</tr>
<tr>
<td align="left">U+0376: GREEK CAPITAL LETTER PAMPHYLIAN DIGAMMA</td>
<td align="left">U+0377: GREEK SMALL LETTER PAMPHYLIAN DIGAMMA</td>
</tr>
<tr>
<td align="left">U+03FA: GREEK CAPITAL LETTER SAN</td>
<td align="left">U+03FB: GREEK SMALL LETTER SAN</td>
</tr>
<tr>
<td align="left">U+052F: CYRILLIC SMALL LETTER EL WITH DESCENDER</td>
<td align="left">U+052E: CYRILLIC CAPITAL LETTER EL WITH DESCENDER</td>
</tr>
<tr>
<td align="left">U+2132: TURNED CAPITAL F</td>
<td align="left">U+214E: TURNED SMALL F</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#family-win-ascent-and-descent">family/win_ascent_and_descent</a></summary>
    <div>


> 
> A font's winAscent and winDescent values should be greater than or equal to
> the head table's yMax, abs(yMin) values. If they are less than these values,
> clipping can occur on Windows platforms
> (https://github.com/RedHatBrand/Overpass/issues/33).
> 
> If the font includes tall/deep writing systems such as Arabic or Devanagari,
> the winAscent and winDescent can be greater than the yMax and absolute yMin
> values to accommodate vowel marks.
> 
> When the 'win' Metrics are significantly greater than the UPM, the linespacing
> can appear too loose. To counteract this, enabling the OS/2 fsSelection
> bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values
> instead. This means the font developer can control the linespacing with
> the 'typo' values, whilst avoiding clipping by setting the 'win' values to
> values greater than the yMax and absolute yMin.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 2297, but got 1984 instead</p>
 [code: ascent]



* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 689, but got 494 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure font doesn't have Mac name table entries (platform=1). <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#no-mac-entries">no_mac_entries</a></summary>
    <div>


> 
> Mac name table entries are not needed anymore. Even Apple stopped producing
> name tables with platform 1. Please see for example the following system font:
> 
> /System/Library/Fonts/SFCompact.ttf
> 
> Also, Dave Opstad, who developed Apple's TrueType specifications, told
> Olli Meier a couple years ago (as of January/2022) that these entries are
> outdated and should not be produced anymore.
> 




> Original proposal: https://github.com/googlefonts/gftools/issues/469





* 🔥 **FAIL** <p>Please remove name ID 1</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 2</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 3</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 4</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 5</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 6</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 10</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 16</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 17</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 18</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 25</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 257</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 298</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 301</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 302</p>
 [code: mac-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure smart dropout control is enabled in "prep" table instructions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#smart-dropout">smart_dropout</a></summary>
    <div>


> 
> This setup is meant to ensure consistent rendering quality for fonts across
> all devices (with different rendering/hinting capabilities).
> 
> Below is the snippet of instructions we expect to see in the fonts:
> B8 01 FF    PUSHW 0x01FF
> 85          SCANCTRL (unconditinally turn on
> dropout control mode)
> B0 04       PUSHB 0x04
> 8D          SCANTYPE (enable smart dropout control)
> 
> "Smart dropout control" means activating rules 1, 2 and 5:
> Rule 1: If a pixel's center falls within the glyph outline,
> that pixel is turned on.
> Rule 2: If a contour falls exactly on a pixel's center,
> that pixel is turned on.
> Rule 5: If a scan line between two adjacent pixel centers
> (either vertical or horizontal) is intersected
> by both an on-Transition contour and an off-Transition
> contour and neither of the pixels was already turned on
> by rules 1 and 2, turn on the pixel which is closer to
> the midpoint between the on-Transition contour and
> off-Transition contour. This is "Smart" dropout control.
> 
> For more detailed info (such as other rules not enabled in this snippet),
> please refer to the TrueType Instruction Set documentation.
> 
> Generally this occurs with unhinted fonts; if you are not using autohinting,
> use gftools-fix-nonhinting (or just gftools-fix-font) to fix this issue.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>The 'prep' table does not contain TrueType instructions enabling smart dropout control. To fix, export the font with autohinting enabled, or run ttfautohint on the font, or run the <code>gftools fix-nonhinting</code> script.</p>
 [code: lacks-smart-dropout]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-mark-chars">opentype/gdef_mark_chars</a></summary>
    <div>


> 
> Mark characters should be in the GDEF mark glyph class.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2877





* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
uni0488 (U+0488), uni0489 (U+0489), uni20DD (U+20DD) and uni20DE (U+20DE)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check glyphs in mark glyph class are non-spacing. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-spacing-marks">opentype/gdef_spacing_marks</a></summary>
    <div>


> 
> Glyphs in the GDEF mark glyph class should be non-spacing.
> 
> Spacing glyphs in the GDEF mark glyph class may have incorrect anchor
> positioning that was only intended for building composite glyphs during design.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2877





* ⚠️ **WARN** <p>The following glyphs seem to be spacing (because they have width &gt; 0 on the hmtx table) so they may be in the GDEF mark glyph class by mistake, or they should have zero width instead:
dotbelow (U+0323)</p>
 [code: spacing-mark-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: numbersign	Contours detected: 4	Expected: 2

- Glyph name: dollar	Contours detected: 2	Expected: 1, 3 or 5

- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: K	Contours detected: 3	Expected: 1 or 2

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: asciicircum	Contours detected: 2	Expected: 1

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: k	Contours detected: 3	Expected: 1 or 2

- Glyph name: braceleft	Contours detected: 3	Expected: 1

- Glyph name: braceright	Contours detected: 3	Expected: 1

- 596 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* Q_rthook (U+024A): L&lt;&lt;1180.0,0.0&gt;--&lt;1407.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* feng.1 (U+EE11): L&lt;&lt;1493.0,0.0&gt;--&lt;1265.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* feng (U+02A9): L&lt;&lt;1581.0,0.0&gt;--&lt;1353.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0452 (U+0452): L&lt;&lt;1052.0,0.0&gt;--&lt;824.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0267 (U+0267): L&lt;&lt;1052.0,0.0&gt;--&lt;824.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* lrthook (U+026D): L&lt;&lt;350.0,0.0&gt;--&lt;123.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0271 (U+0271): L&lt;&lt;1652.0,0.0&gt;--&lt;1424.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* nrthook (U+0273): L&lt;&lt;1052.0,0.0&gt;--&lt;824.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* eng (U+014B): L&lt;&lt;1052.0,0.0&gt;--&lt;824.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* nlfthook (U+0272): L&lt;&lt;350.0,0.0&gt;--&lt;123.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* 9 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>


> 
> Glyphs are either accessible directly through Unicode codepoints or through
> substitution rules.
> 
> In Color Fonts, glyphs are also referenced by the COLR table. And mathematical
> fonts also reference glyphs via the MATH table.
> 
> Any glyphs not accessible by these means are redundant and serve only
> to increase the font's file size.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3160





* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- _part.t_base

- _part.tcurl_base

- koronisaccentleft.cn

- macrondieresiscomb.cn

- tildemacroncomb.cn

- uni1DC4.cn

- uni1DC6.cn
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>
</div>
</details>

<details><summary>[10] NevlinUIPlus-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Check base characters have non-zero advance width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#base-has-width">base_has_width</a></summary>
    <div>


> 
> Base characters should have non-zero advance width.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4906





* 🔥 **FAIL** <p>The following glyphs had zero advance width:
- uni0488 (U+0488)</p>
<pre><code>- uni0489 (U+0489)
</code></pre>
 [code: zero-width-bases]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>


> 
> Ensure that no glyph lacks its corresponding upper or lower counterpart
> (but only when unicode supports case-mapping).
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/3230





* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+01C6: LATIN SMALL LETTER DZ WITH CARON</td>
<td align="left">U+01C4: LATIN CAPITAL LETTER DZ WITH CARON</td>
</tr>
<tr>
<td align="left">U+023A: LATIN CAPITAL LETTER A WITH STROKE</td>
<td align="left">U+2C65: LATIN SMALL LETTER A WITH STROKE</td>
</tr>
<tr>
<td align="left">U+023E: LATIN CAPITAL LETTER T WITH DIAGONAL STROKE</td>
<td align="left">U+2C66: LATIN SMALL LETTER T WITH DIAGONAL STROKE</td>
</tr>
<tr>
<td align="left">U+0265: LATIN SMALL LETTER TURNED H</td>
<td align="left">U+A78D: LATIN CAPITAL LETTER TURNED H</td>
</tr>
<tr>
<td align="left">U+0266: LATIN SMALL LETTER H WITH HOOK</td>
<td align="left">U+A7AA: LATIN CAPITAL LETTER H WITH HOOK</td>
</tr>
<tr>
<td align="left">U+026A: LATIN LETTER SMALL CAPITAL I</td>
<td align="left">U+A7AE: LATIN CAPITAL LETTER SMALL CAPITAL I</td>
</tr>
<tr>
<td align="left">U+026C: LATIN SMALL LETTER L WITH BELT</td>
<td align="left">U+A7AD: LATIN CAPITAL LETTER L WITH BELT</td>
</tr>
<tr>
<td align="left">U+029D: LATIN SMALL LETTER J WITH CROSSED-TAIL</td>
<td align="left">U+A7B2: LATIN CAPITAL LETTER J WITH CROSSED-TAIL</td>
</tr>
<tr>
<td align="left">U+0376: GREEK CAPITAL LETTER PAMPHYLIAN DIGAMMA</td>
<td align="left">U+0377: GREEK SMALL LETTER PAMPHYLIAN DIGAMMA</td>
</tr>
<tr>
<td align="left">U+03FA: GREEK CAPITAL LETTER SAN</td>
<td align="left">U+03FB: GREEK SMALL LETTER SAN</td>
</tr>
<tr>
<td align="left">U+052F: CYRILLIC SMALL LETTER EL WITH DESCENDER</td>
<td align="left">U+052E: CYRILLIC CAPITAL LETTER EL WITH DESCENDER</td>
</tr>
<tr>
<td align="left">U+2132: TURNED CAPITAL F</td>
<td align="left">U+214E: TURNED SMALL F</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#family-win-ascent-and-descent">family/win_ascent_and_descent</a></summary>
    <div>


> 
> A font's winAscent and winDescent values should be greater than or equal to
> the head table's yMax, abs(yMin) values. If they are less than these values,
> clipping can occur on Windows platforms
> (https://github.com/RedHatBrand/Overpass/issues/33).
> 
> If the font includes tall/deep writing systems such as Arabic or Devanagari,
> the winAscent and winDescent can be greater than the yMax and absolute yMin
> values to accommodate vowel marks.
> 
> When the 'win' Metrics are significantly greater than the UPM, the linespacing
> can appear too loose. To counteract this, enabling the OS/2 fsSelection
> bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values
> instead. This means the font developer can control the linespacing with
> the 'typo' values, whilst avoiding clipping by setting the 'win' values to
> values greater than the yMax and absolute yMin.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 2297, but got 1984 instead</p>
 [code: ascent]



* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 689, but got 494 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure font doesn't have Mac name table entries (platform=1). <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#no-mac-entries">no_mac_entries</a></summary>
    <div>


> 
> Mac name table entries are not needed anymore. Even Apple stopped producing
> name tables with platform 1. Please see for example the following system font:
> 
> /System/Library/Fonts/SFCompact.ttf
> 
> Also, Dave Opstad, who developed Apple's TrueType specifications, told
> Olli Meier a couple years ago (as of January/2022) that these entries are
> outdated and should not be produced anymore.
> 




> Original proposal: https://github.com/googlefonts/gftools/issues/469





* 🔥 **FAIL** <p>Please remove name ID 1</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 2</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 3</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 4</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 5</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 6</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 10</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 16</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 17</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 18</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 25</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 257</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 298</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 301</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 302</p>
 [code: mac-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure smart dropout control is enabled in "prep" table instructions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#smart-dropout">smart_dropout</a></summary>
    <div>


> 
> This setup is meant to ensure consistent rendering quality for fonts across
> all devices (with different rendering/hinting capabilities).
> 
> Below is the snippet of instructions we expect to see in the fonts:
> B8 01 FF    PUSHW 0x01FF
> 85          SCANCTRL (unconditinally turn on
> dropout control mode)
> B0 04       PUSHB 0x04
> 8D          SCANTYPE (enable smart dropout control)
> 
> "Smart dropout control" means activating rules 1, 2 and 5:
> Rule 1: If a pixel's center falls within the glyph outline,
> that pixel is turned on.
> Rule 2: If a contour falls exactly on a pixel's center,
> that pixel is turned on.
> Rule 5: If a scan line between two adjacent pixel centers
> (either vertical or horizontal) is intersected
> by both an on-Transition contour and an off-Transition
> contour and neither of the pixels was already turned on
> by rules 1 and 2, turn on the pixel which is closer to
> the midpoint between the on-Transition contour and
> off-Transition contour. This is "Smart" dropout control.
> 
> For more detailed info (such as other rules not enabled in this snippet),
> please refer to the TrueType Instruction Set documentation.
> 
> Generally this occurs with unhinted fonts; if you are not using autohinting,
> use gftools-fix-nonhinting (or just gftools-fix-font) to fix this issue.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>The 'prep' table does not contain TrueType instructions enabling smart dropout control. To fix, export the font with autohinting enabled, or run ttfautohint on the font, or run the <code>gftools fix-nonhinting</code> script.</p>
 [code: lacks-smart-dropout]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-mark-chars">opentype/gdef_mark_chars</a></summary>
    <div>


> 
> Mark characters should be in the GDEF mark glyph class.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2877





* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
uni0488 (U+0488), uni0489 (U+0489), uni20DD (U+20DD) and uni20DE (U+20DE)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check glyphs in mark glyph class are non-spacing. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-spacing-marks">opentype/gdef_spacing_marks</a></summary>
    <div>


> 
> Glyphs in the GDEF mark glyph class should be non-spacing.
> 
> Spacing glyphs in the GDEF mark glyph class may have incorrect anchor
> positioning that was only intended for building composite glyphs during design.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2877





* ⚠️ **WARN** <p>The following glyphs seem to be spacing (because they have width &gt; 0 on the hmtx table) so they may be in the GDEF mark glyph class by mistake, or they should have zero width instead:
dotbelow (U+0323)</p>
 [code: spacing-mark-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: numbersign	Contours detected: 4	Expected: 2

- Glyph name: dollar	Contours detected: 2	Expected: 1, 3 or 5

- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: K	Contours detected: 3	Expected: 1 or 2

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: asciicircum	Contours detected: 2	Expected: 1

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: k	Contours detected: 3	Expected: 1 or 2

- Glyph name: braceleft	Contours detected: 3	Expected: 1

- Glyph name: braceright	Contours detected: 3	Expected: 1

- 596 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* Q_rthook (U+024A): L&lt;&lt;1205.0,0.0&gt;--&lt;1392.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni01AC (U+01AC): L&lt;&lt;447.0,1317.0&gt;--&lt;447.0,1490.0&gt;&gt; has the same coordinates as a previous segment.

* uni0267 (U+0267): L&lt;&lt;1018.0,0.0&gt;--&lt;832.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* lrthook (U+026D): L&lt;&lt;317.0,0.0&gt;--&lt;130.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0271 (U+0271): L&lt;&lt;1615.0,0.0&gt;--&lt;1428.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* nlfthook (U+0272): L&lt;&lt;317.0,0.0&gt;--&lt;130.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* rrthook (U+E05D): L&lt;&lt;317.0,0.0&gt;--&lt;130.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* epsilonclosed (U+029A): L&lt;&lt;972.0,538.0&gt;--&lt;786.0,538.0&gt;&gt; has the same coordinates as a previous segment.

* epsilon1revclosed (U+025E): L&lt;&lt;263.0,538.0&gt;--&lt;77.0,538.0&gt;&gt; has the same coordinates as a previous segment.

* uni04C8 (U+04C8): L&lt;&lt;1026.0,0.0&gt;--&lt;840.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* 5 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>


> 
> Glyphs are either accessible directly through Unicode codepoints or through
> substitution rules.
> 
> In Color Fonts, glyphs are also referenced by the COLR table. And mathematical
> fonts also reference glyphs via the MATH table.
> 
> Any glyphs not accessible by these means are redundant and serve only
> to increase the font's file size.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3160





* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- _part.t_base

- _part.tcurl_base

- koronisaccentleft.cn

- macrondieresiscomb.cn

- tildemacroncomb.cn

- uni1DC4.cn

- uni1DC6.cn
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>
</div>
</details>

<details><summary>[10] NevlinUIPlus-Semibold.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Check base characters have non-zero advance width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#base-has-width">base_has_width</a></summary>
    <div>


> 
> Base characters should have non-zero advance width.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4906





* 🔥 **FAIL** <p>The following glyphs had zero advance width:
- uni0488 (U+0488)</p>
<pre><code>- uni0489 (U+0489)
</code></pre>
 [code: zero-width-bases]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>


> 
> Ensure that no glyph lacks its corresponding upper or lower counterpart
> (but only when unicode supports case-mapping).
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/3230





* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+01C6: LATIN SMALL LETTER DZ WITH CARON</td>
<td align="left">U+01C4: LATIN CAPITAL LETTER DZ WITH CARON</td>
</tr>
<tr>
<td align="left">U+023A: LATIN CAPITAL LETTER A WITH STROKE</td>
<td align="left">U+2C65: LATIN SMALL LETTER A WITH STROKE</td>
</tr>
<tr>
<td align="left">U+023E: LATIN CAPITAL LETTER T WITH DIAGONAL STROKE</td>
<td align="left">U+2C66: LATIN SMALL LETTER T WITH DIAGONAL STROKE</td>
</tr>
<tr>
<td align="left">U+0265: LATIN SMALL LETTER TURNED H</td>
<td align="left">U+A78D: LATIN CAPITAL LETTER TURNED H</td>
</tr>
<tr>
<td align="left">U+0266: LATIN SMALL LETTER H WITH HOOK</td>
<td align="left">U+A7AA: LATIN CAPITAL LETTER H WITH HOOK</td>
</tr>
<tr>
<td align="left">U+026A: LATIN LETTER SMALL CAPITAL I</td>
<td align="left">U+A7AE: LATIN CAPITAL LETTER SMALL CAPITAL I</td>
</tr>
<tr>
<td align="left">U+026C: LATIN SMALL LETTER L WITH BELT</td>
<td align="left">U+A7AD: LATIN CAPITAL LETTER L WITH BELT</td>
</tr>
<tr>
<td align="left">U+029D: LATIN SMALL LETTER J WITH CROSSED-TAIL</td>
<td align="left">U+A7B2: LATIN CAPITAL LETTER J WITH CROSSED-TAIL</td>
</tr>
<tr>
<td align="left">U+0376: GREEK CAPITAL LETTER PAMPHYLIAN DIGAMMA</td>
<td align="left">U+0377: GREEK SMALL LETTER PAMPHYLIAN DIGAMMA</td>
</tr>
<tr>
<td align="left">U+03FA: GREEK CAPITAL LETTER SAN</td>
<td align="left">U+03FB: GREEK SMALL LETTER SAN</td>
</tr>
<tr>
<td align="left">U+052F: CYRILLIC SMALL LETTER EL WITH DESCENDER</td>
<td align="left">U+052E: CYRILLIC CAPITAL LETTER EL WITH DESCENDER</td>
</tr>
<tr>
<td align="left">U+2132: TURNED CAPITAL F</td>
<td align="left">U+214E: TURNED SMALL F</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#family-win-ascent-and-descent">family/win_ascent_and_descent</a></summary>
    <div>


> 
> A font's winAscent and winDescent values should be greater than or equal to
> the head table's yMax, abs(yMin) values. If they are less than these values,
> clipping can occur on Windows platforms
> (https://github.com/RedHatBrand/Overpass/issues/33).
> 
> If the font includes tall/deep writing systems such as Arabic or Devanagari,
> the winAscent and winDescent can be greater than the yMax and absolute yMin
> values to accommodate vowel marks.
> 
> When the 'win' Metrics are significantly greater than the UPM, the linespacing
> can appear too loose. To counteract this, enabling the OS/2 fsSelection
> bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values
> instead. This means the font developer can control the linespacing with
> the 'typo' values, whilst avoiding clipping by setting the 'win' values to
> values greater than the yMax and absolute yMin.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 2297, but got 1984 instead</p>
 [code: ascent]



* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 689, but got 494 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure font doesn't have Mac name table entries (platform=1). <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#no-mac-entries">no_mac_entries</a></summary>
    <div>


> 
> Mac name table entries are not needed anymore. Even Apple stopped producing
> name tables with platform 1. Please see for example the following system font:
> 
> /System/Library/Fonts/SFCompact.ttf
> 
> Also, Dave Opstad, who developed Apple's TrueType specifications, told
> Olli Meier a couple years ago (as of January/2022) that these entries are
> outdated and should not be produced anymore.
> 




> Original proposal: https://github.com/googlefonts/gftools/issues/469





* 🔥 **FAIL** <p>Please remove name ID 1</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 2</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 3</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 4</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 5</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 6</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 10</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 16</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 17</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 18</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 25</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 257</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 298</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 301</p>
 [code: mac-names]



* 🔥 **FAIL** <p>Please remove name ID 302</p>
 [code: mac-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure smart dropout control is enabled in "prep" table instructions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#smart-dropout">smart_dropout</a></summary>
    <div>


> 
> This setup is meant to ensure consistent rendering quality for fonts across
> all devices (with different rendering/hinting capabilities).
> 
> Below is the snippet of instructions we expect to see in the fonts:
> B8 01 FF    PUSHW 0x01FF
> 85          SCANCTRL (unconditinally turn on
> dropout control mode)
> B0 04       PUSHB 0x04
> 8D          SCANTYPE (enable smart dropout control)
> 
> "Smart dropout control" means activating rules 1, 2 and 5:
> Rule 1: If a pixel's center falls within the glyph outline,
> that pixel is turned on.
> Rule 2: If a contour falls exactly on a pixel's center,
> that pixel is turned on.
> Rule 5: If a scan line between two adjacent pixel centers
> (either vertical or horizontal) is intersected
> by both an on-Transition contour and an off-Transition
> contour and neither of the pixels was already turned on
> by rules 1 and 2, turn on the pixel which is closer to
> the midpoint between the on-Transition contour and
> off-Transition contour. This is "Smart" dropout control.
> 
> For more detailed info (such as other rules not enabled in this snippet),
> please refer to the TrueType Instruction Set documentation.
> 
> Generally this occurs with unhinted fonts; if you are not using autohinting,
> use gftools-fix-nonhinting (or just gftools-fix-font) to fix this issue.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>The 'prep' table does not contain TrueType instructions enabling smart dropout control. To fix, export the font with autohinting enabled, or run ttfautohint on the font, or run the <code>gftools fix-nonhinting</code> script.</p>
 [code: lacks-smart-dropout]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-mark-chars">opentype/gdef_mark_chars</a></summary>
    <div>


> 
> Mark characters should be in the GDEF mark glyph class.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2877





* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
uni0488 (U+0488), uni0489 (U+0489), uni20DD (U+20DD) and uni20DE (U+20DE)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check glyphs in mark glyph class are non-spacing. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-spacing-marks">opentype/gdef_spacing_marks</a></summary>
    <div>


> 
> Glyphs in the GDEF mark glyph class should be non-spacing.
> 
> Spacing glyphs in the GDEF mark glyph class may have incorrect anchor
> positioning that was only intended for building composite glyphs during design.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2877





* ⚠️ **WARN** <p>The following glyphs seem to be spacing (because they have width &gt; 0 on the hmtx table) so they may be in the GDEF mark glyph class by mistake, or they should have zero width instead:
dotbelow (U+0323)</p>
 [code: spacing-mark-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: numbersign	Contours detected: 4	Expected: 2

- Glyph name: dollar	Contours detected: 2	Expected: 1, 3 or 5

- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: K	Contours detected: 3	Expected: 1 or 2

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: asciicircum	Contours detected: 2	Expected: 1

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: k	Contours detected: 3	Expected: 1 or 2

- Glyph name: braceleft	Contours detected: 3	Expected: 1

- Glyph name: braceright	Contours detected: 3	Expected: 1

- 596 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* Q_rthook (U+024A): L&lt;&lt;1155.0,0.0&gt;--&lt;1423.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* feng.1 (U+EE11): L&lt;&lt;1566.0,0.0&gt;--&lt;1297.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* feng (U+02A9): L&lt;&lt;1661.0,0.0&gt;--&lt;1392.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0452 (U+0452): L&lt;&lt;1085.0,0.0&gt;--&lt;816.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0267 (U+0267): L&lt;&lt;1085.0,0.0&gt;--&lt;816.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* lrthook (U+026D): L&lt;&lt;383.0,0.0&gt;--&lt;115.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0271 (U+0271): L&lt;&lt;1689.0,0.0&gt;--&lt;1420.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* nrthook (U+0273): L&lt;&lt;1085.0,0.0&gt;--&lt;816.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* eng (U+014B): L&lt;&lt;1085.0,0.0&gt;--&lt;816.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* nlfthook (U+0272): L&lt;&lt;383.0,0.0&gt;--&lt;115.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* 12 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>


> 
> Glyphs are either accessible directly through Unicode codepoints or through
> substitution rules.
> 
> In Color Fonts, glyphs are also referenced by the COLR table. And mathematical
> fonts also reference glyphs via the MATH table.
> 
> Any glyphs not accessible by these means are redundant and serve only
> to increase the font's file size.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3160





* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- _part.t_base

- _part.tcurl_base

- koronisaccentleft.cn

- macrondieresiscomb.cn

- tildemacroncomb.cn

- uni1DC4.cn

- uni1DC6.cn
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 23 | 20 | 149 | 12 | 268 | 0 | 
| 0% | 0% | 5% | 4% | 32% | 3% | 57% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
