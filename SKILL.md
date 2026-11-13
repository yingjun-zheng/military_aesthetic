---
name: military-aesthetic
description: Convert real-world photographs into Soviet constructivist military propaganda posters (the "military constructivist" look - warm cream paper, vermilion red, deep black, ochre gold, hard-edged flat color blocks, bold black ink outlines, diagonal wedges, stepped terraces, industrial skyline silhouettes, parallel hatch lines, halftone offset-print texture), and render new images in that style from scratch. Backgrounds must never use radiating sunburst rays or any fan-shaped light motif, which reads as a Japanese rising-sun flag. This skill should be used when the user supplies a photo and asks to turn it into a poster, mentions 军构美学 / 构成主义海报 / 军事宣传画 / 苏联海报风格 / 复古军事版画 / constructivist military poster / soviet propaganda poster, or wants a batch of images rendered in this style.
agent_created: true
---

# 军构美学 · 照片转军事海报

把实拍照片重构成「苏联构成主义 × 军事宣传画」风格的海报图，或从零生成该风格的军事装备插画。

风格规格与色值见 `references/style-spec.md`；分题材 prompt 模板见 `references/prompt-templates.md`；失败模式与修法见 `references/troubleshooting.md`。

## 何时用

- 用户给出一张照片，要求"改成那种构图/风格"、做成海报、做成宣传画
- 用户提到 军构美学、构成主义、军事宣传画、苏联海报、复古军事版画
- 用户要求批量把一组照片转成同一风格
- 用户要求从零生成该风格的军事题材插画

## 工作流

### 第 1 步：判断模式

| 模式 | 条件 | image1 参数 |
|------|------|-------------|
| **A. 照片转海报** | 用户提供了照片路径 | 传照片绝对路径，`input_fidelity: "high"` |
| **B. 从零生成** | 用户只要该风格的成品 | 不传 image1，纯文本 prompt |

模式 A 是主用途，优先保证照片内容被还原。

### 第 2 步：加载工具

```
ToolSearch(tool_names: ["ImageGen"])
```

ImageGen 是延迟工具，schema 未加载前直接调用会报 InputValidationError。加载后通过 `DeferExecuteTool` 调用。

### 第 3 步：告知积分消耗

**在调用 ImageGen 之前，必须告知用户单次生成的积分消耗（约 5–10 积分/张）和本次预计张数。** 用户批准后再生成；若用户未要求批量，一次出一张。

### 第 4 步：组装 prompt

prompt = `references/prompt-templates.md` 中对应模板 + 主体描述。

模式 A 的主体描述必须逐项覆盖：

- 主体是什么、数量、彼此位置关系
- 每个主体的姿态（尤其手势、朝向）
- 场景元素（甲板/地面/前景物体）
- 需要简化的表面（编号、标志 → 纯色块）

主体描述**不要写"天空/背景长什么样"**——天空统一交给背景方案。

### 第 4.5 步：选背景方案（不可跳过）

从 `references/prompt-templates.md` 的背景方案库（BG-1 城市工业剪影 / BG-2 斜切色块与阶梯 / BG-3 平行斜线束与几何山形 / BG-4 透视网格地面）里**选一个**插入 prompt，替换原照片的整个天空或杂乱背景。

 Soviet 构成主义的背景语言是斜切、阶梯、剪影、平行线束，**不是放射**。背景方案是这套风格成立的地基，也是避开旭日旗的根本手段——只加禁令不给正面方案，模型仍会往扇形光芒上靠。

### 第 4.6 步：带上三段禁令

每次生成必须逐字带上（文本见 `references/prompt-templates.md`）：

```
no text, no lettering, no numbers, no characters, no symbols,
no writing of any kind on any surface, no watermark, no signature, no border frame,
no patches, no badges, no uniform markings, no chest lettering, no insignia
```

```
No sunburst, no radiating rays, no rays from a single point, no fan of light,
no sun, no circular emblem, no badge, no rising-sun motif, no radial composition.
The background contains no radiating or fan-shaped light pattern of any kind.
```

```
All background geometry stays entirely behind the subject and never overlaps it.
The background elements are thin lines and hard-edged slabs placed in the upper left
and lower right areas, leaving open cream paper around the subject.
```

漏掉反旭日禁令段，背景就会退化成旭日旗——这是这套风格的一票否决项。
漏掉第三段，背景色块会压到主体上，被看成装备画错了。

### 第 5 步：调用

模式 A：

```json
{
  "image1": "<照片绝对路径>",
  "input_fidelity": "high",
  "prompt": "<组装好的 prompt>",
  "quality": "high",
  "size": "1536x1024",
  "output_dir": "<工作区>/generated-images/military-aesthetic"
}
```

模式 B：去掉 `image1` 与 `input_fidelity`，其余相同。

尺寸：横向构图 `1536x1024`；竖向构图 `1024x1536`；方形 `1024x1024`。

**横向照片不要强行塞进方形尺寸**——宁可让模型重构构图，否则主体会被裁掉。

### 第 6 步：质检

对每张产出调用 `ViewImage`，逐项核对：

1. **主体完整性** — 主体数量、姿态、手势、结构是否与原照一致
2. **旭日旗检查（一票否决）** — 画面里有没有扇形放射光芒、日轮、圆形放射徽章、任何从一点扩散的线条结构。有就重出，不看其他优点
3. **背景语言** — 是否为斜切色块 / 阶梯 / 工业剪影 / 平行线束 / 透视网格这类苏联式几何背景，而不是放射或写实天空
4. **风格还原** — 是否为平涂硬边色块 + 粗黑轮廓；有无渐变、阴影、写实残留
5. **配色** — 是否锁在五色内（米白底 / 朱红 / 黑 / 赭金 / 少量钴蓝）
6. **印刷质感** — 网点、纸纹、套色错位
7. **文字污染** — 机身/装备上是否长出乱码字符（最常见失败点）
8. **水印** — 右下角平台 AI 标识属工具层，prompt 无法去除

任一项不过，按 `references/troubleshooting.md` 调 prompt 重出。

### 第 7 步：交付

用 `present_files` 交付生成的图片，**一次只交付图片本身**。不要附带提示词模板、参考文档或中间文件。

回复中说明：还原到什么程度、出现了什么问题、下一步可调的方向。

## 批量处理

1. 收集所有照片路径，逐张按第 4–6 步处理
2. 同一批 prompt 的风格描述段保持完全一致，只替换主体描述段——否则批量出图的风格会漂移
3. 批量出图后用 `scripts/contact_sheet.py` 拼成对照图，方便一次挑图：

```bash
python scripts/contact_sheet.py <图片目录> -o <输出拼图路径> --cols 3 --labels
```

依赖 Pillow。本机可用解释器（WorkBuddy 内置 Python 没有 Pillow）：

```bash
/c/Users/zhengyingjun/AppData/Local/Programs/Python/Python313/python.exe scripts/contact_sheet.py ...
```

## 硬性约束

- **禁止旭日旗语言**：任何从单一点向外扩散的放射状线条、扇形光芒、日轮、圆形放射徽章一律不可用。背景一律走斜切色块 / 阶梯 / 工业剪影 / 平行线束 / 透视网格。这条优先于任何风格追求。
- 不要在画面里自行添加装饰性元素（印章、角标、水印式标记、"XX 出品"小戳）。参考图里没有的东西不要加。
- 不要生成任何文字、标语、编号——原始照片上的编号同样处理成纯色块，不要试图复刻。
- 不要因为图生图效果不理想就把"还原照片内容"降级为"重画一个类似场景"；用户要的是他那张照片的构图。
