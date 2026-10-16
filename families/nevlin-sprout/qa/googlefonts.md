## FontSpector report

fontspector version: 1.9.0






## Check results




<details><summary>[1] output/nevlin-sprout-googlefonts/googlefonts/nevlinsprout/NevlinSprout-Bold.ttf</summary>
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


<details><summary>[1] output/nevlin-sprout-googlefonts/googlefonts/nevlinsprout/NevlinSprout-Medium.ttf</summary>
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


<details><summary>[1] output/nevlin-sprout-googlefonts/googlefonts/nevlinsprout</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. (googlefonts/metadata/unreachable_subsetting)</summary>
    <div>


> This check ensures that all encoded glyphs in the font are covered by a subset declared in the METADATA.pb. Google Fonts splits the font into a set of subset fonts based on the contents of the `subsets` field and the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions will not be served in the subsetted fonts, and so will be unreachable to the end user.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4097 and https://github.com/fonttools/fontbakery/pull/4273]





- ⚠️ **WARN** output/nevlin-sprout-googlefonts/googlefonts/nevlinsprout/NevlinSprout-Bold.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, cherokee, math
* U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
* U+0307 COMBINING DOT ABOVE: try adding one of: hebrew, old-permic, math, malayalam, tai-le, canadian-aboriginal, coptic, syriac, tifinagh, todhri, duployan
* U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
* U+030C COMBINING CARON: try adding one of: cherokee, tai-le
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese
* U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese
* U+2190 LEFTWARDS ARROW: try adding one of: symbols, math
* U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols
* U+2264 LESS-THAN OR EQUAL TO: try adding math
* U+2265 GREATER-THAN OR EQUAL TO: try adding math
* U+25CC DOTTED CIRCLE: try adding one of: duployan, mahajani, buginese, saurashtra, takri, gunjala-gondi, lao, tifinagh, javanese, tai-le, balinese, caucasian-albanian, osage, tai-tham, adlam, symbols, sogdian, khudawadi, batak, dogra, kayah-li, grantha, mende-kikakui, miao, psalter-pahlavi, brahmi, sharada, hanifi-rohingya, gujarati, syriac, kannada, marchen, kaithi, bassa-vah, buhid, meetei-mayek, phags-pa, devanagari, tirhuta, newa, old-permic, music, armenian, bengali, hanunoo, canadian-aboriginal, myanmar, elbasan, khojki, limbu, thaana, mandaic, gurmukhi, chakma, cham, kharoshthi, nko, oriya, sinhala, manichaean, khmer, syloti-nagri, tai-viet, wancho, zanabazar-square, tamil, telugu, tagalog, modi, tagbanwa, coptic, thai, warang-citi, new-tai-lue, malayalam, ahom, mongolian, pahawh-hmong, lepcha, siddham, hebrew, soyombo, rejang, sundanese, tibetan, yi, bhaiksuki, masaram-gondi, math

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  


- ⚠️ **WARN** output/nevlin-sprout-googlefonts/googlefonts/nevlinsprout/NevlinSprout-Medium.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, cherokee, math
* U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
* U+0307 COMBINING DOT ABOVE: try adding one of: hebrew, old-permic, math, malayalam, tai-le, canadian-aboriginal, coptic, syriac, tifinagh, todhri, duployan
* U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
* U+030C COMBINING CARON: try adding one of: cherokee, tai-le
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese
* U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese
* U+2190 LEFTWARDS ARROW: try adding one of: symbols, math
* U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols
* U+2264 LESS-THAN OR EQUAL TO: try adding math
* U+2265 GREATER-THAN OR EQUAL TO: try adding math
* U+25CC DOTTED CIRCLE: try adding one of: duployan, mahajani, buginese, saurashtra, takri, gunjala-gondi, lao, tifinagh, javanese, tai-le, balinese, caucasian-albanian, osage, tai-tham, adlam, symbols, sogdian, khudawadi, batak, dogra, kayah-li, grantha, mende-kikakui, miao, psalter-pahlavi, brahmi, sharada, hanifi-rohingya, gujarati, syriac, kannada, marchen, kaithi, bassa-vah, buhid, meetei-mayek, phags-pa, devanagari, tirhuta, newa, old-permic, music, armenian, bengali, hanunoo, canadian-aboriginal, myanmar, elbasan, khojki, limbu, thaana, mandaic, gurmukhi, chakma, cham, kharoshthi, nko, oriya, sinhala, manichaean, khmer, syloti-nagri, tai-viet, wancho, zanabazar-square, tamil, telugu, tagalog, modi, tagbanwa, coptic, thai, warang-citi, new-tai-lue, malayalam, ahom, mongolian, pahawh-hmong, lepcha, siddham, hebrew, soyombo, rejang, sundanese, tibetan, yi, bhaiksuki, masaram-gondi, math

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  


- ⚠️ **WARN** output/nevlin-sprout-googlefonts/googlefonts/nevlinsprout/NevlinSprout-Regular.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, cherokee, math
* U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
* U+0307 COMBINING DOT ABOVE: try adding one of: hebrew, old-permic, math, malayalam, tai-le, canadian-aboriginal, coptic, syriac, tifinagh, todhri, duployan
* U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
* U+030C COMBINING CARON: try adding one of: cherokee, tai-le
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese
* U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese
* U+2190 LEFTWARDS ARROW: try adding one of: symbols, math
* U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols
* U+2264 LESS-THAN OR EQUAL TO: try adding math
* U+2265 GREATER-THAN OR EQUAL TO: try adding math
* U+25CC DOTTED CIRCLE: try adding one of: duployan, mahajani, buginese, saurashtra, takri, gunjala-gondi, lao, tifinagh, javanese, tai-le, balinese, caucasian-albanian, osage, tai-tham, adlam, symbols, sogdian, khudawadi, batak, dogra, kayah-li, grantha, mende-kikakui, miao, psalter-pahlavi, brahmi, sharada, hanifi-rohingya, gujarati, syriac, kannada, marchen, kaithi, bassa-vah, buhid, meetei-mayek, phags-pa, devanagari, tirhuta, newa, old-permic, music, armenian, bengali, hanunoo, canadian-aboriginal, myanmar, elbasan, khojki, limbu, thaana, mandaic, gurmukhi, chakma, cham, kharoshthi, nko, oriya, sinhala, manichaean, khmer, syloti-nagri, tai-viet, wancho, zanabazar-square, tamil, telugu, tagalog, modi, tagbanwa, coptic, thai, warang-citi, new-tai-lue, malayalam, ahom, mongolian, pahawh-hmong, lepcha, siddham, hebrew, soyombo, rejang, sundanese, tibetan, yi, bhaiksuki, masaram-gondi, math

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  


- ⚠️ **WARN** output/nevlin-sprout-googlefonts/googlefonts/nevlinsprout/NevlinSprout-SemiBold.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, cherokee, math
* U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
* U+0307 COMBINING DOT ABOVE: try adding one of: hebrew, old-permic, math, malayalam, tai-le, canadian-aboriginal, coptic, syriac, tifinagh, todhri, duployan
* U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
* U+030C COMBINING CARON: try adding one of: cherokee, tai-le
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese
* U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese
* U+2190 LEFTWARDS ARROW: try adding one of: symbols, math
* U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols
* U+2264 LESS-THAN OR EQUAL TO: try adding math
* U+2265 GREATER-THAN OR EQUAL TO: try adding math
* U+25CC DOTTED CIRCLE: try adding one of: duployan, mahajani, buginese, saurashtra, takri, gunjala-gondi, lao, tifinagh, javanese, tai-le, balinese, caucasian-albanian, osage, tai-tham, adlam, symbols, sogdian, khudawadi, batak, dogra, kayah-li, grantha, mende-kikakui, miao, psalter-pahlavi, brahmi, sharada, hanifi-rohingya, gujarati, syriac, kannada, marchen, kaithi, bassa-vah, buhid, meetei-mayek, phags-pa, devanagari, tirhuta, newa, old-permic, music, armenian, bengali, hanunoo, canadian-aboriginal, myanmar, elbasan, khojki, limbu, thaana, mandaic, gurmukhi, chakma, cham, kharoshthi, nko, oriya, sinhala, manichaean, khmer, syloti-nagri, tai-viet, wancho, zanabazar-square, tamil, telugu, tagalog, modi, tagbanwa, coptic, thai, warang-citi, new-tai-lue, malayalam, ahom, mongolian, pahawh-hmong, lepcha, siddham, hebrew, soyombo, rejang, sundanese, tibetan, yi, bhaiksuki, masaram-gondi, math

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  

</div>
</details>


</div>
</details>


<details><summary>[1] output/nevlin-sprout-googlefonts/googlefonts/nevlinsprout/NevlinSprout-Regular.ttf</summary>
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


<details><summary>[1] output/nevlin-sprout-googlefonts/googlefonts/nevlinsprout/NevlinSprout-SemiBold.ttf</summary>
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
| 8 | 26 | 407 | 248 | 
| 1% | 4% | 59% | 36% | 



