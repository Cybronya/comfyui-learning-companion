---
key: 视频生成/图生视频/LTX2.3 MSR V2 单采升级版_2076685195511685122.json
name: LTX2.3 MSR V2 单采升级版_2076685195511685122.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 MSR V2 单采升级版_2076685195511685122.json
hash: 54ceed0f2c4c736e
coverage: 0.714286
learned_at: 2026-10-15 22:41:32
nodes: [KSamplerSelect, RandomNoise, SetNode, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, Label (rgthree), LoadImage, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SetNode, ResizeImagesByLongerEdge, GetNode, GetNode, CLIPTextEncode, PathchSageAttentionKJ, Reroute, LTXVEmptyLatentAudio, ResizeImagesByLongerEdge, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SamplerCustomAdvanced, EmptyLTXVLatentVideo, CFGGuider, ManualSigmas, ComfyMathExpression, LTX2_NAG, LTXVConcatAVLatent, PrimitiveInt, PrimitiveInt, ComfyMathExpression, LiconMSR, GetNode, PrimitiveInt, ComfyMathExpression, LTXVConditioning, LayerUtility: PurgeVRAM, PrimitiveInt, PrimitiveStringMultiline, LTXVSeparateAVLatent, LTXAddVideoICLoRAGuide, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVCropGuides, ComfyMathExpression, FrameInterpolationModelLoader, PrimitiveStringMultiline, VHS_VideoCombine, PromptRelayEncode, Note, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, LoadImage, LoadImage, LoadImage, LoadImage, ResizeImagesByLongerEdge, UNETLoader, LayerUtility: PurgeVRAM, RTXVideoSuperResolution, FrameInterpolate]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 44, "width": 97}
---

# 视频生成/图生视频/LTX2.3 MSR V2 单采升级版_2076685195511685122.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2076685195511685122.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（70 个）：
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `Label (rgthree)`
- `LoadImage`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `Reroute`
- `LTXVEmptyLatentAudio` ★核心
- `ResizeImagesByLongerEdge`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `EmptyLTXVLatentVideo`
- `CFGGuider`
- `ManualSigmas`
- `ComfyMathExpression`
- `LTX2_NAG`
- `LTXVConcatAVLatent`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `LiconMSR`
- `GetNode`
- `PrimitiveInt`
- `ComfyMathExpression`
- `LTXVConditioning`
- `LayerUtility: PurgeVRAM`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `LTXVSeparateAVLatent`
- `LTXAddVideoICLoRAGuide`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVCropGuides`
- `ComfyMathExpression`
- `FrameInterpolationModelLoader`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `PromptRelayEncode`
- `Note`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResizeImagesByLongerEdge`
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM`
- `RTXVideoSuperResolution`
- `FrameInterpolate`

## 关键参数

- `width` = `97`
- `height` = `44`
- `batch_size` = `1`

## 知识

覆盖率 **71%**（50/70）

**有卡**：`KSamplerSelect`、`RandomNoise`、`ResizeImagesByLongerEdge`、`Label (rgthree)`、`LoadImage`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`EmptyLTXVLatentVideo`、`CFGGuider`、`ManualSigmas`、`ComfyMathExpression`、`LTX2_NAG`、`LTXVConcatAVLatent`、`LiconMSR`、`LTXVConditioning`、`LayerUtility: PurgeVRAM`、`LTXVSeparateAVLatent`、`LTXAddVideoICLoRAGuide`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXVCropGuides`、`FrameInterpolationModelLoader`、`VHS_VideoCombine`、`PromptRelayEncode`、`DualCLIPLoader`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`UNETLoader`、`RTXVideoSuperResolution`、`FrameInterpolate`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
