---
name: unknown_workflow_upscale_clip_vae
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8595
common_nodes: [CLIPTextEncode, GetImageSize+, Image Comparer (rgthree), Image Tiled, ImageFromBatch, ImageResize+, ImageScaleBy, ImageUpscaleWithModel, LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UltimateSDUpscaleNoUpscale, UpscaleModelLoader, easy imageColorMatch]
problems: []
missing: []
members: [图片生成/图生图/超级放大——Seed VR2+TTP+SD_2027970853786357762.json, 平台全量/SEEDVR2+TTP极速一亿像素放大_2000941448604286978.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_vae

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/超级放大——Seed VR2+TTP+SD_2027970853786357762.json、平台全量/SEEDVR2+TTP极速一亿像素放大_2000941448604286978.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `Image Tiled`
- `ImageFromBatch`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UltimateSDUpscaleNoUpscale`
- `UpscaleModelLoader`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 1/2 个有
- `CLIPLoader` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `KOOK_ImageCompression` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `easy float` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
