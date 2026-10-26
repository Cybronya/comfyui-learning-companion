---
key: 视频生成/图生视频/Qwen_Image_2.1_加速PE加in_版，文生图速度翻倍_2113110553781686274.json
name: Qwen_Image_2.1_加速PE加in_版，文生图速度翻倍_2113110553781686274
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1_加速PE加in_版，文生图速度翻倍_2113110553781686274.json
hash: 5b14c45ad2874ca2
coverage: 0.910714
learned_at: 2026-10-26 22:13:55
nodes: [CLIPLoader, CFGGuider, RandomNoise, LoadImage, LoadImage, easy cleanGpuUsed, KSamplerSelect, SamplerCustomAdvanced, VAEDecode, VAELoader, QwenPERewriteT8, LoraLoaderModelOnly, QwenImage21SageAttentionT8, TextEncodeQwenImage21, ComfySwitchNode, ManualSigmas, easy showAnything, LoadImage, LoadImage, EmptyLatentImage, ResolutionSelector, LoadImage, UNETLoader, UNETLoader, LoadImage, CR Prompt Text, SaveImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen_Image_2.1_加速PE加in_版，文生图速度翻倍_2113110553781686274.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1_加速PE加in_版，文生图速度翻倍_2113110553781686274.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `CLIPLoader`
- `CFGGuider`
- `RandomNoise`
- `LoadImage`
- `LoadImage`
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `QwenPERewriteT8`
- `LoraLoaderModelOnly` ★核心
- `QwenImage21SageAttentionT8`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `ManualSigmas`
- `easy showAnything`
- `LoadImage`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `CR Prompt Text`
- `SaveImage`
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
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **91%**（51/56）

**有卡**：`CLIPLoader`、`CFGGuider`、`RandomNoise`、`LoadImage`、`easy cleanGpuUsed`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecode`、`VAELoader`、`QwenPERewriteT8`、`LoraLoaderModelOnly`、`QwenImage21SageAttentionT8`、`TextEncodeQwenImage21`、`ManualSigmas`、`EmptyLatentImage`、`ResolutionSelector`、`UNETLoader`、`CR Prompt Text`、`SaveImage`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
