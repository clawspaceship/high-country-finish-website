import re, sys

PATH = r'C:\Users\Spaceship\.openclaw\workspace\vinyl-website\index.html'

with open(PATH, 'r', encoding='utf-8') as f:
    content = f.read()

original = content  # keep for diff check

# ─────────────────────────────────────────────────────────────────────────────
# CHANGE 1a: Remove novara-waiting-area.jpg from portfolio-full Novara card
# ─────────────────────────────────────────────────────────────────────────────
old = (
    '        <div class="pf-photo-cell" onclick="openGroupModal(this)">\n'
    '          <img src="images/novara-waiting-area.jpg"\n'
    '               alt="Novara waiting area wall graphics Denver office interior vinyl installation"\n'
    '               loading="lazy"/>\n'
    '          <div class="pf-photo-overlay"></div>\n'
    '          <div class="pf-caption">Waiting Area Graphics</div>\n'
    '        </div>\n'
)
assert old in content, "FAIL: novara-waiting-area block not found"
content = content.replace(old, '', 1)
print("✓ CHANGE 1a: removed novara-waiting-area.jpg")

# ─────────────────────────────────────────────────────────────────────────────
# CHANGE 1b: Remove directory-sign.jpg from portfolio-full Office Directory card
#            and change grid from cols-2 to cols-1
# ─────────────────────────────────────────────────────────────────────────────
old = (
    '        <div class="pf-photo-cell" onclick="openGroupModal(this)">\n'
    '          <img src="images/directory-sign.jpg"\n'
    '               alt="Office directory sign installation Denver — interior wayfinding and suite signage"\n'
    '               loading="lazy"/>\n'
    '          <div class="pf-photo-overlay"></div>\n'
    '          <div class="pf-caption">Directory Sign</div>\n'
    '        </div>\n'
)
assert old in content, "FAIL: directory-sign block not found"
content = content.replace(old, '', 1)
print("✓ CHANGE 1b: removed directory-sign.jpg")

# Fix the grid class for Office Directory (now only 1 photo)
old_grid = (
    '    <!-- ── 18. Office Directory ── -->\n'
    '    <div class="pf-project reveal">\n'
    '      <div class="pf-project-header">\n'
    '        <span class="pf-project-name">Office Directory</span>\n'
    '      </div>\n'
    '      <div class="pf-photos-grid cols-2">'
)
new_grid = (
    '    <!-- ── 18. Office Directory ── -->\n'
    '    <div class="pf-project reveal">\n'
    '      <div class="pf-project-header">\n'
    '        <span class="pf-project-name">Office Directory</span>\n'
    '      </div>\n'
    '      <div class="pf-photos-grid cols-1">'
)
assert old_grid in content, "FAIL: Office Directory cols-2 grid not found"
content = content.replace(old_grid, new_grid, 1)
print("✓ CHANGE 1c: Office Directory grid updated to cols-1")

# ─────────────────────────────────────────────────────────────────────────────
# CHANGE 2: Add cybertruck-front.jpg to Vehicle Wraps (after cybertruck-side)
#           and update group-grid from cols-2 to default (3-col)
# ─────────────────────────────────────────────────────────────────────────────
old_cy = (
    '        <div class="group-item" onclick="openGroupModal(this)">\n'
    '          <img src="images/cybertruck-side.jpg"\n'
    '               alt="Cybertruck commercial vehicle graphics Denver — Black Rock Vinyl lettering and body wrap"\n'
    '               loading="lazy"/>\n'
    '          <div class="group-item-overlay">\n'
    '            <span class="group-item-caption">Cybertruck — Black Rock Vinyl Lettering</span>\n'
    '          </div>\n'
    '        </div>'
)
new_cy = (
    '        <div class="group-item" onclick="openGroupModal(this)">\n'
    '          <img src="images/cybertruck-side.jpg"\n'
    '               alt="Cybertruck commercial vehicle graphics Denver — Black Rock Vinyl lettering and body wrap"\n'
    '               loading="lazy"/>\n'
    '          <div class="group-item-overlay">\n'
    '            <span class="group-item-caption">Cybertruck — Black Rock Vinyl Lettering</span>\n'
    '          </div>\n'
    '        </div>\n'
    '\n'
    '        <div class="group-item" onclick="openGroupModal(this)">\n'
    '          <img src="images/cybertruck-front.jpg"\n'
    '               alt="Cybertruck vehicle wrap installation - Black Rock vinyl lettering front view Denver"\n'
    '               loading="lazy"/>\n'
    '          <div class="group-item-overlay">\n'
    '            <span class="group-item-caption">Cybertruck — Black Rock Front</span>\n'
    '          </div>\n'
    '        </div>'
)
assert old_cy in content, "FAIL: cybertruck-side gallery block not found"
content = content.replace(old_cy, new_cy, 1)
print("✓ CHANGE 2: added cybertruck-front.jpg to Vehicle Wraps")

# Change Vehicle Wraps grid from cols-2 to default (3-col) since now 3 items
old_vw_grid = (
    '    <!-- Group 1: Vehicle Wraps -->\n'
    '    <div class="gallery-group reveal">\n'
    '      <div class="gallery-group-title">Vehicle Wraps</div>\n'
    '      <div class="group-grid cols-2">'
)
new_vw_grid = (
    '    <!-- Group 1: Vehicle Wraps -->\n'
    '    <div class="gallery-group reveal">\n'
    '      <div class="gallery-group-title">Vehicle Wraps</div>\n'
    '      <div class="group-grid">'
)
assert old_vw_grid in content, "FAIL: Vehicle Wraps group-grid cols-2 not found"
content = content.replace(old_vw_grid, new_vw_grid, 1)
print("✓ CHANGE 2b: Vehicle Wraps grid updated to 3-col")

# ─────────────────────────────────────────────────────────────────────────────
# CHANGE 3: Replace Elevator & Building Wraps group with Custom & Specialty Installs
# ─────────────────────────────────────────────────────────────────────────────
old_elev = (
    '    <!-- Group 4: Elevator & Building Wraps -->\n'
    '    <div class="gallery-group reveal">\n'
    '      <div class="gallery-group-title">Elevator &amp; Building Wraps</div>\n'
    '      <div class="group-grid cols-1">\n'
    '\n'
    '        <div class="group-item" onclick="openGroupModal(this)">\n'
    '          <img src="images/iheart-elevator-wrap.jpg"\n'
    '               alt="iHeartMedia elevator wrap installation Denver — commercial vinyl elevator door graphics"\n'
    '               loading="lazy"/>\n'
    '          <div class="group-item-overlay">\n'
    '            <span class="group-item-caption">iHeartMedia — Elevator Wrap</span>\n'
    '          </div>\n'
    '        </div>\n'
    '\n'
    '      </div>\n'
    '    </div>'
)
new_elev = (
    '    <!-- Group 4: Custom & Specialty Installs -->\n'
    '    <div class="gallery-group reveal">\n'
    '      <div class="gallery-group-title">Custom &amp; Specialty Installs</div>\n'
    '      <div class="group-grid cols-1">\n'
    '\n'
    '        <div class="group-item" onclick="openGroupModal(this)">\n'
    '          <img src="images/iheart-elevator-wrap.jpg"\n'
    '               alt="iHeartMedia elevator wrap installation Denver — commercial vinyl elevator door graphics"\n'
    '               loading="lazy"/>\n'
    '          <div class="group-item-overlay">\n'
    '            <span class="group-item-caption">iHeartMedia — Custom Elevator Door Wrap</span>\n'
    '          </div>\n'
    '        </div>\n'
    '\n'
    '      </div>\n'
    '    </div>'
)
assert old_elev in content, "FAIL: Elevator & Building Wraps group not found"
content = content.replace(old_elev, new_elev, 1)
print("✓ CHANGE 3: Renamed Elevator group → Custom & Specialty Installs, updated caption")

# ─────────────────────────────────────────────────────────────────────────────
# CHANGE 4: Add Window Film & Frosting placeholder group (between Custom group and Exterior Signage)
# ─────────────────────────────────────────────────────────────────────────────
window_film_gallery = (
    '\n'
    '    <!-- Group 4b: Window Film & Frosting -->\n'
    '    <div class="gallery-group reveal">\n'
    '      <div class="gallery-group-title">Window Film &amp; Frosting</div>\n'
    '      <div class="gallery-coming-soon">Portfolio photos coming soon</div>\n'
    '    </div>\n'
)
old_ext = '    <!-- Group 5: Exterior Signage -->'
assert old_ext in content, "FAIL: Group 5 Exterior Signage comment not found"
content = content.replace(old_ext, window_film_gallery + old_ext, 1)
print("✓ CHANGE 4: added Window Film & Frosting placeholder group")

# ─────────────────────────────────────────────────────────────────────────────
# CHANGE 5: Add gym-wall-mural.jpg and childrens-museum-artstudio.jpg to Wall Murals & Graphics
# ─────────────────────────────────────────────────────────────────────────────
old_gque = (
    '        <div class="group-item" onclick="openGroupModal(this)">\n'
    '          <img src="images/gque-bbq-mural.jpg"\n'
    '               alt="GQue BBQ large format wall mural installation Denver — restaurant interior branded graphics"\n'
    '               loading="lazy"/>\n'
    '          <div class="group-item-overlay">\n'
    '            <span class="group-item-caption">GQue BBQ — Large Format Wall Mural</span>\n'
    '          </div>\n'
    '        </div>\n'
    '\n'
    '      </div>\n'
    '    </div>\n'
    '\n'
    '    <!-- Group 4: Custom & Specialty Installs -->'
)
new_gque = (
    '        <div class="group-item" onclick="openGroupModal(this)">\n'
    '          <img src="images/gque-bbq-mural.jpg"\n'
    '               alt="GQue BBQ large format wall mural installation Denver — restaurant interior branded graphics"\n'
    '               loading="lazy"/>\n'
    '          <div class="group-item-overlay">\n'
    '            <span class="group-item-caption">GQue BBQ — Large Format Wall Mural</span>\n'
    '          </div>\n'
    '        </div>\n'
    '\n'
    '        <div class="group-item" onclick="openGroupModal(this)">\n'
    '          <img src="images/gym-wall-mural.jpg"\n'
    '               alt="large format wall mural installation Denver - commercial gym vinyl graphics"\n'
    '               loading="lazy"/>\n'
    '          <div class="group-item-overlay">\n'
    '            <span class="group-item-caption">Commercial Gym — Large Format Wall Mural</span>\n'
    '          </div>\n'
    '        </div>\n'
    '\n'
    '        <div class="group-item" onclick="openGroupModal(this)">\n'
    '          <img src="images/childrens-museum-artstudio.jpg"\n'
    '               alt="dimensional letter installation Denver - Children\'s Museum art studio wall graphics"\n'
    '               loading="lazy"/>\n'
    '          <div class="group-item-overlay">\n'
    '            <span class="group-item-caption">Children\'s Museum — Art Studio Dimensional Letters</span>\n'
    '          </div>\n'
    '        </div>\n'
    '\n'
    '      </div>\n'
    '    </div>\n'
    '\n'
    '    <!-- Group 4: Custom & Specialty Installs -->'
)
assert old_gque in content, "FAIL: GQue BBQ end-of-wall-murals block not found"
content = content.replace(old_gque, new_gque, 1)
print("✓ CHANGE 5: added gym-wall-mural.jpg and childrens-museum-artstudio.jpg to Wall Murals")

# ─────────────────────────────────────────────────────────────────────────────
# CHANGE 6a: Add "Custom & Specialty" label before iHeartMedia card in portfolio-full
# ─────────────────────────────────────────────────────────────────────────────
old_iheart_comment = '    <!-- ── 7. iHeartMedia ── -->'
new_iheart_comment = (
    '    <!-- ── Custom & Specialty ── -->\n'
    '    <div class="pf-category-label reveal">\n'
    '      <div class="pf-category-heading">Custom &amp; Specialty</div>\n'
    '    </div>\n'
    '\n'
    '    <!-- ── 7. iHeartMedia ── -->'
)
assert old_iheart_comment in content, "FAIL: iHeartMedia portfolio-full comment not found"
content = content.replace(old_iheart_comment, new_iheart_comment, 1)
print("✓ CHANGE 6a: added Custom & Specialty label before iHeartMedia in portfolio-full")

# ─────────────────────────────────────────────────────────────────────────────
# CHANGE 6b: Add Window Film & Frosting placeholder project card after KPA (before Westbound)
# ─────────────────────────────────────────────────────────────────────────────
window_film_pf = (
    '\n'
    '    <!-- ── Window Film & Frosting (placeholder) ── -->\n'
    '    <div class="pf-project reveal">\n'
    '      <div class="pf-project-header">\n'
    '        <span class="pf-project-name">Window Film &amp; Frosting</span>\n'
    '      </div>\n'
    '      <div class="pf-photos-grid cols-1">\n'
    '        <div class="pf-photo-cell pf-coming-soon-cell">\n'
    '          <div class="pf-coming-soon-text">Coming soon — portfolio photos being added</div>\n'
    '        </div>\n'
    '      </div>\n'
    '    </div>\n'
)
old_westbound = '    <!-- ── 15. Westbound & Down Brewing ── -->'
assert old_westbound in content, "FAIL: Westbound comment not found"
content = content.replace(old_westbound, window_film_pf + old_westbound, 1)
print("✓ CHANGE 6b: added Window Film & Frosting placeholder card in portfolio-full")

# ─────────────────────────────────────────────────────────────────────────────
# CSS: Add gallery-coming-soon CSS to gallery style block
# ─────────────────────────────────────────────────────────────────────────────
gallery_css_anchor = (
    '.group-item-caption {\n'
    '  font-size: 13px;\n'
    '  font-weight: 500;\n'
    '  color: #fff;\n'
    '  letter-spacing: .4px;\n'
    '  line-height: 1.4;\n'
    '}\n'
    '</style>'
)
gallery_css_new = (
    '.group-item-caption {\n'
    '  font-size: 13px;\n'
    '  font-weight: 500;\n'
    '  color: #fff;\n'
    '  letter-spacing: .4px;\n'
    '  line-height: 1.4;\n'
    '}\n'
    '\n'
    '/* ── Gallery coming-soon placeholder (scoped) ─────────────────────── */\n'
    '.gallery-coming-soon {\n'
    '  padding: 48px 24px;\n'
    '  border: 1px dashed rgba(201,168,76,.25);\n'
    '  border-radius: 4px;\n'
    '  color: #888880;\n'
    '  font-size: 14px;\n'
    '  font-style: italic;\n'
    '  letter-spacing: 0.3px;\n'
    '  text-align: center;\n'
    '  background: rgba(28,28,28,.5);\n'
    '}\n'
    '</style>'
)
assert gallery_css_anchor in content, "FAIL: gallery CSS anchor not found"
content = content.replace(gallery_css_anchor, gallery_css_new, 1)
print("✓ CSS: added .gallery-coming-soon styles to gallery style block")

# ─────────────────────────────────────────────────────────────────────────────
# CSS: Add portfolio-full scoped CSS for coming-soon and category heading
# ─────────────────────────────────────────────────────────────────────────────
pf_css_anchor = (
    '/* CTA at bottom */\n'
    '#portfolio-full .pf-cta {\n'
    '  text-align: center;\n'
    '  margin-top: 32px;\n'
    '}\n'
    '</style>\n'
    '\n'
    '<section id="portfol'
)
pf_css_new = (
    '/* CTA at bottom */\n'
    '#portfolio-full .pf-cta {\n'
    '  text-align: center;\n'
    '  margin-top: 32px;\n'
    '}\n'
    '\n'
    '/* ── Coming-soon cell (scoped to portfolio-full) ──────────────────── */\n'
    '#portfolio-full .pf-coming-soon-cell {\n'
    '  cursor: default;\n'
    '  min-height: 120px;\n'
    '  display: flex;\n'
    '  align-items: center;\n'
    '  justify-content: center;\n'
    '  background: #1c1c1c;\n'
    '}\n'
    '#portfolio-full .pf-coming-soon-cell:hover img { transform: none; }\n'
    '#portfolio-full .pf-coming-soon-text {\n'
    '  color: #888880;\n'
    '  font-size: 14px;\n'
    '  font-style: italic;\n'
    '  letter-spacing: 0.3px;\n'
    '  padding: 32px;\n'
    '  text-align: center;\n'
    '}\n'
    '\n'
    '/* ── Category heading label (scoped to portfolio-full) ────────────── */\n'
    '#portfolio-full .pf-category-label {\n'
    '  margin-bottom: 32px;\n'
    '  margin-top: 8px;\n'
    '}\n'
    '#portfolio-full .pf-category-heading {\n'
    '  font-family: \'Cormorant Garamond\', serif;\n'
    '  font-size: 18px;\n'
    '  font-weight: 600;\n'
    '  color: #C9A84C;\n'
    '  letter-spacing: 0.06em;\n'
    '  text-transform: uppercase;\n'
    '  padding-bottom: 10px;\n'
    '  border-bottom: 1px solid rgba(201,168,76,.25);\n'
    '  display: flex;\n'
    '  align-items: center;\n'
    '  gap: 12px;\n'
    '}\n'
    '#portfolio-full .pf-category-heading::before {\n'
    '  content: \'\';\n'
    '  display: inline-block;\n'
    '  width: 28px;\n'
    '  height: 2px;\n'
    '  background: #C9A84C;\n'
    '  flex-shrink: 0;\n'
    '}\n'
    '</style>\n'
    '\n'
    '<section id="portfol'
)
assert pf_css_anchor in content, "FAIL: portfolio-full CSS anchor not found"
content = content.replace(pf_css_anchor, pf_css_new, 1)
print("✓ CSS: added coming-soon and category heading styles to portfolio-full style block")

# ─────────────────────────────────────────────────────────────────────────────
# Write output
# ─────────────────────────────────────────────────────────────────────────────
with open(PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ All changes written to index.html successfully.")
print(f"   Characters changed: {len(content) - len(original):+,}")
