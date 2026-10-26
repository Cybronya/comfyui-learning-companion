---
name: text_to_image_upscale_lora_sampler_14
type: Text To Image
frequency: 10
level: strong
coverage: 0.9109
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPLoader_Any, CLIPTextEncode, EmptyLatentImage, ImageScaleToTotalPixels, ImageScaleToTotalPixelsX, ImageUpscaleWithModel, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader, UNETLoader_Any, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, VAELoader_Any, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy imageSize, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI换装去脏自己搞定｜图生图服装随心替换_2098724556809789441.json, 图片生成/图生图/flux2-klein-TTP分块放大｜大图细节不发糊_2097153318652047361.json, 图片生成/图生图/flux2-klein-TTP分块高清放大｜Flux2图生图画质增强工作流_2097023123504844801.json, 图片生成/图生图/去噪点去脏图生图修复流｜图片杂质噪点一键清理干净_2108036253957578754.json, 图片生成/图生图/去噪点去脏工作流，图生图图像去噪处理工具_2108445115881709569.json, 图片生成/图生图/目前效果最好flux2-klein-TTP分块放大_2088518950207447041.json, 图片生成/图生图/轻量版zip批量循环｜flux2-klein_TTP分块高清放大_2092084923728490498.json, 图片生成/图生图/轻量版zip批量循环｜flux2-klein_TTP分块高清放大_2092531113288884226.json, 图片生成/图生图/高清放大轻量版工作流｜图像画质无损增强图生图_2094985201125515266.json, 图片生成/图生图/高清放大轻量版工作流｜图像画质无损增强图生图_2095419593996201986.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_14

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/AI换装去脏自己搞定｜图生图服装随心替换_2098724556809789441.json、图片生成/图生图/flux2-klein-TTP分块放大｜大图细节不发糊_2097153318652047361.json、图片生成/图生图/flux2-klein-TTP分块高清放大｜Flux2图生图画质增强工作流_2097023123504844801.json、图片生成/图生图/去噪点去脏图生图修复流｜图片杂质噪点一键清理干净_2108036253957578754.json、图片生成/图生图/去噪点去脏工作流，图生图图像去噪处理工具_2108445115881709569.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPLoader_Any`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixelsX`
- `ImageUpscaleWithModel`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader`
- `UNETLoader_Any`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VAELoader_Any`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`
- `easy imageSize`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 8/10 个有
- `SaveImageJPG_GH` —— 8/10 个有
- `SaveImage` —— 6/10 个有
- `孤海注释` —— 6/10 个有
- `ImageScaleBy` —— 4/10 个有
- `PreviewImage` —— 4/10 个有
- `LayerFilter: FilmV2` —— 3/10 个有
- `easy float` —— 3/10 个有
- `Bjornulf_ShowInt` —— 2/10 个有
- `GetNode` —— 2/10 个有
- `INTConstant` —— 2/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/10 个有
- `RHBatchImages:` —— 2/10 个有
- `RHExtractImage` —— 2/10 个有
- `RHUploadZip` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `easy forLoopEnd` —— 2/10 个有
- `easy forLoopStart` —— 2/10 个有
- `easy imageCount` —— 2/10 个有
- `workflow>采样` —— 2/10 个有
- `FilmGrain` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
