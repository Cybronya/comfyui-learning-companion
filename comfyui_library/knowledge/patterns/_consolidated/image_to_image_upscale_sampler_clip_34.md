---
name: image_to_image_upscale_sampler_clip_34
type: Image To Image
frequency: 3
level: strong
coverage: 0.862667
common_nodes: [Any Switch (rgthree), CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, FluxKontextImageScale, GetImageSize, GoogleTranslateTextNode, ImageConcatMulti, ImageScaleBy, ImageStitch, ImpactMinMax, KSampler, LoadImage, RHHiddenNodes, ReferenceLatent, RepeatLatentBatch, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/年代照片修复-高清图 质感清晰_2014503932814430209.json, 图片生成/图生图/老照片修复+黑白上色-高清放大_2066805706816319489.json, 图片生成/图生图/老照片修复+黑白上色-高清放大完美版_2013533207559409666.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_34

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/年代照片修复-高清图 质感清晰_2014503932814430209.json、图片生成/图生图/老照片修复+黑白上色-高清放大_2066805706816319489.json、图片生成/图生图/老照片修复+黑白上色-高清放大完美版_2013533207559409666.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GetImageSize`
- `GoogleTranslateTextNode`
- `ImageConcatMulti`
- `ImageScaleBy`
- `ImageStitch`
- `ImpactMinMax`
- `KSampler`
- `LoadImage`
- `RHHiddenNodes`
- `ReferenceLatent`
- `RepeatLatentBatch`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
