---
name: unknown_workflow_upscale_lora_clip_4
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.8015
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageColorMatch]
problems: []
missing: []
members: [图片生成/图生图/Klein 4K直出_0畸变_高清放大_2075474900155977729.json, 图片生成/图生图/klein-直出4K_高清放大_0变形_2080934747756392449.json, 图片生成/图生图/klein-直出4K_高清放大_0变形_2095798320995332097.json, 图片生成/图生图/klein-直出4K_高清放大_0变形_2096155179845509122.json, 图片生成/图生图/商用级-klein-高清4k修复0偏移_2076555894371999746.json, 图片生成/图生图/白膜渲染_2102580135840018433.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_clip_4

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Klein 4K直出_0畸变_高清放大_2075474900155977729.json、图片生成/图生图/klein-直出4K_高清放大_0变形_2080934747756392449.json、图片生成/图生图/klein-直出4K_高清放大_0变形_2095798320995332097.json、图片生成/图生图/klein-直出4K_高清放大_0变形_2096155179845509122.json、图片生成/图生图/商用级-klein-高清4k修复0偏移_2076555894371999746.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `FL_ImageBatchToImageList` —— 5/6 个有
- `FL_ImageListToImageBatch` —— 5/6 个有
- `GetImageSize` —— 5/6 个有
- `ImageResizeKJv2` —— 5/6 个有
- `ImageScale` —— 5/6 个有
- `KSamplerAdvanced` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `TTP_Tile_image_size` —— 5/6 个有
- `Anything Everywhere` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `BasicGuider` —— 2/6 个有
- `BasicScheduler` —— 2/6 个有
- `CLIPLoader_Any` —— 2/6 个有
- `ImageScaleToTotalPixelsX` —— 2/6 个有
- `KSamplerSelect` —— 2/6 个有
- `RandomNoise` —— 2/6 个有
- `SamplerCustomAdvanced` —— 2/6 个有
- `SaveImageJPG_GH` —— 2/6 个有
- `UNETLoader_Any` —— 2/6 个有
- `VAELoader_Any` —— 2/6 个有
- `easy imageBatchToImageList` —— 2/6 个有
- `easy imageListToImageBatch` —— 2/6 个有
- `easy imageSize` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `Flux2Scheduler` —— 1/6 个有
- `FluxGuidance` —— 1/6 个有
- `Joy_caption_two_advanced` —— 1/6 个有
- `Joy_caption_two_load` —— 1/6 个有
- `OllamaCaptionerExtraOptions` —— 1/6 个有
- `PainterFluxImageEdit` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `Text Concatenate (JPS)` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | sa_solver | - | 5 | 100% |
| 重绘幅度 | FlowMatchEulerDiscreteScheduler | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 sa_solver，5 个样本，一致性 100%
- 重绘幅度 最常用 FlowMatchEulerDiscreteScheduler，5 个样本，一致性 100%
