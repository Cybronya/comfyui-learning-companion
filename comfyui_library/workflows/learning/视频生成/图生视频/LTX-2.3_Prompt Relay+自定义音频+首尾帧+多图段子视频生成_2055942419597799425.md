---
key: 视频生成/图生视频/LTX-2.3_Prompt Relay+自定义音频+首尾帧+多图段子视频生成_2055942419597799425.json
name: LTX-2.3_Prompt Relay+自定义音频+首尾帧+多图段子视频生成_2055942419597799425.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3_Prompt Relay+自定义音频+首尾帧+多图段子视频生成_2055942419597799425.json
hash: 8fc1e6cfc071f2a2
coverage: 0.467153
learned_at: 2026-10-15 22:37:59
nodes: [UNETLoader, SetNode, VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, CFGGuider, easy imageSize, SetNode, SetLatentNoiseMask, SolidMask, LTXVAudioVAEEncode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, LTXVImgToVideoInplace, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, FL_IntToFloat, RandomNoise, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, GetNode, GetImageRangeFromBatch, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, easy int, GetNode, SetNode, GetNode, SetNode, SetNode, GetNode, LTXVPreprocess, GetNode, SetNode, EmptyLTXVLatentVideo, SetNode, GetNode, SoundFlow_GetLength, SetNode, PreviewImage, SimpleMath+, PathchSageAttentionKJ, SetNode, SetNode, CLIPTextEncode, GetNode, GetNode, CLIPTextEncode, GetNode, LTXVConditioning, LTXVSeparateAVLatent, SamplerCustomAdvanced, GetNode, GetNode, SetNode, LTXVConcatAVLatent, KSamplerSelect, CFGGuider, RandomNoise, LayerUtility: ImageScaleByAspectRatio V2, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, SetNode, SetNode, easy imageSize, SetNode, INTConstant, SetNode, SetNode, LTXVEmptyLatentAudio, GetNode, LTXVConditioning, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, ManualSigmas, SamplerCustomAdvanced, LTXVPreprocess, LTXVPreprocess, PrimitiveNode, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, GetNode, GetNode, ConditioningZeroOut, SetNode, CLIPTextEncode, PromptRelayEncodeTimeline, GetNode, VHS_VideoCombine, VAEDecode, GetNode, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVCropGuides, GetNode, VHS_VideoCombine, LTXVAudioVAEDecode, VHS_VideoCombine, VHS_VideoCombine, FlashVSRNode, FlashVSRNode, GetNode, GetNode, LTXVAddGuideMulti, GetNode, LoadAudio, DualCLIPLoader, LoraLoaderModelOnly, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 337}
---

# 视频生成/图生视频/LTX-2.3_Prompt Relay+自定义音频+首尾帧+多图段子视频生成_2055942419597799425.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2055942419597799425.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（137 个）：
- `UNETLoader` ★核心
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `CFGGuider`
- `easy imageSize`
- `SetNode`
- `SetLatentNoiseMask`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `FL_IntToFloat`
- `RandomNoise`
- `PrimitiveInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `easy int`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVPreprocess`
- `GetNode`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `GetNode`
- `SoundFlow_GetLength`
- `SetNode`
- `PreviewImage`
- `SimpleMath+`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `RandomNoise`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `SetNode`
- `easy imageSize`
- `SetNode`
- `INTConstant`
- `SetNode`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `LTXVConditioning`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVPreprocess`
- `LTXVPreprocess`
- `PrimitiveNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `SetNode`
- `CLIPTextEncode` ★核心
- `PromptRelayEncodeTimeline`
- `GetNode`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVCropGuides`
- `GetNode`
- `VHS_VideoCombine`
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `FlashVSRNode`
- `FlashVSRNode`
- `GetNode`
- `GetNode`
- `LTXVAddGuideMulti`
- `GetNode`
- `LoadAudio`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `337`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **47%**（64/137）

**有卡**：`UNETLoader`、`VAELoaderKJ`、`CFGGuider`、`easy imageSize`、`SetLatentNoiseMask`、`SolidMask`、`LTXVAudioVAEEncode`、`LTXVImgToVideoInplace`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`FL_IntToFloat`、`RandomNoise`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageRangeFromBatch`、`easy int`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`SoundFlow_GetLength`、`SimpleMath+`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`INTConstant`、`LTXVEmptyLatentAudio`、`ConditioningZeroOut`、`PromptRelayEncodeTimeline`、`VHS_VideoCombine`、`VAEDecode`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXVCropGuides`、`FlashVSRNode`、`LTXVAddGuideMulti`、`LoadAudio`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
