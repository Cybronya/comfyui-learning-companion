---
name: text_to_image_upscale_lora_sampler_53
type: Text To Image
frequency: 5
level: strong
coverage: 0.7962
common_nodes: [AdaptiveLongestEdge_EditUtils, CLIPLoader, CLIPTextEncode, CR Text Concatenate, ConditioningZeroOut, CropWithPadInfo_EditUtils, EditTextEncode_EditUtils, EmptyLatentImage, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, GetNode, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageStitch, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, StringConcatenate, StringFunction|pysssss, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy textIndexSwitch, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 Kelly室内外透视渲染加洗图工作流，手稿到渲染图建筑空间设计_2107194755112333314.json, 图片生成/图生图/Flux2Kelly室内外效果图洗图一键操作 效果图处理方案高质量_2109790885054607362.json, 图片生成/图生图/Flux2Kelly室内渲染图，极简现代手稿到成图转换_2111216011969122305.json, 图片生成/图生图/Flux2_Kelly室内外透视渲染加洗图工作流，手稿到渲染图建筑空间设计_2107330815976886274.json, 图片生成/图生图/Flux2_Kelly室内外透视渲染加洗图工作流，手稿到渲染图建筑空间设计_2107442527170289666.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_53

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux2 Kelly室内外透视渲染加洗图工作流，手稿到渲染图建筑空间设计_2107194755112333314.json、图片生成/图生图/Flux2Kelly室内外效果图洗图一键操作 效果图处理方案高质量_2109790885054607362.json、图片生成/图生图/Flux2Kelly室内渲染图，极简现代手稿到成图转换_2111216011969122305.json、图片生成/图生图/Flux2_Kelly室内外透视渲染加洗图工作流，手稿到渲染图建筑空间设计_2107330815976886274.json、图片生成/图生图/Flux2_Kelly室内外透视渲染加洗图工作流，手稿到渲染图建筑空间设计_2107442527170289666.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
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
- `孤海注释` —— 3/5 个有
- `EmptyImage` —— 2/5 个有
- `PreviewImage` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（10/5 个样本）：Steps较低可能导致细节不足
