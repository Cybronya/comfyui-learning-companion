---
key: 视频生成/文生视频/LTX2.3 数字人说话唱歌对口型 深度优化升级kj版_2056553193026449410.json
name: LTX2.3 数字人说话唱歌对口型 深度优化升级kj版_2056553193026449410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 数字人说话唱歌对口型 深度优化升级kj版_2056553193026449410.json
hash: f22f011d00a0d847
coverage: 0.46087
learned_at: 2026-10-11 19:49:37
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, SolidMask, GetNode, GetNode, GetNode, SetNode, SetNode, LTXVConcatAVLatent, SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, LTXVAudioVAEEncode, VAELoader, INTConstant, INTConstant, ImageResizeKJv2, SetNode, SetNode, DualCLIPLoader, VAELoader, GetNode, JoinStrings, UNETLoader, SetNode, LTXVConditioning, GetNode, VAEDecode, LayerUtility: PurgeVRAM, LTXVSeparateAVLatent, LoraLoaderModelOnly, PrimitiveFloat, LTXVCropGuides, INTConstant, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, VAELoaderKJ, SetLatentNoiseMask, SimpleCalculatorKJ, LTXVChunkFeedForward, SetNode, LTXVPreprocess, MelBandRoFormerModelLoader, RandomNoise, GetNode, GetNode, GetNode, SetNode, GetImageSize, ResizeImageMaskNode, SetNode, SetNode, SetNode, SetNode, CLIPTextEncode, CFGGuider, ModelSamplingSD3, SetNode, BasicScheduler, ImageResizeKJv2, GetNode, SetNode, MelBandRoFormerSampler, TrimAudioDuration, PrimitiveStringMultiline, LTXVImgToVideoInplaceKJ, LTX2_NAG, GetNode, CLIPTextEncode, LTX2SamplingPreviewOverride, TrimAudioDuration, LatentUpscaleModelLoader, LayerUtility: PurgeVRAM, EmptyLTXVLatentVideo, PrimitiveFloat, PathchSageAttentionKJ, LTX2AttentionTunerPatch, Int, SimpleMath+, SimpleMath+, KSamplerSelect, SetNode, SamplerCustomAdvanced, GetNode, GetNode, SetNode, GetNode, ComfySwitchNode, SetNode, SimpleMath+, SetNode, Compare, InversionDemoLazySwitch, SetNode, easy showAnything, VHS_VideoCombine, VHS_LoadAudioUpload, PreviewAudio, LoadImage, INTConstant, GetNode, SetNode, INTConstant, PrimitiveStringMultiline]
patterns: []
missing: [LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SimpleMath+, SimpleMath+, SimpleMath+]
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3 数字人说话唱歌对口型 深度优化升级kj版_2056553193026449410.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 数字人说话唱歌对口型 深度优化升级kj版_2056553193026449410.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（115 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SolidMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `VAELoader`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `DualCLIPLoader`
- `VAELoader`
- `GetNode`
- `JoinStrings`
- `UNETLoader` ★核心
- `SetNode`
- `LTXVConditioning`
- `GetNode`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `LTXVCropGuides`
- `INTConstant`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAELoaderKJ`
- `SetLatentNoiseMask`
- `SimpleCalculatorKJ`
- `LTXVChunkFeedForward`
- `SetNode`
- `LTXVPreprocess`
- `MelBandRoFormerModelLoader`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetImageSize`
- `ResizeImageMaskNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `ModelSamplingSD3`
- `SetNode`
- `BasicScheduler`
- `ImageResizeKJv2`
- `GetNode`
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `TrimAudioDuration`
- `PrimitiveStringMultiline`
- `LTXVImgToVideoInplaceKJ`
- `LTX2_NAG`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LTX2SamplingPreviewOverride`
- `TrimAudioDuration`
- `LatentUpscaleModelLoader`
- `LayerUtility: PurgeVRAM`
- `EmptyLTXVLatentVideo`
- `PrimitiveFloat`
- `PathchSageAttentionKJ`
- `LTX2AttentionTunerPatch`
- `Int`
- `SimpleMath+`
- `SimpleMath+`
- `KSamplerSelect` ★核心
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ComfySwitchNode`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `Compare`
- `InversionDemoLazySwitch`
- `SetNode`
- `easy showAnything`
- `VHS_VideoCombine`
- `VHS_LoadAudioUpload`
- `PreviewAudio`
- `LoadImage`
- `INTConstant`
- `GetNode`
- `SetNode`
- `INTConstant`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **46%**（53/115）

**有卡**：`SolidMask`、`LTXVConcatAVLatent`、`LTXVAudioVAEEncode`、`VAELoader`、`INTConstant`、`ImageResizeKJv2`、`DualCLIPLoader`、`JoinStrings`、`UNETLoader`、`LTXVConditioning`、`VAEDecode`、`LTXVSeparateAVLatent`、`LoraLoaderModelOnly`、`LTXVCropGuides`、`VAELoaderKJ`、`SetLatentNoiseMask`、`SimpleCalculatorKJ`、`LTXVChunkFeedForward`、`LTXVPreprocess`、`MelBandRoFormerModelLoader`、`RandomNoise`、`GetImageSize`、`ResizeImageMaskNode`、`CLIPTextEncode`、`CFGGuider`、`ModelSamplingSD3`、`BasicScheduler`、`MelBandRoFormerSampler`、`TrimAudioDuration`、`LTXVImgToVideoInplaceKJ`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LatentUpscaleModelLoader`、`EmptyLTXVLatentVideo`、`PathchSageAttentionKJ`、`LTX2AttentionTunerPatch`、`Int`、`KSamplerSelect`、`SamplerCustomAdvanced`、`Compare`、`InversionDemoLazySwitch`、`VHS_VideoCombine`、`VHS_LoadAudioUpload`、`PreviewAudio`、`LoadImage`

**缺卡**（5）：`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
