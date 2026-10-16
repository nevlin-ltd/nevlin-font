## FontSpector report

fontspector version: 1.9.0






## Check results




<details><summary>[1] output/nevlin-google-fonts/core-latin/googlefonts/nevlinfont</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. (googlefonts/metadata/unreachable_subsetting)</summary>
    <div>


> This check ensures that all encoded glyphs in the font are covered by a subset declared in the METADATA.pb. Google Fonts splits the font into a set of subset fonts based on the contents of the `subsets` field and the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions will not be served in the subsetted fonts, and so will be unreachable to the end user.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4097 and https://github.com/fonttools/fontbakery/pull/4273]





- ⚠️ **WARN** output/nevlin-google-fonts/core-latin/googlefonts/nevlinfont/NevlinFont-Bold.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, cherokee, math
* U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
* U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, coptic, hebrew, tai-le, todhri, canadian-aboriginal, duployan, syriac, malayalam, tifinagh, math
* U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage
* U+030C COMBINING CARON: try adding one of: cherokee, tai-le
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese
* U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese
* U+25CC DOTTED CIRCLE: try adding one of: tagbanwa, kharoshthi, kaithi, ahom, gunjala-gondi, myanmar, mongolian, hanunoo, soyombo, khojki, masaram-gondi, tai-tham, tifinagh, lepcha, hanifi-rohingya, manichaean, malayalam, khudawadi, old-permic, osage, sundanese, saurashtra, tamil, tirhuta, wancho, zanabazar-square, adlam, javanese, newa, canadian-aboriginal, hebrew, modi, sharada, syloti-nagri, symbols, elbasan, yi, duployan, mandaic, brahmi, buginese, chakma, psalter-pahlavi, tai-le, batak, devanagari, music, rejang, grantha, gujarati, kannada, kayah-li, limbu, meetei-mayek, phags-pa, new-tai-lue, marchen, mahajani, math, tagalog, siddham, caucasian-albanian, thaana, oriya, pahawh-hmong, cham, coptic, sogdian, khmer, dogra, gurmukhi, armenian, bassa-vah, lao, mende-kikakui, buhid, bengali, nko, tai-viet, warang-citi, thai, balinese, sinhala, takri, bhaiksuki, miao, tibetan, syriac, telugu

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  


- ⚠️ **WARN** output/nevlin-google-fonts/core-latin/googlefonts/nevlinfont/NevlinFont-Medium.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, cherokee, math
* U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
* U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, coptic, hebrew, tai-le, todhri, canadian-aboriginal, duployan, syriac, malayalam, tifinagh, math
* U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage
* U+030C COMBINING CARON: try adding one of: cherokee, tai-le
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese
* U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese
* U+25CC DOTTED CIRCLE: try adding one of: tagbanwa, kharoshthi, kaithi, ahom, gunjala-gondi, myanmar, mongolian, hanunoo, soyombo, khojki, masaram-gondi, tai-tham, tifinagh, lepcha, hanifi-rohingya, manichaean, malayalam, khudawadi, old-permic, osage, sundanese, saurashtra, tamil, tirhuta, wancho, zanabazar-square, adlam, javanese, newa, canadian-aboriginal, hebrew, modi, sharada, syloti-nagri, symbols, elbasan, yi, duployan, mandaic, brahmi, buginese, chakma, psalter-pahlavi, tai-le, batak, devanagari, music, rejang, grantha, gujarati, kannada, kayah-li, limbu, meetei-mayek, phags-pa, new-tai-lue, marchen, mahajani, math, tagalog, siddham, caucasian-albanian, thaana, oriya, pahawh-hmong, cham, coptic, sogdian, khmer, dogra, gurmukhi, armenian, bassa-vah, lao, mende-kikakui, buhid, bengali, nko, tai-viet, warang-citi, thai, balinese, sinhala, takri, bhaiksuki, miao, tibetan, syriac, telugu

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  


- ⚠️ **WARN** output/nevlin-google-fonts/core-latin/googlefonts/nevlinfont/NevlinFont-Regular.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, cherokee, math
* U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
* U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, coptic, hebrew, tai-le, todhri, canadian-aboriginal, duployan, syriac, malayalam, tifinagh, math
* U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage
* U+030C COMBINING CARON: try adding one of: cherokee, tai-le
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese
* U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese
* U+25CC DOTTED CIRCLE: try adding one of: tagbanwa, kharoshthi, kaithi, ahom, gunjala-gondi, myanmar, mongolian, hanunoo, soyombo, khojki, masaram-gondi, tai-tham, tifinagh, lepcha, hanifi-rohingya, manichaean, malayalam, khudawadi, old-permic, osage, sundanese, saurashtra, tamil, tirhuta, wancho, zanabazar-square, adlam, javanese, newa, canadian-aboriginal, hebrew, modi, sharada, syloti-nagri, symbols, elbasan, yi, duployan, mandaic, brahmi, buginese, chakma, psalter-pahlavi, tai-le, batak, devanagari, music, rejang, grantha, gujarati, kannada, kayah-li, limbu, meetei-mayek, phags-pa, new-tai-lue, marchen, mahajani, math, tagalog, siddham, caucasian-albanian, thaana, oriya, pahawh-hmong, cham, coptic, sogdian, khmer, dogra, gurmukhi, armenian, bassa-vah, lao, mende-kikakui, buhid, bengali, nko, tai-viet, warang-citi, thai, balinese, sinhala, takri, bhaiksuki, miao, tibetan, syriac, telugu

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  


- ⚠️ **WARN** output/nevlin-google-fonts/core-latin/googlefonts/nevlinfont/NevlinFont-SemiBold.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, cherokee, math
* U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
* U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, coptic, hebrew, tai-le, todhri, canadian-aboriginal, duployan, syriac, malayalam, tifinagh, math
* U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage
* U+030C COMBINING CARON: try adding one of: cherokee, tai-le
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese
* U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese
* U+25CC DOTTED CIRCLE: try adding one of: tagbanwa, kharoshthi, kaithi, ahom, gunjala-gondi, myanmar, mongolian, hanunoo, soyombo, khojki, masaram-gondi, tai-tham, tifinagh, lepcha, hanifi-rohingya, manichaean, malayalam, khudawadi, old-permic, osage, sundanese, saurashtra, tamil, tirhuta, wancho, zanabazar-square, adlam, javanese, newa, canadian-aboriginal, hebrew, modi, sharada, syloti-nagri, symbols, elbasan, yi, duployan, mandaic, brahmi, buginese, chakma, psalter-pahlavi, tai-le, batak, devanagari, music, rejang, grantha, gujarati, kannada, kayah-li, limbu, meetei-mayek, phags-pa, new-tai-lue, marchen, mahajani, math, tagalog, siddham, caucasian-albanian, thaana, oriya, pahawh-hmong, cham, coptic, sogdian, khmer, dogra, gurmukhi, armenian, bassa-vah, lao, mende-kikakui, buhid, bengali, nko, tai-viet, warang-citi, thai, balinese, sinhala, takri, bhaiksuki, miao, tibetan, syriac, telugu

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  

</div>
</details>


</div>
</details>


<details><summary>[1] output/nevlin-google-fonts/core-latin/googlefonts/nevlinfont/NevlinFont-Medium.ttf</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>


> Microsoft keeps a list of font vendors and their respective contact info. This list is updated regularly and is indexed by a 4-char "Vendor ID" which is stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some applications may display the type designer / type foundry contact info on some dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in that list or if it has some of the default values used by the most common font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs. If you registered recently, you're safe to ignore warnings emitted by this check, since your ID will soon be included in one of our upcoming releases.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3943, https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** OS/2 VendorID value 'NONE' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>


</div>
</details>


<details><summary>[2] output/nevlin-google-fonts/core-latin/googlefonts/nevlinfont/NevlinFont-SemiBold.ttf</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? (outline_jaggy_segments)</summary>
    <div>


> This check heuristically detects outline segments which form a particularly small angle, indicative of an outline error. This may cause false positives in cases such as extreme ink traps, so should be regarded as advisory and backed up by manual inspection.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3064]





- ⚠️ **WARN** The following glyphs have jaggy segments:

* r (U+0072): Line(Line { p0: (349.0, 1070.0), p1: (349.0, 851.0) })/Quad(QuadBez { p0: (349.0, 851.0), p1: (360.0, 942.0), p2: (410.0, 998.0) }) = 6.892423122485113 degrees
* racute (U+0155): Line(Line { p0: (349.0, 1070.0), p1: (349.0, 851.0) })/Quad(QuadBez { p0: (349.0, 851.0), p1: (360.0, 942.0), p2: (410.0, 998.0) }) = 6.892423122485113 degrees
* uni0157 (U+0157): Line(Line { p0: (349.0, 1070.0), p1: (349.0, 851.0) })/Quad(QuadBez { p0: (349.0, 851.0), p1: (360.0, 942.0), p2: (410.0, 998.0) }) = 6.892423122485113 degrees
* rcaron (U+0159): Line(Line { p0: (349.0, 1070.0), p1: (349.0, 851.0) })/Quad(QuadBez { p0: (349.0, 851.0), p1: (360.0, 942.0), p2: (410.0, 998.0) }) = 6.892423122485113 degrees
* uni1E59: Line(Line { p0: (349.0, 1070.0), p1: (349.0, 851.0) })/Quad(QuadBez { p0: (349.0, 851.0), p1: (360.0, 942.0), p2: (410.0, 998.0) }) = 6.892423122485113 degrees
* r.sups: Line(Line { p0: (252.0, 1462.0), p1: (252.0, 1341.0) })/Quad(QuadBez { p0: (252.0, 1341.0), p1: (260.0, 1391.0), p2: (294.5, 1422.0) }) = 9.090276920822351 degrees
* r.subs: Line(Line { p0: (252.0, 267.0), p1: (252.0, 145.0) })/Quad(QuadBez { p0: (252.0, 145.0), p1: (260.0, 196.0), p2: (294.5, 227.0) }) = 8.914926957147863 degrees
* uni0157.ss03: Line(Line { p0: (349.0, 1070.0), p1: (349.0, 851.0) })/Quad(QuadBez { p0: (349.0, 851.0), p1: (360.0, 942.0), p2: (410.0, 998.0) }) = 6.892423122485113 degrees
* uni1E59.ss07: Line(Line { p0: (349.0, 1070.0), p1: (349.0, 851.0) })/Quad(QuadBez { p0: (349.0, 851.0), p1: (360.0, 942.0), p2: (410.0, 998.0) }) = 6.892423122485113 degrees
* uni0157.ss07: Line(Line { p0: (349.0, 1070.0), p1: (349.0, 851.0) })/Quad(QuadBez { p0: (349.0, 851.0), p1: (360.0, 942.0), p2: (410.0, 998.0) }) = 6.892423122485113 degrees [code: found-jaggy-segments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>


> Microsoft keeps a list of font vendors and their respective contact info. This list is updated regularly and is indexed by a 4-char "Vendor ID" which is stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some applications may display the type designer / type foundry contact info on some dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in that list or if it has some of the default values used by the most common font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs. If you registered recently, you're safe to ignore warnings emitted by this check, since your ID will soon be included in one of our upcoming releases.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3943, https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** OS/2 VendorID value 'NONE' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>


</div>
</details>


<details><summary>[2] output/nevlin-google-fonts/core-latin/googlefonts/nevlinfont/NevlinFont-Bold.ttf</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? (outline_jaggy_segments)</summary>
    <div>


> This check heuristically detects outline segments which form a particularly small angle, indicative of an outline error. This may cause false positives in cases such as extreme ink traps, so should be regarded as advisory and backed up by manual inspection.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3064]





- ⚠️ **WARN** The following glyphs have jaggy segments:

* M (U+004D): Quad(QuadBez { p0: (1437.0, 1129.0), p1: (1437.0, 1142.0), p2: (1438.0, 1155.0) })/Line(Line { p0: (1438.0, 1155.0), p1: (1428.0, 1121.0) }) = 11.990834979039256 degrees
* uni1E3E: Quad(QuadBez { p0: (1437.0, 1129.0), p1: (1437.0, 1142.0), p2: (1438.0, 1155.0) })/Line(Line { p0: (1438.0, 1155.0), p1: (1428.0, 1121.0) }) = 11.990834979039256 degrees
* uni1E40: Quad(QuadBez { p0: (1437.0, 1129.0), p1: (1437.0, 1142.0), p2: (1438.0, 1155.0) })/Line(Line { p0: (1438.0, 1155.0), p1: (1428.0, 1121.0) }) = 11.990834979039256 degrees
* g (U+0067): Quad(QuadBez { p0: (807.0, 976.5), p1: (851.0, 931.0), p2: (855.0, 865.0) })/Line(Line { p0: (855.0, 865.0), p1: (855.0, 1049.0) }) = 3.4682292589173067 degrees
* gbar (U+01E5): Quad(QuadBez { p0: (807.0, 976.5), p1: (851.0, 931.0), p2: (855.0, 865.0) })/Line(Line { p0: (855.0, 865.0), p1: (855.0, 1049.0) }) = 3.4682292589173067 degrees
* gcircumflex: Quad(QuadBez { p0: (807.0, 976.5), p1: (851.0, 931.0), p2: (855.0, 865.0) })/Line(Line { p0: (855.0, 865.0), p1: (855.0, 1049.0) }) = 3.4682292589173067 degrees
* gbreve (U+011F): Quad(QuadBez { p0: (807.0, 976.5), p1: (851.0, 931.0), p2: (855.0, 865.0) })/Line(Line { p0: (855.0, 865.0), p1: (855.0, 1049.0) }) = 3.4682292589173067 degrees
* gdotaccent (U+0121): Quad(QuadBez { p0: (807.0, 976.5), p1: (851.0, 931.0), p2: (855.0, 865.0) })/Line(Line { p0: (855.0, 865.0), p1: (855.0, 1049.0) }) = 3.4682292589173067 degrees
* uni0123 (U+0123): Quad(QuadBez { p0: (807.0, 976.5), p1: (851.0, 931.0), p2: (855.0, 865.0) })/Line(Line { p0: (855.0, 865.0), p1: (855.0, 1049.0) }) = 3.4682292589173067 degrees
* gcaron (U+01E7): Quad(QuadBez { p0: (807.0, 976.5), p1: (851.0, 931.0), p2: (855.0, 865.0) })/Line(Line { p0: (855.0, 865.0), p1: (855.0, 1049.0) }) = 3.4682292589173067 degrees
* uni01F5: Quad(QuadBez { p0: (807.0, 976.5), p1: (851.0, 931.0), p2: (855.0, 865.0) })/Line(Line { p0: (855.0, 865.0), p1: (855.0, 1049.0) }) = 3.4682292589173067 degrees
* uni1E21: Quad(QuadBez { p0: (807.0, 976.5), p1: (851.0, 931.0), p2: (855.0, 865.0) })/Line(Line { p0: (855.0, 865.0), p1: (855.0, 1049.0) }) = 3.4682292589173067 degrees
* r (U+0072): Line(Line { p0: (390.0, 1070.0), p1: (390.0, 878.0) })/Quad(QuadBez { p0: (390.0, 878.0), p1: (392.0, 929.0), p2: (414.0, 968.0) }) = 2.245742565895211 degrees
* racute (U+0155): Line(Line { p0: (390.0, 1070.0), p1: (390.0, 878.0) })/Quad(QuadBez { p0: (390.0, 878.0), p1: (392.0, 929.0), p2: (414.0, 968.0) }) = 2.245742565895211 degrees
* uni0157 (U+0157): Line(Line { p0: (390.0, 1070.0), p1: (390.0, 878.0) })/Quad(QuadBez { p0: (390.0, 878.0), p1: (392.0, 929.0), p2: (414.0, 968.0) }) = 2.245742565895211 degrees
* rcaron (U+0159): Line(Line { p0: (390.0, 1070.0), p1: (390.0, 878.0) })/Quad(QuadBez { p0: (390.0, 878.0), p1: (392.0, 929.0), p2: (414.0, 968.0) }) = 2.245742565895211 degrees
* uni1E59: Line(Line { p0: (390.0, 1070.0), p1: (390.0, 878.0) })/Quad(QuadBez { p0: (390.0, 878.0), p1: (392.0, 929.0), p2: (414.0, 968.0) }) = 2.245742565895211 degrees
* g.sups: Quad(QuadBez { p0: (539.0, 1427.0), p1: (567.0, 1401.0), p2: (570.0, 1364.0) })/Line(Line { p0: (570.0, 1364.0), p1: (570.0, 1468.0) }) = 4.635463426902618 degrees
* r.sups: Line(Line { p0: (277.0, 1463.0), p1: (277.0, 1358.0) })/Quad(QuadBez { p0: (277.0, 1358.0), p1: (279.0, 1397.0), p2: (306.0, 1423.0) }) = 2.9356734464209744 degrees
* g.subs: Quad(QuadBez { p0: (539.0, 227.0), p1: (567.0, 201.0), p2: (570.0, 164.0) })/Line(Line { p0: (570.0, 164.0), p1: (570.0, 268.0) }) = 4.635463426902618 degrees
* r.subs: Line(Line { p0: (277.0, 268.0), p1: (277.0, 162.0) })/Quad(QuadBez { p0: (277.0, 162.0), p1: (279.0, 201.0), p2: (306.0, 228.0) }) = 2.935673446421099 degrees
* uni24C2: Quad(QuadBez { p0: (1931.0, 1129.0), p1: (1931.0, 1142.0), p2: (1932.0, 1155.0) })/Line(Line { p0: (1932.0, 1155.0), p1: (1922.0, 1121.0) }) = 11.990834979039256 degrees
* M.squared: Quad(QuadBez { p0: (1922.0, 1129.0), p1: (1922.0, 1142.0), p2: (1923.0, 1155.0) })/Line(Line { p0: (1923.0, 1155.0), p1: (1913.0, 1121.0) }) = 11.990834979039256 degrees
* uni0157.ss03: Line(Line { p0: (390.0, 1070.0), p1: (390.0, 878.0) })/Quad(QuadBez { p0: (390.0, 878.0), p1: (392.0, 929.0), p2: (414.0, 968.0) }) = 2.245742565895211 degrees
* uni1E40.ss07: Quad(QuadBez { p0: (1437.0, 1129.0), p1: (1437.0, 1142.0), p2: (1438.0, 1155.0) })/Line(Line { p0: (1438.0, 1155.0), p1: (1428.0, 1121.0) }) = 11.990834979039256 degrees
* gdotaccent.ss07: Quad(QuadBez { p0: (807.0, 976.5), p1: (851.0, 931.0), p2: (855.0, 865.0) })/Line(Line { p0: (855.0, 865.0), p1: (855.0, 1049.0) }) = 3.4682292589173067 degrees
* uni1E59.ss07: Line(Line { p0: (390.0, 1070.0), p1: (390.0, 878.0) })/Quad(QuadBez { p0: (390.0, 878.0), p1: (392.0, 929.0), p2: (414.0, 968.0) }) = 2.245742565895211 degrees
* uni0157.ss07: Line(Line { p0: (390.0, 1070.0), p1: (390.0, 878.0) })/Quad(QuadBez { p0: (390.0, 878.0), p1: (392.0, 929.0), p2: (414.0, 968.0) }) = 2.245742565895211 degrees [code: found-jaggy-segments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>


> Microsoft keeps a list of font vendors and their respective contact info. This list is updated regularly and is indexed by a 4-char "Vendor ID" which is stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some applications may display the type designer / type foundry contact info on some dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in that list or if it has some of the default values used by the most common font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs. If you registered recently, you're safe to ignore warnings emitted by this check, since your ID will soon be included in one of our upcoming releases.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3943, https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** OS/2 VendorID value 'NONE' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>


</div>
</details>


<details><summary>[1] output/nevlin-google-fonts/core-latin/googlefonts/nevlinfont/NevlinFont-Regular.ttf</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>


> Microsoft keeps a list of font vendors and their respective contact info. This list is updated regularly and is indexed by a 4-char "Vendor ID" which is stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some applications may display the type designer / type foundry contact info on some dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in that list or if it has some of the default values used by the most common font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs. If you registered recently, you're safe to ignore warnings emitted by this check, since your ID will soon be included in one of our upcoming releases.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3943, https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** OS/2 VendorID value 'NONE' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>


</div>
</details>






### Summary

| ⚠️ WARN | ℹ️ INFO | ✅ PASS | ⏩ SKIP | 
| ---|---|---|---|
| 10 | 28 | 415 | 236 | 
| 1% | 4% | 60% | 34% | 



