---
key: 视频生成/图生视频/LTX2.3首尾帧生视频（支持自动提示词）_2031682937711759362.json
name: LTX2.3首尾帧生视频（支持自动提示词）_2031682937711759362.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3首尾帧生视频（支持自动提示词）_2031682937711759362.json
hash: 22701a86cc54d29d
coverage: 0.447471
learned_at: 2026-10-15 22:35:32
nodes: [LTXVAudioVAEDecode, CFGGuider, CLIPTextEncode, GetNode, GetNode, GetNode, LTXVEmptyLatentAudio, CLIPTextEncode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, GetNode, LTXVConcatAVLatent, RandomNoise, GetNode, VAEDecode, DF_Int_to_Float, GetNode, DF_Int_to_Float, GetNode, KSamplerSelect, GetNode, VAEDecode, LTXVLatentUpsampler, GetNode, GetNode, GetNode, GetNode, RandomNoise, CFGGuider, GetNode, GetNode, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, LTXVLatentUpsampler, GetNode, GetNode, ManualSigmas, SamplerCustomAdvanced, SamplerCustomAdvanced, LoadImage, GetNode, LTXVFirstLastFrameControl_TTP, LTXVConcatAVLatent, SetNode, CM_FloatToInt, EmptyLTXVLatentVideo, CM_FloatToInt, GetNode, GetNode, GetNode, GetNode, LTXVConditioning, SetNode, CM_IntToFloat, CFGGuider, KSamplerSelect, LTXVScheduler, GetNode, LTXVSeparateAVLatent, SamplerCustomAdvanced, GetNode, GetNode, SetNode, LTXVSeparateAVLatent, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, LTXVSeparateAVLatent, SetNode, SetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, GetNode, DF_Int_to_Float, GetNode, VAEDecode, RandomNoise, GetNode, GetNode, MarkdownNote, GetNode, GetNode, JWIntegerDiv, JWIntegerDiv, GetNode, GetNode, LTXVFirstLastFrameControl_TTP, GetNode, GetNode, GetNode, LTXVFirstLastFrameControl_TTP, GetNode, MarkdownNote, SetNode, SetNode, SetNode, GetNode, MarkdownNote, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), GetNode, GetNode, GetNode, SetNode, LTXVMiddleFrame_TTP, SetNode, INTConstant, LoadImage, GetNode, EmptyImage, EmptyImage, EmptyImage, GetNode, SetNode, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, ImpactSwitch, INTConstant, StringReplace, TextInput_, TextInput_, GetNode, Qwen3_VQA, ToString, ImpactSwitch, ShellAgentPluginOutputText, SetNode, easy cleanGpuUsed, LayerUtility: PurgeVRAM, easy showAnything, TextInput_, Label (rgthree), INTConstant, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ImpactSwitch, SetNode, SetNode, MarkdownNote, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, JoinStrings, Reroute, easy cleanGpuUsed, GetNode, LayerUtility: PurgeVRAM, Label (rgthree), ImageConcatMulti, GetNode, GetNode, ImpactSwitch, ImpactSwitch, LTXVPreprocess, SetNode, GetNode, ImageResizeKJv2, INTConstant, easy ifElse, INTConstant, GetNode, GetNode, Compare, INTConstant, GetNode, GetNode, INTConstant, ImpactSwitch, LTXVPreprocess, SetNode, ImageResizeKJv2, easy ifElse, SetNode, ImpactSwitch, LTXVPreprocess, SetNode, GetNode, GetNode, INTConstant, INTConstant, easy ifElse, ImageResizeKJv2, ImpactSwitch, ImpactSwitch, Compare, Compare, ImpactSwitch, ImpactSwitch, INTConstant, INTConstant, INTConstant, ImpactSwitch, VAELoaderKJ, VAELoaderKJ, CheckpointLoaderSimple, LoraLoaderModelOnly, LatentUpscaleModelLoader, SetNode, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, LTXAVTextEncoderLoader, DualCLIPLoader, GetNode, CR Text, ImpactSwitch, CR Text, CR Text, MarkdownNote, LoadImage, ImpactSwitch, ImpactSwitch, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": null, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3首尾帧生视频（支持自动提示词）_2031682937711759362.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031682937711759362.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（257 个）：
- `LTXVAudioVAEDecode` ★核心
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `GetNode`
- `VAEDecode` ★核心
- `DF_Int_to_Float`
- `GetNode`
- `DF_Int_to_Float`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `GetNode`
- `LTXVFirstLastFrameControl_TTP`
- `LTXVConcatAVLatent`
- `SetNode`
- `CM_FloatToInt`
- `EmptyLTXVLatentVideo`
- `CM_FloatToInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `SetNode`
- `CM_IntToFloat`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `DF_Int_to_Float`
- `GetNode`
- `VAEDecode` ★核心
- `RandomNoise`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `JWIntegerDiv`
- `JWIntegerDiv`
- `GetNode`
- `GetNode`
- `LTXVFirstLastFrameControl_TTP`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVFirstLastFrameControl_TTP`
- `GetNode`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `MarkdownNote`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVMiddleFrame_TTP`
- `SetNode`
- `INTConstant`
- `LoadImage`
- `GetNode`
- `EmptyImage`
- `EmptyImage`
- `EmptyImage`
- `GetNode`
- `SetNode`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `ImpactSwitch`
- `INTConstant`
- `StringReplace`
- `TextInput_`
- `TextInput_`
- `GetNode`
- `Qwen3_VQA`
- `ToString`
- `ImpactSwitch`
- `ShellAgentPluginOutputText`
- `SetNode`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `easy showAnything`
- `TextInput_`
- `Label (rgthree)`
- `INTConstant`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ImpactSwitch`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `JoinStrings`
- `Reroute`
- `easy cleanGpuUsed`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `Label (rgthree)`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `ImpactSwitch`
- `ImpactSwitch`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `INTConstant`
- `easy ifElse`
- `INTConstant`
- `GetNode`
- `GetNode`
- `Compare`
- `INTConstant`
- `GetNode`
- `GetNode`
- `INTConstant`
- `ImpactSwitch`
- `LTXVPreprocess`
- `SetNode`
- `ImageResizeKJv2`
- `easy ifElse`
- `SetNode`
- `ImpactSwitch`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `easy ifElse`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `ImpactSwitch`
- `Compare`
- `Compare`
- `ImpactSwitch`
- `ImpactSwitch`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `ImpactSwitch`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `DualCLIPLoader`
- `GetNode`
- `CR Text`
- `ImpactSwitch`
- `CR Text`
- `CR Text`
- `MarkdownNote`
- `LoadImage`
- `ImpactSwitch`
- `ImpactSwitch`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `None`

## 知识

覆盖率 **45%**（115/257）

**有卡**：`LTXVAudioVAEDecode`、`CFGGuider`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`RandomNoise`、`VAEDecode`、`DF_Int_to_Float`、`KSamplerSelect`、`LTXVLatentUpsampler`、`ManualSigmas`、`SamplerCustomAdvanced`、`LoadImage`、`LTXVFirstLastFrameControl_TTP`、`CM_FloatToInt`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`CM_IntToFloat`、`LTXVScheduler`、`LTXVSeparateAVLatent`、`JWIntegerDiv`、`Label (rgthree)`、`LTXVMiddleFrame_TTP`、`INTConstant`、`EmptyImage`、`CR Text`、`StringReplace`、`TextInput_`、`Qwen3_VQA`、`ToString`、`ShellAgentPluginOutputText`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM`、`JoinStrings`、`ImageConcatMulti`、`LTXVPreprocess`、`ImageResizeKJv2`、`Compare`、`VAELoaderKJ`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`DualCLIPLoader`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
