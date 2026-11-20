---
name: image_to_image_upscale_lora_sampler_41
type: Image To Image
frequency: 5
level: moderate
coverage: 0.8696
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, LatentPixelScale, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图片超级放大_2041442572731682818.json, 图片生成/文生图/Z-Image：神级像素文生图+图生图+高清放大_2072264894711418882.json, 平台全量/1亿像素超清放大Z-Image_2001572481896968193.json, 平台全量/8k修复放大 增加真实细节 皮肤 锋芒毕露  Flux2-Klein 8k 终极高清修复  纤毫毕现_2019973512022204418.json, 平台全量/毛孔级细节 立竿见影 高清修复放大  Flux2-Klein终极高清修复8k_2021097369105862658.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_41

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/图片超级放大_2041442572731682818.json、图片生成/文生图/Z-Image：神级像素文生图+图生图+高清放大_2072264894711418882.json、平台全量/1亿像素超清放大Z-Image_2001572481896968193.json、平台全量/8k修复放大 增加真实细节 皮肤 锋芒毕露  Flux2-Klein 8k 终极高清修复  纤毫毕现_2019973512022204418.json、平台全量/毛孔级细节 立竿见影 高清修复放大  Flux2-Klein终极高清修复8k_2021097369105862658.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
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
- `LayerUtility: ImageReel` —— 3/5 个有
- `LayerUtility: ImageReelComposit` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `EmptyFlux2LatentImage` —— 2/5 个有
- `Qwen3_VQA` —— 2/5 个有
- `ReferenceLatent` —— 2/5 个有
- `easy imageScaleDownBy` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `Int` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `ResizeImagesByLongerEdge` —— 1/5 个有
- `VAEDecode` —— 1/5 个有
- `easy seed` —— 1/5 个有
- `图像缩放V2_孤海` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 10 | 5 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 5 | 60% |
| 调度器 | sgm_uniform | - | 5 | 100% |
| 重绘幅度 | 0.25 | 0.1 - 1 | 5 | 24% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 4/5 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，5 个样本，一致性 60%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 100%
- 重绘幅度 中位数 0.25，观测区间 0.1 - 1，5 个样本，取值分散，一致性仅 24%
- 高发问题（4/5 个样本）：发现KSampler但没有VAEDecode
