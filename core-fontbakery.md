## FontBakery report

fontbakery version: 1.1.0







## Check results



<details><summary>[4] NevlinFont-Bold.ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> METADATA.pb: Designers are listed correctly on the Google Fonts catalog? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-designer-profiles">googlefonts/metadata/designer_profiles</a></summary>
    <div>


> 
> Google Fonts has a catalog of designers.
> 
> This check ensures that the online entries of the catalog can be found based
> on the designer names listed on the METADATA.pb file.
> 
> It also validates the URLs and file formats are all correctly set.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3083





* ⚠️ **WARN** <p>It seems that Nevlin is still not listed on the designers catalog. Please submit a photo and a link to a webpage where people can learn more about the work of this designer/typefoundry.</p>
 [code: profile-not-found]



* ⚠️ **WARN** <p>It seems that Rasmus Andersson is still not listed on the designers catalog. Please submit a photo and a link to a webpage where people can learn more about the work of this designer/typefoundry.</p>
 [code: profile-not-found]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>


> 
> This check ensures that all encoded glyphs in the font are covered by a
> subset declared in the METADATA.pb. Google Fonts splits the font into
> a set of subset fonts based on the contents of the `subsets` field and
> the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions
> will not be served in the subsetted fonts, and so will be unreachable to
> the end user.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4097
> See also: https://github.com/fonttools/fontbakery/pull/4273





* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, cherokee, coptic, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: coptic, tai-le, malayalam, hebrew, old-permic, syriac, canadian-aboriginal, tifinagh, math, duployan, todhri</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math
7 more.</li>
</ul>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>latin</code>, <code>latin-ext</code>, <code>menu</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>


> 
> This check heuristically detects outline segments which form a particularly
> small angle, indicative of an outline error. This may cause false positives
> in cases such as extreme ink traps, so should be regarded as advisory and
> backed up by manual inspection.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3064





* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* M (U+004D): B&lt;&lt;1437.0,1129.0&gt;-&lt;1437.0,1142.0&gt;-&lt;1438.0,1155.0&gt;&gt;/L&lt;&lt;1438.0,1155.0&gt;--&lt;1428.0,1121.0&gt;&gt; = 11.990834979039256

* M.squared: B&lt;&lt;1922.0,1129.0&gt;-&lt;1922.0,1142.0&gt;-&lt;1923.0,1155.0&gt;&gt;/L&lt;&lt;1923.0,1155.0&gt;--&lt;1913.0,1121.0&gt;&gt; = 11.990834979039256

* g (U+0067): B&lt;&lt;807.0,976.5&gt;-&lt;851.0,931.0&gt;-&lt;855.0,865.0&gt;&gt;/L&lt;&lt;855.0,865.0&gt;--&lt;855.0,1049.0&gt;&gt; = 3.468229258917096

* g.subs: B&lt;&lt;539.0,227.0&gt;-&lt;567.0,201.0&gt;-&lt;570.0,164.0&gt;&gt;/L&lt;&lt;570.0,164.0&gt;--&lt;570.0,268.0&gt;&gt; = 4.635463426902618

* g.sups: B&lt;&lt;539.0,1427.0&gt;-&lt;567.0,1401.0&gt;-&lt;570.0,1364.0&gt;&gt;/L&lt;&lt;570.0,1364.0&gt;--&lt;570.0,1468.0&gt;&gt; = 4.635463426902618

* gbar (U+01E5): B&lt;&lt;807.0,976.5&gt;-&lt;851.0,931.0&gt;-&lt;855.0,865.0&gt;&gt;/L&lt;&lt;855.0,865.0&gt;--&lt;855.0,1049.0&gt;&gt; = 3.468229258917096

* gbreve (U+011F): B&lt;&lt;807.0,976.5&gt;-&lt;851.0,931.0&gt;-&lt;855.0,865.0&gt;&gt;/L&lt;&lt;855.0,865.0&gt;--&lt;855.0,1049.0&gt;&gt; = 3.468229258917096

* gcaron (U+01E7): B&lt;&lt;807.0,976.5&gt;-&lt;851.0,931.0&gt;-&lt;855.0,865.0&gt;&gt;/L&lt;&lt;855.0,865.0&gt;--&lt;855.0,1049.0&gt;&gt; = 3.468229258917096

* gcircumflex: B&lt;&lt;807.0,976.5&gt;-&lt;851.0,931.0&gt;-&lt;855.0,865.0&gt;&gt;/L&lt;&lt;855.0,865.0&gt;--&lt;855.0,1049.0&gt;&gt; = 3.468229258917096

* gdotaccent (U+0121): B&lt;&lt;807.0,976.5&gt;-&lt;851.0,931.0&gt;-&lt;855.0,865.0&gt;&gt;/L&lt;&lt;855.0,865.0&gt;--&lt;855.0,1049.0&gt;&gt; = 3.468229258917096

* 18 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>


> 
> Microsoft keeps a list of font vendors and their respective contact info. This
> list is updated regularly and is indexed by a 4-char "Vendor ID" which is
> stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some
> applications may display the type designer / type foundry contact info on some
> dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in
> that list or if it has some of the default values used by the most common
> font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs.
> If you registered recently, you're safe to ignore warnings emitted by this
> check, since your ID will soon be included in one of our upcoming releases.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3943
> See also: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[3] NevlinFont-Medium.ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> METADATA.pb: Designers are listed correctly on the Google Fonts catalog? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-designer-profiles">googlefonts/metadata/designer_profiles</a></summary>
    <div>


> 
> Google Fonts has a catalog of designers.
> 
> This check ensures that the online entries of the catalog can be found based
> on the designer names listed on the METADATA.pb file.
> 
> It also validates the URLs and file formats are all correctly set.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3083





* ⚠️ **WARN** <p>It seems that Nevlin is still not listed on the designers catalog. Please submit a photo and a link to a webpage where people can learn more about the work of this designer/typefoundry.</p>
 [code: profile-not-found]



* ⚠️ **WARN** <p>It seems that Rasmus Andersson is still not listed on the designers catalog. Please submit a photo and a link to a webpage where people can learn more about the work of this designer/typefoundry.</p>
 [code: profile-not-found]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>


> 
> This check ensures that all encoded glyphs in the font are covered by a
> subset declared in the METADATA.pb. Google Fonts splits the font into
> a set of subset fonts based on the contents of the `subsets` field and
> the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions
> will not be served in the subsetted fonts, and so will be unreachable to
> the end user.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4097
> See also: https://github.com/fonttools/fontbakery/pull/4273





* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, cherokee, coptic, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: coptic, tai-le, malayalam, hebrew, old-permic, syriac, canadian-aboriginal, tifinagh, math, duployan, todhri</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math
7 more.</li>
</ul>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>latin</code>, <code>latin-ext</code>, <code>menu</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>


> 
> Microsoft keeps a list of font vendors and their respective contact info. This
> list is updated regularly and is indexed by a 4-char "Vendor ID" which is
> stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some
> applications may display the type designer / type foundry contact info on some
> dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in
> that list or if it has some of the default values used by the most common
> font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs.
> If you registered recently, you're safe to ignore warnings emitted by this
> check, since your ID will soon be included in one of our upcoming releases.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3943
> See also: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[3] NevlinFont-Regular.ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> METADATA.pb: Designers are listed correctly on the Google Fonts catalog? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-designer-profiles">googlefonts/metadata/designer_profiles</a></summary>
    <div>


> 
> Google Fonts has a catalog of designers.
> 
> This check ensures that the online entries of the catalog can be found based
> on the designer names listed on the METADATA.pb file.
> 
> It also validates the URLs and file formats are all correctly set.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3083





* ⚠️ **WARN** <p>It seems that Nevlin is still not listed on the designers catalog. Please submit a photo and a link to a webpage where people can learn more about the work of this designer/typefoundry.</p>
 [code: profile-not-found]



* ⚠️ **WARN** <p>It seems that Rasmus Andersson is still not listed on the designers catalog. Please submit a photo and a link to a webpage where people can learn more about the work of this designer/typefoundry.</p>
 [code: profile-not-found]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>


> 
> This check ensures that all encoded glyphs in the font are covered by a
> subset declared in the METADATA.pb. Google Fonts splits the font into
> a set of subset fonts based on the contents of the `subsets` field and
> the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions
> will not be served in the subsetted fonts, and so will be unreachable to
> the end user.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4097
> See also: https://github.com/fonttools/fontbakery/pull/4273





* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, cherokee, coptic, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: coptic, tai-le, malayalam, hebrew, old-permic, syriac, canadian-aboriginal, tifinagh, math, duployan, todhri</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math
7 more.</li>
</ul>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>latin</code>, <code>latin-ext</code>, <code>menu</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>


> 
> Microsoft keeps a list of font vendors and their respective contact info. This
> list is updated regularly and is indexed by a 4-char "Vendor ID" which is
> stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some
> applications may display the type designer / type foundry contact info on some
> dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in
> that list or if it has some of the default values used by the most common
> font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs.
> If you registered recently, you're safe to ignore warnings emitted by this
> check, since your ID will soon be included in one of our upcoming releases.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3943
> See also: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[4] NevlinFont-SemiBold.ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> METADATA.pb: Designers are listed correctly on the Google Fonts catalog? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-designer-profiles">googlefonts/metadata/designer_profiles</a></summary>
    <div>


> 
> Google Fonts has a catalog of designers.
> 
> This check ensures that the online entries of the catalog can be found based
> on the designer names listed on the METADATA.pb file.
> 
> It also validates the URLs and file formats are all correctly set.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3083





* ⚠️ **WARN** <p>It seems that Nevlin is still not listed on the designers catalog. Please submit a photo and a link to a webpage where people can learn more about the work of this designer/typefoundry.</p>
 [code: profile-not-found]



* ⚠️ **WARN** <p>It seems that Rasmus Andersson is still not listed on the designers catalog. Please submit a photo and a link to a webpage where people can learn more about the work of this designer/typefoundry.</p>
 [code: profile-not-found]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>


> 
> This check ensures that all encoded glyphs in the font are covered by a
> subset declared in the METADATA.pb. Google Fonts splits the font into
> a set of subset fonts based on the contents of the `subsets` field and
> the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions
> will not be served in the subsetted fonts, and so will be unreachable to
> the end user.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4097
> See also: https://github.com/fonttools/fontbakery/pull/4273





* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, cherokee, coptic, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: coptic, tai-le, malayalam, hebrew, old-permic, syriac, canadian-aboriginal, tifinagh, math, duployan, todhri</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math
7 more.</li>
</ul>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>latin</code>, <code>latin-ext</code>, <code>menu</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>


> 
> This check heuristically detects outline segments which form a particularly
> small angle, indicative of an outline error. This may cause false positives
> in cases such as extreme ink traps, so should be regarded as advisory and
> backed up by manual inspection.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3064





* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* r (U+0072): L&lt;&lt;349.0,1070.0&gt;--&lt;349.0,851.0&gt;&gt;/B&lt;&lt;349.0,851.0&gt;-&lt;360.0,942.0&gt;-&lt;410.0,998.0&gt;&gt; = 6.892423122485113

* r.subs: L&lt;&lt;252.0,267.0&gt;--&lt;252.0,145.0&gt;&gt;/B&lt;&lt;252.0,145.0&gt;-&lt;260.0,196.0&gt;-&lt;294.5,227.0&gt;&gt; = 8.914926957147863

* r.sups: L&lt;&lt;252.0,1462.0&gt;--&lt;252.0,1341.0&gt;&gt;/B&lt;&lt;252.0,1341.0&gt;-&lt;260.0,1391.0&gt;-&lt;294.5,1422.0&gt;&gt; = 9.090276920822312

* racute (U+0155): L&lt;&lt;349.0,1070.0&gt;--&lt;349.0,851.0&gt;&gt;/B&lt;&lt;349.0,851.0&gt;-&lt;360.0,942.0&gt;-&lt;410.0,998.0&gt;&gt; = 6.892423122485113

* rcaron (U+0159): L&lt;&lt;349.0,1070.0&gt;--&lt;349.0,851.0&gt;&gt;/B&lt;&lt;349.0,851.0&gt;-&lt;360.0,942.0&gt;-&lt;410.0,998.0&gt;&gt; = 6.892423122485113

* uni0157 (U+0157): L&lt;&lt;349.0,1070.0&gt;--&lt;349.0,851.0&gt;&gt;/B&lt;&lt;349.0,851.0&gt;-&lt;360.0,942.0&gt;-&lt;410.0,998.0&gt;&gt; = 6.892423122485113

* uni0157.ss03: L&lt;&lt;349.0,1070.0&gt;--&lt;349.0,851.0&gt;&gt;/B&lt;&lt;349.0,851.0&gt;-&lt;360.0,942.0&gt;-&lt;410.0,998.0&gt;&gt; = 6.892423122485113

* uni0157.ss07: L&lt;&lt;349.0,1070.0&gt;--&lt;349.0,851.0&gt;&gt;/B&lt;&lt;349.0,851.0&gt;-&lt;360.0,942.0&gt;-&lt;410.0,998.0&gt;&gt; = 6.892423122485113

* uni1E59.ss07: L&lt;&lt;349.0,1070.0&gt;--&lt;349.0,851.0&gt;&gt;/B&lt;&lt;349.0,851.0&gt;-&lt;360.0,942.0&gt;-&lt;410.0,998.0&gt;&gt; = 6.892423122485113

* uni1E59: L&lt;&lt;349.0,1070.0&gt;--&lt;349.0,851.0&gt;&gt;/B&lt;&lt;349.0,851.0&gt;-&lt;360.0,942.0&gt;-&lt;410.0,998.0&gt;&gt; = 6.892423122485113
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>


> 
> Microsoft keeps a list of font vendors and their respective contact info. This
> list is updated regularly and is indexed by a 4-char "Vendor ID" which is
> stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some
> applications may display the type designer / type foundry contact info on some
> dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in
> that list or if it has some of the default values used by the most common
> font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs.
> If you registered recently, you're safe to ignore warnings emitted by this
> check, since your ID will soon be included in one of our upcoming releases.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3943
> See also: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 14 | 239 | 29 | 611 | 0 | 
| 0% | 0% | 0% | 2% | 27% | 3% | 68% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
