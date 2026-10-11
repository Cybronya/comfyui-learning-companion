---
key: 视频生成/文生视频/首尾帧视频生成｜LTX 2.5文生图生视频工作流_2088155779974127617.json
name: 首尾帧视频生成｜LTX 2.5文生图生视频工作流_2088155779974127617
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/首尾帧视频生成｜LTX 2.5文生图生视频工作流_2088155779974127617.json
hash: 24146d52f511bdff
coverage: 0.838235
learned_at: 2026-10-11 20:53:56
nodes: [LTXVConcatAVLatent, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXVAddGuide, ManualSigmas, LTXVAddGuide, LTXVEmptyLatentAudio, LTXVCropGuides, EmptyLTXVLatentVideo, SamplerCustomAdvanced, LTXVConditioning, SamplerEulerAncestral, RandomNoise, CLIPTextEncode, GetImageSize, LTXVDualCFGGuider, PrimitiveInt, PrimitiveInt, PrimitiveInt, TextGenerateLTX2Prompt, PrimitiveBoolean, UNETLoader, VAELoader, VAELoader, CLIPTextEncode, LTXVPreprocess, ResizeImageMaskNode, ResizeImageMaskNode, LTXVPreprocess, VHS_VideoCombine, ComfyMathExpression, ComfyMathExpression, VAEDecodeTiled, ComfySwitchNode, PreviewAny, PrimitiveStringMultiline, LoadImage, LoadImage, CLIPLoader, CLIPLoader, PrimitiveInt, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/首尾帧视频生成｜LTX 2.5文生图生视频工作流_2088155779974127617.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/首尾帧视频生成｜LTX 2.5文生图生视频工作流_2088155779974127617.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
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
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `LTXVDualCFGGuider`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `TextGenerateLTX2Prompt`
- `PrimitiveBoolean`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `VHS_VideoCombine`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `VAEDecodeTiled` ★核心
- `ComfySwitchNode`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `CLIPLoader`
- `PrimitiveInt`
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

覆盖率 **84%**（57/68）

**有卡**：`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXVAddGuide`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`LTXVConditioning`、`SamplerEulerAncestral`、`RandomNoise`、`CLIPTextEncode`、`GetImageSize`、`LTXVDualCFGGuider`、`TextGenerateLTX2Prompt`、`PrimitiveBoolean`、`UNETLoader`、`VAELoader`、`LTXVPreprocess`、`ResizeImageMaskNode`、`VHS_VideoCombine`、`ComfyMathExpression`、`VAEDecodeTiled`、`LoadImage`、`CLIPLoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
