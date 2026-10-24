---
name: image_to_image_sampler_vae_5
type: Image To Image
frequency: 16
level: strong
coverage: 0.839375
common_nodes: [CFGNorm, CLIPLoader, Fast Bypasser (rgthree), GetNode, ImageConcanate, ImageFromBatch, ImageScaleToTotalPixels, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, ModelSamplingAuraFlow, Mute / Bypass Repeater (rgthree), SaveImage, Seed (rgthree), SetNode, Text Load Line From File, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader, easy anythingIndexSwitch, easy batchAnything, easy forLoopEnd, easy forLoopStart]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen图片编辑-一张图片生成15视角-真人 动漫均可_1983464939727855617.json, 图片生成/图生图/【真人+动漫均可】Qwen-Edit 一图生成多视角_1982345702028263426.json, 图片生成/图生图/一图生成   全视角高清图片_2008489428032950273.json, 图片生成/图生图/一图生成15个视角（姿势图可自行更换）_1981949110553067521.json, 图片生成/图生图/一图生成15视角-真人动漫均可使用_2046150612173197313.json, 图片生成/图生图/一图生成15视角_1999754574569369601.json, 图片生成/图生图/一图生成15视角_真人 动漫均可_1988759003389898753.json, 图片生成/图生图/一图生成15视角【真人 动漫均可】_2046386419018502146.json, 图片生成/图生图/一图生成15视角【真人+动漫均可】_1984092175740928002.json, 图片生成/图生图/一图生成15视角【真人+动漫均可】_1984136581793677313.json, 图片生成/图生图/一图生成15视角图生图_2031195463738724354.json, 图片生成/图生图/一图生成固定15视角工作流_1989928369124986882.json, 图片生成/图生图/一键生成多视图（女版）_1993577096310095874.json, 图片生成/图生图/一键生成多视图（完全体版）_1987176415965720578.json, 图片生成/图生图/一键生成多视图（男版）_1993512547475275777.json, 图片生成/图生图/图生图生成15视角，慢剧首选利器_2011489198791991298.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_5

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Qwen图片编辑-一张图片生成15视角-真人 动漫均可_1983464939727855617.json、图片生成/图生图/【真人+动漫均可】Qwen-Edit 一图生成多视角_1982345702028263426.json、图片生成/图生图/一图生成   全视角高清图片_2008489428032950273.json、图片生成/图生图/一图生成15个视角（姿势图可自行更换）_1981949110553067521.json、图片生成/图生图/一图生成15视角-真人动漫均可使用_2046150612173197313.json…）

- **类型**：Image To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 16 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Fast Bypasser (rgthree)`
- `GetNode`
- `ImageConcanate`
- `ImageFromBatch`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `Mute / Bypass Repeater (rgthree)`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `Text Load Line From File`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `ImpactInt` —— 15/16 个有
- `RHHiddenNodes` —— 12/16 个有
- `LoraLoaderModelOnly` —— 4/16 个有
- `PreviewImage` —— 4/16 个有
- `UNETLoader` —— 4/16 个有
- `MathExpression|pysssss` —— 3/16 个有
- `Text Multiline` —— 3/16 个有
- `easy cleanGpuUsed` —— 3/16 个有
- `Bookmark (rgthree)` —— 2/16 个有
- `EmptyLatentImage` —— 2/16 个有
- `ModelPatchTorchSettings` —— 2/16 个有
- `PathchSageAttentionKJ` —— 2/16 个有
- `Fast Groups Bypasser (rgthree)` —— 1/16 个有
- `NunchakuQwenImageDiTLoader` —— 1/16 个有
- `PreviewAny` —— 1/16 个有
- `SimpleMath+` —— 1/16 个有
- `String Literal` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 16 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 16 | 82% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 720 | - | 2 | 100% |
| 高度 | 1440 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，16 个样本，取值集中（一致性 82%）
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 720，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1440，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
