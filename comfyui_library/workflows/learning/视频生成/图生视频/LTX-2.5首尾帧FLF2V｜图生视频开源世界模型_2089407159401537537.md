---
key: 视频生成/图生视频/LTX-2.5首尾帧FLF2V｜图生视频开源世界模型_2089407159401537537.json
name: LTX-2.5首尾帧FLF2V｜图生视频开源世界模型_2089407159401537537
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.5首尾帧FLF2V｜图生视频开源世界模型_2089407159401537537.json
hash: ece75d0bbf9bba94
coverage: 0.849315
learned_at: 2026-10-16 21:43:18
nodes: [SaveVideo, LTXVConcatAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LTXVAddGuide, ManualSigmas, LTXVAddGuide, LTXVEmptyLatentAudio, LTXVCropGuides, EmptyLTXVLatentVideo, SamplerCustomAdvanced, LTXVConditioning, SamplerEulerAncestral, CreateVideo, LTXVDualCFGGuider, RandomNoise, CLIPTextEncode, CLIPTextEncode, ComfySwitchNode, GetImageSize, LTXVPreprocess, LTXVPreprocess, TextGenerateLTX2Prompt, ImageScale, ImageScale, PreviewAny, UNETLoader, VAELoader, VAELoader, CLIPLoader, CLIPLoader, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, ComfyMathExpression, PrimitiveInt, ComfyMathExpression, PrimitiveInt, PrimitiveStringMultiline, ImageFromBatch, SaveImage, SaveAudio, VHS_VideoCombine, LoadImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX-2.5首尾帧FLF2V｜图生视频开源世界模型_2089407159401537537.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX-2.5首尾帧FLF2V｜图生视频开源世界模型_2089407159401537537.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `SaveVideo`
- `LTXVConcatAVLatent`
- `VAEDecodeTiled` ★核心
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
- `CreateVideo`
- `LTXVDualCFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ComfySwitchNode`
- `GetImageSize`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `TextGenerateLTX2Prompt`
- `ImageScale`
- `ImageScale`
- `PreviewAny`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `CLIPLoader`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `PrimitiveInt`
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `ImageFromBatch`
- `SaveImage`
- `SaveAudio`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
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

覆盖率 **85%**（62/73）

**有卡**：`SaveVideo`、`LTXVConcatAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`LTXVAddGuide`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`LTXVConditioning`、`SamplerEulerAncestral`、`CreateVideo`、`LTXVDualCFGGuider`、`RandomNoise`、`CLIPTextEncode`、`GetImageSize`、`LTXVPreprocess`、`TextGenerateLTX2Prompt`、`ImageScale`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`PrimitiveBoolean`、`ComfyMathExpression`、`ImageFromBatch`、`SaveImage`、`SaveAudio`、`VHS_VideoCombine`、`LoadImage`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
