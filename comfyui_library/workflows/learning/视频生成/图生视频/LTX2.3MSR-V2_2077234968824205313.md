---
key: 视频生成/图生视频/LTX2.3MSR-V2_2077234968824205313.json
name: LTX2.3MSR-V2_2077234968824205313.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2077234968824205313.json
hash: de4928aef96bce72
coverage: 0.462185
learned_at: 2026-10-15 22:41:37
nodes: [LTXVSeparateAVLatent, PathchSageAttentionKJ, RandomNoise, KSamplerSelect, LTXVConcatAVLatent, LatentUpscaleModelLoader, SamplerCustomAdvanced, ManualSigmas, GetNode, GetNode, GetNode, CLIPTextEncode, GetNode, GetNode, LTXVLatentUpsampler, GetNode, Reroute, GetNode, GetNode, GetNode, VAEDecodeTiled, LTXVSeparateAVLatent, SetNode, FrameInterpolate, RTXVideoSuperResolution, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, ComfyMathExpression, SetNode, VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, SetNode, ComfyMathExpression, SetNode, ComfyMathExpression, SetNode, SetNode, DualCLIPLoader, SetNode, LTXVCropGuides, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SamplerCustomAdvanced, GetNode, SetNode, LTXVConditioning, GetNode, LTXAddVideoICLoRAGuide, ComfyMathExpression, LTXVAudioVAEDecode, GetNode, LTXVCropGuides, GetNode, GetNode, LayerUtility: PurgeVRAM, FrameInterpolationModelLoader, ManualSigmas, LTXICLoRALoaderModelOnly, CLIPTextEncode, GetNode, RandomNoise, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, UNETLoader, LTXVAddGuideMulti, SetNode, LoraLoaderModelOnly, CFGGuider, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, PrimitiveInt, ResizeImagesByLongerEdge, SetNode, ResizeImagesByLongerEdge, SetNode, ResizeImagesByLongerEdge, SetNode, LiconMSR, LTXVAddGuideMulti, LTXVConcatAVLatent, ComfyMathExpression, GetNode, ComfyMathExpression, GetNode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LayerUtility: PurgeVRAM, SetNode, LTX2_NAG, LoadImage, LoadImage, LoadImage, CFGGuider, KSamplerSelect, PrimitiveInt, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 44, "width": 97}
---

# 视频生成/图生视频/LTX2.3MSR-V2_2077234968824205313.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2077234968824205313.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（119 个）：
- `LTXVSeparateAVLatent`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `SetNode`
- `FrameInterpolate`
- `RTXVideoSuperResolution`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `DualCLIPLoader`
- `SetNode`
- `LTXVCropGuides`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `SetNode`
- `LTXVConditioning`
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `ComfyMathExpression`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `FrameInterpolationModelLoader`
- `ManualSigmas`
- `LTXICLoRALoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `UNETLoader` ★核心
- `LTXVAddGuideMulti`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `CFGGuider`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `LiconMSR`
- `LTXVAddGuideMulti`
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `LTX2_NAG`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `PrimitiveInt`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `44`
- `batch_size` = `1`

## 知识

覆盖率 **46%**（55/119）

**有卡**：`LTXVSeparateAVLatent`、`PathchSageAttentionKJ`、`RandomNoise`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`ManualSigmas`、`CLIPTextEncode`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`FrameInterpolate`、`RTXVideoSuperResolution`、`ComfyMathExpression`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXVCropGuides`、`LTXVConditioning`、`LTXAddVideoICLoRAGuide`、`LTXVAudioVAEDecode`、`LayerUtility: PurgeVRAM`、`FrameInterpolationModelLoader`、`LTXICLoRALoaderModelOnly`、`UNETLoader`、`LTXVAddGuideMulti`、`LoraLoaderModelOnly`、`CFGGuider`、`VHS_VideoCombine`、`ResizeImagesByLongerEdge`、`LiconMSR`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTX2_NAG`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
