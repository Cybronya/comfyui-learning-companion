---
key: 视频生成/图生视频/LTX-2.3 AI2V数字人工作流(双人_多人支持)_2031018087641784321.json
name: LTX-2.3 AI2V数字人工作流(双人_多人支持)_2031018087641784321.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2031018087641784321.json
hash: c03a305ed5f59295
coverage: 0.75
learned_at: 2026-10-15 22:35:29
nodes: [SetNode, GetNode, CFGGuider, SetNode, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, KSamplerSelect, DiffusionModelLoaderKJ, CLIPTextEncode, LTXVConditioning, RandomNoise, CustomSigmas, LTXVConcatAVLatent, LTXVAudioVAEEncode, GetNode, easy showAnything, LoadImage, Reroute, Reroute, SetLatentNoiseMask, LTXVPreprocess, GetNode, RH_LLMAPI_Pro_Node, SolidMask, GetNode, Float, JWInteger, Note, EmptyLTXVLatentVideo, Label (rgthree), Label (rgthree), LTXVSeparateAVLatent, easy cleanGpuUsed, VAEDecodeTiled, CLIPTextEncode, VHS_VideoCombine, LoadAudio, MathExpression|pysssss, CR Prompt Text, 1hew_AudioDuration, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, PathchSageAttentionKJ, LTX2SamplingPreviewOverride, VAELoader, SamplerCustomAdvanced, MarkdownNote, LTXVImgToVideoInplace, SetNode, TrimAudioDuration, PreviewAudio]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX-2.3 AI2V数字人工作流(双人_多人支持)_2031018087641784321.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031018087641784321.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（52 个）：
- `SetNode`
- `GetNode`
- `CFGGuider`
- `SetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `KSamplerSelect` ★核心
- `DiffusionModelLoaderKJ`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `RandomNoise`
- `CustomSigmas`
- `LTXVConcatAVLatent`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `easy showAnything`
- `LoadImage`
- `Reroute`
- `Reroute`
- `SetLatentNoiseMask`
- `LTXVPreprocess`
- `GetNode`
- `RH_LLMAPI_Pro_Node`
- `SolidMask`
- `GetNode`
- `Float`
- `JWInteger`
- `Note`
- `EmptyLTXVLatentVideo`
- `Label (rgthree)`
- `Label (rgthree)`
- `LTXVSeparateAVLatent`
- `easy cleanGpuUsed`
- `VAEDecodeTiled` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `LoadAudio`
- `MathExpression|pysssss`
- `CR Prompt Text`
- `1hew_AudioDuration`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PathchSageAttentionKJ`
- `LTX2SamplingPreviewOverride`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `MarkdownNote`
- `LTXVImgToVideoInplace`
- `SetNode`
- `TrimAudioDuration`
- `PreviewAudio`

## 知识

覆盖率 **75%**（39/52）

**有卡**：`CFGGuider`、`VAELoaderKJ`、`DualCLIPLoader`、`KSamplerSelect`、`DiffusionModelLoaderKJ`、`CLIPTextEncode`、`LTXVConditioning`、`RandomNoise`、`CustomSigmas`、`LTXVConcatAVLatent`、`LTXVAudioVAEEncode`、`LoadImage`、`SetLatentNoiseMask`、`LTXVPreprocess`、`RH_LLMAPI_Pro_Node`、`SolidMask`、`Float`、`JWInteger`、`EmptyLTXVLatentVideo`、`Label (rgthree)`、`LTXVSeparateAVLatent`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`VHS_VideoCombine`、`LoadAudio`、`MathExpression|pysssss`、`CR Prompt Text`、`1hew_AudioDuration`、`LayerUtility: ImageScaleByAspectRatio V2`、`PathchSageAttentionKJ`、`LTX2SamplingPreviewOverride`、`VAELoader`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`TrimAudioDuration`、`PreviewAudio`

**用到的条目**：VAELoader、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent
