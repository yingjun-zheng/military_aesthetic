# Prompt 模板库

所有模板共用同一套「风格描述段」「禁令段」「反旭日禁令段」，只替换 `<主体描述>` 和 `<背景方案>`。

**批量出图时，风格描述段必须逐字一致**，否则不同图片的风格会漂移。

---

## 风格描述段（通用，逐字复制）

```text
Soviet constructivist military propaganda poster, 1930s Russian avant-garde screen-print style.

Render everything as flat unmodulated color blocks with hard-edged geometric shapes and bold black ink outlines, no gradients, no shading, no volumetric rendering, no photorealism, no metallic reflections.

Limited palette only: warm cream paper background (#EFE5D2), vermilion red (#D22B1E), deep black (#16130F), ochre gold (#C79131), and a small amount of steel blue (#3E6E8C).

The composition is structured by bold diagonal geometry: the cream paper field is cut by one large vermilion-red diagonal wedge and one deep-black diagonal slab, with parallel diagonal hatch lines running in a single direction and stepped geometric terraces along the lower edge. One small solid ochre-gold rectangle floats as a graphic accent.

Vintage offset print texture: visible halftone dot pattern, heavy paper grain, slight color misregistration, weathered speckles and scuffs.
```

## 禁令段（通用，逐字复制）

```text
Pure poster artwork, absolutely no text, no lettering, no numbers, no characters, no symbols, no writing of any kind on any surface, no watermark, no signature, no border frame, no patches, no badges, no uniform markings, no chest lettering, no insignia.
```

## 反旭日禁令段（通用，逐字复制，**每次生成必带**）

```text
No sunburst, no radiating rays, no rays from a single point, no fan of light, no sun, no circular emblem, no badge, no rising-sun motif, no radial composition. The background contains no radiating or fan-shaped light pattern of any kind.
```

## 背景分层句（通用，逐字复制，**每次生成必带**）

背景元素必须待在主体后方，且以线条为主、以边角为主，避免压到主体上被误读成外挂装备。

```text
All background geometry stays entirely behind the subject and never overlaps it. The background elements are thin lines and hard-edged slabs placed in the upper left and lower right areas, leaving open cream paper around the subject.
```

---

## 背景方案库（选一个替换原照片的天空/背景）

照片转海报时，**原照片里的天空、墙面、杂乱背景一律替换掉**，换成下面某一种纯几何背景。这是苏联构成主义的标准做法，也让画面彻底远离旭日旗。

### BG-1 城市工业剪影（最苏联，通用首选）

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

<反旭日禁令段>
```

主体描述写法示例（甲板战斗机）：

```text
a large grey naval fighter jet seen from the side dominating the upper half of the frame, its nose pointing right, canopy open, folded wing and air intake geometry intact, the landing gear on the deck, the number on the fuselage simplified into a plain unlettered color block, three deck crew in plain solid yellow vests and two crew in plain solid white vests standing and crouching around the nose gear with their arms raised in hand-signal gestures, the vests are plain solid color with no patches, no writing, no lettering, the flat grey carrier deck with painted lines at the bottom
```

注意：主体描述里**不要写"pale hazy sky behind"**——天空一律交给背景方案处理。

---

## 模板 B：从零生成 · 地面装备（坦克/装甲车）

```text
Soviet constructivist military propaganda poster, 1930s Russian avant-garde screen-print style. A heavy Soviet battle tank charging forward from a low three-quarter angle, dust plume erupting from its tracks, rendered as flat geometric shapes with bold black ink outlines in vermilion red and ochre gold, visible rivet and armor plate geometry.

<背景方案：BG-3>

<风格描述段>

<禁令段>

<反旭日禁令段>
```

## 模板 C：从零生成 · 空中编队

```text
Soviet constructivist military propaganda poster, 1930s Russian avant-garde screen-print style. A formation of four heavy bombers flying toward the viewer, rendered as flat geometric shapes in deep black, vermilion red and ochre gold with bold black ink outlines and hard-edged faceted forms.

<背景方案：BG-3 或 BG-4>

<风格描述段>

<禁令段>

<反旭日禁令段>
```

## 模板 D：从零生成 · 海军

```text
Soviet constructivist military propaganda poster, 1930s Russian avant-garde screen-print style. A naval destroyer cutting through enormous stylized waves, seen from a low frontal angle. The warship rendered in flat vermilion red, deep black and cream-white geometric blocks with bold black ink outlines and hard-edged faceted forms. The sea is a deep steel-blue field broken by huge angular cream and white foam crests built from sharp triangles. Thin black horizontal dash marks suggest spray and distance.

<背景方案：BG-2>

<风格描述段>

<禁令段>

<反旭日禁令段>
```

## 模板 E：从零生成 · 直升机

```text
Soviet constructivist military propaganda poster, 1930s Russian avant-garde screen-print style. A formation of three military helicopters flying low over a valley, seen from below so the undersides and rotor discs dominate the frame. Aircraft rendered as flat geometric shapes in deep black, vermilion red and ochre gold with bold black ink outlines, spinning rotor discs drawn as sharp blade fans. The crew are flat silhouettes with no facial features.

<背景方案：BG-3>

<风格描述段>

<禁令段>

<反旭日禁令段>
```

## 模板 F：从零生成 · 火箭/火炮阵地

```text
Soviet constructivist military propaganda poster, 1930s Russian avant-garde screen-print style. A bank of multiple self-propelled rocket launchers on a hillside firing simultaneously, with multiple white smoke trails streaking diagonally into the sky. Launchers rendered as flat geometric shapes in deep black, vermilion red and ochre gold with bold black ink outlines and hard-edged faceted forms.

<背景方案：BG-1>

<风格描述段>

<禁令段>

<反旭日禁令段>
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
| **任何情况** | **必须带反旭日禁令段** |
