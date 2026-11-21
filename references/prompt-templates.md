# Prompt 模板库

所有模板共用同一套「风格描述段」「禁令段」「旭日旗禁令段」，只替换 `<主体描述>` 和 `<背景方案>`。

**批量出图时，风格描述段必须逐字一致**，否则不同图片的风格会漂移。

---

## 风格描述段（★ 装备识别版 · 2026-11-21 用户七图校准，**当前默认**，逐字复制）

2026-11-21 用户给了七张参考图（M1 坦克群 / J-35 特写 / 歼-15 甲板群 / 直升机 / T-72 开火 / 055 驱逐舰 / 数码迷彩装甲车），校准出新标准：**装备保留真实外观，背景才走海报色**。与旧"高调三色"段的区别：装备不再统一画成卡其土黄，原涂装、编号、机徽直接复刻。

```text
Soviet constructivism military propaganda poster. The subject equipment is rendered as a detailed flat vector illustration with faceted geometric shading instead of gradients. Its real-world appearance is strictly preserved: original paint and camouflage colors reproduced faithfully, hull or serial numbers reproduced digit by digit in their exact positions, unit insignia and markings kept, weapon configuration and structural details intact. Highly recognizable silhouette and type — NOT abstract, NOT repainted into poster colors.

The background is fully rebuilt as bold constructivist geometric planes: large diagonal triangles, wedges and slab shapes in a strictly limited palette of vermilion red, deep black, ochre gold and cream, plus at most one scene color (muted sea blue for naval subjects, dark night green for urban night scenes). Thin gold accent lines run diagonally across the field. No sun, no moon, no circular celestial motif anywhere. Ground elements (deck, road, sea) are simplified into flat geometric shapes and markings.

Overall: flat colors with no gradients, aged beige paper texture, grainy vintage print, low horizon, equipment as the dominant subject, diagonal composition. Landscape format.
```

配套写法：

- 主体描述开头固定加 **"add nothing that is not in it"**，并点清数量——否则图生图会自作主张加装备
- 编号写成具体数字（如 `hull number 106 painted on the bow`），别写 "the number"
- 机徽写具体名称与位置（如 `PLA roundel insignia on the fuselage`）
- 需要强调识别度时加一句 `the aircraft must remain instantly recognizable as a J-15 Flying Shark`（机型按需替换）

## 风格描述段（高调三色版 · 旧默认，仅当用户明确要"装备也海报化配色"时使用）

旧版描述段偏暗（纸底叠重做旧、装备走深灰军绿），交付被用户打回。**照片转海报一律改用下面这段**；旧版仅在用户明确要求"更复古/更做旧"时使用。

```text
Soviet constructivist military propaganda poster rendered as a flat three-tone screen print on bright cream paper, 1930s Russian avant-garde style.

High-key limited palette, only four inks: bright cream paper (#F2EBDC) covering most of the frame, pure black (#14110E) for outlines and solid shadow shapes, bright vermilion red (#D8342A) for accent geometry, warm khaki tan (#C9A46B) as the single mid-tone for all vehicle bodies and equipment. No dark grey, no olive green, no dark brown, no muddy or desaturated tones.

Every object is built from exactly these values: bright cream as the highlight, khaki tan as the mid-tone body colour, pure black as the shadow side, separated by thin crisp black ink lines. No gradients, no shading, no volumetric rendering, no photorealism, no metallic reflections.

The background stays bright and airy, dominated by open cream paper, cut by one large flat vermilion-red triangular wedge entering from the left edge and a few thin straight black lines running diagonally across the open sky area.

Crisp clean modern print: minimal grain, no halftone screen visible at normal size, no grunge overlay, no weathered speckles, no vignette, no darkening at the edges. The overall image reads light, high-key and airy with large areas of bright cream.
```

配套改法：

- 主体描述里的 `grey` / `olive green` 一律换成 `khaki tan`，阴影面写 `shadow side in pure black`
- 去掉 `heavy paper grain`、`weathered speckles and scuffs`
- 主体描述开头固定加一句 **"add nothing that is not in it"**，并点清数量（几架机、几个人）——否则图生图会自作主张加背景飞机
- 全部背景方案（BG-1～BG-4）里的"黑红大色块"降权，只保留**一个**红三角楔 + 几条细黑直线，其余留亮米白

## 风格描述段（旧版 · 仅在明确要求重做旧质感时使用）

```text
Soviet constructivist military propaganda poster, 1930s Russian avant-garde screen-print style.

Render everything as flat unmodulated color blocks with hard-edged geometric shapes and bold black ink outlines, no gradients, no shading, no volumetric rendering, no photorealism, no metallic reflections.

Limited palette only: warm cream paper background (#EFE5D2), vermilion red (#D22B1E), deep black (#16130F), ochre gold (#C79131), and a small amount of steel blue (#3E6E8C).

The composition is structured by bold diagonal geometry: the cream paper field is cut by one large vermilion-red diagonal wedge and one deep-black diagonal slab, with parallel diagonal hatch lines running in a single direction and stepped geometric terraces along the lower edge. One small solid ochre-gold rectangle floats as a graphic accent.

Vintage offset print texture: visible halftone dot pattern, heavy paper grain, slight color misregistration, weathered speckles and scuffs.
```

## 禁令段（★ 修订版 · 2026-11-21，逐字复制）

旧版把"no numbers, no insignia"一刀切，会误删原照上真实存在的编号与机徽。修订版区分"真标识"与"编造字"：

```text
No invented text: no lettering, no numbers, no characters, no symbols other than the markings that exist in the original photo; those must be reproduced exactly in position and content. No watermark, no signature, no border frame, no stamp, no seal, no corner ornament, no maker mark, no invented badges.
```

**记住**：原照有的标识必须留（模型直接复刻，参考图实测 106 / 3506 / FK322 / 红星均渲染可靠）；模型自己编的字必须清。两句都要，不能只做一半。

复杂中文标识（如垂尾书法字）模型画不好时，才退回老路：prompt 里把标识位置留成干净纯色面 + 出图后用 Pillow 按实测坐标补画（见 `style-spec.md` 第 6.5 节与 `_tools/draw_bayi_insignia.py`）。

## 旭日旗专项禁令段（★ 修订版 · 2026-11-21，逐字复制，**每次生成必带**）

旧版把所有放射状光线一刀切，但用户七张参考图里存在非旗色的放射楔形与斜切光线（055 驱逐舰图最典型）。修订版只禁旭日旗构图本体：

```text
No rising-sun motif: never a red or white sun disc with rays radiating from it, no red-on-white radiating bands. Radiating wedge shapes, diagonal light planes and beam fans are allowed only in non-flag colors (black, gold, blue, cream) and only without any central disc.
```

触线判定：**红色日轮 + 放射** 或 **红白大面积放射分割** 才算旭日旗；黑/金/蓝/米白的放射几何不算。

## 背景分层句（通用，逐字复制，**每次生成必带**）

背景元素必须待在主体后方，避免压到主体上被误读成外挂装备。

```text
All background geometry stays entirely behind the subject and never overlaps it. The background elements are thin lines and hard-edged slabs placed in the upper left and lower right areas, leaving open cream paper around the subject.
```

---

## 背景方案库（选一个替换原照片的天空/背景）

照片转海报时，**原照片里的天空、墙面、杂乱背景一律替换掉**，换成下面某一种纯几何背景。

**默认选 BG-5**（2026-11-21 用户七图校准）；BG-1～BG-4 作为备选保留。

### BG-5 大块几何切面 · 场景色（★ 当前默认）

```text
Replace the entire sky and background with large bold constructivist geometric planes: two or three big diagonal triangles and wedges in vermilion red, deep black and ochre gold cutting across an open cream paper field, with at most one scene color plane between them (muted sea blue for naval subjects, dark night green for urban night scenes, warm grey for mountain scenes). Thin gold accent lines run diagonally across the field. No sun, no moon, no circular celestial motif anywhere. The ground plane (carrier deck, road, sea surface) stays as flat geometric panels with simplified painted markings. Flat solid color, hard edges, no gradient.
```

### BG-1 城市工业剪影（备选，最苏联）

```text
Replace the entire background with a hard-edged black silhouette skyline of Soviet industrial architecture — factory sheds, tall smokestacks, water towers, lattice radio masts, rooftop antenna clusters and a construction crane — sitting on a flat cream horizon line, with one solid vermilion-red rectangle floating above the rooftops and a small ochre-gold rectangle beside it. The silhouette is flat black with no interior detail, no gradient, no texture.
```

### BG-2 斜切色块 + 阶梯（构成主义最正宗）

```text
Replace the entire background with bold diagonal geometry: the upper right two-thirds is a solid vermilion-red diagonal wedge, the lower left is a deep-black diagonal slab, between them a cream paper gap, and along the bottom edge a series of stepped geometric terraces in alternating black and cream rectangles like a staircase seen in perspective. One thin ochre-gold rectangle cuts diagonally across the cream gap. Flat solid color, hard edges, no rays, no fan, no sun.
```

### BG-3 平行斜线束 + 几何山形（自然题材用）

```text
Replace the entire background with a warm cream paper field crossed by a dense band of thin parallel diagonal hatch lines in deep black, all running in exactly the same direction, and a row of sharp triangular mountain silhouettes in black and vermilion red along the lower edge. The hatch lines are parallel and never radiate from a point. One solid ochre-gold rectangle floats in the upper left. Flat solid color, hard edges, no gradient, no sun.
```

### BG-4 透视网格地面（机场/甲板题材）

```text
Replace the background sky with a flat warm cream paper field crossed by one solid deep-black diagonal slab in the upper left and one solid vermilion-red diagonal wedge in the lower right, and lay the ground plane as a geometric perspective grid of black, vermilion red and cream rectangular panels converging to a single vanishing point, with one ochre-gold line running along the centre of the grid. Flat solid color, hard edges, no rays, no fan, no sun.
```

---

## 模板 A：照片转海报（模式 A 主力）

```text
Transform this photograph into a Soviet constructivist military propaganda poster, 1930s Russian avant-garde screen-print style.

Preserve the exact subject arrangement and silhouettes of the original photo: <主体描述>

<背景方案>

<风格描述段>

<禁令段>

<旭日旗禁令段>
```

主体描述写法示例（甲板战斗机，2026-11-21 识别度版）：

```text
a large grey naval fighter jet seen from the side dominating the upper half of the frame, its nose pointing right, canopy open, folded wing and air intake geometry intact, landing gear on the deck, its fuselage number reproduced digit by digit in the exact original position, the unit insignia kept on its original spot, missiles and pylons under the wings intact, three deck crew in plain solid yellow vests and two crew in plain solid white vests standing and crouching around the nose gear with their arms raised in hand-signal gestures, the vests are plain solid color with no invented patches or lettering, the flat grey carrier deck with painted lines at the bottom, the jet must remain instantly recognizable as a J-15 Flying Shark
```

注意：主体描述里**不要写"pale hazy sky behind"**——天空一律交给背景方案处理。

---

## 模板 B：从零生成 · 地面装备（坦克/装甲车）

```text
Soviet constructivist military propaganda poster, 1930s Russian avant-garde screen-print style. A heavy Soviet battle tank charging forward from a low three-quarter angle, dust plume erupting from its tracks, rendered as flat geometric shapes with bold black ink outlines in vermilion red and ochre gold, visible rivet and armor plate geometry.

<背景方案：BG-3>

<风格描述段>

<禁令段>

<旭日旗禁令段>
```

## 模板 C：从零生成 · 空中编队

```text
Soviet constructivist military propaganda poster, 1930s Russian avant-garde screen-print style. A formation of four heavy bombers flying toward the viewer, rendered as flat geometric shapes in deep black, vermilion red and ochre gold with bold black ink outlines and hard-edged faceted forms.

<背景方案：BG-3 或 BG-4>

<风格描述段>

<禁令段>

<旭日旗禁令段>
```

## 模板 D：从零生成 · 海军

```text
Soviet constructivist military propaganda poster, 1930s Russian avant-garde screen-print style. A naval destroyer cutting through enormous stylized waves, seen from a low frontal angle. The warship rendered in flat vermilion red, deep black and cream-white geometric blocks with bold black ink outlines and hard-edged faceted forms. The sea is a deep steel-blue field broken by huge angular cream and white foam crests built from sharp triangles. Thin black horizontal dash marks suggest spray and distance.

<背景方案：BG-2>

<风格描述段>

<禁令段>

<旭日旗禁令段>
```

## 模板 E：从零生成 · 直升机

```text
Soviet constructivist military propaganda poster, 1930s Russian avant-garde screen-print style. A formation of three military helicopters flying low over a valley, seen from below so the undersides and rotor discs dominate the frame. Aircraft rendered as flat geometric shapes in deep black, vermilion red and ochre gold with bold black ink outlines, spinning rotor discs drawn as sharp blade fans. The crew are flat silhouettes with no facial features.

<背景方案：BG-3>

<风格描述段>

<禁令段>

<旭日旗禁令段>
```

## 模板 F：从零生成 · 火箭/火炮阵地

```text
Soviet constructivist military propaganda poster, 1930s Russian avant-garde screen-print style. A bank of multiple self-propelled rocket launchers on a hillside firing simultaneously, with multiple white smoke trails streaking diagonally into the sky. Launchers rendered as flat geometric shapes in deep black, vermilion red and ochre gold with bold black ink outlines and hard-edged faceted forms.

<背景方案：BG-1>

<风格描述段>

<禁令段>

<旭日旗禁令段>
```

---

## 参数配方速查

| 情况 | 参数 |
|------|------|
| 照片转海报 | `image1` + `input_fidelity: "high"` |
| 从零生成 | 不传 `image1` |
| 横构图 | `size: "1536x1024"` |
| 竖构图 | `size: "1024x1536"` |
| 方形 | `size: "1024x1024"` |
| 通用质量 | `quality: "high"` |
| **任何情况** | **必须带旭日旗专项禁令段** |
