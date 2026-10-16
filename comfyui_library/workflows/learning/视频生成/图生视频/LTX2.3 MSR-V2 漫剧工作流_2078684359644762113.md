---
key: 视频生成/图生视频/LTX2.3 MSR-V2 漫剧工作流_2078684359644762113.json
name: LTX2.3 MSR-V2 漫剧工作流_2078684359644762113.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2078684359644762113.json
hash: 6b349d6ff9361e8d
coverage: 0.743902
learned_at: 2026-10-15 22:41:54
nodes: [LTXVEmptyLatentAudio, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, PrimitiveInt, PrimitiveInt, LTX2_NAG, LTXVConditioning, ManualSigmas, ComfyMathExpression, PrimitiveInt, ComfyMathExpression, CLIPTextEncode, ComfyMathExpression, RandomNoise, LayerUtility: PurgeVRAM, SamplerCustomAdvanced, PathchSageAttentionKJ, EmptyLTXVLatentVideo, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LiconMSR, LTXAddVideoICLoRAGuide, GetNode, CLIPTextEncode, RandomNoise, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVCropGuides, SamplerCustomAdvanced, ManualSigmas, GetNode, GetNode, GetNode, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, LTXVAddGuideMulti, LTXVAddGuideMulti, PrimitiveInt, RTXVideoSuperResolution, FrameInterpolate, LayerUtility: PurgeVRAM, FrameInterpolationModelLoader, VAEDecodeTiled, LTXVSeparateAVLatent, LTXVCropGuides, LayerUtility: PurgeVRAM, LTXVAudioVAEDecode, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, SetNode, UNETLoader, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, LoadImage, LoadImage, GetNode, GetNode, RHHiddenNodes, RHLLMChatNode, GetNode, SetNode, SetNode, SetNode, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, LoadImage, VHS_VideoCombine, LoraLoaderModelOnly, CR Prompt Text, Int, ResizeImagesByLongerEdge]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 44, "width": 97}
---

# 视频生成/图生视频/LTX2.3 MSR-V2 漫剧工作流_2078684359644762113.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2078684359644762113.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（82 个）：
- `LTXVEmptyLatentAudio` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTX2_NAG`
- `LTXVConditioning`
- `ManualSigmas`
- `ComfyMathExpression`
- `PrimitiveInt`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `RandomNoise`
- `LayerUtility: PurgeVRAM`
- `SamplerCustomAdvanced` ★核心
- `PathchSageAttentionKJ`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LiconMSR`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `LTXVAddGuideMulti`
- `LTXVAddGuideMulti`
- `PrimitiveInt`
- `RTXVideoSuperResolution`
- `FrameInterpolate`
- `LayerUtility: PurgeVRAM`
- `FrameInterpolationModelLoader`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LayerUtility: PurgeVRAM`
- `LTXVAudioVAEDecode` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `GetNode`
- `GetNode`
- `RHHiddenNodes`
- `RHLLMChatNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `Int`
- `ResizeImagesByLongerEdge`

## 关键参数

- `width` = `97`
- `height` = `44`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（61/82）

**有卡**：`LTXVEmptyLatentAudio`、`CFGGuider`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTX2_NAG`、`LTXVConditioning`、`ManualSigmas`、`ComfyMathExpression`、`CLIPTextEncode`、`RandomNoise`、`LayerUtility: PurgeVRAM`、`SamplerCustomAdvanced`、`PathchSageAttentionKJ`、`EmptyLTXVLatentVideo`、`LiconMSR`、`LTXAddVideoICLoRAGuide`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXVAddGuideMulti`、`RTXVideoSuperResolution`、`FrameInterpolate`、`FrameInterpolationModelLoader`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`LoadImage`、`RHHiddenNodes`、`RHLLMChatNode`、`ResizeImagesByLongerEdge`、`VHS_VideoCombine`、`CR Prompt Text`、`Int`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
