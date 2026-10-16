---
key: 视频生成/图生视频/首尾帧图生视频提示词全自动｜LTX2.5视频生成工作流_2088146840704339970.json
name: 首尾帧图生视频提示词全自动｜LTX2.5视频生成工作流_2088146840704339970
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧图生视频提示词全自动｜LTX2.5视频生成工作流_2088146840704339970.json
hash: 66261df670a3373d
coverage: 0.852941
learned_at: 2026-10-16 21:28:18
nodes: [SamplerEulerAncestral, LTXVCropGuides, VAEDecodeTiled, LTXVAudioVAEDecode, ComfyMathExpression, ComfyMathExpression, RH_LLMAPI_Pro_Node, CLIPTextEncode, UNETLoader, VAELoader, VAELoader, CLIPLoader, LTXVSeparateAVLatent, ManualSigmas, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConditioning, LTXVAddGuide, LTXVAddGuide, PrimitiveInt, PrimitiveInt, PrimitiveInt, LoadImage, ResizeImageMaskNode, ResizeImageMaskNode, LTXVPreprocess, VHS_VideoCombine, Label (rgthree), RandomNoise, PreviewAny, LTXVDualCFGGuider, Label (rgthree), LoadImage, SamplerCustomAdvanced, GetImageSize, LTXVPreprocess, CR Text, PrimitiveInt, PrimitiveStringMultiline, CLIPTextEncode, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/首尾帧图生视频提示词全自动｜LTX2.5视频生成工作流_2088146840704339970.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/首尾帧图生视频提示词全自动｜LTX2.5视频生成工作流_2088146840704339970.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `SamplerEulerAncestral` ★核心
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RH_LLMAPI_Pro_Node`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `LTXVAddGuide`
- `LTXVAddGuide`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `VHS_VideoCombine`
- `Label (rgthree)`
- `RandomNoise`
- `PreviewAny`
- `LTXVDualCFGGuider`
- `Label (rgthree)`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `GetImageSize`
- `LTXVPreprocess`
- `CR Text`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
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

覆盖率 **85%**（58/68）

**有卡**：`SamplerEulerAncestral`、`LTXVCropGuides`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ComfyMathExpression`、`RH_LLMAPI_Pro_Node`、`CLIPTextEncode`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LTXVSeparateAVLatent`、`ManualSigmas`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`LTXVAddGuide`、`LoadImage`、`ResizeImageMaskNode`、`LTXVPreprocess`、`VHS_VideoCombine`、`Label (rgthree)`、`RandomNoise`、`LTXVDualCFGGuider`、`SamplerCustomAdvanced`、`GetImageSize`、`CR Text`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
