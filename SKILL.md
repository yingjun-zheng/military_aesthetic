---
name: military-aesthetic
description: 照片转「苏联构成主义 × 军事宣传画」海报，或从零生成该风格军事插画。装备识别度优先：严格保留装备原涂装/迷彩、编号、机徽与结构细节（模型直接复刻），仅重构背景为红/黑/赭金/米白构成主义几何切面（可选一个场景色）。触发词：军构美学、构成主义、军事宣传画、苏联海报、照片转海报。
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

**装备识别度优先（2026-11-21 用户校准，最高优先级）**：装备主体必须一眼可辨机型/舰型/车型。模式 A 的主体描述必须逐项覆盖：

- 主体是什么、数量、彼此位置关系
- 每个主体的姿态（尤其手势、朝向）
- **原涂装/迷彩颜色照搬**——数码迷彩就写数码迷彩、海灰就写海灰、沙漠迷彩就写沙黄，不许替换成海报色
- **编号/舷号逐位复刻**（如 106、3506、FK322）、红星机徽与识别涂装按原位保留——模型直接画，实测短编号渲染可靠
- 武器构型与结构细节（挂载、起落架、履带、雷达）完整保留
- 明确写 "highly recognizable, NOT abstract"

场景元素（甲板/地面/前景人物）写进主体描述，但**不要写"天空/背景长什么样"**——天空统一交给背景方案。

### 第 4.5 步：选背景方案（不可跳过）

从 `references/prompt-templates.md` 的背景方案库里**选一个**插入 prompt，替换原照片的整个天空或杂乱背景。

**默认选 BG-5（大块几何切面 · 场景色，2026-11-21 用户七图校准）**——海军题材配海蓝场景色，城市夜戏配夜绿场景色，其余题材米白打底。老方案 BG-1～BG-4 作为备选保留。

 Soviet 构成主义的背景语言是斜切、楔形、色块面。放射状平面在**非旗色**（黑/金/蓝/米白）下可用，但红日轮+放射的旭日旗构图仍然一票否决（见第 4.6 步）。

### 第 4.6 步：带上禁令段（2026-11-21 修订版）

每次生成必须带上 `references/prompt-templates.md` 中的修订版禁令段：

**禁令段（区分"真标识"与"编造字"）：**

```
No invented text: no lettering, no numbers, no characters, no symbols other than
the markings that exist in the original photo; those must be reproduced exactly
in position and content. No watermark, no signature, no border frame, no stamp,
no seal, no corner ornament, no maker mark, no invented badges.
```

**旭日旗专项禁令段（每次生成必带）：**

```
No rising-sun motif: never a red or white sun disc with rays radiating from it,
no red-on-white radiating bands. Radiating wedge shapes, diagonal light planes
and beam fans are allowed only in non-flag colors (black, gold, blue, cream)
and only without any central disc.
```

漏掉旭日旗禁令段，模型可能退化成红白放射旗构图——这是这套风格的一票否决项。
原照片上的真实编号、机徽**直接让模型复刻**（2026-11-21 起，参考图实测短编号渲染可靠）；复杂中文标识（如垂尾书法字）模型画不好时，才退回"留纯色面 + Pillow 补画"的老路（见 `style-spec.md` 第 6.5 节）。

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

1. **主体完整性** — 主体数量、姿态、结构是否与原照一致
2. **识别度与标识保真（2026-11-21 新增）** — 机型/舰型/车型一眼可辨；原涂装/迷彩颜色未被替换；编号逐位正确；机徽、识别涂装在原位。任何一项丢了就重出
3. **旭日旗检查（一票否决）** — 画面里有没有"红/白日轮 + 放射光芒"的旭日旗构图。注意：非旗色（黑/金/蓝/米白）的放射楔形、斜切光线**允许**（参考族实测存在），只有红色日轮+放射才算触线
4. **背景语言** — 是否为大块构成主义几何切面（斜三角/楔形/放射平面，BG-5）或老方案 BG-1～BG-4，而不是写实天空
5. **风格还原** — 装备为精细扁平矢量插画 + 几何切面明暗；有无渐变、写实照片残留
6. **配色** — 背景锁在红/黑/赭金/米白 + 至多一个场景色；装备保留原涂装配色（不受背景调色板约束）
7. **印刷质感** — 做旧纸纹、颗粒、网点
8. **文字污染** — 机身/装备上是否长出**原照没有的**乱码字符（最常见失败点）；原照真实编号错位/变形也算失败
9. **水印** — 右下角平台 AI 标识属工具层，prompt 无法去除

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

- **装备识别度优先（2026-11-21，最高优先级）**：原涂装/迷彩颜色、编号、机徽、武器构型一律保留并让模型直接复刻，绝不抽象化、绝不把装备颜色统一成海报色。这条优先于任何配色规则。
- **禁止旭日旗构图**：红/白日轮 + 放射光芒一律不可用。非旗色的放射楔形、斜切光线允许。这条优先于任何风格追求。
- **不放太阳（2026-11-21 用户拍板）**：背景一律不加太阳/月亮/圆形天体——黑圆也不行（实测放主体后方会变成"机身后开黑洞"，参考族七图中也没有太阳）。
- 不要在画面里自行添加装饰性元素（印章、角标、水印式标记、"XX 出品"小戳）。参考图里没有的东西不要加。
- 不要生成**原照上没有的**文字、标语、编号；原照真实编号/机徽必须保留。
- 不要因为图生图效果不理想就把"还原照片内容"降级为"重画一个类似场景"；用户要的是他那张照片的构图。
