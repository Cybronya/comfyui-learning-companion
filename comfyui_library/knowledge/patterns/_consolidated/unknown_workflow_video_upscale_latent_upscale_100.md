---
name: unknown_workflow_video_upscale_latent_upscale_100
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.927
common_nodes: [1hew_AudioDuration, BasicScheduler, CFGGuider, CLIPTextEncode, CM_FloatToInt, CM_IntToFloat, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, INTConstant, ImageFromBatch, ImageResizeKJv2, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVEnhanceAVideoKJ, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: NumberCalculatorV2, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveFloat, RTXVideoSuperResolution, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, Text, TrimAudioDuration, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ, easy positive]
problems: []
missing: []
members: [视频生成/图生视频/解说漫-三图声音控时长V1_2054612092153548802.json, 视频生成/图生视频/解说漫-三图音频_2054399661825380353.json, 视频生成/图生视频/解说漫-二图声音控时长V1_2057031917425487874.json, 视频生成/图生视频/解说漫-二图声音控时长_2054997494110670850.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_100

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/解说漫-三图声音控时长V1_2054612092153548802.json、视频生成/图生视频/解说漫-三图音频_2054399661825380353.json、视频生成/图生视频/解说漫-二图声音控时长V1_2057031917425487874.json、视频生成/图生视频/解说漫-二图声音控时长_2054997494110670850.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `1hew_AudioDuration`
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CM_IntToFloat`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVEnhanceAVideoKJ`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: NumberCalculatorV2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RTXVideoSuperResolution`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `Text`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 3/4 个有
- `LTXVAddGuideMulti` —— 2/4 个有
- `LTXVAddGuideMultiDynamic` —— 2/4 个有
- `STGGuiderAdvanced` —— 2/4 个有
- `LTXVAudioVAEEncode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 24 - 25 | 4 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，4 个样本，取值集中（一致性 98%）
