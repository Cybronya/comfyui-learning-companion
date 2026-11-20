---
name: text_to_image_lora_sampler_clip_738
type: Text To Image
frequency: 2
level: weak
coverage: 0.9325
common_nodes: [CLIPTextEncode, CR Text Replace, ColorMatch, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, Image Comparer (rgthree), ImageCASharpening+, ImageScale, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, Primitive string multiline [Crystools], RH_LLMAPI_NODE, ReferenceLatent, SaveImage, SeedVR2, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/提取图案 _ 平铺整个画布_1873776789674967042.json, 数字人/数字人/Kontext提取图案印花纹理+高清放大_2034148378560434178.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_738

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/提取图案 _ 平铺整个画布_1873776789674967042.json、数字人/数字人/Kontext提取图案印花纹理+高清放大_2034148378560434178.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text Replace`
- `ColorMatch`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageScale`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Primitive string multiline [Crystools]`
- `RH_LLMAPI_NODE`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `1hew_MaskFillHole` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageCropByMask` —— 1/2 个有
- `MaskPreview` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `RunningHub SeedXPro Translator` —— 1/2 个有
- `SDVN RGBA to RGB` —— 1/2 个有
- `SolidMask` —— 1/2 个有
- `easy ifElse` —— 1/2 个有
- `easy isMaskEmpty` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 0.99 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1248 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 0.99，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1248，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.99，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
