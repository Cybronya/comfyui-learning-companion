---
name: image_to_image_upscale_lora_sampler_22
type: Image To Image
frequency: 8
level: moderate
coverage: 0.575
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/去油修复+SeedVR2放大，解决皮肤纹理差的问题_2086643087371235330.json, 图片生成/图生图/去油修复+SeedVR2放大，解决皮肤纹理差的问题_2088509976024272898.json, 图片生成/图生图/去油修复+SeedVR2放大，解决皮肤纹理差的问题_2090270550118723586.json, 图片生成/图生图/去油修复+SeedVR2放大，解决皮肤纹理差的问题_2092626734549127169.json, 平台全量/Flux2 Klein 9b 毛坯图转效果图_2026650745990287362.json, 平台全量/产品图精修 Flux-2-klein-9B  HYPIR产品高清放大（最大支持8倍）+SeedVR2_2026495816893997058.json, 平台全量/去AI感去油修复+SeedVR2放大，解决皮肤纹理差的问题_2085645947341721601.json, 平台全量/拯救全能图片G-image-2出图服装面料，服装面料细节精修_2077225201623982081.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_22

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/去油修复+SeedVR2放大，解决皮肤纹理差的问题_2086643087371235330.json、图片生成/图生图/去油修复+SeedVR2放大，解决皮肤纹理差的问题_2088509976024272898.json、图片生成/图生图/去油修复+SeedVR2放大，解决皮肤纹理差的问题_2090270550118723586.json、图片生成/图生图/去油修复+SeedVR2放大，解决皮肤纹理差的问题_2092626734549127169.json、平台全量/Flux2 Klein 9b 毛坯图转效果图_2026650745990287362.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `easy int` —— 7/8 个有
- `ColorMatch` —— 6/8 个有
- `ConstrainImage|pysssss` —— 6/8 个有
- `GetImageSize` —— 6/8 个有
- `GetNode` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `easy imageSizeBySide` —— 6/8 个有
- `Float` —— 1/8 个有
- `FluxGuidance` —— 1/8 个有
- `HYPIRAdvancedRestoration` —— 1/8 个有
- `ImageConcatMulti` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `ImpactInt` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `MuyeTextEditOutput` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy imageSize` —— 1/8 个有
- `easy promptConcat` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 8 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 0.05 - 1 | 8 | 64% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.05 - 1，8 个样本
- 风险：重绘幅度 观测到 0.05，低于常用下限 0.1（）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
