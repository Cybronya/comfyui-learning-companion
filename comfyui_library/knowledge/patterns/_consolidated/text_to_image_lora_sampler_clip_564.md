---
name: text_to_image_lora_sampler_clip_564
type: Text To Image
frequency: 2
level: weak
coverage: 0.8655
common_nodes: [Bounded Image Crop, Bounded Image Crop with Mask, CLIPLoader, CLIPTextEncode, ColorMatch, DF_Integer, EmptyLatentImage, Get Image Size, GetImageSize+, Image Comparer (rgthree), ImageSmartSharpen+, ImageToMask, ImpactInt, JjkText, KSampler, LG_Color_Match_V2, LoadImage, LoraLoaderModelOnly, PreviewImage, ResizeAndPadImage, ResizeImageMixlab, SaveImage, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/KoneText溶图打光 图生图处理工具_2100651281701498882.json, 图片生成/图生图/konetext溶图打光｜图生图打光高清放大三连，溶图氛围感直接拉满_2100511396101451778.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_564

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/KoneText溶图打光 图生图处理工具_2100651281701498882.json、图片生成/图生图/konetext溶图打光｜图生图打光高清放大三连，溶图氛围感直接拉满_2100511396101451778.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `Bounded Image Crop`
- `Bounded Image Crop with Mask`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `DF_Integer`
- `EmptyLatentImage`
- `Get Image Size`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageSmartSharpen+`
- `ImageToMask`
- `ImpactInt`
- `JjkText`
- `KSampler`
- `LG_Color_Match_V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ResizeAndPadImage`
- `ResizeImageMixlab`
- `SaveImage`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy imageSize`
- `solarL_SaveImagesToZip`
- `孤海注释`

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
