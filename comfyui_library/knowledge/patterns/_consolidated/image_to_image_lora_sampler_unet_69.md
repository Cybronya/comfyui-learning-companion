---
name: image_to_image_lora_sampler_unet_69
type: Image To Image
frequency: 8
level: strong
coverage: 0.912625
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/51号特工：视角自由+随意改变图片角度和镜头+图生图_2039240266967687170.json, 图片生成/图生图/67.tonnie--2511改背景、换角度_2009983274596179970.json, 图片生成/图生图/68.tonnie-2511位移、质量下降及色差_2009989683740155905.json, 图片生成/图生图/76.tonnie-2511图像多角度_2011789730735722497.json, 图片生成/图生图/QWEN-2511-人物角色多角度一致性工作流_2053126067094859778.json, 图片生成/图生图/Qwen-edit-2511-人像多角度随意调整_2008543202546028546.json, 图片生成/图生图/修改角度工作流_2042886227157848065.json, 图片生成/图生图/全能生图 千问 2511多角度变换_2012356861068054529.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_69

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/51号特工：视角自由+随意改变图片角度和镜头+图生图_2039240266967687170.json、图片生成/图生图/67.tonnie--2511改背景、换角度_2009983274596179970.json、图片生成/图生图/68.tonnie-2511位移、质量下降及色差_2009989683740155905.json、图片生成/图生图/76.tonnie-2511图像多角度_2011789730735722497.json、图片生成/图生图/QWEN-2511-人物角色多角度一致性工作流_2053126067094859778.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `QwenMultiangleCameraNode` —— 6/8 个有
- `easy promptList` —— 6/8 个有
- `easy showAnything` —— 5/8 个有
- `FluxKontextMultiReferenceLatentMethod` —— 4/8 个有
- `INTConstant` —— 3/8 个有
- `VNCCS_VisualPositionControl` —— 3/8 个有
- `ConditioningZeroOut` —— 2/8 个有
- `ConstrainImage|pysssss` —— 1/8 个有
- `Display Any (rgthree)` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `InpaintCrop` —— 1/8 个有
- `InpaintStitch` —— 1/8 个有
- `MultiTextConcatenate` —— 1/8 个有
- `RH_Nano_Banana2_Image2Image` —— 1/8 个有
- `ReferenceLatent` —— 1/8 个有
- `Text Multiline` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 5 - 10 | 8 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 5 - 10，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（6/8 个样本）：Steps较低可能导致细节不足
