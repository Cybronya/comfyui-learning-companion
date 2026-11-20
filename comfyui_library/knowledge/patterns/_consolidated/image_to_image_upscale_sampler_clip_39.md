---
name: image_to_image_upscale_sampler_clip_39
type: Image To Image
frequency: 4
level: strong
coverage: 0.82
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Florence2ModelLoader, Florence2Run, GetNode, Image Comparer (rgthree), ImageFromBatch, ImageResize+, ImageScaleToTotalPixels, ImageTile+, ImageUntile+, ImageUpscaleWithModel, KSampler, LoadImage, PreviewImage, RH_Captioner_Pro, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UltimateSDUpscaleNoUpscale, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize, easy int]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/zimage分块放大高清细节_2057662040130539522.json, 图片生成/图生图/zimage分块放大高清细节_2061057523846828034.json, 平台全量/z-image分块放大_2048963225928081410.json, 平台全量/分块放大 z-image_2051972624342892546.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_39

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/zimage分块放大高清细节_2057662040130539522.json、图片生成/图生图/zimage分块放大高清细节_2061057523846828034.json、平台全量/z-image分块放大_2048963225928081410.json、平台全量/分块放大 z-image_2051972624342892546.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageFromBatch`
- `ImageResize+`
- `ImageScaleToTotalPixels`
- `ImageTile+`
- `ImageUntile+`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `RH_Captioner_Pro`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UltimateSDUpscaleNoUpscale`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy imageSize`
- `easy int`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 5 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | dpmpp_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 0.15 | 0.15 - 0.15 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 4/4 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 5，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 0.15，观测区间 0.15 - 0.15，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
- 高发问题（4/4 个样本）：发现KSampler但没有VAEDecode
