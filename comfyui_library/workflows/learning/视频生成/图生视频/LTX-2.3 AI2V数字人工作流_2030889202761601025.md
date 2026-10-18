---
key: 视频生成/图生视频/LTX-2.3 AI2V数字人工作流_2030889202761601025.json
name: LTX-2.3 AI2V数字人工作流_2030889202761601025.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3 AI2V数字人工作流_2030889202761601025.json
hash: c7efeaa7bce6ae21
coverage: 0.764706
learned_at: 2026-10-15 22:35:28
nodes: [SetNode, GetNode, CFGGuider, SetNode, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, KSamplerSelect, DiffusionModelLoaderKJ, CLIPTextEncode, LTXVConditioning, PathchSageAttentionKJ, RandomNoise, CustomSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, SetNode, MelBandRoFormerModelLoader, MelBandRoFormerSampler, 1hew_AudioDuration, MathExpression|pysssss, LTXVAudioVAEEncode, GetNode, easy showAnything, LoadImage, Reroute, Reroute, SetLatentNoiseMask, LayerUtility: ImageScaleByAspectRatio V2, LTXVPreprocess, GetNode, LTXVImgToVideoInplace, RH_LLMAPI_Pro_Node, PreviewAudio, SolidMask, LTXVSeparateAVLatent, GetNode, Float, JWInteger, CR Prompt Text, easy showAnything, Note, CLIPTextEncode, LoadAudio, TrimAudioDuration, easy cleanGpuUsed, VHS_VideoCombine, EmptyLTXVLatentVideo, VAEDecodeTiled, Label (rgthree), Label (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX-2.3 AI2V数字人工作流_2030889202761601025.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2030889202761601025.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（51 个）：
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
- `PathchSageAttentionKJ`
- `RandomNoise`
- `CustomSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `1hew_AudioDuration`
- `MathExpression|pysssss`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `easy showAnything`
- `LoadImage`
- `Reroute`
- `Reroute`
- `SetLatentNoiseMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVPreprocess`
- `GetNode`
- `LTXVImgToVideoInplace`
- `RH_LLMAPI_Pro_Node`
- `PreviewAudio`
- `SolidMask`
- `LTXVSeparateAVLatent`
- `GetNode`
- `Float`
- `JWInteger`
- `CR Prompt Text`
- `easy showAnything`
- `Note`
- `CLIPTextEncode` ★核心
- `LoadAudio`
- `TrimAudioDuration`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `EmptyLTXVLatentVideo`
- `VAEDecodeTiled` ★核心
- `Label (rgthree)`
- `Label (rgthree)`

## 知识

覆盖率 **76%**（39/51）

**有卡**：`CFGGuider`、`VAELoaderKJ`、`DualCLIPLoader`、`KSamplerSelect`、`DiffusionModelLoaderKJ`、`CLIPTextEncode`、`LTXVConditioning`、`PathchSageAttentionKJ`、`RandomNoise`、`CustomSigmas`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`1hew_AudioDuration`、`MathExpression|pysssss`、`LTXVAudioVAEEncode`、`LoadImage`、`SetLatentNoiseMask`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`RH_LLMAPI_Pro_Node`、`PreviewAudio`、`SolidMask`、`LTXVSeparateAVLatent`、`Float`、`JWInteger`、`CR Prompt Text`、`LoadAudio`、`TrimAudioDuration`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`EmptyLTXVLatentVideo`、`VAEDecodeTiled`、`Label (rgthree)`

**用到的条目**：CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVConcatAVLatent、LTXVSeparateAVLatent
