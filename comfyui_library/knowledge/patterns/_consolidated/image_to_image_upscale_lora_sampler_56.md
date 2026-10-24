---
name: image_to_image_upscale_lora_sampler_56
type: Image To Image
frequency: 3
level: moderate
coverage: 0.877667
common_nodes: [CLIPLoader, CLIPTextEncode, ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/wan2.2图生图高质量_1987726436859621378.json, "图片生成/图生图/wan2.2高清放大修复高质量,4K_1983123878350352386.json", 图片生成/文生图/Wan2.2 TTP高阶放大（全网ID ：楚门的AI世界）_1950100432455647233.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_56

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/wan2.2图生图高质量_1987726436859621378.json、图片生成/图生图/wan2.2高清放大修复高质量,4K_1983123878350352386.json、图片生成/文生图/Wan2.2 TTP高阶放大（全网ID ：楚门的AI世界）_1950100432455647233.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `SaveImagePlus` —— 2/3 个有
- `ImageStitch` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `easy showAnything` —— 1/3 个有
- `workflow>wan2.2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 12 | 3 | 0% |
| 采样算法 | heun | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 0.1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 12，3 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 heun，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 0.1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
