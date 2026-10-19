---
name: unknown_workflow_upscale_latent_upscale_lora_45
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.8455
common_nodes: [Any Switch (rgthree), Audio Duration (mtb), AudioCrop, CFGGuider, CLIPTextEncode, CreateVideo, EmptyLTXVLatentVideo, GetImageSize, ImageResizeKJv2, KSamplerSelect, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, PreviewAny, PrimitiveBoolean, PrimitiveInt, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, SaveVideo, SetLatentNoiseMask, Sigmas Rescale, SimpleMathDual+, SolidMask, VAEDecodeTiled, easy convertAnything, easy ifElse, easy positive]
problems: []
missing: []
members: [视频生成/图生视频/2030925818993582082.json, 视频生成/图生视频/2031738492585254914.json, 视频生成/图生视频/2031034066862084097.json, 视频生成/图生视频/2045119325643743233.json, 视频生成/图生视频/2045304246991593473.json, 视频生成/文生视频/LTX2.3 文_图_音_生视频 1080P 多合一_2030698400957603841.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_45

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2030925818993582082.json、视频生成/图生视频/2031738492585254914.json、视频生成/图生视频/2031034066862084097.json、视频生成/图生视频/2045119325643743233.json、视频生成/图生视频/2045304246991593473.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Audio Duration (mtb)`
- `AudioCrop`
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetLatentNoiseMask`
- `Sigmas Rescale`
- `SimpleMathDual+`
- `SolidMask`
- `VAEDecodeTiled`
- `easy convertAnything`
- `easy ifElse`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 5/6 个有
- `LTXVAudioVAELoader` —— 5/6 个有
- `LTXVEnhanceAVideoKJ` —— 5/6 个有
- `easy float` —— 5/6 个有
- `ImageBatchMulti` —— 3/6 个有
- `ImageScaleToTotalPixels` —— 3/6 个有
- `LTXVAddGuideMulti` —— 3/6 个有
- `PrimitiveString` —— 3/6 个有
- `ResizeImagesByShorterEdge` —— 3/6 个有
- `SimpleMath+` —— 3/6 个有
- `TextSplitByDelimiter` —— 3/6 个有
- `easy batchAnything` —— 3/6 个有
- `easy forLoopEnd` —— 3/6 个有
- `easy forLoopStart` —— 3/6 个有
- `easy imagesSplitImage` —— 3/6 个有
- `easy indexAnything` —— 3/6 个有
- `easy int` —— 3/6 个有
- `easy lengthAnything` —— 3/6 个有
- `CM_IntToFloat` —— 2/6 个有
- `GetNode` —— 2/6 个有
- `LTX2SamplingPreviewOverride` —— 2/6 个有
- `LayerUtility: PurgeVRAM V2` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `VHS_VideoCombine` —— 2/6 个有
- `图像缩放V2_孤海` —— 2/6 个有
- `DeepTranslatorTextNode` —— 1/6 个有
- `ImpactSwitch` —— 1/6 个有
- `PrimitiveFloat` —— 1/6 个有
- `UNETLoader` —— 1/6 个有
- `VAELoader` —— 1/6 个有
- `easy anythingIndexSwitch` —— 1/6 个有
- `easy blocker` —— 1/6 个有
- `easy compare` —— 1/6 个有
- `easy mathInt` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 25 - 25 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
