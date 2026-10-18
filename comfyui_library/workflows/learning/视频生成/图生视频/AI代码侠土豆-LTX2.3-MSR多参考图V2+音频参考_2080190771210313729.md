---
key: 视频生成/图生视频/AI代码侠土豆-LTX2.3-MSR多参考图V2+音频参考_2080190771210313729.json
name: AI代码侠土豆-LTX2.3-MSR多参考图V2+音频参考_2080190771210313729.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AI代码侠土豆-LTX2.3-MSR多参考图V2+音频参考_2080190771210313729.json
hash: 7eab45913bb49a1b
coverage: 0.460674
learned_at: 2026-10-15 22:42:10
nodes: [Label (rgthree), UNETLoader, SetNode, LTXICLoRALoaderModelOnly, SetNode, VAELoaderKJ, SetNode, SetNode, SetNode, SetNode, Float, SetNode, SimpleMath+, SetNode, SetNode, SetNode, easy imageRemBg, easy imageRemBg, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, LTXVAudioVAEEncode, GetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, GetNode, SetNode, LTXVConditioning, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, ManualSigmas, LTXAVTextEncoderLoader, SamplerCustomAdvanced, GetNode, SetNode, LiconMSR, CFGGuider, LTXVConcatAVLatent, GetNode, SetNode, VAELoaderKJ, SetNode, SetLatentNoiseMask, LoadImage, LTXAddVideoICLoRAGuide, LoadImage, LoadImage, RandomNoise, SolidMask, PromptRelayEncode, GetNode, LTXVCropGuides, LTXVSeparateAVLatent, GetNode, VAEDecode, GetNode, LTXVAudioVAEDecode, PreviewAudio, easy cleanGpuUsed, SetNode, GetNode, VHS_VideoCombine, Int, TTResolutionSelector, Text, Text, Label (rgthree), LoadAudio]
patterns: []
missing: []
---

# 视频生成/图生视频/AI代码侠土豆-LTX2.3-MSR多参考图V2+音频参考_2080190771210313729.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2080190771210313729.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（89 个）：
- `Label (rgthree)`
- `UNETLoader` ★核心
- `SetNode`
- `LTXICLoRALoaderModelOnly` ★核心
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Float`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy imageRemBg`
- `easy imageRemBg`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `LTXVConditioning`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXAVTextEncoderLoader`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `SetNode`
- `LiconMSR`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `GetNode`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetLatentNoiseMask`
- `LoadImage`
- `LTXAddVideoICLoRAGuide`
- `LoadImage`
- `LoadImage`
- `RandomNoise`
- `SolidMask`
- `PromptRelayEncode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `PreviewAudio`
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `Int`
- `TTResolutionSelector`
- `Text`
- `Text`
- `Label (rgthree)`
- `LoadAudio`

## 知识

覆盖率 **46%**（41/89）

**有卡**：`Label (rgthree)`、`UNETLoader`、`LTXICLoRALoaderModelOnly`、`VAELoaderKJ`、`Float`、`SimpleMath+`、`easy imageRemBg`、`LTXVAudioVAEEncode`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`LTXVConditioning`、`KSamplerSelect`、`ManualSigmas`、`LTXAVTextEncoderLoader`、`SamplerCustomAdvanced`、`LiconMSR`、`CFGGuider`、`LTXVConcatAVLatent`、`SetLatentNoiseMask`、`LoadImage`、`LTXAddVideoICLoRAGuide`、`RandomNoise`、`SolidMask`、`PromptRelayEncode`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVAudioVAEDecode`、`PreviewAudio`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`Int`、`TTResolutionSelector`、`Text`、`LoadAudio`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
