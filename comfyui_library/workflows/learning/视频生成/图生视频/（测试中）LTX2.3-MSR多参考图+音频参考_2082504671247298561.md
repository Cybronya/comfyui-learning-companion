---
key: 视频生成/图生视频/（测试中）LTX2.3-MSR多参考图+音频参考_2082504671247298561.json
name: （测试中）LTX2.3-MSR多参考图+音频参考_2082504671247298561.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（测试中）LTX2.3-MSR多参考图+音频参考_2082504671247298561.json
hash: 66ad18d12442ef85
coverage: 0.454545
learned_at: 2026-10-15 22:42:32
nodes: [UNETLoader, LTXICLoRALoaderModelOnly, VAELoaderKJ, SetNode, SetNode, easy imageRemBg, GetNode, GetNode, GetNode, LTXVAudioVAEEncode, GetNode, GetNode, SetNode, SetNode, GetNode, LTXAVTextEncoderLoader, SamplerCustomAdvanced, CFGGuider, VAELoaderKJ, SetNode, SetLatentNoiseMask, RandomNoise, SolidMask, LTXVSeparateAVLatent, VAEDecode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, PromptRelayEncode, CLIPTextEncode, LTXVConditioning, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SimpleMath+, EmptyLTXVLatentVideo, SetNode, SetNode, LTXAddVideoICLoRAGuide, LiconMSR, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, GetNode, GetNode, ManualSigmas, LTXVConcatAVLatent, LTXVCropGuides, easy cleanGpuUsed, VHS_VideoCombine, LTXVAudioVAEDecode, PreviewAudio, Label (rgthree), SetNode, LoadImage, TTResolutionSelector, Int, Float, SetNode, SetNode, GetNode, LoadImage, SetNode, GetNode, LoadImage, easy imageRemBg, SetNode, Text, LoadAudio, Text]
patterns: []
missing: []
---

# 视频生成/图生视频/（测试中）LTX2.3-MSR多参考图+音频参考_2082504671247298561.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2082504671247298561.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（88 个）：
- `UNETLoader` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `easy imageRemBg`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXAVTextEncoderLoader`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `VAELoaderKJ`
- `SetNode`
- `SetLatentNoiseMask`
- `RandomNoise`
- `SolidMask`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PromptRelayEncode`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `SetNode`
- `LTXAddVideoICLoRAGuide`
- `LiconMSR`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `LTXVAudioVAEDecode` ★核心
- `PreviewAudio`
- `Label (rgthree)`
- `SetNode`
- `LoadImage`
- `TTResolutionSelector`
- `Int`
- `Float`
- `SetNode`
- `SetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `GetNode`
- `LoadImage`
- `easy imageRemBg`
- `SetNode`
- `Text`
- `LoadAudio`
- `Text`

## 知识

覆盖率 **45%**（40/88）

**有卡**：`UNETLoader`、`LTXICLoRALoaderModelOnly`、`VAELoaderKJ`、`easy imageRemBg`、`LTXVAudioVAEEncode`、`LTXAVTextEncoderLoader`、`SamplerCustomAdvanced`、`CFGGuider`、`SetLatentNoiseMask`、`RandomNoise`、`SolidMask`、`LTXVSeparateAVLatent`、`VAEDecode`、`PromptRelayEncode`、`CLIPTextEncode`、`LTXVConditioning`、`SimpleMath+`、`EmptyLTXVLatentVideo`、`LTXAddVideoICLoRAGuide`、`LiconMSR`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`LTXVAudioVAEDecode`、`PreviewAudio`、`Label (rgthree)`、`LoadImage`、`TTResolutionSelector`、`Int`、`Float`、`Text`、`LoadAudio`

**用到的条目**：VAEDecode、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
