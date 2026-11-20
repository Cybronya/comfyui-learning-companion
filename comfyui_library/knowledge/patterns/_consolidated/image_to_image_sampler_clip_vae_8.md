---
name: image_to_image_sampler_clip_vae_8
type: Image To Image
frequency: 23
level: strong
coverage: 0.826783
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/你说我改+一句话改图（kontext图像编辑)_1971800112290787330.json, 图片生成/图生图/全能去除图形_字体_水印图片【无残留】_2057355116965089281.json, 图片生成/图生图/千府AI-Kontext Nunchaku极速一键改图_1943474948276953089.json, 图片生成/图生图/去水印_2010982510636834818.json, 图片生成/图生图/去除图像水印_2018512334502760449.json, 图片生成/图生图/双截棍-kontext（dev）_1938464979685433345.json, 图片生成/图生图/和年老的自己拥抱-kontext拥抱融合_1976483796184899585.json, 图片生成/图生图/图像去水印无损文字_2038086597199011842.json, 图片生成/图生图/急速去水印（支持多图）_2057371599556403202.json, 图片生成/图生图/急速版去水印（支持多图）_2057637156197330946.json, 图片生成/图生图/极速图像水印擦除无损文字_1939681317691035649.json, 图片生成/图生图/极速图像水印擦除无损文字_1942419516015980546.json, 图片生成/图生图/极速图像水印擦除无损文字_1975100385578889218.json, 图片生成/图生图/极速图像水印擦除无损文字_1999672895452442626.json, 图片生成/图生图/极速图像水印擦除无损文字_2005560503084740610.json, 图片生成/图生图/极速图像水印擦除无损文字_2013500753469513730.json, 图片生成/图生图/极速图像水印擦除无损文字_2097887846026797057.json, 图片生成/图生图/极速图像水印擦除无损文字_2099415419806380034.json, 图片生成/图生图/极速版去水印（支持多图）_2069976135907233793.json, 图片生成/图生图/极速版去水印（支持多图）_2070339562018271234.json, 图片生成/图生图/水印去除无损文字_2034837976974368770.json, 平台全量/Kontext-DEV去水印_加速Nunchaku版_1939874954219589633.json, 平台全量/中文版FLUX-kontext对话式修图工作流_1954365946536312834.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_8

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（图片生成/图生图/你说我改+一句话改图（kontext图像编辑)_1971800112290787330.json、图片生成/图生图/全能去除图形_字体_水印图片【无残留】_2057355116965089281.json、图片生成/图生图/千府AI-Kontext Nunchaku极速一键改图_1943474948276953089.json、图片生成/图生图/去水印_2010982510636834818.json、图片生成/图生图/去除图像水印_2018512334502760449.json…）

- **类型**：Image To Image
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 23 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 22/23 个有
- `NunchakuFluxDiTLoader` —— 21/23 个有
- `ImageStitch` —— 20/23 个有
- `LoadImageOutput` —— 19/23 个有
- `PreviewImage` —— 18/23 个有
- `EmptySD3LatentImage` —— 12/23 个有
- `DeepTranslatorTextNode` —— 5/23 个有
- `UNETLoader` —— 2/23 个有
- `CR Simple Image Compare` —— 1/23 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/23 个有
- `NunchakuFluxLoraLoader` —— 1/23 个有
- `RH_Translator` —— 1/23 个有
- `easy cleanGpuUsed` —— 1/23 个有
- `easy showAnything` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 23 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 23 | 100% |
| 采样算法 | euler | - | 23 | 100% |
| 调度器 | simple | - | 23 | 96% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，23 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，23 个样本，一致性 100%
- 调度器 最常用 simple，23 个样本，一致性 96%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
