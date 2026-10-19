---
name: unknown_workflow_upscale_latent_upscale_lora_15
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.915846
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecode]
problems: []
missing: []
members: [视频生成/图生视频/2012083779858337794.json, 视频生成/图生视频/2008825760601088002.json, 视频生成/图生视频/2025561649809199106.json, 视频生成/图生视频/2008521515309998081.json, 视频生成/图生视频/2008777293526732801.json, 视频生成/图生视频/2019249142207352834.json, 视频生成/图生视频/2009275287908913153.json, 视频生成/图生视频/2012538447445106690.json, 视频生成/图生视频/2011488577225494530.json, 视频生成/图生视频/2032297089098588161.json, 视频生成/图生视频/2008723483076861954.json, 视频生成/图生视频/2012047557043687425.json, 视频生成/图生视频/2014309275279036418.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_15

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/2012083779858337794.json、视频生成/图生视频/2008825760601088002.json、视频生成/图生视频/2025561649809199106.json、视频生成/图生视频/2008521515309998081.json、视频生成/图生视频/2008777293526732801.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 10/13 个有
- `ResizeImagesByLongerEdge` —— 10/13 个有
- `VHS_VideoCombine` —— 7/13 个有
- `CreateVideo` —— 6/13 个有
- `ImageResizeKJv2` —— 6/13 个有
- `SaveVideo` —— 6/13 个有
- `JWInteger` —— 5/13 个有
- `PreviewImage` —— 4/13 个有
- `CR Text` —— 3/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/13 个有
- `MathExpression|pysssss` —— 3/13 个有
- `easy cleanGpuUsed` —— 3/13 个有
- `PreviewAny` —— 2/13 个有
- `AudioAdjustVolume` —— 1/13 个有
- `AudioMerge` —— 1/13 个有
- `CR Prompt Text` —— 1/13 个有
- `DF_Int_to_Float` —— 1/13 个有
- `ImpactSwitch` —— 1/13 个有
- `LoadAudio` —— 1/13 个有
- `MemoryCleaner` —— 1/13 个有
- `RH_LLMAPI_NODE` —— 1/13 个有
- `Resize` —— 1/13 个有
- `ResizeImageMaskNode` —— 1/13 个有
- `TextGenerateLTX2Prompt` —— 1/13 个有
- `TrimAudioDuration` —— 1/13 个有
- `easy promptConcat` —— 1/13 个有
- `easy seed` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 13 | 100% |
| 高度 | 25 | 25 - 25 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，13 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，13 个样本，取值集中（一致性 100%）
