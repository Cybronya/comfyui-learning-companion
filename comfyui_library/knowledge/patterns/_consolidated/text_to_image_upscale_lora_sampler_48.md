---
name: text_to_image_upscale_lora_sampler_48
type: Text To Image
frequency: 2
level: weak
coverage: 0.7985
common_nodes: [AdaptiveLongestEdge_EditUtils, CLIPLoader, CLIPTextEncode, CR Text Concatenate, ConditioningZeroOut, CropWithPadInfo_EditUtils, EditTextEncode_EditUtils, EmptyLatentImage, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, GetNode, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageStitch, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, StringConcatenate, StringFunction|pysssss, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy textIndexSwitch, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 Kelly室内外透视渲染加洗图工作流，手稿到渲染图建筑空间设计_2107194755112333314.json, 图片生成/图生图/Flux2_Kelly室内外透视渲染加洗图工作流，手稿到渲染图建筑空间设计_2107330815976886274.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_48

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux2 Kelly室内外透视渲染加洗图工作流，手稿到渲染图建筑空间设计_2107194755112333314.json、图片生成/图生图/Flux2_Kelly室内外透视渲染加洗图工作流，手稿到渲染图建筑空间设计_2107330815976886274.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `AdaptiveLongestEdge_EditUtils`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `CropWithPadInfo_EditUtils`
- `EditTextEncode_EditUtils`
- `EmptyLatentImage`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinOutputExtractor_EditUtils`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageStitch`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `StringConcatenate`
- `StringFunction|pysssss`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy textIndexSwitch`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
