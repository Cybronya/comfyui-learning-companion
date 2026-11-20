---
name: unknown_workflow_inpaint_sampler_clip_24
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.921286
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, DifferentialDiffusion, EmptyImage, FluxGuidance, ImageCrop, ImageScale, ImageScaleToTotalPixels, ImageToMask, InpaintModelConditioning, KSampler, LayerUtility: CropByMask V2, LayerUtility: NumberCalculator, LayerUtility: RestoreCropBox, LoadImage, MaskToImage, ReduxAdvanced, SaveImage, StyleModelLoader, VAEDecode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/A3、万物迁移F.1版本 - 和风_1990399537883865089.json, 平台全量/1比1换装还原细小图案及花纹_1915349947808415745.json, 平台全量/万物迁移原图直出优化版-Flux-OneReward_2017152566487949314.json, 平台全量/万物迁移增强版_1904740528515387393.json, 平台全量/万物迁移工作流V1_1910526334005669889.json, 平台全量/换装迁移_1919592647407632385.json, 平台全量/高清换装plus_1944748442864242690.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/A3、万物迁移F.1版本 - 和风_1990399537883865089.json、平台全量/1比1换装还原细小图案及花纹_1915349947808415745.json、平台全量/万物迁移原图直出优化版-Flux-OneReward_2017152566487949314.json、平台全量/万物迁移增强版_1904740528515387393.json、平台全量/万物迁移工作流V1_1910526334005669889.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `EmptyImage`
- `FluxGuidance`
- `ImageCrop`
- `ImageScale`
- `ImageScaleToTotalPixels`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: CropByMask V2`
- `LayerUtility: NumberCalculator`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `MaskToImage`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 6/7 个有
- `ImagePadForOutpaintMasked` —— 6/7 个有
- `LayerMask: MaskGrow` —— 6/7 个有
- `LayerUtility: ImageRemoveAlpha` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `easy float` —— 6/7 个有
- `DualCLIPLoaderGGUF` —— 5/7 个有
- `UnetLoaderGGUF` —— 5/7 个有
- `DualCLIPLoader` —— 2/7 个有
- `UNETLoader` —— 2/7 个有
- `ACE_TextTranslate` —— 1/7 个有
- `ApplyFBCacheOnModel` —— 1/7 个有
- `Bjornulf_ShowStringText` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `DeepTranslatorTextNode` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `JWFloat` —— 1/7 个有
- `RH_Translator` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `easy clearCacheAll` —— 1/7 个有
- `easy imageConcat` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 5 - 30 | 7 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | sgm_uniform | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 5 - 30，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
