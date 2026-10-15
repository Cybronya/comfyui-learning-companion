---
key: 视频生成/文生视频/多参考图视频工作流｜LTX2.5文生图生视频生视频_2092608834547314689.json
name: 多参考图视频工作流｜LTX2.5文生图生视频生视频_2092608834547314689
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/多参考图视频工作流｜LTX2.5文生图生视频生视频_2092608834547314689.json
hash: 132b7d9fcc7220b2
coverage: 0.597561
learned_at: 2026-10-15 22:48:27
nodes: [TrimAudioDuration, LTXVAudioVAEEncode, GetNode, SetNode, SetNode, GetNode, SetNode, INTConstant, INTConstant, LTXVEmptyLatentAudio, GetNode, GetNode, EmptyLTXVLatentVideo, LTXVConditioning, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVSeparateAVLatent, LTXVCropGuides, LTXVConcatAVLatent, PathchSageAttentionKJ, SetNode, SetNode, CLIPLoader, SetNode, VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, SetNode, INTConstant, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, LoadAudio, PrimitiveBoolean, SetNode, GetNode, ComfyMathExpression, CM_IntToFloat, GetNode, GetNode, GetNode, ComfyMathExpression, ComfyMathExpression, CM_IntToFloat, CLIPTextEncode, CLIPTextEncode, SetNode, SetNode, LatentUpscaleModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CM_IntToFloat, GetNode, VHS_VideoCombine, GetNode, LTXVConditioning, CFGGuider, RandomNoise, KSamplerSelect, LTXVConcatAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVAudioVAEDecode, VAEDecodeTiled, SetNode, VHS_VideoCombine, SamplerCustomAdvanced, GetNode, GetNode, SetLatentNoiseMask, Switch any [Crystools], SolidMask, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, LTXVPreprocess, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LTXVPreprocess, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LTXVPreprocess, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LTXVPreprocess, LoadImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LTXVPreprocess, LoadImage, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), TextGenerateLTX2Prompt, CLIPLoader, GetNode, GetNode, GetNode, RH_Captioner, ImageConcanate, PrimitiveString, PreviewAny, SetNode, Fast Groups Bypasser (rgthree), ManualSigmas, UNETLoader, StringFunction|pysssss, ComfyUILTX25MSRMultiReferenceGuide, ComfyUILTX25MSRMultiReferenceGuide, GetNode, GetNode, ComfyUILTX25MSRICLoRALoader, LoadImage, LoadImage, Text Multiline, INTConstant, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/多参考图视频工作流｜LTX2.5文生图生视频生视频_2092608834547314689.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/多参考图视频工作流｜LTX2.5文生图生视频生视频_2092608834547314689.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（164 个）：
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
- `GetNode`
- `GetNode`
- `ComfyUILTX25MSRICLoRALoader` ★核心
- `LoadImage`
- `LoadImage`
- `Text Multiline`
- `INTConstant`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **60%**（98/164）

**有卡**：`TrimAudioDuration`、`LTXVAudioVAEEncode`、`INTConstant`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoaderKJ`、`LoadAudio`、`PrimitiveBoolean`、`ComfyMathExpression`、`CM_IntToFloat`、`CLIPTextEncode`、`LatentUpscaleModelLoader`、`VHS_VideoCombine`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`SetLatentNoiseMask`、`Switch any [Crystools]`、`SolidMask`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVPreprocess`、`LoadImage`、`TextGenerateLTX2Prompt`、`RH_Captioner`、`ImageConcanate`、`UNETLoader`、`StringFunction|pysssss`、`ComfyUILTX25MSRMultiReferenceGuide`、`ComfyUILTX25MSRICLoRALoader`、`Text Multiline`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
