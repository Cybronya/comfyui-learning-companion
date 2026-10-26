---
name: unknown_workflow_upscale_sampler_clip_11
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.767333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, ImageUpscaleWithModel, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/分块高清放大工作流_1934782777130688514.json, 图片生成/图生图/图片超级高清放大_1915403255067639810.json, 图片生成/图生图/放大-F.1_1942192673929498626.json, 图片生成/图生图/放大照片无损_1963489445680074754.json, 图片生成/图生图/放大照片无损_1975073868308197377.json, 图片生成/图生图/无损高清放大（新技术）_1963484675418443777.json, 图片生成/图生图/超级好用无损放大照片_1976081180497940482.json, 图片生成/图生图/高清放大工作流（TRANCE）_1925847949354422273.json, 图片生成/图生图/高清放大（零变形）_1953056397183356930.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_11

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/分块高清放大工作流_1934782777130688514.json、图片生成/图生图/图片超级高清放大_1915403255067639810.json、图片生成/图生图/放大-F.1_1942192673929498626.json、图片生成/图生图/放大照片无损_1963489445680074754.json、图片生成/图生图/放大照片无损_1975073868308197377.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `Florence2ModelLoader` —— 8/9 个有
- `Florence2Run` —— 8/9 个有
- `Image Comparer (rgthree)` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `ImageScaleToTotalPixels` —— 7/9 个有
- `LoraLoader` —— 7/9 个有
- `ShowText|pysssss` —— 7/9 个有
- `easy imageListToImageBatch` —— 7/9 个有
- `ImageListToImageBatch` —— 6/9 个有
- `easy cleanGpuUsed` —— 6/9 个有
- `GetNode` —— 5/9 个有
- `ImageScale` —— 5/9 个有
- `ImageScaleBy` —— 5/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/9 个有
- `SeedVR2` —— 5/9 个有
- `SeedVR2BlockSwap` —— 5/9 个有
- `SetNode` —— 5/9 个有
- `easy imageSize` —— 5/9 个有
- `easy imageSizeBySide` —— 5/9 个有
- `ImageResize+` —— 3/9 个有
- `Constant Number` —— 2/9 个有
- `easy imageInsetCrop` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `ImageListToBatch+` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `Text Find and Replace` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.8 - 1 | 7 | 93% |
| LoRA 文本强度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，7 个样本，取值集中（一致性 93%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
