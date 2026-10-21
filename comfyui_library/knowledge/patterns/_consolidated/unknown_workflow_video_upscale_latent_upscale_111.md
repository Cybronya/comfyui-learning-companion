---
name: unknown_workflow_video_upscale_latent_upscale_111
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.619333
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, GuHaiAutoImageSplit, ImageFromBatch+, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PreviewImage, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleMath+, Text, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2046461995771236354.json, 视频生成/图生视频/2037855814051958786.json, 视频生成/图生视频/2041772367239712769.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_111

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2046461995771236354.json、视频生成/图生视频/2037855814051958786.json、视频生成/图生视频/2041772367239712769.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GuHaiAutoImageSplit`
- `ImageFromBatch+`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleMath+`
- `Text`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Float To Integer` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `LTXVEmptyLatentAudio` —— 2/3 个有
- `LoadAudio` —— 2/3 个有
- `MelBandRoFormerModelLoader` —— 2/3 个有
- `MelBandRoFormerSampler` —— 2/3 个有
- `PreviewAudio` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `easy anythingIndexSwitch` —— 2/3 个有
- `AudioCrop` —— 1/3 个有
- `AudioInfo` —— 1/3 个有
- `CM_IntToFloat` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `DapaoSmartMemoryOptimizerNode` —— 1/3 个有
- `Display Any (rgthree)` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImpactInversedSwitch` —— 1/3 个有
- `LTXVAudioVAEEncode` —— 1/3 个有
- `LTXVReferenceAudio` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `NormalizeAudioLoudness` —— 1/3 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `SetLatentNoiseMask` —— 1/3 个有
- `SolidMask` —— 1/3 个有
- `TTResolutionSelector` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有
- `easy int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
