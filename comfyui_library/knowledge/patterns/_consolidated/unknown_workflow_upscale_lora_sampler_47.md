---
name: unknown_workflow_upscale_lora_sampler_47
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.67275
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, FluxGuidance, GetNode, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, ImpactImageBatchToImageList, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/一键反推提示词——TTP高清放大工作流_1856530108285915137.json, 图片生成/图生图/10秒图生图反推提示词_1889569357415047169.json, 图片生成/图生图/FluxGirl产品图衣服_2012758919466196993.json, 图片生成/文生图/FLUX无损高清放大修复    波浪Ai_1894631241784930305.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_47

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/一键反推提示词——TTP高清放大工作流_1856530108285915137.json、图片生成/图生图/10秒图生图反推提示词_1889569357415047169.json、图片生成/图生图/FluxGirl产品图衣服_2012758919466196993.json、图片生成/文生图/FLUX无损高清放大修复    波浪Ai_1894631241784930305.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 3/4 个有
- `CLIPTextEncode` —— 3/4 个有
- `DeepTranslatorTextNode` —— 3/4 个有
- `DepthAnythingPreprocessor` —— 3/4 个有
- `LayerFilter: FilmV2` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `RH_Captioner` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `DisableNoise` —— 1/4 个有
- `EmptyLatentImage` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Int` —— 1/4 个有
- `LayerUtility: ImageBlendAdvance` —— 1/4 个有
- `ModelSamplingFlux` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `SaveImageAndMetadata_` —— 1/4 个有
- `Seed Everywhere` —— 1/4 个有
- `SplitSigmasDenoise` —— 1/4 个有
- `VAEDecode` —— 1/4 个有
- `workflow/展示文本` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 1 | 100% |
| 高度 | 512 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
