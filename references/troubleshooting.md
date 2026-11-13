# 失败模式与修法

按出现频率排序。每条给出**症状 → 根因 → 修法**。

## 0. 背景变成旭日旗（一票否决，最高优先级）

**症状**：主体背后出现扇形放射光芒、红白对分、或一个圆形日轮。

**根因**：prompt 里出现了 `sunburst` / `radiating rays` / "光芒从主体背后炸开" 这类措辞，或沿用了旧版风格描述段里的 `hard-edged radiating red and black sunburst rays`。

**为什么一票否决**：红白放射 = 日本旭日旗，二战轴心国军旗符号。军事题材里出现这个构图，无论配色多"苏联"都可能被当右翼符号处理，作品直接不可用。

**修法**（按顺序做，缺一步就复发）：

1. 删掉全部放射类词汇：`sunburst`、`radiating rays`、`rays`、`fan of light`、`sun`、`bursting from behind`
2. 追加反旭日禁令段（`references/prompt-templates.md` 有全文）：

```
No sunburst, no radiating rays, no rays from a single point, no fan of light, no sun, no circular emblem, no badge, no rising-sun motif, no radial composition. The background contains no radiating or fan-shaped light pattern of any kind.
```

3. **换背景，不要只加禁令**——用 `references/prompt-templates.md` 的背景方案（BG-1 城市剪影 / BG-2 斜切阶梯 / BG-3 平行线束 / BG-4 透视网格）替换整个天空或背景。禁令只能压住一部分，正面给出苏联式的背景语言才靠得住。
4. 背景里的朱红改成**楔形/斜带**出现，别做"红白大面积对分"，那也是旗子联想。
5. 背景辅助线改用**同向平行的 hatch lines**，绝不用发散的射线。

**自检口径**：画面里最显眼的扩散形结构是不是扇形/放射状？是就重出。

## 1. 机身/装备上长出乱码字符（最常见）

**症状**：机身上出现两个毫无意义的假汉字，或出现乱码拉丁字母、假徽标。

**根因**：原照片上带有水印或编号，模型会把这类"文字区域"一并重绘，生成语义不明的字符。

**修法**：禁令段写全，并追加一句：

```
all equipment surfaces are blank solid color blocks with no markings
```

同时在主体描述里明确"机身编号处理成无字纯色块"，给模型一个替代解释。

**不要**试图让模型复刻真实编号——它做不到稳定，且失败率高。

## 2. 主体被改得认不出

**症状**：照片里的飞机变成另一种飞机，人物姿态错乱，甲板变成地面。

**根因**：`input_fidelity` 调到 `medium`/`low`，或主体描述太笼统。

**修法**：

- `input_fidelity` 必须是 `"high"`
- 主体描述逐项写清：数量、位置、朝向、手势、关键结构
- 宁可描述冗长，不要写"一架战斗机停在甲板上"这种一句话

## 3. 画面发暗、纸底发脏

**症状**：整体偏褐、灰，缺少参考图那种干净的米白与强对比。

**根因**：做旧词权重过高，模型把"weathered speckles / scuffs / grain"渲染成了脏污覆盖。

**修法**：在风格描述段末尾追加：

```
clean bright cream paper, minimal grunge, crisp high-contrast shapes
```

并把 `heavy paper grain` 降级为 `subtle paper grain`。

## 4. 出现渐变、阴影、写实金属反射

**症状**：装备有立体感、有高光，不平涂。

**根因**：禁令段漏了 `no gradients, no shading, no volumetric rendering, no metallic reflections`。

**修法**：四件套必须齐全：

```
no gradients, no shading, no volumetric rendering, no metallic reflections
```

另外在主体描述后追加 `flat unmodulated color blocks`（双重保险）。

## 5. 右上角 AI 水印

**症状**：右下角出现"AI生成"字样和工具标识。

**根因**：工具层强制添加的合规标识。

**修法**：**prompt 无法去除**。这是平台层行为。可选处理：

- 交付时说明，由用户自行裁切
- 生成时把 `size` 选成稍大的画幅，后续裁边

不要谎称水印已经去掉。

## 6. 折叠机翼/外挂装备变成悬空色块

**症状**：原图中挂在机翼上的部件被渲染成漂浮的大矩形。

**根因**：模型把"与主体有连接关系的部件"当作独立几何元素处理。

**修法**：在主体描述中强调连接关系：

```
the folded wing remains attached to the fuselage with a visible hinge line, no detached floating blocks
```

## 7. 人物长出多余手指或扭曲手臂

**症状**：地勤人员的手部畸形。

**根因**：小尺寸人脸/手部在风格化渲染下容易崩坏。

**修法**：把人数控制在 3–5 人以内；对关键人物用"剪影"描述：

```
the crew are rendered as flat silhouettes with simplified raised-arm gestures, no facial features
```

不要写"表情严肃""眼神坚定"这类需要五官的描述。

## 8. 批量出图风格漂移

**症状**：同一批里第一张和最后一张像两个风格。

**根因**：每次手写 prompt 时描述段有细微差异。

**修法**：风格描述段与禁令段逐字复制，只替换主体描述段；用 `references/prompt-templates.md` 里的固定文本。

## 9. 生成内容不合要求

**症状**：画面出现装饰性印章、角标、"出品"字样等参考图里没有的元素。

**根因**：模型对"复古海报"的先验会自作主张加徽章。

**修法**：追加：

```
no emblem, no badge, no stamp, no seal, no corner ornament, no maker mark
```

## 10. 衣服/背心上出现乱码字

**症状**：地勤的黄背心或白背心上出现"起飞"之类的假汉字，或者任何衣服表面出现字符。

**根因**：原照片里衣服上有胸牌、番号或文字，模型会一并复刻成语义不明的字符。

**修法**：在**主体描述**里点名衣服表面（这是关键，光在禁令段写不够）：

```
the crew wear plain solid yellow and white vests with no patches, no writing, no lettering, no chest markings
```

同时禁令段追加：

```
no patches, no badges, no uniform markings, no chest lettering, no insignia
```

## 11. 背景色块压在主体上，像零件漂浮

**症状**：一个金色或黑色矩形块叠在机翼/舰体上方，看起来像外挂装备而不是背景。

**根因**："平行斜线束"被模型理解成实心矩形条；且 prompt 没有限定背景与主体的空间关系。

**修法**：

1. 强调线而非块：`thin parallel diagonal lines, not solid slabs`
2. 明确分层关系：`all background geometry stays entirely behind the subject, nothing overlapping the aircraft`
3. 若仍然压主体，把背景方案改成**画面边角区域**落位：`the background elements occupy the upper left and lower right corners only, leaving the area around the subject empty cream paper`

**为什么重要**：参考图的背景元素永远与主体留有间隙，压上去就变成"装备画错了"，观感比不做背景更糟。
