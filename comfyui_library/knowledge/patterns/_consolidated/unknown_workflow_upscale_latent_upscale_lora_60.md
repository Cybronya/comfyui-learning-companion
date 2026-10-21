---
name: unknown_workflow_upscale_latent_upscale_lora_60
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.78725
common_nodes: [CFGGuider, CLIPTextEncode, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/2044772850472591362.json, 视频生成/图生视频/2018342004555522049.json, 视频生成/图生视频/2008987818990772225.json, 视频生成/图生视频/2008792079337529345.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_60

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2044772850472591362.json、视频生成/图生视频/2018342004555522049.json、视频生成/图生视频/2008987818990772225.json、视频生成/图生视频/2008792079337529345.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 3/4 个有
- `EmptyImage` —— 3/4 个有
- `GetImageSize` —— 3/4 个有
- `ImageScaleBy` —— 3/4 个有
- `LTXAVTextEncoderLoader` —— 3/4 个有
- `LTXVAudioVAELoader` —— 3/4 个有
- `LTXVScheduler` —— 3/4 个有
- `ResizeImagesByLongerEdge` —— 3/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `ImpactExecutionOrderController` —— 2/4 个有
- `LTXVCropGuides` —— 2/4 个有
- `LTXVGemmaEnhancePrompt` —— 2/4 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `VAEDecodeTiled` —— 2/4 个有
- `CM_FloatToInt` —— 1/4 个有
- `DF_Int_to_Float` —— 1/4 个有
- `DualCLIPLoader` —— 1/4 个有
- `Float to Int` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `JWStringReplace` —— 1/4 个有
- `LTXVGemmaCLIPModelLoader` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `TextInput_` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `VAELoaderKJ` —— 1/4 个有
- `WanVideoImageResizeToClosest` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有
- `easy float` —— 1/4 个有
- `easy int` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 109 | 97 - 121 | 4 | 89% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 109，观测区间 97 - 121，4 个样本，取值集中（一致性 89%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
