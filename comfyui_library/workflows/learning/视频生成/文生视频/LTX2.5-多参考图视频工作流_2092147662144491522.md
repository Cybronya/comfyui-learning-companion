---
key: 视频生成/文生视频/LTX2.5-多参考图视频工作流_2092147662144491522.json
name: LTX2.5-多参考图视频工作流_2092147662144491522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5-多参考图视频工作流_2092147662144491522.json
hash: 9b1e4bb318c4be97
coverage: 0.543478
learned_at: 2026-10-15 22:45:16
nodes: [TrimAudioDuration, LTXVAudioVAEEncode, GetNode, SetNode, SetNode, GetNode, SetNode, INTConstant, INTConstant, LTXVEmptyLatentAudio, GetNode, GetNode, EmptyLTXVLatentVideo, LTXVConditioning, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVSeparateAVLatent, LTXVCropGuides, LTXVConcatAVLatent, PathchSageAttentionKJ, SetNode, SetNode, CLIPLoader, SetNode, VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, SetNode, INTConstant, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, LoadAudio, PrimitiveBoolean, SetNode, GetNode, ComfyMathExpression, CM_IntToFloat, GetNode, GetNode, GetNode, ComfyMathExpression, ComfyMathExpression, CM_IntToFloat, CLIPTextEncode, CLIPTextEncode, SetNode, SetNode, LatentUpscaleModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CM_IntToFloat, GetNode, VHS_VideoCombine, GetNode, LTXVConditioning, CFGGuider, RandomNoise, KSamplerSelect, LTXVConcatAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVAudioVAEDecode, VAEDecodeTiled, SetNode, VHS_VideoCombine, SamplerCustomAdvanced, GetNode, GetNode, SetLatentNoiseMask, Switch any [Crystools], SolidMask, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, LTXVPreprocess, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LTXVPreprocess, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LTXVPreprocess, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LTXVPreprocess, LoadImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LTXVPreprocess, LoadImage, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), TextGenerateLTX2Prompt, CLIPLoader, GetNode, GetNode, GetNode, RH_Captioner, ImageConcanate, PrimitiveString, PreviewAny, SetNode, Fast Groups Bypasser (rgthree), ManualSigmas, UNETLoader, StringFunction|pysssss, ComfyUILTX25MSRMultiReferenceGuide, ComfyUILTX25MSRMultiReferenceGuide, MarkdownNote, GetNode, GetNode, ComfyUILTX25MSRICLoRALoader, LoadImage, LoadImage, Text Multiline, INTConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.5-多参考图视频工作流_2092147662144491522.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5-多参考图视频工作流_2092147662144491522.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（138 个）：
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVConcatAVLatent`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `INTConstant`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LoadAudio`
- `PrimitiveBoolean`
- `SetNode`
- `GetNode`
- `ComfyMathExpression`
- `CM_IntToFloat`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CM_IntToFloat`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CM_IntToFloat`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `LTXVConditioning`
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `SetNode`
- `VHS_VideoCombine`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `SetLatentNoiseMask`
- `Switch any [Crystools]`
- `SolidMask`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVPreprocess`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVPreprocess`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LTXVPreprocess`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVPreprocess`
- `LoadImage`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVPreprocess`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `RH_Captioner`
- `ImageConcanate`
- `PrimitiveString`
- `PreviewAny`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `ManualSigmas`
- `UNETLoader` ★核心
- `StringFunction|pysssss`
- `ComfyUILTX25MSRMultiReferenceGuide`
- `ComfyUILTX25MSRMultiReferenceGuide`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `ComfyUILTX25MSRICLoRALoader` ★核心
- `LoadImage`
- `LoadImage`
- `Text Multiline`
- `INTConstant`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **54%**（75/138）

**有卡**：`TrimAudioDuration`、`LTXVAudioVAEEncode`、`INTConstant`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoaderKJ`、`LoadAudio`、`PrimitiveBoolean`、`ComfyMathExpression`、`CM_IntToFloat`、`CLIPTextEncode`、`LatentUpscaleModelLoader`、`VHS_VideoCombine`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`SetLatentNoiseMask`、`Switch any [Crystools]`、`SolidMask`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVPreprocess`、`LoadImage`、`TextGenerateLTX2Prompt`、`RH_Captioner`、`ImageConcanate`、`UNETLoader`、`StringFunction|pysssss`、`ComfyUILTX25MSRMultiReferenceGuide`、`ComfyUILTX25MSRICLoRALoader`、`Text Multiline`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
