---
name: unknown_workflow_video_upscale_latent_upscale_56
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.812143
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, ImageResizeKJv2, ImageScaleToTotalPixels, KSamplerSelect, LTX2_NAG, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PreviewAudio, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, SoundFlow_GetLength, TrimAudioDuration, UNETLoader, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy int, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2068875271280873474.json, 视频生成/图生视频/2069018499376312322.json, 视频生成/图生视频/2069213658181365761.json, 视频生成/图生视频/2068898654504706050.json, 视频生成/图生视频/2069966527956344833.json, 视频生成/图生视频/2075040945753640962.json, 视频生成/图生视频/图生视频-LTX2.3数字人30S只要10分钟_2095739123867938818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_56

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2068875271280873474.json、视频生成/图生视频/2069018499376312322.json、视频生成/图生视频/2069213658181365761.json、视频生成/图生视频/2068898654504706050.json、视频生成/图生视频/2069966527956344833.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PreviewAudio`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `SoundFlow_GetLength`
- `TrimAudioDuration`
- `UNETLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CM_IntUnaryCondition` —— 6/7 个有
- `CR Prompt Text` —— 6/7 个有
- `CR String To Boolean` —— 6/7 个有
- `ImpactConditionalBranch` —— 6/7 个有
- `IndexTTS2Run` —— 6/7 个有
- `JoinStrings` —— 6/7 个有
- `LTXVTiledVAEDecode` —— 6/7 个有
- `ModelSamplingSD3` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `easy anythingIndexSwitch` —— 6/7 个有
- `ComfySwitchNode` —— 1/7 个有
- `JoinStringMulti` —— 1/7 个有
- `LTX2SamplingPreviewOverride` —— 1/7 个有
- `ResolutionSelector` —— 1/7 个有
- `VAEDecode` —— 1/7 个有
- `easy float` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 25 - 25 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
