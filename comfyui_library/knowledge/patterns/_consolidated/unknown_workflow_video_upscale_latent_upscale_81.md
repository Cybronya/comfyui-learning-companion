---
name: unknown_workflow_video_upscale_latent_upscale_81
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8928
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CM_FloatToInt, CM_IntToFloat, CR Text Concatenate, ComfyMathExpression, DualCLIPLoader, EmptyImage, EmptyLTXVLatentVideo, GetImagesFromBatchIndexed, GetNode, INTConstant, ImageAddMulti, ImageBatchMulti, ImageFromBatch, ImageResizeKJv2, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: NumberCalculatorV2, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PreviewImage, PrimitiveFloat, PrimitiveInt, RTXVideoSuperResolution, RandomNoise, RegexExtract, SamplerCustomAdvanced, SetNode, ShowText|pysssss, TrimAudioDuration, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy convertAnything, easy imageRemBg, easy indexAnything, easy positive, easy promptLine, easy promptReplace]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3邪修采样多参人物场景分镜短剧V1_2046412566104121345.json, 视频生成/图生视频/LTX2.3邪修采样多参人物场景分镜短剧V2_2049366462388768769.json, 视频生成/图生视频/LTX2.3邪修采样多参人物场景分镜短剧_2046143007354789890.json, 视频生成/图生视频/多参_2049760575089070082.json, 视频生成/图生视频/多参直连_2050048108033257473.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_81

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/LTX2.3邪修采样多参人物场景分镜短剧V1_2046412566104121345.json、视频生成/图生视频/LTX2.3邪修采样多参人物场景分镜短剧V2_2049366462388768769.json、视频生成/图生视频/LTX2.3邪修采样多参人物场景分镜短剧_2046143007354789890.json、视频生成/图生视频/多参_2049760575089070082.json、视频生成/图生视频/多参直连_2050048108033257473.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CM_IntToFloat`
- `CR Text Concatenate`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImagesFromBatchIndexed`
- `GetNode`
- `INTConstant`
- `ImageAddMulti`
- `ImageBatchMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: NumberCalculatorV2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RTXVideoSuperResolution`
- `RandomNoise`
- `RegexExtract`
- `SamplerCustomAdvanced`
- `SetNode`
- `ShowText|pysssss`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy convertAnything`
- `easy imageRemBg`
- `easy indexAnything`
- `easy positive`
- `easy promptLine`
- `easy promptReplace`

**可变部分**（部分 workflow 才有）：
- `LongTextToList` —— 4/5 个有
- `MultiTextConcatenate` —— 4/5 个有
- `CR Text` —— 3/5 个有
- `LTXVAudioVAELoader` —— 3/5 个有
- `LTXVCropGuides` —— 3/5 个有
- `LTXVEnhanceAVideoKJ` —— 3/5 个有
- `Text Multiline` —— 3/5 个有
- `VisualizeSigmasKJ` —— 3/5 个有
- `CheckpointLoaderSimple` —— 2/5 个有
- `SplitSigmas` —— 2/5 个有
- `easy promptList` —— 2/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
