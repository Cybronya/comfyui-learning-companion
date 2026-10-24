---
name: unknown_workflow_video_lora_sampler_608
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.954667
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CFGGuider, CLIPTextEncode, DF_Int_to_Float, DiffusionModelLoaderKJ, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, Int, JWIntegerToString, KSamplerSelect, LTX2_NAG, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, PreviewAudio, RandomNoise, RunningHub_VoxCPM_Generate, RunningHub_VoxCPM_LoadModel, SamplerCustomAdvanced, SamplerEulerAncestral, SetLatentNoiseMask, ShowAnything|Mie, SolidMask, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy getNode, easy int, easy setNode, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3音频参考、图生视频、首尾帧、多帧参考三模一致性_去字幕全面优化版_2051564460493557762.json, 视频生成/图生视频/LTX2.3音频参考、图生视频、首尾帧、多帧参考三模一致性_去字幕全面优化版_2051946649047576577.json, 视频生成/图生视频/VOXCPM2 +LTX 2.3 数字人图生视频V3_2051952349974937602.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_608

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/LTX2.3音频参考、图生视频、首尾帧、多帧参考三模一致性_去字幕全面优化版_2051564460493557762.json、视频生成/图生视频/LTX2.3音频参考、图生视频、首尾帧、多帧参考三模一致性_去字幕全面优化版_2051946649047576577.json、视频生成/图生视频/VOXCPM2 +LTX 2.3 数字人图生视频V3_2051952349974937602.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CFGGuider`
- `CLIPTextEncode`
- `DF_Int_to_Float`
- `DiffusionModelLoaderKJ`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `Int`
- `JWIntegerToString`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `PreviewAudio`
- `RandomNoise`
- `RunningHub_VoxCPM_Generate`
- `RunningHub_VoxCPM_LoadModel`
- `SamplerCustomAdvanced`
- `SamplerEulerAncestral`
- `SetLatentNoiseMask`
- `ShowAnything|Mie`
- `SolidMask`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy getNode`
- `easy int`
- `easy setNode`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `JjkText` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
