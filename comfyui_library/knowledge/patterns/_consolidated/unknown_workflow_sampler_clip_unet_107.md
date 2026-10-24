---
name: unknown_workflow_sampler_clip_unet_107
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8654
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, ImageListToImageBatch, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/无损高清放大工作流｜一键超清_1914134415251861506.json, 图片生成/图生图/无损高清放大工作流｜一键超清_1942154651460595713.json, 图片生成/图生图/极致高清放大_2068619553789276162.json, 图片生成/图生图/电商高清放大  精修处理_2015156106552676353.json, 图片生成/图生图/超清放大 物-景-人 通用_1911244460179582977.json, 图片生成/图生图/超级高清放大，任意图像变无比高清图_1923649088472928257.json, 图片生成/图生图/高清放大  精修处理_2004411744959295490.json, 图片生成/图生图/高清放大(7)flux放大丨支持在线一键生成_1914340386142154754.json, 图片生成/图生图/高清放大_1929750961344954370.json, 图片生成/文生图/kontext 文生图+图生图  后期高清放大_1931964242503905282.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_107

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/无损高清放大工作流｜一键超清_1914134415251861506.json、图片生成/图生图/无损高清放大工作流｜一键超清_1942154651460595713.json、图片生成/图生图/极致高清放大_2068619553789276162.json、图片生成/图生图/电商高清放大  精修处理_2015156106552676353.json、图片生成/图生图/超清放大 物-景-人 通用_1911244460179582977.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 8/10 个有
- `ImageUpscaleWithModel` —— 8/10 个有
- `LoraLoader` —— 8/10 个有
- `UpscaleModelLoader` —— 8/10 个有
- `ImageResizeKJ` —— 5/10 个有
- `Joy_caption_two` —— 5/10 个有
- `Joy_caption_two_load` —— 5/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `ShowText|pysssss` —— 3/10 个有
- `CR Simple Image Compare` —— 2/10 个有
- `ColorMatch` —— 2/10 个有
- `Florence2ModelLoader` —— 2/10 个有
- `Florence2Run` —— 2/10 个有
- `GetNode` —— 2/10 个有
- `PlaySound|pysssss` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `workflow>放大预处理` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `PMRF` —— 1/10 个有
- `RH_ComfyFluxKontext` —— 1/10 个有
- `RH_Translator` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 8 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
