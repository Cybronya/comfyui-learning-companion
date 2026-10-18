---
key: 视频生成/图生视频/LTX2.5首尾帧生视频｜高质量图生视频生成_2095603376045248514.json
name: LTX2.5首尾帧生视频｜高质量图生视频生成_2095603376045248514
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧生视频｜高质量图生视频生成_2095603376045248514.json
hash: c03f0b479a3042e0
coverage: 0.847222
learned_at: 2026-10-17 01:09:31
nodes: [LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVAddGuide, ManualSigmas, LTXVAddGuide, LTXVEmptyLatentAudio, LTXVCropGuides, EmptyLTXVLatentVideo, SamplerCustomAdvanced, LTXVConditioning, SamplerEulerAncestral, LTXVDualCFGGuider, RandomNoise, CLIPTextEncode, CLIPTextEncode, ComfySwitchNode, GetImageSize, LTXVPreprocess, LTXVPreprocess, TextGenerateLTX2Prompt, PreviewAny, UNETLoader, VAELoader, VAELoader, CLIPLoader, ComfyMathExpression, ComfyMathExpression, PrimitiveInt, PrimitiveStringMultiline, LTXVAudioVAEDecode, ResizeImageMaskNode, PrimitiveInt, PrimitiveInt, ResizeImageMaskNode, VHS_VideoCombine, VAEDecodeTiled, LoadImage, LoadImage, CLIPLoader, PrimitiveBoolean, PrimitiveInt, VHS_VideoCombine, FlashVSRNode, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.5首尾帧生视频｜高质量图生视频生成_2095603376045248514.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧生视频｜高质量图生视频生成_2095603376045248514.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVAddGuide`
- `ManualSigmas`
- `LTXVAddGuide`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVCropGuides`
- `EmptyLTXVLatentVideo`
- `SamplerCustomAdvanced` ★核心
- `LTXVConditioning`
- `SamplerEulerAncestral` ★核心
- `LTXVDualCFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ComfySwitchNode`
- `GetImageSize`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `LTXVAudioVAEDecode` ★核心
- `ResizeImageMaskNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `FlashVSRNode`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
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

覆盖率 **85%**（61/72）

**有卡**：`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVAddGuide`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`LTXVConditioning`、`SamplerEulerAncestral`、`LTXVDualCFGGuider`、`RandomNoise`、`CLIPTextEncode`、`GetImageSize`、`LTXVPreprocess`、`TextGenerateLTX2Prompt`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`LTXVAudioVAEDecode`、`ResizeImageMaskNode`、`VHS_VideoCombine`、`VAEDecodeTiled`、`LoadImage`、`PrimitiveBoolean`、`FlashVSRNode`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
