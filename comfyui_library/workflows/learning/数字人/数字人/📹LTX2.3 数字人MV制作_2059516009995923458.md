---
key: 数字人/数字人/📹LTX2.3 数字人MV制作_2059516009995923458.json
name: 📹LTX2.3 数字人MV制作_2059516009995923458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/📹LTX2.3 数字人MV制作_2059516009995923458.json
hash: f160ffb3291bf665
coverage: 0.903846
learned_at: 2026-10-26 02:06:19
nodes: [Note, MarkdownNote, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2SamplingPreviewOverride, VAELoaderKJ, Note, UNETLoader, LoraLoaderModelOnly, LTX2_NAG, SamplerCustomAdvanced, CFGGuider, KSamplerSelect, BasicScheduler, DualCLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, LTXVSeparateAVLatent, SolidMask, VAELoaderKJ, SoundFlow_GetLength, easy showAnything, ImageResizeKJv2, EmptyLTXVLatentVideo, SetLatentNoiseMask, RandomNoise, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVConditioning, PathchSageAttentionKJ, PreviewImage, LTX2SamplingPreviewOverride, LTXVCropGuides, KSampler, CreateVideo, SaveAudio, VAEDecodeTiled, VAELoaderKJ, LTXVAudioVAELoader, LTXVAudioVAEDecode, MathExpression|pysssss, LTXVPreprocess, Audio Cut (mtb), LTXVAudioVAEEncode, intToFloat _O, LTXVSeparateAVLatent, LoadImage, LoadAudio, Int, CLIPTextEncode, SaveVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.5000000000000001, "sampler_name": "euler_cfg_pp", "scheduler": "simple", "seed": 123, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 数字人/数字人/📹LTX2.3 数字人MV制作_2059516009995923458.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/📹LTX2.3 数字人MV制作_2059516009995923458.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `Note`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2SamplingPreviewOverride`
- `VAELoaderKJ`
- `Note`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVSeparateAVLatent`
- `SolidMask`
- `VAELoaderKJ`
- `SoundFlow_GetLength`
- `easy showAnything`
- `ImageResizeKJv2`
- `EmptyLTXVLatentVideo`
- `SetLatentNoiseMask`
- `RandomNoise`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `LTX2SamplingPreviewOverride`
- `LTXVCropGuides`
- `KSampler` ★核心
- `CreateVideo`
- `SaveAudio`
- `VAEDecodeTiled` ★核心
- `VAELoaderKJ`
- `LTXVAudioVAELoader`
- `LTXVAudioVAEDecode` ★核心
- `MathExpression|pysssss`
- `LTXVPreprocess`
- `Audio Cut (mtb)`
- `LTXVAudioVAEEncode` ★核心
- `intToFloat _O`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoadAudio`
- `Int`
- `CLIPTextEncode` ★核心
- `SaveVideo`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `123`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_cfg_pp`
- `scheduler` = `simple`
- `denoise` = `0.5000000000000001`

## 知识

覆盖率 **90%**（47/52）

**有卡**：`LoraLoaderModelOnly`、`LTX2SamplingPreviewOverride`、`VAELoaderKJ`、`UNETLoader`、`LTX2_NAG`、`SamplerCustomAdvanced`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`DualCLIPLoader`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LTXVSeparateAVLatent`、`SolidMask`、`SoundFlow_GetLength`、`ImageResizeKJv2`、`EmptyLTXVLatentVideo`、`SetLatentNoiseMask`、`RandomNoise`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`LTXVConditioning`、`PathchSageAttentionKJ`、`LTXVCropGuides`、`KSampler`、`CreateVideo`、`SaveAudio`、`VAEDecodeTiled`、`LTXVAudioVAELoader`、`LTXVAudioVAEDecode`、`MathExpression|pysssss`、`LTXVPreprocess`、`Audio Cut (mtb)`、`LTXVAudioVAEEncode`、`intToFloat _O`、`LoadImage`、`LoadAudio`、`Int`、`SaveVideo`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
