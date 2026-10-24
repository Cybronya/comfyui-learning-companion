---
name: unknown_workflow_upscale_sampler_clip_11
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.925125
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/Kontext一句话图像万能编辑 +高清放大_1996471448782913538.json, 图片生成/图生图/TTP高清放大（米薯）_1996232515604070402.json, 图片生成/图生图/图像TTP分块放大 增加真实细节  高清修复放大-TTP放大 写实4K 万物通用版v1.0_2094731786977890306.json, 图片生成/图生图/图像超分-10.23-flux-tile放大_1981552116315635713.json, 图片生成/图生图/室内外洗图_2004029442542477314.json, 图片生成/图生图/室内外洗图洗稿2.0丨超强质感3k高清_1925214634473627650.json, 图片生成/图生图/室内建筑场景洗图+高清修复_1937868192171606018.json, 图片生成/图生图/室内建筑场景洗图+高清修复_1976190617967558657.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_11

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Kontext一句话图像万能编辑 +高清放大_1996471448782913538.json、图片生成/图生图/TTP高清放大（米薯）_1996232515604070402.json、图片生成/图生图/图像TTP分块放大 增加真实细节  高清修复放大-TTP放大 写实4K 万物通用版v1.0_2094731786977890306.json、图片生成/图生图/图像超分-10.23-flux-tile放大_1981552116315635713.json、图片生成/图生图/室内外洗图_2004029442542477314.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageScaleToTotalPixels`
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
- `Image Comparer (rgthree)` —— 7/8 个有
- `ImageListToImageBatch` —— 5/8 个有
- `LoraLoader` —— 5/8 个有
- `VAEDecode` —— 5/8 个有
- `ConstrainImage|pysssss` —— 4/8 个有
- `ImageResizeKJ` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `Float` —— 3/8 个有
- `easy imageListToImageBatch` —— 3/8 个有
- `LayerMask: LoadFlorence2Model` —— 2/8 个有
- `LayerUtility: Florence2Image2Prompt` —— 2/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `EmptyLatentImage` —— 1/8 个有
- `Florence2ModelLoader` —— 1/8 个有
- `Florence2Run` —— 1/8 个有
- `FluxResolutionNode` —— 1/8 个有
- `Joy_caption_two` —— 1/8 个有
- `Joy_caption_two_load` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `LoadImagesFromURL` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `ModelSamplingFlux` —— 1/8 个有
- `NunchakuFluxDiTLoader` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `ReferenceLatent` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1280 | - | 1 | 100% |
| LoRA 模型强度 | 0.5 | 0.5 - 1 | 5 | 65% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.5，观测区间 0.5 - 1，5 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
