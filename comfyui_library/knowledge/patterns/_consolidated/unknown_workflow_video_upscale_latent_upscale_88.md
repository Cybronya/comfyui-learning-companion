---
name: unknown_workflow_video_upscale_latent_upscale_88
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.55825
common_nodes: [AudioCrop, CFGGuider, CLIPTextEncode, ComfySwitchNode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, ImageScaleBy, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, ManualSigmas, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelPatchTorchSettings, PathchSageAttentionKJ, PreviewAudio, PreviewImage, PrimitiveFloat, RHHiddenNodes, RandomNoise, SamplerCustomAdvanced, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, SetLatentNoiseMask, SetNode, SimpleCalculatorKJ, SimpleMath+, SolidMask, TrimAudioDuration, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy int, easy showAnything]
problems: []
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, LoadDiffusionModelShared //Inspire, MathExpression|pysssss, SimpleMath+, Text Concatenate, easy int]
members: [视频生成/图生视频/2034220843508703234.json, 视频生成/图生视频/1897892598386741250.json, 视频生成/图生视频/1959793923826855938.json, 视频生成/文生视频/1955807480933597185.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_88

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2034220843508703234.json、视频生成/图生视频/1897892598386741250.json、视频生成/图生视频/1959793923826855938.json、视频生成/文生视频/1955807480933597185.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioCrop`
- `CFGGuider`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `ManualSigmas`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PreviewAudio`
- `PreviewImage`
- `PrimitiveFloat`
- `RHHiddenNodes`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleCalculatorKJ`
- `SimpleMath+`
- `SolidMask`
- `TrimAudioDuration`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AudioEvenSplitNode` —— 1/4 个有
- `AudioSelectNode` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `EmptyImage` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetImageRangeFromBatch` —— 1/4 个有
- `GetImageSizeAndCount` —— 1/4 个有
- `ImageStringBatch` —— 1/4 个有
- `ImpactMinMax` —— 1/4 个有
- `ImpactSwitch` —— 1/4 个有
- `LTXAVTextEncoderLoader` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `LoadDiffusionModelShared //Inspire` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `Qwen3_VQA` —— 1/4 个有
- `Qwen3_VQA_Plus` —— 1/4 个有
- `SelectImageString` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `SoundFlow_GetLength` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有
- `easy convertAnything` —— 1/4 个有
- `easy forLoopEnd` —— 1/4 个有
- `easy forLoopStart` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerUtility: ImageScaleByAspectRatio V2、LoadDiffusionModelShared //Inspire、MathExpression|pysssss、SimpleMath+
