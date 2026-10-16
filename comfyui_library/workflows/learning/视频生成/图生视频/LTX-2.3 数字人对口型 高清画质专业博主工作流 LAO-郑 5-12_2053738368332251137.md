---
key: 视频生成/图生视频/LTX-2.3 数字人对口型 高清画质专业博主工作流 LAO-郑 5-12_2053738368332251137.json
name: LTX-2.3 数字人对口型 高清画质专业博主工作流 LAO-郑 5-12_2053738368332251137.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2053738368332251137.json
hash: c1543083a70a2af2
coverage: 0.507812
learned_at: 2026-10-15 22:37:42
nodes: [LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVLatentUpsampler, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, VAEDecodeTiled, GetNode, SamplerCustom, SetNode, Seed (rgthree), LatentUpscaleModelLoader, DualCLIPLoader, VAELoader, VAELoaderKJ, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, LTXVChunkFeedForward, PathchSageAttentionKJ, SetNode, SetNode, SetNode, SetNode, PrimitiveBoolean, INTConstant, INTConstant, INTConstant, GetNode, GetNode, GetNode, GetNode, SimpleMath+, ManualSigmas, UNETLoader, LoraLoaderModelOnly, GetNode, KSamplerSelect, GetNode, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode, LTXVPreprocess, GetNode, EmptyLTXVLatentVideo, GetNode, GetNode, GetNode, SetNode, LTXVImgToVideoInplace, LTXVConcatAVLatent, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, LTXVConditioning, SetNode, SetNode, ImageResizeKJv2, SetNode, ResizeImagesByLongerEdge, SetNode, JDC_ResizeFactor, SetNode, SetNode, GetImageSize, GetNode, GetNode, LTXVScheduler, KSamplerSelect, GetNode, GetNode, GetNode, SamplerCustom, SetNode, ManualSigmas, LTXVScheduler, GetNode, SetNode, LTX2_NAG, Display Any (rgthree), SimpleMath+, AudioInfo, SimpleMath+, GetNode, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PreviewAudio, PreviewAudio, SetNode, SetNode, LTXVAudioVAEEncode, SetLatentNoiseMask, GetNode, SolidMask, SetNode, GetNode, GetNode, TextInput_, TextInput_, TextInput_, RH_LLMAPI_NODE, ShowText|pysssss, SetNode, GetNode, JoinStrings, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, LoadAudio, AudioCrop, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadAudio]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX-2.3 数字人对口型 高清画质专业博主工作流 LAO-郑 5-12_2053738368332251137.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2053738368332251137.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（128 个）：
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `SamplerCustom` ★核心
- `SetNode`
- `Seed (rgthree)`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveBoolean`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `ManualSigmas`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `JDC_ResizeFactor`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `GetNode`
- `GetNode`
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustom` ★核心
- `SetNode`
- `ManualSigmas`
- `LTXVScheduler`
- `GetNode`
- `SetNode`
- `LTX2_NAG`
- `Display Any (rgthree)`
- `SimpleMath+`
- `AudioInfo`
- `SimpleMath+`
- `GetNode`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `PreviewAudio`
- `PreviewAudio`
- `SetNode`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `GetNode`
- `SolidMask`
- `SetNode`
- `GetNode`
- `GetNode`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `SetNode`
- `GetNode`
- `JoinStrings`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadAudio`
- `AudioCrop`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`

## 知识

覆盖率 **51%**（65/128）

**有卡**：`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`SamplerCustom`、`Seed (rgthree)`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`PrimitiveBoolean`、`INTConstant`、`SimpleMath+`、`ManualSigmas`、`UNETLoader`、`LoraLoaderModelOnly`、`KSamplerSelect`、`VHS_VideoCombine`、`CLIPTextEncode`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`ImageResizeKJv2`、`ResizeImagesByLongerEdge`、`JDC_ResizeFactor`、`GetImageSize`、`LTXVScheduler`、`LTX2_NAG`、`Display Any (rgthree)`、`AudioInfo`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`PreviewAudio`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`TextInput_`、`RH_LLMAPI_NODE`、`JoinStrings`、`LoadImage`、`LoadAudio`、`AudioCrop`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、MelBandRoFormerSampler
