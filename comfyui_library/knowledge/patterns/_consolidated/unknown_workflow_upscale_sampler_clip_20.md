---
name: unknown_workflow_upscale_sampler_clip_20
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.754167
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoadImage, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/10秒图生图反推提示词_1889569357415047169.json, 图片生成/图生图/4Kttpflux 放大工作流 api 版本_1984539387545468930.json, 图片生成/图生图/F1一键精修+放大，金属，户外带通用_1993247312828891137.json, 图片生成/图生图/FLUX-高清修复-保留细节_1963975272259272705.json, 图片生成/文生图/FLUX-高清修复-不改变人物_商品主体细节-API便捷调用版_1989960138809372674.json, 图片生成/文生图/FLUX无损高清放大修复    波浪Ai_1894631241784930305.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_20

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/10秒图生图反推提示词_1889569357415047169.json、图片生成/图生图/4Kttpflux 放大工作流 api 版本_1984539387545468930.json、图片生成/图生图/F1一键精修+放大，金属，户外带通用_1993247312828891137.json、图片生成/图生图/FLUX-高清修复-保留细节_1963975272259272705.json、图片生成/文生图/FLUX-高清修复-不改变人物_商品主体细节-API便捷调用版_1989960138809372674.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
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

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `easy imageBatchToImageList` —— 4/6 个有
- `ImageListToImageBatch` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `ShowText|pysssss` —— 3/6 个有
- `Anything Everywhere` —— 2/6 个有
- `CR Text` —— 2/6 个有
- `DeepTranslatorTextNode` —— 2/6 个有
- `DifferentialDiffusion` —— 2/6 个有
- `FloatConstant` —— 2/6 个有
- `ImpactImageBatchToImageList` —— 2/6 个有
- `Joy_caption_two` —— 2/6 个有
- `Joy_caption_two_load` —— 2/6 个有
- `LoraLoader` —— 2/6 个有
- `Text Concatenate (JPS)` —— 2/6 个有
- `VAEEncodeTiled` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `DepthAnythingPreprocessor` —— 1/6 个有
- `ImageListToBatch+` —— 1/6 个有
- `LayerFilter: FilmV2` —— 1/6 个有
- `LoadImagesFromURL` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `workflow/展示文本` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
