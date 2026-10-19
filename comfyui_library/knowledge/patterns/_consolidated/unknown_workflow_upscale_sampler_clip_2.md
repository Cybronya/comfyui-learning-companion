---
name: unknown_workflow_upscale_sampler_clip_2
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.736667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: [easy imageBatchToImageList, CR Text, LayerUtility: ImageScaleByAspectRatio V2, Text Concatenate (JPS)]
members: [图片生成/文生图/1931964242503905282.json, 图片生成/文生图/1985899421487509506.json, 图片生成/文生图/1989960138809372674.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1931964242503905282.json、图片生成/文生图/1985899421487509506.json、图片生成/文生图/1989960138809372674.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `PreviewImage`
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
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageResizeKJ` —— 2/3 个有
- `Joy_caption_two` —— 2/3 个有
- `Joy_caption_two_load` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `DifferentialDiffusion` —— 1/3 个有
- `EmptyLatentImage` —— 1/3 个有
- `FloatConstant` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoadImagesFromURL` —— 1/3 个有
- `RH_ComfyFluxKontext` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `Text Concatenate (JPS)` —— 1/3 个有
- `VAEDecode` —— 1/3 个有
- `VAEEncodeTiled` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.9 | - | 2 | 89% |
| LoRA 文本强度 | 0.9 | - | 2 | 89% |
| 宽度 | 1360 | - | 1 | 100% |
| 高度 | 768 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy imageBatchToImageList、CR Text、LayerUtility: ImageScaleByAspectRatio V2、Text Concatenate (JPS)
