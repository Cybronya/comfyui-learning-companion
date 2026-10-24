---
name: image_to_image_upscale_lora_sampler_101
type: Image To Image
frequency: 2
level: weak
coverage: 0.8595
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, LatentPixelScale, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/图片超级放大_2041442572731682818.json, 图片生成/文生图/Z-Image：神级像素文生图+图生图+高清放大_2072264894711418882.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_101

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图片超级放大_2041442572731682818.json、图片生成/文生图/Z-Image：神级像素文生图+图生图+高清放大_2072264894711418882.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LatentPixelScale`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `Int` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LayerUtility: ImageReel` —— 1/2 个有
- `LayerUtility: ImageReelComposit` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `ResizeImagesByLongerEdge` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `图像缩放V2_孤海` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.175 | - | 2 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 1/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.175，样本不足，未给区间，2 个样本
- 高发问题（1/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
