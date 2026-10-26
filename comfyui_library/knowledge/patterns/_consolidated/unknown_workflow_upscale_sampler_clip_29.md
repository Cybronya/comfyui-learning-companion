---
name: unknown_workflow_upscale_sampler_clip_29
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9098
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/Kontext一句话图像万能编辑 +高清放大_1996471448782913538.json, 图片生成/图生图/TTP高清放大（米薯）_1996232515604070402.json, 图片生成/图生图/图片-TTP高清修复放大_1978037084130791426.json, 图片生成/图生图/室内外洗图_2004029442542477314.json, 图片生成/图生图/高清放大_1929750961344954370.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Kontext一句话图像万能编辑 +高清放大_1996471448782913538.json、图片生成/图生图/TTP高清放大（米薯）_1996232515604070402.json、图片生成/图生图/图片-TTP高清修复放大_1978037084130791426.json、图片生成/图生图/室内外洗图_2004029442542477314.json、图片生成/图生图/高清放大_1929750961344954370.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
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
- `easy imageListToImageBatch` —— 4/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `NunchakuFluxDiTLoader` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `VAEDecode` —— 2/5 个有
- `ConstrainImage|pysssss` —— 1/5 个有
- `EmptyLatentImage` —— 1/5 个有
- `FluxResolutionNode` —— 1/5 个有
- `ImageListToImageBatch` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `ModelSamplingFlux` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `ReferenceLatent` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1280 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
