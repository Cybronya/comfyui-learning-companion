---
key: 视频生成/图生视频/Qwen_Image_2.1_Turbo多参考图加速版，文生图图生图高效出图_2116030300252893185.json
name: Qwen_Image_2.1_Turbo多参考图加速版，文生图图生图高效出图_2116030300252893185
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1_Turbo多参考图加速版，文生图图生图高效出图_2116030300252893185.json
hash: 076e824edcf7d5fa
coverage: 0.670732
learned_at: 2026-10-30 23:28:48
nodes: [LoadImage, SetNode, SetNode, GetNode, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, LoadImage, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, LoadImage, LoadImage, BatchImagesNode, QwenImage21Cache, SamplerCustomAdvanced, KSamplerSelect, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, ManualSigmas, CFGGuider, PathchSageAttentionKJ, PrimitiveStringMultiline, ComfySwitchNode, PreviewAny, CLIPLoader, PrimitiveBoolean, PrimitiveStringMultiline, TextGenerate, RandomNoise, SaveImageAdvanced, ComfySwitchNode, PrimitiveBoolean, EmptyLatentImage, VAEDecode, SaveImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen_Image_2.1_Turbo多参考图加速版，文生图图生图高效出图_2116030300252893185.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1_Turbo多参考图加速版，文生图图生图高效出图_2116030300252893185.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `LoadImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `BatchImagesNode`
- `QwenImage21Cache`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `ManualSigmas`
- `CFGGuider`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `PreviewAny`
- `CLIPLoader`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `TextGenerate`
- `RandomNoise`
- `SaveImageAdvanced`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
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

覆盖率 **67%**（55/82）

**有卡**：`LoadImage`、`BatchImagesNode`、`QwenImage21Cache`、`SamplerCustomAdvanced`、`KSamplerSelect`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`ManualSigmas`、`CFGGuider`、`PathchSageAttentionKJ`、`PrimitiveBoolean`、`TextGenerate`、`RandomNoise`、`SaveImageAdvanced`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
