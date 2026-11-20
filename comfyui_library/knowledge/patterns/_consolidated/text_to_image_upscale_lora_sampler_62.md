---
name: text_to_image_upscale_lora_sampler_62
type: Text To Image
frequency: 5
level: strong
coverage: 0.7152
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, INTConstant, ImageScale, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text, UNETLoader, VAEDecode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize, easy imageSizeBySide]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/超广角低角度摄影 夸张角度写实拍摄 Z-Image极速生图版 高清放大 SeedVR反推提示词_2063454144324792321.json, 图片生成/文生图/Z-Image 超广角低角度摄影_2060698009343713282.json, 图片生成/文生图/古装 _ 现代短剧高级氛围感美图_2054026317141692417.json, 图片生成/文生图/文生图+高清放大+电商高级氛围感美图+全节点注释_2054058582009761794.json, 图片生成/文生图/文生图-高清放大--电商高级氛围感美图-全节点注释_2054872415896915969.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_62

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/超广角低角度摄影 夸张角度写实拍摄 Z-Image极速生图版 高清放大 SeedVR反推提示词_2063454144324792321.json、图片生成/文生图/Z-Image 超广角低角度摄影_2060698009343713282.json、图片生成/文生图/古装 _ 现代短剧高级氛围感美图_2054026317141692417.json、图片生成/文生图/文生图+高清放大+电商高级氛围感美图+全节点注释_2054058582009761794.json、图片生成/文生图/文生图-高清放大--电商高级氛围感美图-全节点注释_2054872415896915969.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 5 个 workflow 都包含：
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
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 5 | 100% |
| 高度 | 1920 | 1920 - 1920 | 5 | 100% |
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | res_2s_ode | - | 5 | 100% |
| 调度器 | kl_optimal | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s_ode，5 个样本，一致性 100%
- 调度器 最常用 kl_optimal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
