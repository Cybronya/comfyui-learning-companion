---
key: 视频生成/图生视频/LTX2.3 MSR V2 单采升级版+自定义语音_2076686212194193410.json
name: LTX2.3 MSR V2 单采升级版+自定义语音_2076686212194193410.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 MSR V2 单采升级版+自定义语音_2076686212194193410.json
hash: 5e1867a14a38dabd
coverage: 0.721519
learned_at: 2026-10-15 22:41:32
nodes: [RandomNoise, ResizeImagesByLongerEdge, SetNode, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, Label (rgthree), LoadImage, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SetNode, ResizeImagesByLongerEdge, LoadImage, ResizeImagesByLongerEdge, SetNode, SetNode, SetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, CFGGuider, PrimitiveInt, ComfyMathExpression, LTXVAudioVAEDecode, VAEDecodeTiled, PrimitiveInt, PrimitiveInt, LTXVCropGuides, PrimitiveStringMultiline, GetNode, GetNode, GetNode, GetNode, GetNode, SamplerCustomAdvanced, LayerUtility: PurgeVRAM, Reroute, ComfyMathExpression, PathchSageAttentionKJ, CLIPTextEncode, PromptRelayEncode, PrimitiveInt, LTXAddVideoICLoRAGuide, KSamplerSelect, LTXVConditioning, ManualSigmas, SetNode, LTXVSeparateAVLatent, GetNode, PrimitiveStringMultiline, LTX2_NAG, EmptyLTXVLatentVideo, LTXVConcatAVLatent, ComfyMathExpression, ComfyMathExpression, FrameInterpolationModelLoader, Note, LayerUtility: PurgeVRAM, LiconMSR, VHS_VideoCombine, TrimAudioDuration, ComfyMathExpression, MelBandRoFormerSampler, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, UNETLoader, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, LoadImage, LoadImage, LoadImage, LoadAudio, MelBandRoFormerModelLoader, RTXVideoSuperResolution, FrameInterpolate]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.3 MSR V2 单采升级版+自定义语音_2076686212194193410.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2076686212194193410.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（79 个）：
- `RandomNoise`
- `ResizeImagesByLongerEdge`
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
- `LoadImage`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `CFGGuider`
- `PrimitiveInt`
- `ComfyMathExpression`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVCropGuides`
- `PrimitiveStringMultiline`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `Reroute`
- `ComfyMathExpression`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `PromptRelayEncode`
- `PrimitiveInt`
- `LTXAddVideoICLoRAGuide`
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `ManualSigmas`
- `SetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `PrimitiveStringMultiline`
- `LTX2_NAG`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `FrameInterpolationModelLoader`
- `Note`
- `LayerUtility: PurgeVRAM`
- `LiconMSR`
- `VHS_VideoCombine`
- `TrimAudioDuration`
- `ComfyMathExpression`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `RTXVideoSuperResolution`
- `FrameInterpolate`

## 知识

覆盖率 **72%**（57/79）

**有卡**：`RandomNoise`、`ResizeImagesByLongerEdge`、`Label (rgthree)`、`LoadImage`、`CFGGuider`、`ComfyMathExpression`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`LayerUtility: PurgeVRAM`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`PromptRelayEncode`、`LTXAddVideoICLoRAGuide`、`KSamplerSelect`、`LTXVConditioning`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTX2_NAG`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`FrameInterpolationModelLoader`、`LiconMSR`、`VHS_VideoCombine`、`TrimAudioDuration`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`DualCLIPLoader`、`VAELoaderKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`LoadAudio`、`MelBandRoFormerModelLoader`、`RTXVideoSuperResolution`、`FrameInterpolate`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
