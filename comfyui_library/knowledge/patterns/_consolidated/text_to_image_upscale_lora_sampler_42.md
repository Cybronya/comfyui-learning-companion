---
name: text_to_image_upscale_lora_sampler_42
type: Text To Image
frequency: 6
level: moderate
coverage: 0.743667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, INTConstant, ImageScale, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize, easy imageSizeBySide]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/4K图像高清放大｜SeedVR 2.5+TTP清晰图片处理_2092925104920555521.json, 图片生成/图生图/超广角低角度摄影 夸张角度写实拍摄 Z-Image极速生图版 高清放大 SeedVR反推提示词_2063454144324792321.json, 图片生成/文生图/Z-Image 超广角低角度摄影_2060698009343713282.json, 图片生成/文生图/古装 _ 现代短剧高级氛围感美图_2054026317141692417.json, 图片生成/文生图/文生图+高清放大+电商高级氛围感美图+全节点注释_2054058582009761794.json, 图片生成/文生图/文生图-高清放大--电商高级氛围感美图-全节点注释_2054872415896915969.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_42

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/4K图像高清放大｜SeedVR 2.5+TTP清晰图片处理_2092925104920555521.json、图片生成/图生图/超广角低角度摄影 夸张角度写实拍摄 Z-Image极速生图版 高清放大 SeedVR反推提示词_2063454144324792321.json、图片生成/文生图/Z-Image 超广角低角度摄影_2060698009343713282.json、图片生成/文生图/古装 _ 现代短剧高级氛围感美图_2054026317141692417.json、图片生成/文生图/文生图+高清放大+电商高级氛围感美图+全节点注释_2054058582009761794.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 6 个 workflow 都包含：
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
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy imageSize`
- `easy imageSizeBySide`

**可变部分**（部分 workflow 才有）：
- `Text` —— 5/6 个有
- `LoadImage` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `solarL_SaveImagesToZip` —— 1/6 个有
- `孤海注释` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 80 - 1080 | 6 | 59% |
| 高度 | 1920 | 80 - 1920 | 6 | 57% |
| 采样步数 | 8 | 4 - 8 | 6 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 6 | 18% |
| 采样算法 | res_2s_ode | - | 6 | 83% |
| 调度器 | kl_optimal | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 80 - 1080，6 个样本
- 高度 中位数 1920，观测区间 80 - 1920，6 个样本
- 采样步数 中位数 8，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，6 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 res_2s_ode，6 个样本，一致性 83%
- 调度器 最常用 kl_optimal，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
