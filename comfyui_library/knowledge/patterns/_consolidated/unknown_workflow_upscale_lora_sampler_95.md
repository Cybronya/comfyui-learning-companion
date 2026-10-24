---
name: unknown_workflow_upscale_lora_sampler_95
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8345
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Prompt Text, CheckpointLoaderSimple, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxResolutionNode, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, JjkText, KSamplerSelect, LoraLoader, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextCombinerTwo, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [图片生成/图生图/【独一无二】【图生图】【专属定制】_1901982736465158145.json, 图片生成/文生图/3D蛇年定制头像_1882053493610700801.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_95

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【独一无二】【图生图】【专属定制】_1901982736465158145.json、图片生成/文生图/3D蛇年定制头像_1882053493610700801.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxResolutionNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `JjkText`
- `KSamplerSelect`
- `LoraLoader`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextCombinerTwo`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `AegisFlow/aflogo` —— 1/2 个有
- `Anything Everywhere` —— 1/2 个有
- `ApplyPulidFlux` —— 1/2 个有
- `CLIPVisionEncode` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PulidFluxEvaClipLoader` —— 1/2 个有
- `PulidFluxInsightFaceLoader` —— 1/2 个有
- `PulidFluxModelLoader` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `RH_Prompter` —— 1/2 个有
- `StyleModelApplyAdvanced` —— 1/2 个有
- `StyleModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.9 | - | 2 | 89% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1280 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
