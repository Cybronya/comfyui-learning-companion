---
name: unknown_workflow_upscale_sampler_clip_12
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9086
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/Kontext一句话图像万能编辑 +高清放大_1996471448782913538.json, 图片生成/图生图/TTP高清放大（米薯）_1996232515604070402.json, 图片生成/图生图/图片-TTP高清修复放大_1978037084130791426.json, 图片生成/图生图/室内外洗图_2004029442542477314.json, 图片生成/图生图/高清放大_1929750961344954370.json, 平台全量/07.最新产品精修工作流_2000793049980694529.json, 平台全量/Flux极速放大（TTP）_1969976177567952897.json, 平台全量/Kontext 一句话一张图 【一键】图像万能编辑 + TTP高清放大_1954930531898048513.json, 平台全量/产品精修+高清放大_傲雪AIGC_1958509350312636418.json, 平台全量/高清放大-TTP方案_2020439708702085121.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Kontext一句话图像万能编辑 +高清放大_1996471448782913538.json、图片生成/图生图/TTP高清放大（米薯）_1996232515604070402.json、图片生成/图生图/图片-TTP高清修复放大_1978037084130791426.json、图片生成/图生图/室内外洗图_2004029442542477314.json、图片生成/图生图/高清放大_1929750961344954370.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/10 个有
- `easy imageListToImageBatch` —— 6/10 个有
- `Image Comparer (rgthree)` —— 5/10 个有
- `PreviewImage` —— 5/10 个有
- `ImageListToImageBatch` —— 4/10 个有
- `LoraLoader` —— 3/10 个有
- `NunchakuFluxDiTLoader` —— 3/10 个有
- `VAEDecode` —— 3/10 个有
- `CR Simple Image Compare` —— 2/10 个有
- `EmptyLatentImage` —— 2/10 个有
- `FluxResolutionNode` —— 2/10 个有
- `MathExpression|pysssss` —— 2/10 个有
- `ModelSamplingFlux` —— 2/10 个有
- `RH_Translator` —— 2/10 个有
- `ReferenceLatent` —— 2/10 个有
- `ConstrainImage|pysssss` —— 1/10 个有
- `PlaySound|pysssss` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1280 | - | 2 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
