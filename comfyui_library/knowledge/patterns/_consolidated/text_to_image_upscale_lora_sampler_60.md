---
name: text_to_image_upscale_lora_sampler_60
type: Text To Image
frequency: 2
level: weak
coverage: 0.695
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, INTConstant, ImageScale, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text, UNETLoader, VAEDecode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize, easy imageSizeBySide]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image 超广角低角度摄影_2060698009343713282.json, 图片生成/文生图/文生图+高清放大+电商高级氛围感美图+全节点注释_2054058582009761794.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_60

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-Image 超广角低角度摄影_2060698009343713282.json、图片生成/文生图/文生图+高清放大+电商高级氛围感美图+全节点注释_2054058582009761794.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `INTConstant`
- `ImageScale`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy imageSize`
- `easy imageSizeBySide`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | - | 2 | 100% |
| 高度 | 1920 | - | 2 | 100% |
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_2s_ode | - | 2 | 100% |
| 调度器 | kl_optimal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s_ode，2 个样本，一致性 100%
- 调度器 最常用 kl_optimal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
